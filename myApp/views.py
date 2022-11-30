from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib import messages





# Create your views here.
def begen(request):
    urunid = request.POST['urunId']
    print(urunid) 
    favoriurun = Urun.objects.get( id = urunid)
    if Favori.objects.filter( urun = urunid ).exists():
        favori = Favori.objects.get( urun = urunid )
        favori.delete()
    else:
        favori = Favori( urun = favoriurun , kullanici = request.user ) 
        favori.save() 
def search (request):

   

    searched = ''
    urunler = ''
    if request.GET.get('searched'):
        searched = request.GET['searched']
        urunler = Urun.objects.filter(
            Q(kategori__isim__contains = searched) |
            Q(altkategori__isim__contains = searched)
        ) 
        if 'favori' in request.POST:
            begen(request)   
        
    sepetMiktar = ''
    favoriMiktar = ''
    if request.user.is_authenticated:
        sepetMiktar = len(Sepet.objects.filter( kullanici = request.user))
        favoriMiktar = Favori.objects.filter( kullanici = request.user).count() 
      
    context = {
            'searched' : searched , 
            'urunler' : urunler ,
            'favoriMiktar' : favoriMiktar,
            'sepetMiktar' : sepetMiktar
        }          
    return render(request , 'search.html', context) 

def alibaba(request ):
    kategoriler = Kategori.objects.all()
    ustkategori = Kategori.objects.all()[:2]
    altkategori = Kategori.objects.all()[2:4]
    markalar = AltKategori.objects.all()
    sepetMiktar = 0
    favoriMiktar = 0
    if request.user.is_authenticated:

        sepetMiktar = len(Sepet.objects.filter(kullanici = request.user))
        favoriMiktar = len(Favori.objects.filter( kullanici = request.user))

    
    context = {
        'kategoriler' : kategoriler,
        'markalar' : markalar,
        'ustkategori' : ustkategori ,
        'altkategori' : altkategori ,
        'sepetMiktar' : sepetMiktar,
        'favoriMiktar' : favoriMiktar,
    } 
    return render(request , 'Alibaba.html' , context)

def kategori(request, kategoriId ):
    urunler = Urun.objects.filter( kategori__slug = kategoriId)
    sepetMiktar = ''
    if request.user.is_authenticated:
        sepetMiktar = len(Sepet.objects.filter( kullanici = request.user))
    # favoriMiktar = len(Favori.objects.filter( kullanici = request.user))

    if request.method == 'POST' :
        # urunkey = list(request.POST)[1]
        # urunid = urunkey[6:]  
        begen(request)
    sepetMiktar = ''
    favoriMiktar = ''
    if request.user.is_authenticated:
        sepetMiktar = len(Sepet.objects.filter( kullanici = request.user))
        favoriMiktar = Favori.objects.filter( kullanici = request.user).count()  
    context = {
        'urunler' : urunler,
        'sepetMiktar' : sepetMiktar,
        'favoriMiktar' : favoriMiktar
    }
    return render(request , 'kategori.html',context)    

def marka(request , markaId):
    urunler = Urun.objects.filter( altkategori__slug = markaId )
    # sepetMiktar = len(Sepet.objects.filter( kullanici = request.user))
    
    if request.method == 'POST' :
        # urunkey = list(request.POST)[1]
        # urunid = urunkey[6:]  
        urunid = request.POST['urunId']
        print(urunid) 
        favoriurun = Urun.objects.get( id = urunid)
        if Favori.objects.filter( urun = urunid ).exists():
            favori = Favori.objects.get( urun = urunid )
            favori.delete()
        else:

            favori = Favori( urun = favoriurun , kullanici = request.user ) 
            favori.save() 
    # favoriMiktar = Favori.objects.filter( kullanici = request.user).count()  
    sepetMiktar = ''
    favoriMiktar = ''
    if request.user.is_authenticated:
        sepetMiktar = len(Sepet.objects.filter( kullanici = request.user))
        favoriMiktar = Favori.objects.filter( kullanici = request.user).count() 


    context = {
        'urunler' : urunler,
        'sepetMiktar' : sepetMiktar,
        'favoriMiktar' : favoriMiktar
    }  

    return render(request , 'marka.html' , context)

