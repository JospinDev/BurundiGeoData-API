from rest_framework import viewsets,mixins
from api.models import Province, Commune, Zone, Quartier
from api.serializers import ProvinceSerializer, CommuneSerializer, ZoneSerializer, QuartierSerializer