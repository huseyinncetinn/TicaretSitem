from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify



# Create your models here.

class Kategori(models.Model):
    isim = models.CharField(max_length=50)
    resim = models.FileField(upload_to ='urunler/')
    slug = models.SlugField(null=True , unique = True , blank = True ,editable = False) 
    stok = models.FloatField()

    
    def save(self, *args , **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args , **kwargs)

    def __str__(self):
        return self.isim + ' ' + str(self.id)

class AltKategori(models.Model):
    isim = models.CharField(max_length = 50)
    slug = models.SlugField(null=True , unique = True , blank = True ,editable = False)
    stok = models.FloatField()


    def save(self, *args , **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args , **kwargs)
    
    def __str__(self):
        return self.isim

class Urun(models.Model):
    olsturan = models.ForeignKey(User , on_delete = models.CASCADE , null = True)
    kategori = models.ForeignKey(Kategori , on_delete =models.CASCADE , null=True)
    altkategori = models.ForeignKey(AltKategori , on_delete = models.CASCADE , null=True)
    isim = models.CharField(max_length = 100)
    aciklama = models.TextField(max_length = 500)
    resim = models.FileField(upload_to = 'urunler/')
    fiyat = models.IntegerField(null=True)
    stok = models.IntegerField()
    slug = models.SlugField(null=True , unique = True , blank = True ,editable = False) 

    def save(self , *args , **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args , **kwargs)
    
    def __str__(self):
        return self.isim 

class Sepet (models.Model):
    urun = models.ForeignKey(Urun , on_delete = models.CASCADE)
    kullanici = models.ForeignKey(User , on_delete = models.CASCADE)
    sepetAdet = models.IntegerField()
    sepetFiyat = models.FloatField() 

    def __str__(self):
        return self.urun.isim    

class Favori(models.Model):
    urun = models.ForeignKey(Urun , on_delete = models.CASCADE)
    kullanici = models.ForeignKey (User , on_delete = models.CASCADE)
    
class Yorum(models.Model):
    urun = models.ForeignKey(Urun , related_name='yorum' , on_delete=models.CASCADE)
    yorum = models.TextField(max_length=400 , verbose_name='yorum')
    yorumTarih = models.DateTimeField(auto_now_add=True)
    kullanici = models.ForeignKey(User , null=True , on_delete=models.CASCADE)

    def __str__(self):
        return self.urun.isim         
