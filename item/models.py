from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='itemOwner')
    item_name = models.CharField(max_length=120)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    item_image = models.URLField(max_length=220)

    def __str__(self):
        return self.item_name[:30]
