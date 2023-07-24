from django.urls import path

from . import views

urlpatterns = [
    path('chat/', views.chat_view, name='chat_view'),
    path('api/chat/', views.chat, name='chat'),
]
