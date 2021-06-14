from django.db import models
from django.shortcuts import reverse


class Tag(models.Model):
    title = models.CharField(max_length=15)
    slug = models.SlugField(max_length=25, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})
