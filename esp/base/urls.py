from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('seg', views.seven_seg, name="7seg"),

    path('C0', views.status_get, name="zero"),
    path('C1', views.state_1, name="one"),

    path('EBget', views.state_0, name="esp_button_get"),


    path('EA/<int:value>', views.analog_put, name="Eanalog_write"),

    path('CAget', views.analog_get, name="Canalog_read"),


]
