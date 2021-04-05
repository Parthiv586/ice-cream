from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ind,name='ind'),
    path('cup',views.cups,name='cup'),
    path('cons',views.cons,name='cons'),
    path('contact/',views.contact,name='contact'),
    path('contact2/',views.contact2,name='contact'),
    path('family',views.family,name='family'),
    path('about',views.about,name='about'),
    # path('',views.,name=''),

]
