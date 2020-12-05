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



## Example body response when [GET] request to get post/tag/comment which without in database:
```json
{
    "detail": "Not found."
}
```



# Posts

## Get all posts:
```[GET] [protocol]://www.[domain_name]:[port]/blog/api/posts/```

### Example body response:
```json
[
	{
        "id": 12,
        "slug": "test-api",
        "title": "Test-api",
        "body": "test-api",
        "tags": [],
        "date_pub": "2020-12-03T20:10:03.508144Z",
        "comments": [
            7
        ]
    },
    {
        "id": 6,
        "slug": "test-test",
        "title": "Test test",
        "body": "test",
        "tags": [],
        "date_pub": "2020-12-01T21:06:00.541259Z",
        "comments": []
    }	
]
```



## Get all posts by 'id_tag':
```[GET] [protocol]://www.[domain_name]:[port]/blog/api/tags/<int:id_tag>/posts/```

```json
[	
	{
        "id": 1,
        "slug": "my-first-post",
        "title": "My first post",
        "body": "It's quite hard to understand what is happening here, it seems that there is static roots...",
        "tags": [
            2,
            3,
            1
        ],
        "date_pub": "2020-12-01T20:53:15.212776Z",
        "comments": [
            1,
            2,
            5,
            6
        ]
    }
]
```



## Get post by 'id_post':
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
{
	"id":23,
	"slug":"test-api",
	"title":"Test-api",
	"body":"test-api",
	"tags":[1,3],
	"date_pub":"2020-12-03T20:29:43.292398Z"
}
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



## Get tag by 'id_tag':
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
        "author_name": "Ivan",
        "text": "Cheers!",
        "date_pub": "2020-12-01T20:53:48.443631Z",
        "approved_comment": true,
		"post": 1
    },
    {
		"id": 2,
        "author_name": "Ivan",
        "text": "Congratulations!",
        "date_pub": "2020-12-01T20:54:04.905761Z",
        "approved_comment": true,
		"post": 1
    }
]
```



## Get all comments by 'id_post':
```[GET] [protocol]://www.[domain_name]:[port]/blog/api/posts/<int:id_post>/comments/```

### Example body response:
```json
[
   {
        "id": 1,
        "author_name": "Ivan",
        "text": "Cheers!",
        "date_pub": "2020-12-01T20:53:48.443631Z",
        "approved_comment": true,
        "post": 1
    },
    {
        "id": 2,
        "author_name": "Ivan",
        "text": "Congratulations!",
        "date_pub": "2020-12-01T20:54:04.905761Z",
        "approved_comment": true,
        "post": 1
    }
]
```
*this separation is needed to load less unnecessary data in different activities.



## Get comment by 'id_comment':
```[GET] [protocol]://www.[domain_name]:[port]/blog/api/comments/<int:id_comment>/```

### Example response body:
```json
{
	"id": 1,
	"author_name": "Ivan",
    "text": "Cheers!",
    "date_pub": "2020-12-01T20:53:48.443631Z",
    "approved_comment": true,
	"post": 1
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
