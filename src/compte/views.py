from django.shortcuts import render


# Create your views here.

def inscription(request):
    return render(request, "compte/inscription.html")
