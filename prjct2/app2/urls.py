from django.urls import path
from app2.views import *
from django.contrib.auth import views as auth_views
# from django.views.generic.base import TemplateView


urlpatterns = [
    #path('',TemplateView.as_view(template_name='auth/home.html'),name='home'),
    path('', employee_list, name='employee_list'),
    path('<int:id>/details/', employee_details, name="employee_details"),
    path('<int:id>/edit/', employee_edit, name="employee_edit"),
    path('add/',employee_add, name="employee_add"),
    path('<int:id>/delete/', employee_delete, name="employee_delete"),
    # path('<int:id>/change/',)
    # path('password_reset/', auth_views.PasswordResetView, name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView, name='password_reset_done'),
    # path('reset/(?P<uidb64>', auth_views.PasswordResetConfirmView, name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView, name='password_reset_complete'),
    #
# Paet'),
#
#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
#      name='password_reset_complete')
# ]ssword reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
#     path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_reset_complete.html'),
#         name='password_reset+9----------------------------------------------------------------------------------------------------------------------------------------------------------------------_complete'),
#
#     path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_reset_confirm.html'),
#         name='password_change'),
#
#     path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
#      name='password_reset_done'),
#
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_res
]