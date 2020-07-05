from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name='Kateqoriya'


class Post(models.Model):
    category=models.ManyToManyField(Category)
    titles=models.CharField(max_length=120,blank=False,verbose_name="Bashliq")
    content = models.TextField(blank=False,verbose_name="Mezmun")
    draft=models.BooleanField(default=False,verbose_name="Qaralama olaraq yadda saxlanilsin?")

    create_time = models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titles
    class Meta:
        verbose_name = "Paylaşım"
        verbose_name_plural = "Paylaşımlar"
        ordering=['-create_time']

class Drafts(models.Model):
    drafts=models.ManyToManyField(Post)
