from django.db import models


class Category(models.Model):

    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank=True)
    image = models.ImageField()
    parent = models.ManyToManyField('self',on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name

    