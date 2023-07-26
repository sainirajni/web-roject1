from rest_framework.generics import ListAPIView
from facebook.models import User
from facebook.serializer.response import UserListResponse
from rest_framework.permissions import IsAuthenticated
from django.core.validators import EmailValidator


class UserListView(ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = UserListResponse

    def get_queryset(self):
        queryset = User.objects.exclude(id=self.request.user.id)
        return queryset

    def filter_queryset(self, queryset):
        search_param = self.request.query_params.get('param')
        if search_param:
            if self.is_valid_email(search_param):
                queryset = queryset.filter(email__iexact=search_param)
            else:
                queryset = queryset.filter(first_name__icontains=search_param)
        return queryset

    def is_valid_email(self, email):
        try:
            validator_obj = EmailValidator()
            validator_obj(email)
            return True
        except Exception as e:
            print("Email validation error: ", str(e))
            return False


