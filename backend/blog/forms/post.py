from django import forms

from blog.models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'body', 'tags')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean_slug_self(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug in IGNORE_SLUGS:
            raise ValidationError(
                'This name of slug should be changed. Name \'create\' already reserved the system.')

        return new_slug
