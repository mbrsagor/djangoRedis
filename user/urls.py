from django.urls import path
from .views import UserRegisterView, RetrieveUserAPIView

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('me/', RetrieveUserAPIView.as_view()),
]
