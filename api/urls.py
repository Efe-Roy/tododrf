from rest_framework import routers
from . views import ApprovalViewset

router = routers.DefaultRouter()
router.register(r'api/approval', ApprovalViewset, 'approval')

urlpatterns = router.urls