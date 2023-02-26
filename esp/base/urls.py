from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),

    path('C0', views.state_0, name="zero"),
    path('C1', views.state_1, name="one"),

    path('EBget', views.status_get, name="esp_button_get"),


    path('EA/<int:value>', views.analog_put, name="Eanalog_write"),

    path('CAget', views.analog_get, name="Canalog_read"),


]
