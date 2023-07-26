from rest_framework.views import APIView
from facebook.models import User
from facebook.serializer.request import LoginUserRequest
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


class LoginUserView(APIView):

    def post(self, request):
        serializer = LoginUserRequest(data=request.data)
        validation = serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        response_data = dict()
        user = authenticate(email=validated_data["email"], password=validated_data["password"])
        if user is None:
            response_data["message"] = "Invalid credentials"
            response_data["success"] = False
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)

        token_obj, created = User.get_token(user)
        response_data["token"] = token_obj.key
        response_data["success"] = True
        response_data["message"] = "User logged-in successfully"
        return Response(response_data, status=status.HTTP_200_OK)
