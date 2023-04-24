from apps.Twiddit_notifications.models import *

from rest_framework import serializers

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        exclude = ('id', 'created_at', )

class CreateNotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        exclude = ('created_at', )