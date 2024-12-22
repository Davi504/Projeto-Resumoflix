# url - view - template


from django.urls import path, include
from .views import Homefilmes, Homepage



urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path ('filmes/', Homefilmes.as_view()),
]