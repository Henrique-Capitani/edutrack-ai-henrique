// DELETE (unassign) a subject from the current user
api user/subjects/{subject_id} {
  method = "DELETE"
  description = "Unassign a subject from the current user"

  input = {
    fields = [
      {
        name = "subject_id"
        type = "int"
        required = true
        from = "path"
      }
    ]
  }

  output = {
    fields = [
      {
        name = "success"
        type = "boolean"
      }
    ]
  }

  handler = {
    // Get the current user's ID
    eval user_id = "auth:id"

    // Find the record in the user_subject table
    find from user_subject {
      input = {
        user_id = "user_id"
        subject_id = "input:subject_id"
      }
      output = {
        name = "user_subject"
      }
    }

    // Delete the record from the user_subject table
    delete from user_subject {
      input = {
        id = "user_subject.id"
      }
    }

    return {
      success = true
    }
  }
}