from django.shortcuts import render

# Create your views here.



def index(request, name):
    # name = "Eric Gabriel"
    
    colors = ['Red', 'White', 'Green', 'Yellow']
    print(type(name))
    
    return render(
        request=request, 
        template_name="app1/index.html", 
        context={
            "name": name, 
            "colors": colors
        })
