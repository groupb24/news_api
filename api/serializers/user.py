from api.serializers.base import *


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "id", "first_name", "last_name",
            "username", "password"
        )
