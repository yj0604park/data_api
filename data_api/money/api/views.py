from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from data_api.money.filters import SalaryDetailFilter, SalaryFilter
from data_api.money.models import Salary, SalaryDetailItem

from .serializers import SalaryDetailSerializer, SalarySerializer


class SalaryViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
):
    serializer_class = SalarySerializer
    queryset = Salary.objects.all()
    filterset_class = SalaryFilter
    lookup_field = "date"


class SalaryDetailItemViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
):
    serializer_class = SalaryDetailSerializer
    queryset = SalaryDetailItem.objects.all()
    filterset_class = SalaryDetailFilter
    lookup_field = "name"
