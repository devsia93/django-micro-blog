# API documentation:

# Invalid requests

## Example body response when [POST, DELETE] request have not contains token authorization:
```json
{
	"detail": "Authentication credentials were not provided."
}
```


## Example body response when post.slug(model) of [POST] request is equal to any post.slug in database:   
```json
{
	"slug": [
		"post with this slug already exists."
	]
}
```


## Example body response when [POST] request to create post with tag.id which without in database:
```json
{"tags":["Invalid pk \"234\" - object does not exist."]}
```


# Posts

## Get all posts:
```[GET] [protocol]://www.[domain_name]:[port]/blog/api/posts/```

### Example body response:
```json
[
	{
		"id": 24,
		"slug": "test-api",
		"title": "Test-api",
		"body": "test-api",
		"tags": [
			1,
			3
		],
		"date_pub": "2020-12-03T21:02:21.797154Z",
		"comments": []
	},
	{
		"id": 18,
		"slug": "new-record-rating-on-chesscom",
		"title": "New record rating on chess.com",
		"body": "Hello! My new rating on chess.com - 2200",
		"tags": [
			5
		],
		"date_pub": "2020-11-12T16:48:16.077142Z",
		"comments": [
			1,
			2,
			4,
			17,
			22,
			23
		]
	}	
]
```


## Get post within 'id_post':
```[GET] [protocol]://www.[domain_name]:[port]/blog/api/posts/<int:id_post>/```

### Example body response:
```json
{
	"id": 24,
	"slug": "test-api",
	"title": "Test-api",
	"body": "test-api",
	"tags": [
		1,
		3
	],
	"date_pub": "2020-12-03T21:02:21.797154Z",
	"comments": []
}
```


## Create new post:
```[POST] [protocol]://www.[domain_name]:[port]/blog/api/posts/```

### Example body request:
```json
{
	"slug": "test-api",
	"title": "test-api",
	"body": "test-api",
	"tags":["1","3"]
}
```

### Example body response:
```json
{"id":23,"slug":"test-api","title":"Test-api","body":"test-api","tags":[1,3],"date_pub":"2020-12-03T20:29:43.292398Z"}
```


## Delete post
```[DELETE] [protocol]://www.[domain_name]:[port]/blog/api/posts/<int:id_post>```

### Example body request:
This method have not request body.

### Example body response:
This method does not return data.


# Tags

## Get all tags:
```[GET] [protocol]://www.[domain_name]:[port]/blog/api/tags/```

### Example body response:
```json
[
	{
		"id": 1,
		"slug": "django",
		"title": "django"
	},
	{
		"id": 3,
		"slug": "framework",
		"title": "framework"
	}
]
```


## Get tag within 'id_tag':
```[GET] [protocol]://www.[domain_name]:[port]/blog/api/tags/<int:id_tag>/```

### Example body response:
```json
{
	"title": "django",
	"slug": "django",
	"id": 1
}
```


## Create tag:
```[POST] [protocol]://www.[domain_name]:[port]/blog/api/tags/create/```  

### Example body request:
```json
    {
	"title":"test-api",
	"slug":"test-api"
    } 
```

### Example body response:
```json
{
	"id": 14,
	"slug": "test-api",
	"title": "test-api"
}
```


## Delete tag
```[DELETE] [protocol]://www.[domain_name]:[port]/blog/api/tags/<int:id_tag>```

### Example body request:
This method have not request body.

### Example body response:
This method does not return data.


# Comments

## Get all comments:
```[GET] [protocol]://www.[domain_name]:[port]/blog/api/comments/```

### Example body response:
```json
[
   {
		"id": 1,
		"post": 1,
        "author_name": "Ivan",
        "text": "Cheers!",
        "date_pub": "2020-12-01T20:53:48.443631Z",
        "approved_comment": true
    },
    {
		"id": 2,
		"post": 1,
        "author_name": "Ivan",
        "text": "Congratulations!",
        "date_pub": "2020-12-01T20:54:04.905761Z",
        "approved_comment": true
    }
]
```


## Get comment within 'id_comment':
```[GET] [protocol]://www.[domain_name]:[port]/blog/api/comments/<int:id_comment>/```

### Example response body:
```json
{
	"id": 1,
	"post": 1,
    "author_name": "Ivan",
    "text": "Cheers!",
    "date_pub": "2020-12-01T20:53:48.443631Z",
    "approved_comment": true
}
```


## Create comment:
```[POST] [protocol]://www.[domain_name]:[port]/blog/api/comments/```

### Example request body:
```json
{
	"post":24,
	"author_name":"api", 
	"text":"test post"
}
```

### Example response body:
```json
{
	"id": 25,
	"author_name": "api",
	"text": "test post",
	"date_pub": "2020-12-03T21:51:47.930005Z",
	"approved_comment": false,
	"post": 24
}
```


## Delete comment:
```[DELETE] [protocol]://www.[domain_name]:[port]/blog/api/comments/<int:id_comment>```

### Example body request:
This method have not request body.

### Example body response:
This method does not return data.


## Update comment:
```[PATCH] [protocol]://www.[domain_name]:[port]/blog/api/comments/<int:id_comment>```

### Example body request:
```json
{
	"approved_comment": true
}
```

### Example body response:
```json
{
	"id": 9,
	"author_name": "test",
	"text": "test",
	"date_pub": "2020-11-26T18:33:35.574768Z",
	"approved_comment": true,
	"post": 17
}
```
