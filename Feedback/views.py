from .models import Feedback
from .serializers import FeedbackSerializer
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class FeedbackAPI(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

@api_view(['POST'])
def feedback_view(request, *args, **kwargs):
    serializer = FeedbackSerializer(data = request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({}, status=400)
