from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'medical-records', views.MedicalRecordViewSet)
router.register(r'appointments', views.AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.CustomAuthToken.as_view()),
]
