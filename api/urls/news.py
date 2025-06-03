from rest_framework.routers import DefaultRouter

import api.views.news as views

router = DefaultRouter()
router.register("news", views.NewsModelViewSet)

urlpatterns = router.urls
