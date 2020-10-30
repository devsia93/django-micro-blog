from djanYou need to define a name for your url. It's better.

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]

Like this, in your template, you can use this name on url tag

<h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>

First info (with name define for url)

    The first argument is a url() name. It can be a quoted literal or any other context variable.

Second info (In your case, url without name)

    If you’d like to retrieve a namespaced URL, specify the fully qualified name:

    {% url 'myapp:view-name' %}
go.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
