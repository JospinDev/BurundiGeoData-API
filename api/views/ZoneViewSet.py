from .dependencies import *

class ZoneViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer