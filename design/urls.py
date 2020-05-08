from django.urls import path
from . import views

urlpatterns=[path('',views.index,name="index"),
             path('login',views.login,name="login"),
             path('regester',views.regester,name="regester"),
             path('logout',views.logout,name="logout"),
              path('kitchen',views.kitchen,name="kitchen"),
               path('livingroom',views.livingroom,name="livingroom"),
                path('bedroom',views.bedroom,name="bedroom"),
                 path('price',views.price,name="price"),
                  path('testi',views.testi,name="testi"),
                   path('about',views.about,name="about"),
                    path('regidesigner',views.regidesigner,name="regidesigner")]