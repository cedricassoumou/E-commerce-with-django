from django.db import models

# Create your models here.

"""
Produit
- Nom
- Prix
- Quantité en stock
- Description
- Image

"""

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.FloatField(default=0.0)
    quantite = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="produits", blank=True, null=True)
