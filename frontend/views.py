from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):

    return render(request, 'index.html')

def aboutus(request):

    return render(request, 'about.html', )

def careers(request):
    vaccancy = post.objects.all()
    return render(request, 'career.html', {'vaccancy':vaccancy})

def upload(request, post_id, postname):

    if request.method == 'POST':
        name = request.POST.get('name')
        cv = request.FILES['cv']
        # postname = request.POST.get('postname')
        fs = FileSystemStorage()
        # fs.save(cv.name, cv)


        # final_cv = {
        #     "name":name,
        #     "cv":cv,
        #     postname: postname
        # }

        cvModel.objects.create(cv=cv, post_id=post_id)
        
        message = "success"

        return render(request, 'upload_cv.html', {'message':message})

    posst = post.objects.get(post_id=post_id)
    return render(request, 'upload_cv.html', {'post':posst})



def cvview(request, cv):

    cvs = cvModel.objects.get(cv=cv)

    return render(request, 'cvview.html', {'cvs':cvs})





def contact(request):

    return render(request, 'contact.html')

def services(request):
    return render(request, 'service.html')

def projects(request):
    return render(request, 'Projects.html')

def p1(request):
    return render(request, 'p1.html')

def p2(request):
    return render(request, 'p2.html')

def p3(request):
    return render(request, 'p3.html')

def p4(request):
    return render(request, 'p4.html')

def p5(request):
    return render(request, 'p5.html')

def p6(request):
    return render(request, 'p6.html')

def p7(request):
    return render(request, 'p7.html')

def p8(request):
    return render(request, 'p8.html')

def p9(request):
    return render(request, 'p9.html')

def p10(request):
    return render(request, 'p10.html')

def p11(request):
    return render(request, 'p11.html')

def p12(request):
    return render(request, 'p12.html')

def p13(request):
    return render(request, 'p13.html')

def p14(request):
    return render(request, 'p14.html')

def p15(request):
    return render(request, 'p15.html')

def p16(request):
    return render(request, 'p16.html')

def p17(request):
    return render(request, 'p17.html')

def p18(request):
    return render(request, 'p18.html')

def p19(request):
    return render(request, 'p19.html')

# def p20(request):
#     return render(request, 'p20.html')

def water(request):
    return render(request, 'Water and Irrigation.html')

def roads(request):
    return render(request, 'roads and highways.html')

def industry(request):
    return render(request, 'industrial and residential.html')