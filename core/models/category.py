from core.models.base import *


class Category(BaseModel):
    name = models.CharField(max_length=100)
    order_num = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order_num",)
