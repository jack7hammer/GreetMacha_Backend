from django.shortcuts import render
from .models import storedInformation
import json
from base64 import b64encode

# Create your views here.
def home(request):
	return render(request,"homepage/index.html",{})

def t1(request):

	if request.method=='POST':
		name=request.POST['bfname']
		message=request.POST['message']
		inImg = request.FILES["inputImage"].read()
		encoded = b64encode(inImg).decode('ascii')
		mime = "image/jpg"
		mime = mime + ";" if mime else ";"
		input_image = "data:%sbase64,%s" % (mime, encoded)
		context={'name':name,'message':message, 'input_image':input_image}
		return render(request,"templates/birthday_template.html", context)
	return render(request,"templates/birthday_template.html")