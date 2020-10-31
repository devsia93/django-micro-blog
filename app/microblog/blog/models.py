from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from transliterate import translit, get_available_language_codes
from time import time
# Create your models here.


def generation_slug(text):
    new_slug=slugify(translit(u"".join(text), 'ru', reversed=True))
    return new_slug


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=75, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True) #blank - поле может быть пустым
    date_pub = models.DateTimeField(auto_now_add=True) #автоматически заполняется при сохранении в бд
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generation_slug(self.title)
        super().save(*args, **kwargs)

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug':self.slug})
    
    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug':self.slug})

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug':self.slug})

    def __str__(self):
       return self.title

    def check_available_tag(self):
        if len(self.tags.all()) > 0:
            return True
        else :
            return False

class Tag(models.Model):
    title = models.CharField(max_length=15)
    slug = models.SlugField(max_length=25, unique=True)

    def __str__(self):
        return self.title

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug':self.slug})

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug':self.slug})
