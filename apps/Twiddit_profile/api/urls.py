from django.urls import path
from apps.Twiddit_profile.api.views import *

urlpatterns = [
    path('<pk>', GetUserInfo.as_view())
]
