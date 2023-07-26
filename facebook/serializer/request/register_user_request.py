from rest_framework import serializers


class RegisterUserRequest(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128)
    first_name = serializers.CharField(max_length=150, allow_null=True, allow_blank=True, required=False)
    last_name = serializers.CharField(max_length=150, allow_null=True, allow_blank=True, required=False)
