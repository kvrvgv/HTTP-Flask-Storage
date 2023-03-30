

## Download
Authorization: not required

`GET /download/hash=abcdef123456`
#### Responses
- *200* (everything is OK)
- *418* (file with this hash doesn't exist)

## Upload
Authorization: Basic

`POST /upload`

`form-data: %filename%: %file$`
#### Responses
- *200* (everything is OK)
- *400* (file not attached)
- *401* (authorization required)
- *405* (method not allowed)

## Delete
Authorization: Basic

`GET /delete?hash=abcdef123456`
#### Responses
- *200* (everything is OK)
- *400* (bad hash argument or file not found)
- *401* (authorization required)
- *403* (not your file)

## Default Users
|    Login    | Password |                              SHA-256                               |
|:-----------:|:--------:|:------------------------------------------------------------------:|
|    admin    |  admin   |  8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918  |
|   kvrvgv    |  kvrvgv  |  dc388534fda69a2a45898a068af466eaefb9b2c2d8199f98a96ae97e042a3982  |

