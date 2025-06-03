from api.serializers.base import *


class NewsSerializer(BaseModelSerializer):
    class Meta:
        model = models.News
        exclude = ("author", "views_count")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["category"] = CategoryRelationSerializer(instance.category).data
        data["author"] = UserRelatioSerializer(instance.author).data
        return data
