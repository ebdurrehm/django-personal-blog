from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

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
        form_post = Forms(request.POST, files=request.FILES)
        if form_post.is_valid():
            print("valid")
            form_post.save(commit=True)
            messages.success(request,"ugurla yaradildi")

            return HttpResponseRedirect(reverse('post_detail', kwargs={'slugfy':form_post.instance.slugfy}))
    else:

         form_post=Forms()
    return render(request, template_name='Posts/create.html', context={'field': form_post})


def update(request,slugfy):
    post=get_object_or_404(Post,slugfy=slugfy)
    formup=Forms(instance=post)
    if request.method=='POST':
        formup=Forms(data=request.POST,instance=post, files=request.FILES)
        if formup.is_valid():
            formup.save(commit=True)
            return HttpResponseRedirect(reverse('post_detail', kwargs={'slugfy':formup.instance.slugfy}))
    return render(request,template_name='Posts/post_update.html',context={'form':formup})

    return HttpResponse("this command will update psts on database")
def delete(request,slugfy):
    post= get_object_or_404(Post,slugfy=slugfy)
    post.delete()
    return HttpResponseRedirect(reverse('posts'))

def detail(request,slugfy):
    post=Post.objects.get(slugfy=slugfy)
    return render(request,template_name="Posts/detail.html",context={'post':post})

def req_det(request):
    post=Post.objects.all()
    return render(request, template_name="Posts/post.html", context={'posts': post})

def trying(request):
    return render(request,template_name='Posts/try.html',context=None)
