from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

#URLs for our API. Django Rest Framework includes a router system to define readable URLs that map to the API's ViewSets.

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('api/', include(router.urls)),
]

