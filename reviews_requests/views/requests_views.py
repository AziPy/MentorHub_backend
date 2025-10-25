from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema
from reviews_requests.models import RequestsNew
from reviews_requests.serializers import RequestsNewSerializer
from reviews_requests.permissions import IsMentor
@extend_schema_view(
    list=extend_schema(tags=['Requests']),
    retrieve=extend_schema(tags=['Requests']),
    create=extend_schema(tags=['Requests']),
    update=extend_schema(tags=['Requests']),
    partial_update=extend_schema(tags=['Requests']),
    destroy=extend_schema(tags=['Requests']),
)
class RequestsNewViewSet(viewsets.ModelViewSet):
    queryset = RequestsNew.objects.all()
    serializer_class = RequestsNewSerializer
    permission_classes = [IsMentor]

    def get_queryset(self):
        qs = super().get_queryset()
        status_param = self.request.query_params.get('status')
        if status_param:
            qs = qs.filter(status=status_param)
        return qs
