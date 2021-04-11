from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Rasm')
    title = models.CharField(max_length=30)
    price = models.IntegerField(verbose_name='Narxi', default=0)
    body = models.TextField()
    data = models.DateField(auto_now=True)


    def __str__(self):
        return self.title 
    
    class Meta:
        ordering = ['id']
        managed = True
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'