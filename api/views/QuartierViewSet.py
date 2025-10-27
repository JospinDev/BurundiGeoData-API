from .dependencies import *

class QuartierViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quartier.objects.all()
    serializer_class = QuartierSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = {
        'zone__name': ['exact'],
        'name': ['icontains'],
    }