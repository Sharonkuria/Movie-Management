from django.conf.urls.static import  static
from movieproject import settings
from django.urls import path
from . import views
from . forms import MovieForm
app_name='movieapp'

urlpatterns = [
    path('',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)