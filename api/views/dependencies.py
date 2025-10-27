from rest_framework import viewsets,mixins
from api.models import Province, Commune, Zone, Quartier
from api.serializers import ProvinceSerializer, CommuneSerializer, ZoneSerializer, QuartierSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response