// DELETE a subject
api subjects/{id} {
  method = "DELETE"
  description = "Delete a subject"

  input = {
    fields = [
      {
        name = "id"
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
    // Delete the record from the subject table
    delete from subject {
      input = {
        id = "input:id"
      }
    }
    return {
      success = true
    }
  }
}