def create (request):
    form = UrunForm()
    if request.method == 'POST':
        form = UrunForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request , 'Ürün Oluşturuldu')
            return redirect('Alibaba')
    sepetMiktar = len(Sepet.objects.filter( kullanici = request.user))
    favoriMiktar = len(Favori.objects.filter( kullanici = request.user))


    context = {
        'form' : form ,
        'sepetMiktar' : sepetMiktar,
        'favoriMiktar' :favoriMiktar

    }        
    return render(request , 'create.html' , context)

def favori(request):
    favoriler = Favori.objects.filter( kullanici = request.user)
    sepetMiktar = len(Sepet.objects.filter( kullanici = request.user))
    favoriMiktar = Favori.objects.filter( kullanici = request.user).count()
    

    context = {
       
       'favoriler' : favoriler ,
       'sepetMiktar' : sepetMiktar , 
       'favoriMiktar' : favoriMiktar,
     
    }
    return render(request , 'favori.html' ,context)

def urunDetay(request,urunId):
    urundetay = Urun.objects.get( slug = urunId )

    if 'ekle' in request.POST:
        adet = int(request.POST.get('number'))
         
        if Sepet.objects.filter(kullanici = request.user, urun = urundetay):
            urun = Sepet.objects.get(kullanici = request.user, urun = urundetay )
            urun.sepetAdet += adet
            urun.sepetFiyat += adet * urundetay.fiyat
            urundetay.stok -= adet
            urun.save()
        else:

            sepet = Sepet( urun = urundetay , kullanici = request.user , sepetAdet = adet , sepetFiyat = adet * urundetay.fiyat)
            sepet.save() 
    form = YorumForm()
    if 'yorum' in request.POST:
        form = YorumForm(request.POST or None)
        if form.is_valid():
            yorum=form.save(commit=False)
            yorum.urun = urundetay
            yorum.kullanici = request.user
            yorum.save()
    yorumlar = Yorum.objects.filter(urun = urundetay)

    sepetMiktar = len(Sepet.objects.filter( kullanici = request.user))
    favoriMiktar = len(Favori.objects.filter( kullanici = request.user))

    context = {
        'urundetay' : urundetay,
        'sepetMiktar' : sepetMiktar,
        'favoriMiktar' : favoriMiktar,
        'yorumlar' : yorumlar ,
        'form' : form


    }
    return render(request, 'urun-detay.html' ,context)

def sepet (request):
    urunler = Sepet.objects.filter( kullanici = request.user)
    toplamFiyat = 0
    if request.method == 'POST':
        adetkey = list(request.POST)[1]
        adetid=adetkey[6:]
        adet = request.POST[adetkey]
        urun = Sepet.objects.get(id = adetid)

        birimfiyat = float(urun.sepetFiyat) / float(urun.sepetAdet)
        urun.sepetAdet = adet
        urun.sepetFiyat = birimfiyat * float(adet)
        urun.save()
    for i in urunler:
        toplamFiyat += i.sepetFiyat

    sepetMiktar = len(Sepet.objects.filter( kullanici = request.user))
    favoriMiktar = len(Favori.objects.filter( kullanici = request.user))


    context= {
        'urunler' : urunler ,
        'toplamFiyat' : toplamFiyat ,
        'sepetMiktar' : sepetMiktar , 
        'favoriMiktar' :favoriMiktar,

    }
    return render (request, 'sepet.html' , context)    

def deleteUrun(request , id):
    urun = Sepet.objects.get(id = id)
    urun.delete()
    return redirect ('sepet')
    
def deletefav (request , id):
    urun = Favori.objects.get(id = id)
    urun.delete()
    return redirect('favori')    

