from django.shortcuts import render
from Elearning import settings
# Create your views here.
from django.http import JsonResponse
import openai

def chat(request):
    openai.api_key = settings.OPENAI_API_KEY
    message = request.GET.get('message')
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "Your name is 'Vision' you are a helpful Tutor you help students who wants to learn English as their second language."},
            {"role": "user", "content": message},
        ]
    )
    return JsonResponse({'response': response['choices'][0]['message']['content']}, safe=False)

#Render another function to deal with html

def chat_view(request):
    return render(request, 'chatgpt/chat.html')
