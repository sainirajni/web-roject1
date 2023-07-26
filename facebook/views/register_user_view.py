from rest_framework.views import APIView
from facebook.models import User
from facebook.serializer.request import RegisterUserRequest
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password


class RegisterUserView(APIView):

    def post(self, request):
        data = request.data
        post_data = dict(
            email=data["email"],
            password=data["password"],
            first_name=data.get("first_name") if data.get("first_name") else "",
            last_name=data.get("last_name") if data.get("last_name") else ""
        )
        serializer = RegisterUserRequest(data=post_data)
        validation = serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        response_data = dict()
        if User.objects.filter(email=validated_data["email"]).exists():
            response_data["message"] = "User with this email already exist"
            response_data["success"] = False
            return Response(response_data, status=status.HTTP_409_CONFLICT)

        user = User.objects.create(
            email=validated_data["email"],
            password=make_password(validated_data["password"]),
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            is_staff=False,
            is_superuser=False
        )
        token_obj, created = User.get_token(user)
        response_data["token"] = token_obj.key
        response_data["success"] = True
        response_data["message"] = "User successfully created"
        return Response(response_data, status=status.HTTP_201_CREATED)
