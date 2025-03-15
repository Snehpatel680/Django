from django.shortcuts import render

def employee(request):
    if request.method == "POST":
        emp = emplo()
        emp.fname = request.POST.get('fname')
        emp.image = request.FILES.get('image')
        emp.save()
        return redirect('emplist')
    else:
        return render(request, 'employee.html')
# Create your views here.
