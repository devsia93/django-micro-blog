from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from precise_bbcode.fields import BBCodeTextField

from transliterate import translit, get_available_language_codes
from time import time
import datetime


def generation_slug(text):
    new_slug = slugify(translit(u"".join(text), 'ru', reversed=True))
    return new_slug


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=75, blank=True, unique=True)
    body = BBCodeTextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    image = models.ImageField(upload_to='post-title', blank=True)

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
        for i in self.comments.all():
            if i.approved_comment:
                result += 1
        return result

    class Meta:
        ordering = ['-date_pub']


class Tag(models.Model):
    title = models.CharField(max_length=15)
    slug = models.SlugField(max_length=25, unique=True)

    def __str__(self):
        return self.title

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']


class Comment(models.Model):
    author_name = models.CharField(max_length=15, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = BBCodeTextField()
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return str(self.text)

    class Meta:
        ordering = ['approved_comment', 'date_pub']
