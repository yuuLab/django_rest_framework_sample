import django_filters
from rest_framework import viewsets, filters

from .models import UserAccount
from .serializer import UserAccountSerializer


class UserAccountViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer