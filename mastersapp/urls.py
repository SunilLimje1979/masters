from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
     ######################### Medicines Instruction ############################
     path("get_medicine_instruction",get_medicine_instruction,name='get_medicine_instruction'),
     path("delete_medicine_instruction",delete_medicine_instruction,name='delete_medicine_instruction'),
     path("insert_medicine_instruction",insert_medicine_instruction,name='insert_medicine_instruction'),
     path("update_medicine_instruction",update_medicine_instruction,name='update_medicine_instruction'),
     path("get_medicine_instructionsbydoctorId",get_medicine_instructionsbydoctorId,name='get_medicine_instructionsbydoctorId'),
     

     ######################### Data Code Master ############################
     path("get_datacodemaster",get_datacodemaster,name='get_datacodemaster'),
     path("insert_datacodemaster",insert_datacodemaster,name='insert_datacodemaster'),
     path("update_datacodemaster",update_datacodemaster,name='update_datacodemaster'),
     path("delete_datacodemaster",delete_datacodemaster,name='delete_datacodemaster'),
     
     path("get_datacodemaster_byname",get_datacodemaster_byname,name='get_datacodemaster_byname'),
     path("get_datacodemaster_by_name_and_doctor/",get_datacodemaster_by_name_and_doctor),
     path("update_datacodemaster_byid/",update_datacodemaster_byid),
     path('login/',login,name='login'),
     path("insert_lead/",insert_lead,name='insert_lead'),
     path('get_all_leads/',get_all_leads,name='get_all_leads'),
     path('get_lead_by_id/',get_lead_by_id,name='get_lead_by_id'),
     path('update_lead/',update_lead,name='update_lead'),
     path('get_leads_by_handler_or_by_id/',get_leads_by_handler_or_by_id,name='get_leads_by_handler_or_by_id'),
     path('insert_lead_followup/',insert_lead_followup,name='insert_lead_followup'),
     path('insert_lead_followup/',insert_lead_followup,name='insert_lead_followup'),
     path('get_followups_by_lead_id/',get_followups_by_lead_id,name='get_followups_by_lead_id'),
     path('get_all_countries/',get_all_countries,name='get_all_countries'),
     path('get_country_by_id/',get_country_by_id,name='get_country_by_id'),
     path('get_all_states/',get_all_states,name='get_all_states'),
     path('get_state_by_id/',get_state_by_id,name='get_state_by_id'),
     path('get_states_by_country_id/',get_states_by_country_id,name='get_states_by_country_id'),
     path('get_cities_by_state_id/',get_cities_by_state_id,name='get_cities_by_state_id'),
     path('get_city_by_id/',get_city_by_id,name='get_city_by_id'),
     path('get_cities_by_state_and_country/',get_cities_by_state_and_country,name='get_cities_by_state_and_country'),
     path('get_followups_by_user_and_app/',get_followups_by_user_and_app,name='get_followups_by_user_and_app'),
     path('get_all_Authusers/',get_all_Authusers,name='get_all_Authusers'),
     path('insert_doctor_subscription/',insert_doctor_subscription,name='insert_doctor_subscription'),
     path('get_all_master_subscriptions/',get_all_master_subscriptions,name='get_all_master_subscriptions'),
     path('validate_subscription/',validate_subscription,name='validate_subscription'),

]