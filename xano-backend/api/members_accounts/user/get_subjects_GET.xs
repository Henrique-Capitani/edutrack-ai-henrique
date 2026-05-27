// GET all subjects for the current user
api user/subjects {
  method = "GET"
  description = "Get all subjects for the current user"

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
    // Get the current user's ID
    eval user_id = "auth:id"

    // Query all records from the user_subject table for the current user
    all from user_subject where user_id == "user_id" {
      output = {
        name = "user_subjects"
        fields = ["subject_id"]
      }
    }

    // Extract the subject IDs
    eval subject_ids = "user_subjects.subject_id"

    // Query all subjects with the extracted IDs
    all from subject where id in "subject_ids" {
      output = {
        name = "subjects"
        fields = ["id", "name", "description"]
      }
    }
  }
}