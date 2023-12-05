
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [

    path('', views.index),
    path('index.html', views.index),
    path('listings.html', views.listings, name='listings'),
    path('create.html', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('listing/<int:id>/', views.listing, name='listing'),
    path('bidding/<int:id>/', views.bidding, name='bidding'),
    path('bidform.html', views.create_bid, name='create_bid'),  # Add this line for bidform 
    path('delete/<int:id>/', views.delete, name='delete'),
    path('bid_update/<int:id>/', views.bid_update, name='bid_update'),
    path('logout/',views.LogoutPage,name='logout'),
    path('login/',views.LoginPage,name='login'),
    
    
    path('index.html', views.index), 
    path('about.html', views.webpage2), 
    path('service.html', views.webpage3),
    path('team.html', views.webpage7),
    path('contact.html', views.webpage9),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    