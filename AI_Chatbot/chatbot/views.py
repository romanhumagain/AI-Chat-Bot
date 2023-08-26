from django.shortcuts import render , redirect
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Chat
from django.contrib.auth import authenticate, login , logout
import os
import openai
from django.utils import timezone

# Create your views here.
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def ask_openai(message):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=message,
            max_tokens=50,
            temperature=0.4,
        )
        return response.choices[0].text.strip()
    except openai.error.RateLimitError:
        print("Rate Limit Error in ask_openai")
        raise
    except Exception as e:
        print("Unexpected error in ask_openai:", e)
        raise

def chatbot(request):
    chats = Chat.objects.filter(user = request.user)

    if request.method == "POST":
        print(f"POST Data: {request.POST}")
        
        message = request.POST.get('message')
        response = None

        try:
            response = ask_openai(message)
        except openai.error.RateLimitError:
            response = "We're currently on a limited OpenAI plan. For extended features and uninterrupted responses, please consider upgrading the API plan. Thanks for understanding!"
        except Exception as e:
            print(f"Error getting response from OpenAI: {e}")
            response = 'Failed to get response from OpenAI.'

        try:
            print(f"Message: {message}")
            print(f"Response: {response}")
            
            chat = Chat.objects.create(user=request.user, message=message, response=response, created_at=timezone.now()) 
            chat.save()
        except Exception as e:
            print(f"Error saving chat to database: {e}")
            return JsonResponse({'error': 'Failed to save chat.'})

        return JsonResponse({'message': message, 'response': response})

    return render(request, 'chatbot/chatbot.html', {'chats':chats})


class LoginView(View):
  def get(self, request):
    return render(request, 'chatbot/login.html' , {})
  def post(self , request):
    data = request.POST
    username = data.get('username')
    password = data.get('password')
            
    if not User.objects.filter(username=username).exists():
        messages.error(request ,'Invalid Username')
        return redirect('login')
                
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('chatbot')
    else:
        messages.error(request ,'Invalid Credentials')
        return redirect('login')
      
      
def register_user(request):
  
  if request.method == "POST":
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = User.objects.create(email = email , username = username)
    user.set_password(password)
    user.save()
    messages.success(request, 'your account has been created!')
    return redirect('login')
    
  return render(request , 'chatbot/register.html')

def logout_user(request):
  logout(request)
  return redirect('login')
    
    