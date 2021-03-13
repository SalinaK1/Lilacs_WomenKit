# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.lilacs, name='lilacs')
# ]

from rest_framework import routers
from .views import QnAAPI

router = routers.DefaultRouter()
router.register('qna', QnAAPI, 'qna')

urlpatterns = router.urls