from rest_framework import routers
from .views import FeedbackAPI, feedback_view
from django.urls import path


# router = routers.DefaultRouter()
# router.register('feedback', FeedbackAPI, 'feedback')

# urlpatterns = router.urls
urlpatterns = [
    path('feedback/', feedback_view),
]

