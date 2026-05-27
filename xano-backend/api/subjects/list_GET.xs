// GET all subjects
api subjects/ {
  method = "GET"
  description = "Get all subjects"

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
    // Query all records from the subject table
    all from subject {
      output = {
        name = "subjects"
        fields = ["id", "name", "description"]
      }
    }
  }
}