from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    billing_address1 = models.CharField(max_length=100, null=True, blank=True)
    billing_address2 = models.CharField(max_length=100, null=True, blank=True)
    billing_city = models.CharField(max_length=100, null=True, blank=True)
    billing_state = models.CharField(max_length=100, null=True, blank=True)
    billing_zip = models.CharField(max_length=100, null=True, blank=True)
    billing_country = models.CharField(max_length=2, default='US')
    shipping_address1 = models.CharField(max_length=100, null=True, blank=True)
    shipping_address2 = models.CharField(max_length=100, null=True, blank=True)
    shipping_city = models.CharField(max_length=100, null=True, blank=True)
    shipping_state = models.CharField(max_length=100, null=True, blank=True)
    shipping_zip = models.CharField(max_length=100, null=True, blank=True)
    shipping_country = models.CharField(max_length=100, default='US')

    def __str__(self):
        return self.name
