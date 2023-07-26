from rest_framework import serializers


class SendFriendRequest(serializers.Serializer):
    friend_id = serializers.IntegerField()
