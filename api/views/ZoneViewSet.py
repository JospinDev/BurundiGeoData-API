from .dependencies import *

class ZoneViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = {
        'commune__name': ['exact'],
        'name': ['icontains'],
    }


    @action(methods=['GET'], detail=True, serializer_class=QuartierSerializer, url_path='quartiers', url_name='zone_quartiers')
    def quartiers(self, request, pk=None):
        zone = self.get_object()
        quartiers = zone.quartiers.all()
        serializer = QuartierSerializer(quartiers, many=True)
        return Response(serializer.data, status=200)