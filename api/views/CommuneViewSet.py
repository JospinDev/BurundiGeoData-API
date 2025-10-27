from .dependencies import *
class CommuneViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializer