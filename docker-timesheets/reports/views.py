from django.shortcuts import render

# Create your views here.
def report(request):
    template = " timesheet/report.html"

    context = {


    }
    return render(request, template, context)