from rest_framework import views, status, permissions
from rest_framework.response import Response

from .serializer import UserAccountSerializer
from .models import UserAccount


# User custom registration
class UserRegisterView(views.APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        try:
            data = request.data
            name = data['name']
            email = data['email']
            email = email.lower()
            password = data['password']
            re_password = data['re_password']
            is_relator = data['is_relator']

            if is_relator == 'True':
                is_relator = True
            else:
                is_relator = False

            if password == re_password:
                if len(password) >= 8:
                    if not UserAccount.objects.filter(email=email).exists():
                        if not is_relator:
                            UserAccount.objects.create_user(name=name, email=email, password=password)
                            return Response(
                                {'success': 'User has been created successfully'},
                                status=status.HTTP_201_CREATED
                            )
                        else:
                            UserAccount.objects.create_relator(name=name, email=email, password=password)
                            return Response(
                                {'success': 'Relator account has been created successfully'},
                                status=status.HTTP_201_CREATED
                            )
                    else:
                        return Response(
                            {'error': 'use with the email already exists'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response(
                        {'error': 'password must be at least 8 numbers.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {'error': 'password do not match'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as e:
            print(e)
            return Response(
                {"error": f"Something went to wrong registering and account. Exception: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class RetrieveUserAPIView(views.APIView):
    def get(self, request):
        try:
            user = request.user
            serializer = UserAccountSerializer(user)
            return Response(
                {'user': serializer.data},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {"error": "Something went to wrong when user view profile"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
