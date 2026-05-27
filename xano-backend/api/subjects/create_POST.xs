// POST a new subject
api subjects/ {
  method = "POST"
  description = "Create a new subject"

  input = {
    fields = [
      {
        name = "name"
        type = "text"
        required = true
      },
      {
        name = "description"
        type = "text"
      },
      {
        name = "teacher_id"
        type = "int"
        required = true
      }
    ]
  }

  output = {
    fields = [
      {
        name = "subject"
        type = "table"
        table = "subject"
      }
    ]
  }

  handler = {
    // Create a new record in the subject table
    add to subject {
      input = {
        name = "input:name"
        description = "input:description"
        teacher_id = "input:teacher_id"
      }
      output = {
        name = "subject"
      }
    }
  }
}