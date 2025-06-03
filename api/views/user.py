from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

import api.serializers as serializer
import core.models as models


class UserCreateMixin(CreateModelMixin, GenericViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializer.UserSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data.get("password")
        user = serializer.save()
        user.set_password(password)
        user.save()


class GetMeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        data = serializer.UserSerializer(user).data
        return Response(data)
