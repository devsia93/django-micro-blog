from django import forms

from blog.models import Comment


class CommentForm(forms.ModelForm):
    author_name = forms.TextInput()
    text = forms.Textarea()

    class Meta:
        model = Comment
        fields = ['author_name', 'text']

        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-control',
                                                  'id': 'inlineFormInputGroup',
                                                  'placeholder': 'nickname',
                                                  'type': 'text'}),
            'text': forms.Textarea(attrs={'class': 'form-control',
                                          'aria-label': 'Comment',
                                          'type': 'text',
                                          'rows': 4})
        }
