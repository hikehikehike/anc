from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, generate_db, EmployeeListViews, EmployeeUpdateViews

app_name = "create_hierarchy"

urlpatterns = [
    path("", index, name="index"),
    path("generate_db/", generate_db, name="generate_db"),
    path("employee/<int:pk>/update", EmployeeUpdateViews.as_view(), name="employee_update"),
    path("employee_list/", EmployeeListViews.as_view(), name="employee_list"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
