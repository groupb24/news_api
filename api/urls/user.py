from django.urls import path
from rest_framework.routers import DefaultRouter

import api.views.user as views

router = DefaultRouter()
router.register("user/create", views.UserCreateMixin)

urlpatterns = [
                  path("user/get-me", views.GetMeAPIView.as_view())
              ] + router.urls
