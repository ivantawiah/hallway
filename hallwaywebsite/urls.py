from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name = 'register'),
    path('blog', views.blog, name = 'blog'),
    path('blog/article/<str:pk>', views.article, name='article'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
    path('blog2', views.blog_two, name='blog 2'),
    #path('post/<str:pk>', views.article, name='post')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)