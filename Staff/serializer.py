from rest_framework import serializers

from .models import staff

class staffSerializer(serializers.ModelSerializer):
    class Meta:
        model   = staff
        fields  = "__all__"
