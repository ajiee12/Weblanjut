from django.contrib import admin
from django.urls import path, include



#untuk media
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

#memanggil fungsi home yang ada di vile views


from . views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #apps
    path('dashboard/', include('blog.urls')),
    path('', home, name='home'),
    path('artikel/<int:id>/detail/', detail_artikel, name='detail_artikel'),
    path('about/', about, name='about'),

    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registrasi, name='registrasi'),

    path('ckeditor/', include('ckeditor_uploader.urls')),


]

#untuk media
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
