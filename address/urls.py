from . import views
from django.urls import path


app_name = "address"
urlpatterns = [
    path('', views.login, name="login"),

    path('signup', views.signup, name="signup"),

    path('address-book', views.address_book, name="address_book"),

    path('add-address', views.add_address, name="add_address"),

    path('view-address/<int:id>', views.view_address, name="view_address"),

    path('edit-address/<int:edit_id>', views.edit_address, name="edit_address"),

    path('logout', views.logout, name="logout"),

    path('search', views.search, name="search"),

    path('geo', views.test1, name="geo"),
]
