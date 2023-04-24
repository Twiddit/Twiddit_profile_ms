from django.urls import path
from apps.Twiddit_notifications.api.views import *

urlpatterns = [
    path('<int:id>', GetNotifications.as_view()),
    path('createNotification/', CreateNotification.as_view())
]
