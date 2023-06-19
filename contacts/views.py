from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Contact
from .serializer import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
