from rest_framework import serializers
from .models import Province, Commune, Zone, Quartier

class QuartierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quartier
        fields = ['id', 'name']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['zone'] = instance.zone.values('id', 'name').first()
        return rep

class ZoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zone
        fields = ['id', 'name']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['quartiers'] = instance.quartiers.values('id', 'name')
        return rep

class CommuneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commune
        fields = ['id', 'name']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['province'] = instance.province.values('id', 'name').first()
        return rep

class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = ['id', 'name', 'communes']
