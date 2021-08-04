from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response

from .models import Post, Report
from .serializers import PostSerializer, ReportSerializer
from .utils import post_validation_service
from .custom_response import *


def index(request):
    return render(request, 'feedapp/index.html')


def reports(request):
    return render(request, 'feedapp/reports.html')


class PostAPIView(views.APIView):

    def get_object(self, pk):
        try:
            return Post.objects.filter(id=pk).first()
        except Post.DoesNotExist:
            return None

    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        if not serializer:
            return Response(serializer.default_empty_html, status=status.HTTP_204_NO_CONTENT)
        elif serializer or post:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        validate_error = post_validation_service(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=status.HTTP_400_BAD_REQUEST)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        post = self.get_object(pk)
        if post is not None:
            post.delete()
            return Response(prepare_success_response("Data deleted successfully"), status=status.HTTP_200_OK)
        else:
            return Response(prepare_error_response("Content Not found"), status=status.HTTP_400_BAD_REQUEST)
