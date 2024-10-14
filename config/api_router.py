from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from data_api.money.api.views import SalaryDetailItemViewSet
from data_api.money.api.views import SalaryViewSet
from data_api.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("salarydetailitem", SalaryDetailItemViewSet)
router.register("salary", SalaryViewSet)


app_name = "api"
urlpatterns = router.urls
