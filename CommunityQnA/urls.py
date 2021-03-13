# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.lilacs, name='lilacs')
# ]

from rest_framework import routers
from .views import QnAAPI, qna_get, qna_view
from django.urls import path

router = routers.DefaultRouter()
router.register('qna', QnAAPI, 'qna')

urlpatterns = [
    path('qna_list/', qna_get),
    path('qna/', qna_view)
]
