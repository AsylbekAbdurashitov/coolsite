
from django.urls import path
from products import views

from products.views import index, glavnaya, o_nas, contacty, vopros #from products import views
urlpatterns = [
    # path("index/", index, name="home"),
    # path("glavnaya/", glavnaya, name="glavnaya"),
    # path("o_nas/", o_nas, name="o_nas"),
    # path("contacty/", contacty, name="contacty"),
    # path("vopros/", vopros, name="voprosy"),

    path("animal/", views.animal, name="animal"),
    path("animal/<str:animal_name>/", views.detail_animal),
    #path("delete-animal/<int:animal_id>/",views.delete_animal),
    path("delete-animal-by-name/<str:animal_name>/", views.delete_animal_by_name),
    path("add-animal/", views.create_animal),
    path("edit-animal/<int:animal_id>/", views.edit_animal),
    path("food/", views.food, name="food"),

]


