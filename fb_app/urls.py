from django.urls import path
from fb_app import views, admin_views, modal_views

urlpatterns = [
    path("", views.render_login, name="render_login"),
    path("perform_login", views.perform_login, name="perform_login"),
    path("dashboard/", admin_views.render_dashboard, name="render_dashboard"),
    path("customers/", admin_views.render_customers, name="render_customers"),
    path("products/", admin_views.render_products, name="render_products"),
    path("calendar/", admin_views.render_calendar, name="render_calendar"),
    path("perform_add_customer", modal_views.perform_add_customer, name="perform_add_customer"),
    path("perform_add_product", modal_views.perform_add_product, name="perform_add_product"),
    path("perform_add_session", modal_views.perform_add_session, name="perform_add_session"),
    path("perform_add_schedule", modal_views.perform_add_schedule, name="perform_add_schedule"),
    path("perform_add_sale", modal_views.perform_add_sale, name="perform_add_sale"),
    path("perform_add_payment", modal_views.perform_add_payment, name="perform_add_payment"),
    path("perform_add_expense", modal_views.perform_add_expense, name="perform_add_expense"),
]