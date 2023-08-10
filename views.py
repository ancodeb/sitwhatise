from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,"main.html")
def new(request):
    return render(request,'new.html')
def page_not_found(request, exception):
	return render(request, '404.html')
def page_error(request):
	return render(request, '403.html')
def OnUploadFile(request):
    text=request.POST.get("a")
    print(text)

