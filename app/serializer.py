from rest_framework import serializers

from .models import UserAccount

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('user_id', 'first_name', 'last_name', 'email', 'cellphone_number')
