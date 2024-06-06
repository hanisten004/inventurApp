from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    target_quantity = models.IntegerField(default=1)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name  # Implementieren Sie die __str__-Methode hier

class Kasten(models.Model):
    SIZE_CHOICES = [
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=6, choices=SIZE_CHOICES)
    products = models.ManyToManyField(Product, through='KastenProduct')

    def __str__(self):
        return f"{self.name} ({self.size})"

class KastenProduct(models.Model):
    kasten = models.ForeignKey(Kasten, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    target_quantity = models.IntegerField(default=1)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.kasten.name} - {self.product.name} ({self.quantity})"

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    place = models.CharField(max_length=200)
    floor = models.CharField(max_length=200, default='Unknown')
    room = models.CharField(max_length=200, default='Unknown')
    adresse = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    fk_kasten = models.ForeignKey(Kasten, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.place
