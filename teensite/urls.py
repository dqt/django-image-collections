from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'teensite.myapp.views.home', name='home'),
    url(r'categories/', 'teensite.myapp.views.view_categories', name='categories'),
    url(r'posts/', 'teensite.myapp.views.view_posts', name='posts'),
    # url(r'^teensite/', include('teensite.foo.urls')),
    url(
        r'^view/(?P<slug>[^\.]+)',
        'teensite.myapp.views.view_post',
        name='view_post'),
    url(
        r'^category/(?P<slug>[^\.]+)',
        'teensite.myapp.views.view_category',
        name='view_category'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
