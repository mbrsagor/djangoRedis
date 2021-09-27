from rest_framework import serializers
from .models import UserAccount, Role


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'name', 'email', 'is_relator')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = [
            'id',
            'name',
            'user',
            'is_active',
            'created_at'
        ]
