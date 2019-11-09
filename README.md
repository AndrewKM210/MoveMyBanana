# MoveMyBanana
## API
### Create a box
*POST* /create
```json
{
  "id": "O.1 | D.1",
  "type": "origin | target",
  "posX": 0.0,
  "posY": 0.0,
  "products" : [
    {
        "name": "Banana",
        "quantity": 0
    }
  ]
}
```
### List all boxes
*GET* /view
