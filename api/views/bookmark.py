from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

import core.models as models
import api.serializers.bookmark as serializer


class BookmarkAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=serializer.BookmarkSerializer
    )
    def post(self, request):
        data = request.data
        user = request.user
        news = models.Bookmark.objects.filter(user=user, news_id=data.get("news"))
        if news.exists():
            news.delete()
            return Response({'status': 'unsaved'})
        else:
            models.Bookmark.objects.create(
                user=user,
                news_id=data.get("news")
            )
            return Response({'status': 'saved'})
