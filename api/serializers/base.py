from rest_framework import serializers

import core.models as models


class BaseModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["added_at"] = instance.added_at.strftime("%Y-%m-%d %H:%M")
        data["update_at"] = instance.update_at.strftime("%Y-%m-%d %H:%M")
        return data


class CategoryRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("id", "name")


class UserRelatioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ("id", "username")
