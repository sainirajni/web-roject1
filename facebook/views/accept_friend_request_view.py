from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from facebook.models import Connections


class AcceptFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        response_data = dict()
        qs = Connections.objects.filter(id=pk)
        if not qs.exists():
            response_data["message"] = "Invalid Id"
            response_data["success"] = False
            return Response(response_data, status=status.HTTP_409_CONFLICT)

        instance = qs[0]
        instance.status = Connections.Status.ACCEPT.value
        instance.save()
        response_data["success"] = True
        response_data["message"] = "Friend request accepted"
        return Response(response_data, status=status.HTTP_200_OK)
