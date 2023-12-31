from django.urls import path
from . import views
from .views import registration_form

# from .views import Especialidad
# from .views import appointment_calendar

urlpatterns = [
    path("", views.index, name="inicio"),
    #  path('misturnos/', views.misturnos, name="misturnos"),
    path("ingreso/", views.ingreso, name="ingreso"),
    path('logout/', views.exit, name='exit'),
    path("turnostodos/", views.turnostodos),
    path("turnosporespecialidad/", views.turnosporespecialidad),
    path("turnosporprofesional/", views.turnosporprofesional),
    path("turnospordni/<int:dni>", views.turnospordni),
    path('register/', views.registration_form, name='registration_form'),
    #  path('turnos/', views.turnos, name="turnos"),
    # para la lista desplegable
    path("especialidad/", views.turnos, name="especialidad"),
      
    #   path('appointments/<str:especialidad>/', appointment_calendar, name='appointment_calendar'),
    # --------------------------------------------------------------------
    path("paciente/<str:nombre>", views.paciente, name="paciente"),
    path("contacto/", views.contacto, name="contacto"),
    path('abm/', views.especialidades_index , name="abm"),
    path('especialidad/nuevo/', views.especialidad_nuevo, name='especialidad_nuevo'),
    path('especialidad/editar/<int:id_especialidad>', views.especialidad_editar, name='especialidad_editar'),
    path('especialidad/eliminar/<int:id_especialidad>', views.especialidad_eliminar, name='especialidad_eliminar'),
    path('especialidad/especialidades/', views.get_especialidades, name='get_especialidades'),
    path('especialidad/medicos/<int:especialidad_id>', views.get_medicos, name='get_medicos'),

    path('medicosview/', views.MedicoListView.as_view(), name='medicos_index_view'),
    path('turno/nuevoturno', views.TurnosCreate.as_view(), name='nuevo_turno' ),
    path('turno/turnosview', views.TurnosListView.as_view(), name='turnos_index_view' ),
    path('turno/editar/<int:pk>', views.TunosUpdateView.as_view(), name='turno_editar'),
    path('turno/eliminar/<int:pk>', views.TunosDeleteView.as_view(), name='turno_eliminar'),

    # --------------------------------------------------------------------
]
