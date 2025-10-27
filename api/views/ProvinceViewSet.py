from .dependencies import *

class ProvinceViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer