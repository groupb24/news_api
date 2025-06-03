from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

import core.models as models
import api.permissions as perms
import api.serializers as serializer


class NewsModelViewSet(ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializer.NewsSerializer
    permission_classes = [perms.ManagerPermission]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views_count += 1
        instance.save()
        return Response(self.get_serializer(instance).data)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
