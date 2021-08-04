from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response

from .models import Post, Report
from .serializers import PostSerializer, ReportSerializer


def index(request):
    return render(request, 'feedapp/index.html')


def reports(request):
    return render(request, 'feedapp/reports.html')


class PostAPIView(views.APIView):
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
        pass
