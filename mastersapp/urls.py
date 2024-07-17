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

     
    
]