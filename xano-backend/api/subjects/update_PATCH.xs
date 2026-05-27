// PATCH (update) a subject
api subjects/{id} {
  method = "PATCH"
  description = "Update a subject"

  input = {
    fields = [
      {
        name = "id"
        type = "int"
        required = true
        from = "path"
      },
      {
        name = "name"
        type = "text"
      },
      {
        name = "description"
        type = "text"
      },
      {
        name = "teacher_id"
        type = "int"
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
    // Edit the record in the subject table
    edit from subject {
      input = {
        id = "input:id"
        fields = {
          name = "input:name"
          description = "input:description"
          teacher_id = "input:teacher_id"
        }
      }
      output = {
        name = "subject"
      }
    }
  }
}