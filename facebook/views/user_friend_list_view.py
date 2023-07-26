from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from facebook.models import Connections
from facebook.serializer.response import UserFriendListResponse
from django.db.models import F, CharField, Value
from django.db.models.functions import Concat


class UserFriendListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserFriendListResponse

    def get_queryset(self):
        queryset = Connections.objects.filter(
            user=self.request.user,
            status=Connections.Status.ACCEPT.value
        ).annotate(
            user_name=Concat(F("user__first_name"), Value(' '), F("user__last_name"), output_field=CharField()),
            friend_name=Concat(F("friend__first_name"), Value(' '), F("friend__last_name"), output_field=CharField()),
        )
        return queryset
