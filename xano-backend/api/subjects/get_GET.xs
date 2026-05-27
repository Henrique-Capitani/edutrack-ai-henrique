// GET a single subject by ID
api subjects/{id} {
  method = "GET"
  description = "Get a single subject by ID"

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
        name = "subject"
        type = "table"
        table = "subject"
      }
    ]
  }

  handler = {
    // Get the record from the subject table
    get from subject {
      input = {
        id = "input:id"
      }
      output = {
        name = "subject"
      }
    }
  }
}