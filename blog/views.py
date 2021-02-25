from django.shortcuts import render , get_object_or_404
from .models import Blog , Tag , Category , Comments
from .forms import CommentForm
# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all()


    context = {
        "blogs":blogs
    }

    return render(request,"blog/blog_list.html",context)

def blog_detail(request,id):
    blog = Blog.objects.get(id=id)
    tags = Tag.objects.all().filter(blogs=blog)
    recents = Blog.objects.all().order_by("-created_at")[:4]
    categories = Category.objects.all()
    comments = Comments.objects.all().filter(blog=blog)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_email = form.cleaned_data["email"]
            new_message = form.cleaned_data["message"]

            new_comment = Comments(blog=blog,name=new_name,email=new_email,message=new_message)
            new_comment.save()

    context = {
        "blog":blog,
        "tags":tags,
        "recents":recents,
        "categories":categories,
        "comments":comments,
    }
    return render(request,"blog/blog_detail.html",context)

def blog_tag(request,tag):
    blogs = Blog.objects.filter(tags__slug=tag)
    context = {
        "blogs":blogs
    }
    return render(request,"blog/blog_list.html",context)

def blog_category(request,category):
    blogs = Blog.objects.filter(category__slug=category)
    context = {
        "blogs":blogs
    }
    return render(request,"blog/blog_list.html",context)