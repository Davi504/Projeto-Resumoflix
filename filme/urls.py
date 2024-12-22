# url - view - template


from django.urls import path, include
from .views import Homefilmes, Homepage, DetalhesFilme



urlpatterns = [
    path('', Homepage.as_view(),),
    path ('filmes/', Homefilmes.as_view()),
    path ('filmes/<int:pk>/', DetalhesFilme.as_view()),
]