from rest_framework import serializers
from library.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['User_id', 'UPI_id',]