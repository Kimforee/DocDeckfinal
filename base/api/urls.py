from django.urls import path
from .views import PatientDataListCreate
from .views import getRoutes
from .views import predictPatientData
from .views import getPatientDataDetail
from .views import getPatientData
urlpatterns = [
    # path('', PatientDataListCreate.as_view(), name='patient_data_list'),
    path('', getRoutes, name='api-routes'),
    path('patient-data/', getPatientData, name='get-patient-data'),
    path('patient-data/<int:pk>/', getPatientDataDetail, name='get-patient-data-detail'),
    path('predict/', predictPatientData, name='predict-patient-data'),
]
