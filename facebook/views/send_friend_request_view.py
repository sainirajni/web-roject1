from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from facebook.models import User, Connections
from facebook.serializer.request import SendFriendRequest
from datetime import datetime, timedelta


class SendFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SendFriendRequest(data=request.data)
        validation = serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        response_data = dict()

        if not User.objects.filter(id=validated_data["friend_id"]).exists():
            response_data["message"] = "Invalid Friend Id"
            response_data["success"] = False
            return Response(response_data, status=status.HTTP_409_CONFLICT)

        dt_min_ago = datetime.now() - timedelta(minutes=1)
        friend_request_count = Connections.objects.filter(
            user=request.user,
            created_at__gte=dt_min_ago
        ).count()
        if friend_request_count >= 3:
            response_data["message"] = "You can not send more than 3 friend request within a minute"
            response_data["success"] = False
            return Response(response_data, status=status.HTTP_409_CONFLICT)

        instance = Connections(
            user=request.user,
            friend_id=validated_data["friend_id"],
            status=Connections.Status.PENDING.value
        )
        instance.save()
        response_data["success"] = True
        response_data["message"] = "Friend request sent"
        return Response(response_data, status=status.HTTP_200_OK)
