from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.register_user, name='register'),

    path('login/', views.login_user, name='login'),

    path('logout/', views.logout_user, name='logout'),

    path('profile/', views.profile, name='profile'),
    path(
    'admin-report/',
    views.admin_report,
    name='admin_report'
),
path(
    'export-excel-report/',
    views.export_excel_report,
    name='export_excel_report'
),

]