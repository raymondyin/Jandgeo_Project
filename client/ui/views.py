from django.shortcuts import render
from django.conf import settings
import os
import json
from django import template

def frontpage(request):

	return render(request, "signin.html")

def dashboard(request):

	# with open(os.path.join(settings.MEDIA_ROOT, 'data/testoutput.json')) as file1:
	# 	print file1
	# file1.close()
	data =json.dumps({"t130816043436": "367", "t130816043427": "369", "t130816043431": "365"})
	return render(request, "dashboard.html", {'bigdata' : data})

def test(request):
	return render(request, "testchart.html")


# Helper functions for view functions-------->
