from django.db import models


class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    sub_description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


