from django.shortcuts import render
from .models import Vacancy
from .forms import FindForm

def home_view(request):
    form = FindForm()
    language = request.GET.get('language')
    citi = request.GET.get('citi')
    form_request = dict()
    if language or citi:
        if language:
            form_request['language__slug'] = language
        if citi:
            form_request['citi__slug'] = citi
    querySet = Vacancy.objects.filter(**form_request)
    return render(request, 'myapp/home.html', {'object_list': querySet,
                                                      'form': form})


