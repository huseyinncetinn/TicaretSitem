from .models import *
from django.forms import ModelForm

class UrunForm(ModelForm):
    class Meta:
        model = Urun
        fields = ['kategori' ,'altkategori' , 'isim' , 'aciklama' , 'resim' , 'fiyat' , 'stok' ]
    def __init__(self , *args , **kwargs):
        super(UrunForm , self).__init__(*args ,**kwargs)
        for name , field in self.fields.items():
            field.widget.attrs.update({'class' : 'form-control'})  

class YorumForm(ModelForm):
    class Meta:
        model = Yorum
        fields = [
            'yorum'
        ]
    def __init__(self , * args , **kwargs):
        super(YorumForm , self ).__init__(*args , kwargs)
        for name , field in self.fields.items():
            field.widget.attrs.update({'class' : 'form-control'})                
