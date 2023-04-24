from apps.Twiddit_notifications.models import *
from apps.Twiddit_notifications.api.serializers import *
from rest_framework import generics
from rest_framework.response import Response

class GetNotifications(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get(self, request, id): 
        qs = self.queryset.filter(followedId = id)
        serializer = self.serializer_class(qs, many = True)
        return Response(serializer.data)

class CreateNotification(generics.CreateAPIView): 
    serializer_class = CreateNotificationSerializer
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : f"Notificaion exitosa"})