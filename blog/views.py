from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import Forms

# Create your views here.
def index(request):
    return HttpResponse("this is main page of site")
def form(request):
    text = request.GET.get('text',None)
    return render(request,template_name='Posts/form.html',context={'txt':text})
def create(request):

    if request.method=="POST":
        form_post = Forms(request.POST)
        if form_post.is_valid():
            print("valid")
            form_post.save(commit=True)
            return HttpResponseRedirect('posts')
    else:

         form_post=Forms()
    return render(request, template_name='Posts/create.html', context={'field': form_post})


def update(request):
    return HttpResponse("this command will update psts on database")
def delete(request):
    return HttpResponse("this command will delete posts from database")
def detail(request,pk):
    post=Post.objects.get(pk=pk)
    return render(request,template_name="Posts/detail.html",context={'post':post})
def req_det(request):
    post=Post.objects.all()
    return render(request, template_name="Posts/post.html", context={'posts': post})