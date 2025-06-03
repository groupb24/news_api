from django.urls import path, include

urlpatterns = [
    path("", include("api.urls.user")),
    path("", include("api.urls.news")),
    path("", include("api.urls.category")),
    path("", include("api.urls.bookmarks"))
]
