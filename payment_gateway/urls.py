from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('detail/',views.detail,name="detail"),
    path('detail/payment',views.payment,name="payment"),
]