from .dependencies import *
class CommuneViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = {
        'province__name': ['exact'],
        'name': ['icontains'],
    }

    @action(
        methods=['GET'],
        detail=True,
        serializer_class=ZoneSerializer,
        url_path='zones',
        url_name='commune_zones'
    )
    def zones(self, request, pk=None):
        commune = self.get_object()
        zones = commune.zones.all()
        serializer = ZoneSerializer(zones, many=True)
        return Response(serializer.data, status=200)