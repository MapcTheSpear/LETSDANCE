from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer, UserAuthSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from users.models import ConfirmationCode


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    User.objects.create_user(username=username, password=password, is_active=False)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def authorisation_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = authenticate(**serializer.validated_data)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED)


def user_confirm_api_view(request):
    code = request.data.get('code')
    try:
        confirmation_code = ConfirmationCode.objects.get(code=code)
        if confirmation_code.is_expired():
            return Response(data={"error": "Confirmation code has expired. Please register again."},
                            status=status.HTTP_400_BAD_REQUEST)
        user = confirmation_code.user
        user.is_active = True
        user.save()
        return Response(data={"message": "AYY, welcome, bro"},
                        status=status.HTTP_200_OK)
    except ConfirmationCode.DoesNotExist:
        return Response(data={"error": "NAAH, that's wrong code cuh"})
