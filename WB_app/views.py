from wsgiref.util import request_uri
from django.shortcuts import render
import joblib

# Create your views here.

def home(request):
    return render(request,'home.html')

def predict(request):
    model = joblib.load('wb_model.sav')
    #model = joblib.load(r'C:\Users\pc\Desktop\wb\wb_model.sav')
    input = []
    input.append(request.GET['lfya9'])
    input.append(request.GET['salaire'])
    input.append(request.GET['lwlad'])
    input.append(request.GET['tkarfis'])
    print(input)
    inputint = []
    for n in input:
        n = int(n)
        inputint.append(n)
    pred = model.predict([inputint])
    ins =[ 'lfya9' , 'salaire' , 'lwlad' , 'tkarfis' ]
    return render(request,'predict.html',{'pred':pred, 'inputint':inputint, 'ins':ins})
