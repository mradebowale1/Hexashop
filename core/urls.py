from django.urls import path
from .views import initiate_payment

urlpatterns = [
    path("", initiate_payment, name="initiate_payment"),
    # path("verify/<str:ref>/", verify_payment, name="verify-payment")
]