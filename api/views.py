from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ApprovalSerializer
from .models import Approval
# Create your views here.

class ApprovalViewset(viewsets.ModelViewSet):
    serializer_class = ApprovalSerializer
    queryset = Approval.objects.all() 