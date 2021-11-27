from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.site.site_header = 'Engage Student Welfare'      # default: "Django Administration"
admin.site.index_title = 'Admin Site'                 # default: "Site administration"
admin.site.site_title = 'Powered by Microsoft Engage Program' # default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('student/',include('student.urls')),
    path('dadmin/',include('admin.urls')),
    path('faculty/',include('faculty.urls')),
    path('librarian/',include('librarian.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'base.views.handler404'