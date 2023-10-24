from django.shortcuts import render

def moj_widok(request):
    return render(request, 'base.html')
