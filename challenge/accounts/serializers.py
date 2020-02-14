from rest_framework import serializers

from . import models


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = '__all__'


class AccountWithoutName(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = '__all__'
        extra_kwargs = {'name': {'required': False}}