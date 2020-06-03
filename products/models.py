from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Категория')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = ['parent']
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    manufacturer = models.ForeignKey('Manufacturer',
                                     on_delete=models.CASCADE)
    img = models.ImageField()
    price = models.PositiveIntegerField()
    category = TreeForeignKey('Category', blank=True, null=True,
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.title
