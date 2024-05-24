from django.urls import path
from .views import registro_view, login_view, admin_view, user_crud_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('admin/', admin_view, name='admin_view'),
    path('admin/usuario/<int:user_id>/', user_crud_view, name='user_crud'),
    path('admin/usuario/nuevo/', user_crud_view, name='user_crud_nuevo'),
]
