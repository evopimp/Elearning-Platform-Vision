from blog.models import Post
from django.contrib.auth.models import User

def create_post(username, title):
    try:
        user = User.objects.get(username=username)
        post = Post(title=title, 
                    
                    content ='n this example, the create_post function takes three arguments: username, title, and content. It retrieves the user based on the provided username, creates a new Post object, assigns the user as the author, saves the post to the database, and prints a success message.',

                      author=user)
        post.save()
        print("Post created successfully!")
    except User.DoesNotExist:
        print(f"User '{username}' does not exist.")
