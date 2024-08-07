from django.contrib import admin

# Register your models here.
from medicify_project.models import *


# Register your models here.

@admin.register(TblDoctorSubscription)
class TblDoctorSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('doctor_subscription_id', 'doctor_id', 'master_subscription_id', 'subscription_start_on', 'subscription_end_on', 'subscription_price', 'subscription_tax1', 'subscription_tax2', 'subscription_amount', 'subscription_paid_amount', 'subscription_discount_amount', 'subscription_discount_type', 'subscription_promo_code', 'subscription_type', 'subscription_billing_name', 'subscription_billing_GstNo', 'subscription_billing_address', 'subscription_billing_pincode', 'subscription_billing_city', 'subscription_status', 'entry_operator_type', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'deleted_by', 'is_deleted')

@admin.register(TblMasterSubscription)
class TblMasterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('master_subscription_id', 'name', 'price', 'tax_one', 'tax_two', 'is_trial', 'total_days', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'deleted_by', 'is_deleted')

@admin.register(TblDoctorSubscriptionPromocodes)
class TblDoctorSubscriptionPromocodesAdmin(admin.ModelAdmin):
    list_display = ('promocode_id', 'promo_code', 'promo_code_activation_on', 'promo_code_valid_till', 'promo_code_value', 'promo_code_value_type', 'promo_code_status', 'entry_operator_id', 'entry_operator_type', 'promo_code_used_by', 'promo_code_used_on', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'deleted_by', 'is_deleted')

