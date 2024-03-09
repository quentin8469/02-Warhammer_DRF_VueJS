from rest_framework import serializers
from account.models import CustomUser


class AccountCustomUserSerializer(serializers.ModelSerializer):
    """Account CustomUser serializer"""

    class Meta:
        model = CustomUser
        fields = "__all__"
