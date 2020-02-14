from django.contrib import admin

from . import models


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name',)
    list_filter = (
        ('shipping_country', admin.AllValuesFieldListFilter),
    )