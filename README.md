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
### List all boxes
*GET* /view/box
### List all products
*GET* /view/product
### List all instructions
*GET* /view/instruction
### Resume instructions
*GET* /resume
Returns:
```json
{
  "action": "take | put",
  "name": "Banana",
  "quantity": 1,
  "box": "O.1"
}
```
### Take products from box
*POST* /take
```json
{
  "id": "O.1",
  "name": "Banana",
  "quantity": 1
}
```
Returns:
```json
{
  "action": "take | put",
  "name": "Banana",
  "quantity": 1,
  "box": "O.1",
  "error": "true | false"
}
```
### Put products to a box
*POST* /put
```json
{
  "id": "O.1",
  "name": "Banana",
  "quantity": 1
}
```
Returns:
```json
{
  "action": "take | put",
  "name": "Banana",
  "quantity": 1,
  "box": "O.1",
  "error": "true | false"
}
```
### Create test scenario
*POST* /test
