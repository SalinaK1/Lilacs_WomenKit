from .models import Feedback
from .serializers import FeedbackSerializer
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets, mixins

# Create your views here.
class FeedbackAPI(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
