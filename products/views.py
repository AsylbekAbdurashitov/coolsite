from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models import Animal, Actor, Food
from django import forms




menudd = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]

data_db = [
    {'id': 1, 'title': 'Асылбек', 'content': 'Биография Асылбека', 'is_published': True},
    {'id': 2, 'title': 'Луиза', 'content': 'Биография Луизы', 'is_published': True},
    {'id': 3, 'title': 'Нурмухаммед', 'content': 'Биография Нурмухаммеда', 'is_published': False},
]
#
# def index(request):
#     data = {"menu": menu,
#             "posts": data_db,
#             "title": "Glavnaya stranisa"}
#     return render(request, "Index.html", context=data)

# def about(request):
#     return render(request, "about.html", {"title": "O saite"})
def show_post(request, post_id):
    return HttpResponse(f"Otabrajenie stati s id = {post_id}")
def addpage(request):
    return HttpResponse('Добавление поста')
def contact(request):
    return HttpResponse('Обратная связь')
def login(request):
    return HttpResponse('Авторизация')
new_names = ["Ishak", "Nurislam", "Ariet", "Eldar", "Asylbek", "Bek", "Aidana", "Luiza"]


def index(request):
    names = {"new_names": new_names}
    return render(request, "index.html", context=names)


hobby = ["Sleeping", "Programming", "Footbal", "Reading", "Volleybal", "Table tennis"]

menu = ["Главная страница", "О нас", "Наши контакты", "Вопросы"]


def animal(request):
    animal = Animal.objects.all()
    new_animal = {"new_animal": animal}
    return render(request, "animal2.html", context=new_animal)


def detail_animal(request, animal_name):
    animal = Animal.objects.filter(name=animal_name)
    new_animal = {"new_animal": animal}
    return render(request, "animal2.html", context=new_animal)


def create_animal(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        breed = request.POST.get("breed")
        animal = Animal.objects.create(
            name=name,
            age=age,
            breed=breed,
        )
        animal.save()
        return redirect("animal")


# def delete_animal(request, animal_id):
#     animal = Animal.objects.filter(id=animal_id)
#     animal.delete()
#     return redirect(request, "animal.html", context=new_animals)


def delete_animal_by_name(request, animal_name):
    animal = Animal.objects.filter(name=animal_name)
    animal.delete()
    return redirect("animal")


def edit_animal(request, animal_id):
    animal = Animal.objects.filter(id=animal_id).first()
    new_animal = {"animal": animal}
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        breed = request.POST.get("breed")
        Animal.objects.filter(id=animal_id).update(
            name=name,
            age=age,
            breed=breed
        )
        return redirect("animal")
    return render(request, "edit_animal.html", context=new_animal)





def actor(request):
    actor = Actor.objects.all()
    new_actor = {"new_actor": actor}
    return render(request, "actor.html", context=new_actor)


def detail_actor(request, actor_name):
    actor = Actor.objects.filter(name=actor_name)
    new_actor = {"new_actor": actor}
    return render(request, "actor.html", context=new_actor)


def add_actor(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        age = request.POST.get("age")
        bio = request.POST.get("bio")
        salary = request.POST.get("salary")
        image = request.POST.get("Photo")
        actor = Actor.objects.create(
            firstname=firstname,
            lastname=lastname,
            age=age,
            bio=bio,
            salary=salary,
            image=image
        )
        actor.save()
        return redirect("actor")


def edit_actor(request, actor_id):
    actor = Actor.objects.filter(id=actor_id).first()
    new_actor = {"actor": actor}
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        print(111111)
        lastname = request.POST.get("lastname")
        age = request.POST.get("age")
        bio = request.POST.get("bio")
        salary = request.POST.get("salary")
        image = request.POST.get("Photo")
        Actor.objects.filter(id=actor_id).update(
            firstname=firstname,
            lastname=lastname,
            age=age,
            bio=bio,
            salary=salary,
            image=image
        )
        return redirect("actor")
    return render(request, "edit_actor.html", context=new_actor)


def delete_actor_by_firstname(request, actor_firstname):
    actor = Actor.objects.filter(name=actor_firstname)
    actor.delete()
    return redirect("actor")


def delete_actor(request, actor_id):
   actor = Actor.objects.filter(id=actor_id)
   actor.delete()
   return redirect("actor")


menu1 = [{'title': "Главная страница", 'url_name': 'glavnaya'},
        {'title': "О нас", 'url_name': 'o_nas'},
        {'title':  "Наши контакты", 'url_name': 'contact'},
        {'title': "Вопросы", 'url_name': 'vopros'}
        ]


def glavnaya(request):
    return HttpResponse('Главная страница')


def o_nas(request):
    return HttpResponse('О нас')


def contacty(request):
    return HttpResponse('Наши контакты')


def vopros(request):
    return HttpResponse('Вопросы"')


menu = ["Главная страница", "О нас", "Наши контакты", "Вопросы"]


def food(request):
    food = Food.objects.all()
    new_food = {"new_food": food, "menu": menu}
    return render(request, "food.html", context=new_food)


