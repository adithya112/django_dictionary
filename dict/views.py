from .logic import get_word_data, get_meanings
from django.shortcuts import render, redirect
from django.contrib import messages


def home_page(request):
    return render(request, 'dict/home.html')

def search_meaning(request):
    
    if request.method == 'POST':
        word = request.POST['hero-field']
        data = get_word_data(word)
        print(type(data))
        if not isinstance(data, list):
            messages.info(request, data['message'])
            return redirect('dict:search')
            
        meanings_seperated_wrt_pos = []

        for meaning in data[0]["meanings"]:
            meanings_seperated_wrt_pos.append(get_meanings(meaning))
        
        context = {
            'meanings_seperated_wrt_pos':meanings_seperated_wrt_pos
        }
        
        return render(request, 'dict/meanings.html', context)

    
    return render(request, 'dict/search.html')
