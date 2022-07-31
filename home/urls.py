from django.urls import path
from . import views


urlpatterns = [path("",views.home,name='home'),path("about/",views.about,name="about")
               ,path("org/",views.org,name="org"),path("barn/",views.barn,name="barn")

]

