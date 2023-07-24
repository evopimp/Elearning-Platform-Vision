from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer

# ViewSet which is a type of class-based View that provides default read and write operations.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


