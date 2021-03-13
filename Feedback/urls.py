from rest_framework import routers
from .views import FeedbackAPI


router = routers.DefaultRouter()
router.register('feedback', FeedbackAPI, 'feedback')

urlpatterns = router.urls