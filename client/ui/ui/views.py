from django.shortcuts import render

def frontpage(request):
	return render(request, "signin.html")

def dashboard(request):
	return render(request, "dashboard.html")

def test(request):
	return render(request, "testchart.html")