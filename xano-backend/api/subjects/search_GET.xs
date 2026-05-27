// api:GET /subjects/search
api subjects/search {
  method = "GET"
  description = "Search for subjects by name and filter by overdue tasks."

  input = {
    fields = [
      {
        name = "name"
        type = "text"
        description = "The name of the subject to search for."
        required = false
      },
      {
        name = "has_overdue_tasks"
        type = "boolean"
        description = "Whether to filter for subjects with overdue tasks."
        required = false
      }
    ]
  }

  output = {
    fields = [
      {
        name = "subjects"
        type = "table[]"
        table = "subject"
      }
    ]
  }

  handler = {
    // 1. Get current user's ID
    eval user_id = "auth:id"
    // Fails if no user is authenticated
    assert user_id != null "Unauthorized: You must be logged in to perform this action."

    // 2. Base query: Get all subject IDs for the current user
    all from user_subject where user_subject.user_id == user_id {
      output = {
        name = "user_subjects"
        fields = ["subject_id"]
      }
    }
    eval subject_ids_for_user = "user_subjects.subject_id"

    // 3. Conditional: Filter for subjects with overdue tasks
    if "input:has_overdue_tasks" == true {
      // Find overdue tasks for the user
      all from academic_tasks where academic_tasks.user_id == user_id && academic_tasks.due_date < "now" && academic_tasks.status != "done" {
        output = {
          name = "overdue_tasks"
          fields = ["subject_id"]
        }
      }
      // Get unique subject IDs from overdue tasks
      eval overdue_subject_ids = "overdue_tasks.subject_id"
      eval unique_overdue_subject_ids = "unique(overdue_subject_ids)"
      
      // Intersect the user's subjects with the overdue subjects
      eval subject_ids = "array_intersect(subject_ids_for_user, unique_overdue_subject_ids)"
    } else {
      // If not filtering by overdue tasks, use all of the user's subject IDs
      eval subject_ids = "subject_ids_for_user"
    }

    // 4. Final Query: Get subjects based on calculated IDs and name filter
    query from subject {
      where {
        group {
          // Subject must be in the calculated list of IDs
          subject.id in subject_ids

          // Conditional: filter by name if provided
          if "input:name" != null && "input:name" != "" {
            // Using ilike for case-insensitive contains search
            subject.name ilike "%" + "input:name" + "%"
          }
        }
      }
      output = {
        name = "subjects"
        fields = ["id", "name", "description"]
      }
    }
  }
}
