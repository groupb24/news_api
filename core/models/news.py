from core.models.base import *


class News(BaseModel):
    NEWS_STATUS = (
        ('pending', "Pending"),
        ('published', "Published")
    )
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL,
        null=True, related_name="news")
    image = models.ImageField(upload_to="news/%Y-%m-%d")
    title = models.CharField(max_length=255)
    post = models.TextField()
    status = models.CharField(max_length=100, choices=NEWS_STATUS, default="pending")
    author = models.ForeignKey(
        "CustomUser", on_delete=models.SET_NULL,
        null=True, related_name="my_news"
    )
    views_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-id",)
