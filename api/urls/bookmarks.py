from django.urls import path

import api.views.bookmark as views

urlpatterns = [
    path("bookmark", views.BookmarkAPIView.as_view())
]
