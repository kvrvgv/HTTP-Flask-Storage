

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
Password = Login

|    Login    | Password |                              SHA-256                               |
|:-----------:|:--------:|:------------------------------------------------------------------:|
|    admin    |  admin   |  8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918  |
|   kvrvgv    |  kvrvgv  |  dc388534fda69a2a45898a068af466eaefb9b2c2d8199f98a96ae97e042a3982  |

## Preloaded Files
Original files extension - **\*.jpg**

| id  | Owner  |                            File name                             |
|:---:|:------:|:----------------------------------------------------------------:|
|  1  | kvrvgv | 3013de3845828533e40291243447b2851986778aafeceffd7b9435161cf31e01 |
|  2  | kvrvgv | e13479b8e85a78677481839191a43526810b30af91a17e08f7acdce45689be8d |
|  3  | admin  | 5fd5ddaf20056147520c6c5355efb57fd5c0eacb0eb56fcbdf3a7f689c971e58 |
|  4  | admin  | 65637d35ec2a9cb567f8cd34b22af4490568e504593bcd471946405f6079e36a |

