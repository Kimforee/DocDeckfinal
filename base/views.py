from rest_framework import generics
from .models import PatientData
from .serializers import PatientDataSerializer
import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PatientDataSerializer

# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         'GET /api',
#     ]
#     return Response(routes)


# class PatientDataListCreate(generics.ListCreateAPIView):
#     queryset = PatientData.objects.all()
#     serializer_class = PatientDataSerializer

#     def perform_create(self, serializer):
#         gender = 1 if serializer.validated_data.get('gender') == 'M' else 0
#         # Process data here as per your requirements before saving to the database

#         # Load the model and make predictions
#         model = pickle.load(open('static\pickle\clf9', 'rb'))
#         data = serializer.validated_data
#         data.pop('predicted_category')  # Remove predicted_category to avoid conflicts
#         new_data = {'M/F': gender, **data}
#         input_data = pd.DataFrame(new_data, index=[0])
#         predicted = model.predict(input_data)

#         if predicted == [0]:
#             serializer.save(predicted_category='Converted')
#         elif predicted == [1]:
#             serializer.save(predicted_category='Demented')
#         elif predicted == [2]:
#             serializer.save(predicted_category='Non-Demented')

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PatientData
from .serializers import PatientDataSerializer
import pickle
import pandas as pd

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/patient-data',
        'GET /api/patient-data/<id>'
    ]
    return Response(routes)

@api_view(['GET'])
def getPatientData(request):
    patient_data = PatientData.objects.all()
    serializer = PatientDataSerializer(patient_data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPatientDataDetail(request, pk):
    patient_data = PatientData.objects.get(id=pk)
    serializer = PatientDataSerializer(patient_data)
    return Response(serializer.data)

@api_view(['POST'])
def predictPatientData(request):
    if request.method == 'POST':
        gender = 1 if request.data.get('gender') == 'M' else 0
        model = pickle.load(open('static/pickle/clf9', 'rb'))
        data = request.data
        data.pop('predicted_category', None)  # Remove predicted_category to avoid conflicts
        new_data = {'M/F': gender, **data}
        input_data = pd.DataFrame(new_data, index=[0])
        predicted = model.predict(input_data)

        predicted_category = ''
        if predicted == [0]:
            predicted_category = 'Converted'
        elif predicted == [1]:
            predicted_category = 'Demented'
        else:
            predicted_category = 'Non-Demented'

        data['predicted_category'] = predicted_category
        serializer = PatientDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
