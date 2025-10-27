from .dependencies import *

class ProvinceViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

    @action(
        methods=['GET'],
        detail=True,
        serializer_class=CommuneSerializer,
        url_path='communes',
        url_name='province_communes'
    )
    def communes(self, request, pk=None):
        province = self.get_object()
        communes = province.communes.all()
        serializer = CommuneSerializer(communes, many=True)
        return Response(serializer.data, status=200)
    
    @action(
        methods=['GET'],
        detail=True,
        serializer_class=CommuneSerializer,
        url_path='communes',
        url_name='province_communes'
    )
    def communes(self, request, pk=None):
        province = self.get_object()
        communes = province.communes.all()
        serializer = CommuneSerializer(communes, many=True)
        return Response(serializer.data, status=200)