from rest_framework import routers
from .views import UserAccountViewSet


router = routers.DefaultRouter()
router.register(r'userAccount', UserAccountViewSet)
