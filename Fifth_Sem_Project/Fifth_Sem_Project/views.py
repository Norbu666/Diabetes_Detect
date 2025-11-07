from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import Patient
import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, '..', 'MLModel', 'model.pkl')
scaler_path = os.path.join(BASE_DIR, '..', 'MLModel', 'scaler.pkl')

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

def cover(request):
    return render(request, 'cover.html')

def index(request):
    form = PatientForm()
    return render(request, 'index.html', {'form': form})

def result_view(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)

            # Prepare data for prediction
            input_data = np.array([[
                patient.pregnancies,
                patient.glucose,
                patient.blood_pressure,
                patient.skin_thickness,
                patient.insulin,
                patient.bmi,
                patient.diabetes_pedigree,
                patient.age
            ]])

            #scale and predict
            scaled_input = scaler.transform(input_data)
            prediction = model.predict(scaled_input)
            
            #save result
            patient.result = "Has diabetes" if prediction == 1 else "No diabetes"
            patient.save()

            return render(request, 'result.html', {
                'result': patient.result,
                'data': request.POST    
            })
    return redirect('form')
