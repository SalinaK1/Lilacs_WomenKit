# from django.shortcuts import render

# # Create your views here.

# def lilacs(request):
#     return render(request, 'lilacs.html')
from .models import QnA
from .serializers import QnASerializer
from rest_framework import viewsets, mixins
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class QnAAPI(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = QnA.objects.all()
    serializer_class = QnASerializer


@api_view(['GET'])
def qna_get(request, *args, **kwargs):
    qna = QnA.objects.all()
    serializer = QnASerializer (qna, many=True)
    return Response(serializer.data, status = 200)

@api_view(['POST'])
def qna_view(request, *args, **kwargs):
    serializer = QnASerializer(data = request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({}, status=400)
