// Stores subject information 
table subject {

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
  
    text name filters=trim
    text? description filters=trim
  
    // Reference to the user that teaches the subject.
    int teacher_id? {
      table = "user"
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
  ]

  tags = ["edutrack-ia"]
  guid = "g8tpjso2orFaPgdxKGzuuR66M1l"
}