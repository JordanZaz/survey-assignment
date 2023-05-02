from django.urls import path
from . import views

urlpatterns = [
    path('', views.onboarding_form, name='onboarding_form'),
    path('onboarding_form/save_data/',
         views.save_form_data, name='save_form_data'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('results/', views.results, name='results'),
    path('clear_survey_id/', views.clear_survey_id, name='clear_survey_id'),
]
