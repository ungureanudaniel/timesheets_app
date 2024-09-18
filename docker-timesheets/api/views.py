from django.shortcuts import render
#api imports
from rest_framework import generics, permissions
from reports.models import MonthlyReport
from .serializers import MonthlyReportSerializer

class MonthlyReportCreateView(generics.CreateAPIView):
    queryset = MonthlyReport.objects.all()
    serializer_class = MonthlyReportSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class MonthlyReportListView(generics.ListAPIView):
    queryset = MonthlyReport.objects.all()
    serializer_class = MonthlyReportSerializer
    http_method_names = ['get']
