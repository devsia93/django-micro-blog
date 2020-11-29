# API:

## All responses for create objects will be contains this format:
```json
{"successfully":true}
```
or
```json
{"successfully":false}
```

## Urls:

```[GET] [protocol]://www.[domain_name]:[port]/blog/api/posts/``` - get all posts.
## Example body response:
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

```[GET] [protocol]://www.[domain_name]:[port]/blog/api/posts/<int:id_post>/``` - get post within contains 'id_post'.
## Example body response:
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

```[GET] [protocol]://www.[domain_name]:[port]/blog/api/tags/``` - get all tags.
## Example body response:
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

```[GET] [protocol]://www.[domain_name]:[port]/blog/api/tags/<int:id_tag>/``` - get tag within contains 'id_tag'.
## Example body response:
```json
{
	"title": "django",
	"slug": "django",
	"id": 1
}
```

```[POST] [protocol]://www.[domain_name]:[port]/blog/api/tags/create/``` - create tag.  
## Example body request for tag creating:
```json
    {
	"title":"test-api",
	"slug":"test-api"
    } 
```

```[GET] [protocol]://www.[domain_name]:[port]/blog/api/comments/``` - get all comments.
## Example body response:
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

```[GET] [protocol]://www.[domain_name]:[port]/blog/api/comments/<int:id_comment>/``` - get comment within contains 'id_comment'.
## Example response body:
```json
{
	"author_name": "api",
	"text": "test post",
	"date_pub": "2020-11-28T20:41:52.255696Z",
	"post": 18,
	"id": 22
}
```

```[POST] [protocol]://www.[domain_name]:[port]/blog/api/comments/<pk>/create``` - create comment, where 'pk' == id_post.
## Example request body:
```json
{
	"author_name":"api", 
	"text":"test post"
}
```