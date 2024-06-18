from django.urls import path
from . import views

from .views import (SaleProductLine, SpecialTaskShops, TrafficShops, ChecksShops,
                    MainIndicatorShops, ConversionShops, ChartSalesShops, ChartSpecialTaskShops)



urlpatterns = [

    path('sale/', SaleProductLine.as_view(), name='sale'),
    path('stask/', SpecialTaskShops.as_view(), name='stask'),
    path('traffic/', TrafficShops.as_view(), name='traffic'),
    path('check/', ChecksShops.as_view(), name='check'),
    path('conf/', ConversionShops.as_view(), name='conf'),
    path('chsale/', ChartSalesShops.as_view(), name='conf'),
    path('chspecsale/', ChartSpecialTaskShops.as_view(), name='conf'),
    path('mi/', MainIndicatorShops.as_view(), name='mi'),
    #path('__debug__/', include("debug_toolbar.urls")),

]