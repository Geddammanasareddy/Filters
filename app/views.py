from django.shortcuts import render

# Create your views here.

def built_in_filters(request):
    import datetime
    dt=datetime.datetime.now()

    d={'data':'hI HoW ArE yOu','dt':dt,'c':3}



    return render(request,'built_in_filters.html',d)