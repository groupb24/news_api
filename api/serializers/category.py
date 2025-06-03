from api.serializers.base import *


class CategorySerializer(BaseModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"
