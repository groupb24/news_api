from api.serializers.base import *


class BookmarkSerializer(BaseModelSerializer):
    class Meta:
        model = models.Bookmark
        fields = ("news", )
