from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reports/', views.reports, name='reports'),
    # Post api endpoint
    path('post/', views.PostAPIView.as_view()),
    path('post/delete/<int:pk>/', views.PostAPIView.as_view()),
]
