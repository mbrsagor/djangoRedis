from django.urls import path
from .views import CategoryListCreateAPIView

urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view()),
]
