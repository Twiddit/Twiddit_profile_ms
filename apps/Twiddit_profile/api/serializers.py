from apps.Twiddit_profile.models import *

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('id', 'created_at', 'updated_at', 'deleted_at', 'password',)