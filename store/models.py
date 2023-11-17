from django.utils import timezone
from decimal import Decimal
from django.db import models
from django.urls import reverse

class ProductManager(models.Manager):
    def search(self, query):
        return self.filter(models.Q(name__icontains=query) | models.Q(description__icontains=query))

class Product(models.Model):
    name = models.CharField(max_length=255, default='')
    category = models.CharField(max_length=255, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.IntegerField(null=True, blank=True)
    discount_start_date = models.DateField(null=True, blank=True)
    discount_end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, default='')
    thumbnail = models.ImageField(upload_to='products', null=True, blank=True)
    slug = models.SlugField(max_length=255)

    objects = ProductManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

    @property
    def discount_price(self):
        if (
            self.discount_percentage is not None
            and self.discount_start_date
            and self.discount_end_date
            and self.discount_start_date <= timezone.now().date() <= self.discount_end_date
        ):
            discounted_price = float(self.price) * (1 - self.discount_percentage / 100)
            return discounted_price
        return None