from rest_framework.serializers import ModelSerializer
from base.api.models import PatientData

class PatientDataSerializer(ModelSerializer):
    class Meta:
        model = PatientData
        fields = '__all__'
