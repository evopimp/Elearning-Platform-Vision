from django.shortcuts import render
from Elearning import settings
from typing import List, Dict
from django.http import JsonResponse
import openai

# Save the conversation history
with open("/Users/murad/Desktop/MyProject/Elearning/chatgpt/Prompt.txt", "r") as file:
    # Read the contents of the file
    text = file.read()

conversation_history: List[Dict[str, str]] = [
    {"role": "system", "content": text}]


# def chat(request):
#     openai.api_key = settings.OPENAI_API_KEY
#     # Retrieve the new message from the user
#     new_message = request.GET.get('hi')

#     # Add the new message to the conversation history
#     conversation_history.append({"role": "user", "content": new_message})

#     # Use the entire conversation history when generating a response
#     response_generator = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=conversation_history,
#         stream=True,
#     )

#     ai_response = None
#     for response in response_generator:

#         print(response) 
#         # Add the AI's response to the conversation history
#         ai_response = response['choices'][0]['message']['content']
#         conversation_history.append({"role": "assistant", "content": ai_response})

#     # If there was no response, return an empty JSON response
#     if ai_response is None:
#         return JsonResponse({}, safe=False)

#     # Return the AI's response as a JSON response
#     return JsonResponse({'response': ai_response}, safe=False)



def chat(request):
    openai.api_key = settings.OPENAI_API_KEY
    # Retrieve the new message from the user
    new_message = request.GET.get('message')

    # Add the new message to the conversation history
    conversation_history.append({"role": "user", "content": new_message})

    # Use the entire conversation history when generating a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        
    )

    # Add the AI's response to the conversation history
    ai_response = response['choices'][0]['message']['content']
    conversation_history.append({"role": "assistant", "content": ai_response})

    # Return the AI's response as a JSON response
    return JsonResponse({'response': ai_response}, safe=False)




# intial function for retrieval of the the data which is very premitive and will be discarted
# def chat(request):
#     openai.api_key = settings.OPENAI_API_KEY
#     message = request.GET.get('message')
#     response = openai.ChatCompletion.create(
#       model="gpt-3.5-turbo",
#       messages=[
#             {"role": "system", "content": "Your name is 'Vision' you are created by Murad an MSc Computer Science Student in Dundee university, you are a helpful Tutor you help students who wants to learn English as their second language, your main user are students whose mother tungue is Farsi/Persian and want to learn english, you try to read the context from the a ready made lessons which are structured ESL (english as a second language) in the Elearning platform and then help students understand those materials better, your secondry objective is to create a report on the students later on and send it to the teache this feature will be added later on  "},
#             {"role": "user", "content": message},
#         ]
#     )

#     return JsonResponse({'response': response['choices'][0]['message']['content']}, safe=False)

#rendering a chat.html located in this directroy just for testing purpose will be 
#deleted during producation and publication.

def chat_view(request):
    return render(request, 'chatgpt/chat.html')
