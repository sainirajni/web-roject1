from django.urls import path
from facebook.views import (
    RegisterUserView,
    LoginUserView,
    UserListView,
    UserFriendListView,
    SendFriendRequestView,
    AcceptFriendRequestView,
    RejectFriendRequestView,
    PendingFriendRequestListView,
)


urlpatterns = [
    path("user/register", RegisterUserView.as_view(), name="register_user"),
    path("user/login", LoginUserView.as_view(), name="login_user"),
    path("users", UserListView.as_view(), name="user_listing"),
    path("friends", UserFriendListView.as_view(), name="user_friend_listing"),
    path("friends/request/send", SendFriendRequestView.as_view(), name="send_friend_request"),
    path("friends/request/<int:pk>/accept", AcceptFriendRequestView.as_view(), name="accept_friend_request"),
    path("friends/request/<int:pk>/reject", RejectFriendRequestView.as_view(), name="reject_friend_request"),
    path("friends/request/pending", PendingFriendRequestListView.as_view(), name="pending_friend_request_listing"),
]