from django.shortcuts import render
# api imports
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from reports.models import MonthlyReport
from .serializers import MonthlyReportSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class MonthlyReportPagination(PageNumberPagination):
    """
    Custom pagination class for Monthly
    """
    page_size = 10  # Customize page size
    page_size_query_param = 'page_size'
    max_page_size = 100


class MonthlyReportCreateView(generics.CreateAPIView):
    """
    This class handles the creation of MonthlyReport instances.
    """
    queryset = MonthlyReport.objects.all()
    serializer_class = MonthlyReportSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']


class MonthlyReportListView(generics.ListAPIView):
    """
    This class handles the listing of MonthlyReport instances.
    """
    queryset = MonthlyReport.objects.all()
    serializer_class = MonthlyReportSerializer
    http_method_names = ['get']
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user__username', 'month']
    ordering_fields = ['created_at', 'updated_at']
    pagination_class = MonthlyReportPagination

    def get_queryset(self):
        user = self.request.user
        # return MonthlyReport.objects.filter(user=user)
        return MonthlyReport.objects.select_related('user').all()


class MonthlyReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class handles the retrieval, update, and deletion of a MonthlyReport instance.
    """
    queryset = MonthlyReport.objects.all()
    serializer_class = MonthlyReportSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'put', 'delete']
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
