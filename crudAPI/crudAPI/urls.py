from django.contrib import admin
from django.urls import path
from library.views import PaymentList, PaymentDetail



urlpatterns = [
    path('api/payments', PaymentList.as_view()),
    path('api/payments/<int:pk>', PaymentDetail.as_view()),
    path('admin/', admin.site.urls),
]
