from django.db import models
from django.contrib.auth.models import User


class DomainEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(DomainEntity):
    name = models.CharField(max_length=120)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='main_category', blank=True, null=True)

    def __str__(self):
        return self.name[:30]

    class Meta:
        ordering = ['-id']

    def get_children(self):
        return Category.objects.filter(parent=self)

    def children_count(self):
        return Category.objects.filter(parent=self).count()


class Tag(DomainEntity):
    name = models.CharField(max_length=120)


class Item(DomainEntity):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='itemOwner')
    item_name = models.CharField(max_length=120)
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='itemCategory')
    price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, related_name='courses')
    item_image = models.URLField(max_length=220)

    def __str__(self):
        return self.item_name[:30]
