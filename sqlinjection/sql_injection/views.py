'''Use pip install -r requirements.txt to install all neccessary dependencies'''

'''Importing nessessary class needed'''
from django.shortcuts import redirect, render
from .forms import InputForm
from .models import SqlInjection

'''This function handles the incoming post request and check 
   if the incoming data from the request body is suspicious.'''
def index(request):
    if request.method == "POST":
        form = InputForm(request.POST)  
        if form.is_valid():
            statement = request.POST.get('statement')
            injection = SqlInjection.objects.filter(statement=statement)
            if injection.exists():
                return redirect('success-page')
            else:
                return redirect('failed')
        else:
            return redirect('index')
    else:
        form = InputForm()
    return render(request, 'index.html', context={"form":form})

'''This function display the success page if the query is not suspecious'''
def success_page(request):
    return render(request, 'success-page.html')

'''This function display failed page if the query is suspecious'''
def failed(request):
    return render(request, 'failed-page.html')