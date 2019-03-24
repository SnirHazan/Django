from django.shortcuts import render

def index(request):
    context_dict = {'text':'Hello world','number':100}
    return render(request,'basicApp/index.html',context_dict)

def other(request):
    return render(request,'basicApp/other.html')

def relative(request):
    return render(request,'basicApp/relative_url_templates.html')