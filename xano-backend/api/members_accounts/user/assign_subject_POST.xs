// POST (assign) a subject to the current user
api user/subjects {
  method = "POST"
  description = "Assign a subject to the current user"

  input = {
    fields = [
      {
        name = "subject_id"
        type = "int"
        required = true
      }
    ]
  }

  output = {
    fields = [
      {
        name = "user_subject"
        type = "table"
        table = "user_subject"
      }
    ]
  }

  handler = {
    // Get the current user's ID
    eval user_id = "auth:id"

    // Create a new record in the user_subject table
    add to user_subject {
      input = {
        user_id = "user_id"
        subject_id = "input:subject_id"
      }
      output = {
        name = "user_subject"
      }
    }
  }
}