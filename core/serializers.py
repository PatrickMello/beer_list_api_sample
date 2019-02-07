from rest_framework import serializers

from core.models import Beer, BeerType


class BeerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerType
        fields = ('id', 'name',)


class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = ('id', 'name', 'beer_type',)

    beer_type = BeerTypeSerializer()
