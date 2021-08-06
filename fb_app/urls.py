from django.urls import path
from fb_app import views, admin_views, modal_views

urlpatterns = [
    path("", views.render_login, name="render_login"),
    path("perform_login", views.perform_login, name="perform_login"),
    path("dashboard/", admin_views.render_dashboard, name="render_dashboard"),
    path("perform_add_customer", modal_views.perform_add_customer, name="perform_add_customer"),
]