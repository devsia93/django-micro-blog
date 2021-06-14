from django.db import models
from django.shortcuts import reverse

from precise_bbcode.fields import BBCodeTextField

from blog.utils import generation_slug


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=75, blank=True, unique=True)
    body = BBCodeTextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    image = models.ImageField(upload_to='post-title', blank=True)

    class Meta:
        ordering = ['-date_pub']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generation_slug(self.title)
        self.title = '. '.join(
            map(lambda s: s.strip().capitalize(), self.title.split('. ')))
        super().save(*args, **kwargs)

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def check_available_tag(self):
        if len(self.tags.all()) > 0:
            return True
        else:
            return False

    def get_all_comments(self):
        return self.comments

    def count_of_approved_comments(self):
        result = 0
        for comment in self.comments.all():
            if comment.is_approved:
                result += 1
        return result
