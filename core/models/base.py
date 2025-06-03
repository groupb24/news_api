from django.db import models


class BaseModel(models.Model):
    """
    This is base model for all other models

    added fields:
      --added_at
      --update_at
    """
    added_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
