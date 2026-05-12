from django.shortcuts import render


def home(request):

    questions = [
        {"country": "France", "capital": "Paris", "image": "images/france.png"},
        {"country": "Canada", "capital": "Montreal", "image": "images/canada.png"},
        {"country": "Brazil", "capital": "Brasilia", "image": "images/brazil.png"},
        {"country": "Monaco", "capital": "Monaco", "image": "images/monaco.png"},
        {"country": "Spain", "capital": "Madrid", "image": "images/spain.png"},
        {"country": "Singapore", "capital": "Singapore", "image": "images/singapore.png"},
        {"country": "Japan", "capital": "Tokio", "image": "images/japan.png"},
        {"country": "Israel", "capital": "Jerusalem", "image": "images/israel.png"},
        {"country": "China", "capital": "Beijing", "image": "images/china.png"},
        {"country": "Australia", "capital": "Canberra", "image": "images/australia.png"},
    ]

    current_question = questions[0]

    context = {
        "country_name": current_question["country"],
        "flag_image": current_question["image"],
    }

    return render(request, 'index.html', context)