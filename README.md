# starthack18

# API: http://130.82.5.194:8000


## REST API
| Path                        | Method   | Data                | Description |
| --------------------------- | -------- | --------------------| --------------- |
| `/users/:id`                | PUT      | JSON of user<sup>[1]</sup>        | Change user object |
| `/users/:id`                | GET      |                     | Returns user object |
| `/users/:id`                | DELETE   |                     | Delete user object |
| `/users`                    | GET      |                     | Get list of all users |
| `/users`                    | POST     | JSON of user<sup>[1]</sup>        | Register new user |
| | | | |
| `/cars`                    | GET     |        | Get all cars |
| `/cars`                    | POST     | JSON of car<sup>[2]</sup>        | Create new car |
| `/cars/:id`                | PUT      | JSON of car<sup>[2]</sup>        | Change car object |
| `/cars/:id`                | GET      |                     | Returns car object |
| `/cars/:id`                | DELETE   |                     | Delete car object |
| `/cars/unlock/:car/:user`  | PUT   |                     | Unlock a car |
| `/cars/lock/:car/:user`  | PUT   |                     | Lock a car |
| `/cars/reserve/:car/:user`  | PUT   |                     | Reserve a car | 
| | | | |
| `/game/scores`                    | GET     |        | Get all user scores |
| `/game/scores`                    | PUT     | Json with user_id and score | Update the score of a user |
| `/game/leaderboard/:nr`             | GET     |           | Get the top x of the leaderboard |

[1] User JSON contains first_name, last_name, age, gender and email   
[2] Car contains model, location (`"x,y"`) and icon



## Car websocket
All cars are kindly requested to open a websocket to `/carsws/:car_id`. Messages are sent when a user unlocks a car.

### Websocket message types
Messages over the WebSocket are in json. The following message types exist:


| Message type | Required fields | Send by app/backend |
| ------- | --- | ---- |
| update_score | user_id, score | app |
| new_location | location | app |
| end_trip |  | app |
| encounter | model, score | backend |
| unlock | user | backend |
| lock | | backend |

Example message: 
```json
{
  "type": "update_score",
  "user_id": 1,
  "score": 520
  }
```
