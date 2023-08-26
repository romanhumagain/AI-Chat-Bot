from django.urls import path
from .views import chatbot , LoginView , register_user , logout_user
# creating the url pattern for this app

urlpatterns = [
  path('chatbot/' ,chatbot , name='chatbot' ),
  path('', LoginView.as_view() , name="login" ),
  path('register/', register_user , name="register" ),
  path('logout/', logout_user , name="logout" ),
]