from rest_framework import views, status
from rest_framework.response import Response

from .models import Category, Tag, Item
from .serializers import CategorySerializer
from .prepare_response import prepare_success_response
from .utils import Res


class CategoryListCreateAPIView(views.APIView):

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        # caches = Res.set("API", serializer)
        return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)

    def post(self, request):
        pass
