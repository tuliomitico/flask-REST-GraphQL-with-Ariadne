# flask-REST-GraphQL-with-Ariadne

A Flask App build with REST using SQLALchemy and MarshMallow and GraphQL using Ariadne.

## Running locally
To run this project in your machine assure that you have Python and any Flask 1.1.x to run it.
## Docs

The route to access the docs of this project while running locally is `http://localhost:5000/rapidoc`.

They were generated with `flask-smorest`

## Dependencies

- `Flask`
- `SQLALchemy`
- `marshmallow`
- `flask_marshmallow`
- `Ariadne`
- `flask-smorest`

## Inspiration

it was heavily inspired by the video of RocketSeat Youtube channel: [GraphQL e Rest na mesma aplicação? Como utilizar? - Code/drops #96](https://youtu.be/2KmrpT5dDbo)

## Routes

|Methods| Rule | Desc |
|:---:|:---:|:---:|
GET   |   /openapi.json | JSON to mount the docs
GET   |   /rapidoc      | The docs of the project rendered in Rapidoc Style |
GET   |   /graphql | The GraphQL PlayGround
POST  |   /graphql | The GraphQL route
GET   |   /posts/user/<int:id> | Get posts made for a specified user ID
POST  |   /users | The subscribed users
GET   |   /posts | List all the posts made for all users
GET   |   /      | Welcome to the project