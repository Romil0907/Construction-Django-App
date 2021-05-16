from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.aboutus, name = 'about us'),
    path('services/',views.services, name = 'services'),
    path('services/water-and-irrigation/', views.water, name = 'Water and Irrigation'),
    path('services/roads-and-highways/', views.roads, name = 'Water and Irrigation'),
    path('services/industrial-and-residential/', views.industry, name = 'Industrial & Residential'),
    path('contact/',views.contact, name='contact'),
    path('career/',views.careers, name='careers'),
    path('career/<str:postname>/<int:post_id>',views.upload, name='upload'),
    path('projects/', views.projects, name = 'projects'),
    path('projects/Construction-of-Underground-Drainage/', views.p1, name='p1'),
    path('projects/Construction-of-Underground-Drainage-project-for-Bikaner/', views.p2, name='p2'),
    path('projects/Construction-of-Underground-Drainage-project-for-Kanpur/', views.p3, name='p3'),
    path('projects/Construction-of-Underground-Drainage-project-for-Loni-Ghaziabad/', views.p4, name='p4'),
    path('projects/Constructing-of-Sewage-Collection-network-at-Zone-A-Zone-B-and-Zone-C-including-electro-mechanical-works-along-with-Operation-and-Maintenance-for-a-period-of-(05)-Five-years-at-Palanpur/', views.p5, name='p5'),
    path('projects/Survey-review-the-designs-redesign-where-necessary-and-build-sewage-collection-and-conveyance-system-sewage-treatment-and-disposal-system-of-Narsinghpur-Nagar-Palika-district-Narsinghpur-of-Madhya-Pradesh-and-operate-and-maintain-the-built-system-for-10-years/', views.p6, name='p6'),
    path('projects/Survey-Review-the-Designs-Redesign-Where-Necessary-and-Build-Water-Supply-Augmentation-Scheme-for-Sewda-Town-Datia-District-of-Madhya-Pradesh-And-Operate-and-Maintain-the-Built-System-for-5-Years/', views.p7, name='p7'),
    path('projects/Construction-of-Barbed-Wire-fencing-and-Road-for-Gift-Project/', views.p8, name='p8'),
    path('projects/Construction-of-Commercial-Building-Shangri-La-Arcade-t-satellite-Ahmedabad/', views.p9, name='p9'),
    path('projects/Augmentation-to-Water-Supply-Scheme-at-Santrampur/', views.p10, name='p10'),
    path('projects/Construction-and-Development-of-Sez-Building-at-GIFT-City-Gandhinagar/', views.p11, name='p11'),
    path('projects/Construction-of-Commercial-Building-S-Mall-at-Kubernagar-Naroda-Ahmedabad/', views.p12, name='p12'),
    path('projects/Construction-of-Sez-Building-(ZFC-Extension)-In-GIFT-Sez-Area/', views.p13, name='p13'),
    path('projects/Construction-of-District-Cooling-System/', views.p14, name='p14'),
    path('projects/Construction-of-sewerage-project-at-Khedbhrama/', views.p15, name='p15'),
    path('projects/Construction-of-sewerage-project-at-Santrampur-town/', views.p16, name='p16'),
    path('projects/Construction-of-sewerage-project-at-Palanpur/', views.p17, name='p17'),
    path('projects/Construction-of-sewerage-project-and-allied-work-at-Roorkee-Uttarakhand/', views.p18, name='p18'),
    path('projects/Construction-of-Underground-Drainage-project-for-town-Nimbahera-Bari-Sadri-Kushalgarh-and-Fatehnagar/', views.p19, name='p19'),
    # path('projects/', views.p20, name='p20'),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, cv_root=settings.MEDIA_ROOT)