# MoveMyBanana
## API
### Create a box
*POST* /create/box
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
*GET* /view/box
### Create an instruction
*POST* /create/instruction
```json
{
  "action": "take | drop",
  "name": "Banana",
  "quantity": 1,
  "box": "O.1"
}
```
### List all instructions
*GET* /view/instruction
### Set distance in between boxes
*POST* /distance
```json
{
  "box1": "O.1",
  "box2": "D.1",
  "distance": 1.0
}
```
