from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from data_api.money.filters import SalaryDetailFilter
from data_api.money.filters import SalaryFilter
from data_api.money.models import Salary
from data_api.money.models import SalaryDetailItem

from .serializers import SalaryDetailSerializer
from .serializers import SalarySerializer


class SalaryViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = SalarySerializer
    queryset = Salary.objects.all()
    filterset_class = SalaryFilter
    lookup_field = "date"


class SalaryDetailItemViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = SalaryDetailSerializer
    queryset = SalaryDetailItem.objects.all()
    filterset_class = SalaryDetailFilter
    lookup_field = "name"
