from django.contrib import admin
from django.urls import path
from academico import views
# Importamos las nuevas vistas de la carpeta accounts
from accounts.views import MyLoginView, MyLogoutView 

urlpatterns = [
    path('admin/', admin.site.urls),

    # ----------------------------- INDEX -------------------------
    path('', views.mostrarIndex, name='index'),

    # ----------------------------- INICIO DE USUARIO -------------------------
    # Actualizado para usar MyLoginView y el template templates/accounts/login.html
    path('login/', MyLoginView.as_view(), name='login'),

    # ----------------------------- CIERRA SESION -------------------------
    # Actualizado para usar MyLogoutView
    path('logout/', MyLogoutView.as_view(), name='logout'),

    # ------------------------------ REGRESAR AL MENU ----------------------
    path('menu_principal/', views.volverMenu, name='menu_principal'),

    # ----------------------------- REGISTRAR NOTAS -------------------------
    path('form_registrar_notas/', views.MostrarFormRegistrarNotas, name='form_registrar_notas'),
    path('form_registrar_nota/', views.InsertarNotas, name='insertar_nota'),
    
    # ----------------------------- LISTAR NOTAS -------------------------
    path('listado_notas/', views.MostrarListadoNotas, name='listado_notas'),

    # ----------------------------- MODIFICAR NOTAS -------------------------
    path('form_actualizar_notas/<int:id>/', views.MostrarModificarNotas, name='form_actualizar_notas'),
    path('actualizar_notas/<int:id>/', views.ModificarNotas, name='actualizar_notas'),

    # ----------------------------- ELIMINAR NOTAS -------------------------
    path('eliminar_nota/<int:id>/', views.EliminarNotas, name='eliminar_nota'),

    # ----------------------------- LISTAR ALUMNOS -------------------------
    path('listado_alumnos/', views.MostrarListadoAlumnos, name='listado_alumnos'),

    # ----------------------------- MODIFICAR ALUMNOS -------------------------
    path('form_actualizar_alumno/<int:id>/', views.MostrarModificarAlumnos, name='form_actualizar_alumno'),
    path('actualizar_alumnos/<int:id>/', views.ModificarAlumnos, name='actualizar_alumnos'),

    # ----------------------------- ELIMINAR ALUMNOS -------------------------
    path('eliminar_alumno/<int:id>/', views.EliminarAlumnos, name='eliminar_alumno'),

    # ----------------------------- REGISTRAR ALUMNOS -------------------------
    path('form_registrar_alumnos/', views.MostrarFormRegistrarAlumnos, name='form_registrar_alumnos'),
    path('form_registrar_alumno/', views.InsertarAlumnos, name='insertar_alumno'),

    # --------------------------- NOTAS POR ALUMNO ---------------------------
    path('listado_notas_alumno/<int:id>/', views.MostrarListadoNotasAlumno, name='listado_notas_alumno'),

    # ------------------------------ REGRESAR AL MENU 2 ----------------------
    path('menu_principal2/', views.volverMenu2, name='menu_principal2')
]