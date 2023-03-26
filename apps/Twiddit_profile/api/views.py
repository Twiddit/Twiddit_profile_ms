from apps.Twiddit_profile.models import *
from apps.Twiddit_profile.api.serializers import *
from rest_framework import generics
from rest_framework.response import Response

class GetUserInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer