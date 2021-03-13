# from django.shortcuts import render

# # Create your views here.

# def lilacs(request):
#     return render(request, 'lilacs.html')
from .models import QnA
from .serializers import QnASerializer
from rest_framework import viewsets, mixins

# Create your views here.
class QnAAPI(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = QnA.objects.all()
    serializer_class = QnASerializer


