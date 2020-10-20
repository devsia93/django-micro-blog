from django import forms
from blog.models import Tag
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):


    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                   'slug':forms.TextInput(attrs={'class':'form-control'})}
                   

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('This name for slug should be changed. Name \'create\' already reserved the system.')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('This tag already exists.')
        return new_slug