from rest_framework import serializers


class UserFriendListResponse(serializers.Serializer):
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    user_name = serializers.CharField(max_length=255, allow_null=True, allow_blank=True, required=False)
    friend_id = serializers.IntegerField()
    friend_name = serializers.CharField(max_length=255, allow_null=True, allow_blank=True, required=False)
