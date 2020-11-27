from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import Post, Tag, Comment
from .forms import CommentForm


class ObjectDetailMixin:
    model = None
    template = None
    comment_form = CommentForm()

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        if self.model.__name__.lower() == "post":
            return render(request, self.template, context={self.model.__name__.lower():obj, 'admin_object':obj, 'detail':True, 'comment_form':self.comment_form})
        else:
            return render(request, self.template, context={self.model.__name__.lower():obj, 'admin_object':obj, 'detail':True})

    def post(self, request, slug):
        bound_form = CommentForm(data=request.POST)        
        if (bound_form.is_valid()):
            new_comment = bound_form.save(commit=False)
            new_comment.post = get_object_or_404(Post, slug=slug)
            new_comment.save()
            return redirect(request.path_info)
        return render(request, self.template, context={'comment_form':bound_form})


class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form':form})

    def post(self, request):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form':bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None 

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form':bound_form, self.model.__name__.lower():obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form:':bound_form, self.model.__name__.lower():tag})


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower():obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
