from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reports/', views.reports, name='reports'),
    # Post api endpoint
    path('post/', views.PostAPIView.as_view()),
    path('post/update/<int:pk>/', views.PostAPIView.as_view()),
    path('post/delete/<int:pk>/', views.PostAPIView.as_view()),
    # Report api endpoint
    path('report/', views.ReportAPIView.as_view()),
    path('report/delete/<int:pk>/', views.ReportAPIView.as_view()),
]
