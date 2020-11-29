# API:

## All responses for create objects will be contains this format:
```json
{"successfully":true}
```
or
```json
{"successfully":false}
```


## Get all posts:
```[GET] [protocol]://www.[domain_name]:[port]/blog/api/posts/```

### Example body response:
```json
[
    {
		"id": 11,
		"tags": [
			{
				"title": "django",
				"slug": "django"
			}
		],
		"title": "Some titlle",
		"slug": "some-titlle",
		"_body_rendered": "some body",
		"body": "some body",
		"date_pub": "2020-11-09T14:00:53.822745Z"
	},
	{
		"id": 7,
		"tags": [
			{
				"title": "chess",
				"slug": "chess"
			},
			{
				"title": "django",
				"slug": "django"
			},
			{
				"title": "framework",
				"slug": "framework"
			}
		],
		"title": "First post. Это первый пост. Hello",
		"slug": "first-post-1",
		"_body_rendered": "Тут какой-то текст, пока не будем углубляться...update test",
		"body": "Тут какой-то текст, пока не будем углубляться...update test",
		"date_pub": "2020-10-21T19:06:44.296730Z"
	}
]
```


## Get post within contains 'id_post':
```[GET] [protocol]://www.[domain_name]:[port]/blog/api/posts/<int:id_post>/```

### Example body response:
```json
{
	"id": 11,
	"tags": [
		{
			"title": "django",
			"slug": "django"
		}
	],
	"title": "Some titlle",
	"slug": "some-titlle",
	"_body_rendered": "some body",
	"body": "some body",
	"date_pub": "2020-11-09T14:00:53.822745Z"
}
```


## Get all tags:
```[GET] [protocol]://www.[domain_name]:[port]/blog/api/tags/```

### Example body response:
```json
[
	{
		"title": "chess",
		"slug": "chess",
		"id": 5
	},
	{
		"title": "django",
		"slug": "django",
		"id": 1
	},
	{
		"title": "framework",
		"slug": "framework",
		"id": 3
	}
]
```


## Get tag within contains 'id_tag':
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

### Example body request for tag creating:
```json
    {
	"title":"test-api",
	"slug":"test-api"
    } 
```


## Get all comments:
```[GET] [protocol]://www.[domain_name]:[port]/blog/api/comments/```

### Example body response:
```json
[
    {
		"author_name": "ivan",
		"text": "Cheer!",
		"date_pub": "2020-11-24T19:57:32.811897Z",
		"post": 18,
        "id":2
	},
	{
		"author_name": "ivan",
		"text": "It's quite hard to understand what is happening here, it seems that there is an indent block...",
		"date_pub": "2020-11-24T20:37:49.769463Z",
		"post": 17,
        "id":3
	}
]
```


## Get comment within contains 'id_comment':
```[GET] [protocol]://www.[domain_name]:[port]/blog/api/comments/<int:id_comment>/```

### Example response body:
```json
{
	"author_name": "api",
	"text": "test post",
	"date_pub": "2020-11-28T20:41:52.255696Z",
	"post": 18,
	"id": 22
}
```


## Create comment, where 'pk' == id_post:
```[POST] [protocol]://www.[domain_name]:[port]/blog/api/comments/<pk>/create```

### Example request body:
```json
{
	"author_name":"api", 
	"text":"test post"
}
```