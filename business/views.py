from django.shortcuts import render
from business.models import BusinessForm


def hello(request):
    return render(request, "index.html")


def rezultat(request):

    if request.method == "POST":
        userform = BusinessForm(request.POST)
        info = request.POST
        i = info.dict()
        name = i.get('name')
        business_name = i.get('business_name')
        text = {'form': userform, 'name': name, 'business_name': business_name}
        return render(request, "business_name.html", text)

    else:
        userform = BusinessForm()
        return render(request, "business_name.html", {'form': userform})


