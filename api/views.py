from django.shortcuts import render
from rest_framework import generics
from .serializers import ReporterSerializer
from .models import Reporter

class ReporterList(generics.ListCreateAPIView):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer
