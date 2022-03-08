from django.shortcuts import render
from rest_framework import generics
from library.models import Payment
from library.serializers import PaymentSerializer



class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment
    serializer_class = PaymentSerializer


def index(request):
    return render(request,'index.html')