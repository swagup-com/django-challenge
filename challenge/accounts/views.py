from rest_framework import mixins, viewsets
from django.http import JsonResponse
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




def fizzbuzz(request):
    x = request.GET.get('x', 100)
    x = int(x)

    response = {'x': x, "fizzbuzz": ''.join((solve_fizz(i) for i in range(1,x)))}
    return JsonResponse(response)


def fizzbuzz2(request):
    x = request.GET.get('x', 100)
    x = int(x)

    response = {'x': x, "fizzbuzz": [solve_fizz(i) for i in range(1,x)]}
    return JsonResponse(response)


def solve_fizz(x: int)->str:
    ans = ''
    if x % 3 == 0:
        ans += 'Fizz'

    if x%5 == 0:
        ans += 'Buzz'

    if not ans:
        return str(x)

    return ans