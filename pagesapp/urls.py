from django.urls import path
from .views import HomePageView , AboutPageView , NewsPageView , ConPageView

urlpatterns = [
    path('', HomePageView.as_view() , name='home'),
    path('about/' , AboutPageView.as_view() , name='about'),
    path('news/' , NewsPageView.as_view() , name='news'),
    path('contacts/' , ConPageView.as_view() , name='contacts'),
]