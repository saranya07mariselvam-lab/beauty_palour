from django.contrib import admin
from .models import Service, Testimonial, Enquiry, SalonInfo


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'for_gender', 'price', 'duration_minutes', 'is_featured', 'is_active')
    list_filter = ('category', 'for_gender', 'is_featured', 'is_active')
    search_fields = ('name', 'description')
    list_editable = ('price', 'is_featured', 'is_active')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'rating', 'is_active', 'created_at')
    list_filter = ('rating', 'is_active')
    search_fields = ('customer_name', 'message')


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service', 'status', 'created_at')
    list_filter = ('status', 'service')
    search_fields = ('name', 'phone', 'email')
    list_editable = ('status',)
    readonly_fields = ('created_at',)


@admin.register(SalonInfo)
class SalonInfoAdmin(admin.ModelAdmin):
    list_display = ('salon_name', 'phone', 'email')

    def has_add_permission(self, request):
        return not SalonInfo.objects.exists()