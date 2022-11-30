from django.contrib import admin
from .models import *

class ProfilAdmin (admin.ModelAdmin):
    list_display = ( 'isim' ,'slug', 'id'  )
    readonly_fields = ('slug',)
    search_fields = ('isim' ,)

# Register your models here.
admin.site.register(Urun,ProfilAdmin)
admin.site.register(Kategori,ProfilAdmin)
admin.site.register(AltKategori,ProfilAdmin)
admin.site.register(Sepet)
admin.site.register(Favori)
admin.site.register(Yorum)

