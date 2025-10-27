from .dependencies import *

class QuartierViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quartier.objects.all()
    serializer_class = QuartierSerializer