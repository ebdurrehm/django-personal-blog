from django.db import models
from django.utils.text import slugify




class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name='Kateqoriya'


class Post(models.Model):
    category=models.ManyToManyField(Category)
    titles=models.CharField(max_length=120,blank=False,verbose_name="Bashliq")
    slugfy = models.SlugField(max_length=123, editable=False, null=False, unique=True)
    content = models.TextField(blank=False,verbose_name="Mezmun")
    image = models.ImageField(blank=True,verbose_name='məqalə üçün şəkil')
    draft=models.BooleanField(default=False,verbose_name="Qaralama olaraq yadda saxlanilsin?")

    create_time = models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.titles

    def get_image_or_none(self):
        if self.image and hasattr(self.image,'url'):
            return self.image.url
        return None
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slugfy = slugify(self.titles)
        super(Post, self).save()

   



    class Meta:
        verbose_name = "Paylaşım"
        verbose_name_plural = "Paylaşımlar"
        ordering=['-create_time']

class Drafts(models.Model):
    drafts=models.ManyToManyField(Post)
