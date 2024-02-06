from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    nama_category = models.CharField(max_length=255)
    
    def __str__(self) :
        return self.nama_category

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    deskripsi = models.TextField()
    tanggal = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='media/')
    slug = models.SlugField(unique=True, editable=False)
    total_views=models.PositiveIntegerField( default=0)

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save()
        
class Komentar(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='komentar')
    pengguna = models.ForeignKey(User, on_delete=models.CASCADE)
    isi_komentar = models.TextField()
    waktu_komentar = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    
class ArticleLike(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like')