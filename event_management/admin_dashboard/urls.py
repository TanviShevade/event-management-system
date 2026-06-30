from django.urls import path
from . import views
from .views import admin_dashboard, admin_report
urlpatterns = [

    path(
        '',
        views.admin_dashboard,
        name='admin_dashboard'
    ),
     path(
        'report/',
        admin_report,
        name='admin_report'
    ),
    path(
        'excel-report/',
        views.export_excel_report,
        name='export_excel_report'
    ),

]