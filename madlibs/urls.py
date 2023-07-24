from django.urls import path

from madlibs import views

# namespacing
app_name = 'madlibs'

urlpatterns = [
    path('', views.index, name="index"),
    path('madlibs/', views.stories, name="stories"),
    path('madlibs/<int:story_id>', views.story, name="play"),
    path('story/<int:record_id>', views.read_story, name="read_story"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]