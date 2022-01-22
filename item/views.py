from rest_framework import views, status
from rest_framework.response import Response

from .models import Category, Tag, Item


class CategoryListCreateAPIView(views.APIView):

    def get(self, request):
        pass
