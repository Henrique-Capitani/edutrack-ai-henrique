// Linking table for the many-to-many relationship between users and subjects.
table user_subject {

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }

    // Reference to the user.
    int user_id {
      table = "user"
    }

    // Reference to the subject.
    int subject_id {
      table = "subject"
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "user_id"}, {name: "subject_id"}]}
  ]

  tags = ["edutrack-ia"]
  guid = "g8tpjso2orFaPgdxKGzuuR66M1m"
}