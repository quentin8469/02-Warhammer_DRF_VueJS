from django.shortcuts import render
from rest_framework import viewsets
from account.models import CustomUser
from account.serializers import AccountCustomUserSerializer


# Create your views here.
class AccountCustomUserViewSet(viewsets.ModelViewSet):
    """Account CustomUser API views"""

    queryset = CustomUser.objects.all()
    serializer_class = AccountCustomUserSerializer
