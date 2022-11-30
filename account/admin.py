from django.contrib import admin

class ProfilAdmin (admin.ModelAdmin):
    list_display = ('isim' , 'slug' , )

# Register your models here.
