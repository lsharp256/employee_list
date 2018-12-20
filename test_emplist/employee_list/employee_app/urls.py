from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='home'),
    path('create_employee/', views.CreateEmployeeView.as_view(), name='create'),
    path('<int:pk>/update_employee/', views.UpdateEmployeeView.as_view(), name='update'),
    path('<int:pk>/delete_employee/', views.EmployeeDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
