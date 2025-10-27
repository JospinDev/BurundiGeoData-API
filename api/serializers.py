from rest_framework import serializers
from .models import Province, Commune, Zone, Quartier

class QuartierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quartier
        fields = ['id', 'name','zone']

class ZoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zone
        fields = ['id', 'name','commune']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['commune'] = {
            "id": instance.commune.id,
            "name": instance.commune.name
        } if instance.commune else None
        return rep

class CommuneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commune
        fields = ['id', 'name', 'province']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['province'] = {
        "id": instance.province.id,
        "name": instance.province.name
    } if instance.province else None
        return rep

class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = ['id', 'name']
