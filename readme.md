# Title

# Description

- the function is invoked with an API gateway, using the put method
- writes to the users dynamodb with the info thats in the body of the api call
- use the `email`, `name`, and `phoneNumber` fields in the json

# Usage

sample command to add a user to the `users` dynamoDB:
`curl -X PUT -H "Content-Type: application/json" -d '{"email":"jack.durham.dev@gmail.com","name":"Jack Durham","phoneNumber": "2146822126"}' https://mnf2qsqt3m.execute-api.us-east-2.amazonaws.com/default/user`