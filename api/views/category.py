from rest_framework.viewsets import ModelViewSet

import core.models as models
import api.permissions as perm
import api.serializers as serializer


class CategoryModelViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategorySerializer
    permission_classes = [perm.ManagerPermission]
