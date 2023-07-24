from blog.models import Post
from django.shortcuts import render

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'Elearning/post_list.html', {'posts': posts})