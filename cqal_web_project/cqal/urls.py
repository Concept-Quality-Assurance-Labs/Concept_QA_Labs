from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('knowmore/', views.Knowmore, name="Knowmore"),
    path('cmmi/', views.cmmi, name="cmmi"),
    path('faq/', views.faq, name="faq"),
    path('training/', views.training, name="training"),
    path('iso/', views.iso, name="iso"),
    path('ai/', views.ai, name="ai"),
    path('metrics/', views.metrics, name="metrics"),
    path('appraisals/', views.Appraisals, name="appraisals"),
    path('iso9001/', views.iso9001, name="iso9001"),
    path('iso27001/', views.iso27001, name="iso27001"),
    path('iso20000/', views.iso20000, name="iso20000"),
    path('directory/', views.directory, name="directory"),
    path('accrediatations/', views.Accrediatations, name="accrediatations"),
    path('update1/', views.update_1, name="update1"),
    path('update2/', views.update_2, name="update2"),
    path('update3/', views.update_3, name="update3"),



]

