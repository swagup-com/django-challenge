from rest_framework import mixins, viewsets

from . import models
from . import serializers


class AccountViewSet(mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """
        API endpoint that allows accounts to be viewed.

        list:
        Return all the accounts available.

        create:
        Create an account.

        update:
        Update an account.

        retrieve:
        Return a given account.
    """

    model = models.Account
    serializer_class = serializers.AccountSerializer
    queryset = models.Account.objects.all()


    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = serializers.AccountWithoutName

        return serializer_class