from core.models.base import *


class Bookmark(BaseModel):
    user = models.ForeignKey("CustomUser", on_delete=models.SET_NULL, null=True, related_name="news")
    news = models.ForeignKey("News", on_delete=models.CASCADE, related_name="my_news")

    class Meta:
        ordering = ("-id",)
