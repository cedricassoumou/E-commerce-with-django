from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from store.models import Produit


def index(request):

    produits = Produit.objects.all()  #liste de produits

    return render(request, "store/index.html", {"produits": produits, "index": 1})


def detail_produit(request, slug):

    detail = get_object_or_404(Produit, slug=slug)

    return render(request, "store/detail_produit.html", {"produit": detail})
