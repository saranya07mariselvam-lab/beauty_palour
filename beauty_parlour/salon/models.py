from django.db import models


class Service(models.Model):
    """A single service offered by the parlour, e.g. 'Bridal Makeup'."""

    CATEGORY_CHOICES = [
        ('facial', 'Facial'),
        ('nails', 'Manicure, Pedicure & Nail Art'),
        ('makeup', 'Makeup'),
    ]

    FOR_CHOICES = [
        ('women', 'Women'),
        ('men', 'Men'),
        ('unisex', 'Unisex'),
    ]

    name = models.CharField(max_length=150)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='facial')
    for_gender = models.CharField(max_length=10, choices=FOR_CHOICES, default='unisex')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_minutes = models.PositiveIntegerField(default=30, help_text="Approx. time this service takes")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    is_featured = models.BooleanField(default=False, help_text="Show on homepage highlights")
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Testimonial(models.Model):
    """Customer review shown on the homepage."""

    customer_name = models.CharField(max_length=100)
    message = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=5, help_text="Out of 5 stars")
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.customer_name} - {self.rating}★"


class Enquiry(models.Model):
    """Enquiry / interest form submitted by a visitor from the Contact page."""

    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('closed', 'Closed'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField(blank=True, help_text="Preferred date/time or any special request")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return f"{self.name} - {self.phone} ({self.status})"


class SalonInfo(models.Model):
    """
    Singleton-style model to hold general salon details
    (address, phone, hours) so the owner can edit it from admin
    without touching code.
    """

    salon_name = models.CharField(max_length=150, default="Your Salon Name")
    tagline = models.CharField(max_length=200, blank=True)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    opening_hours = models.CharField(max_length=100, default="Mon - Sun: 9:00 AM - 8:00 PM")
    instagram_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    about_text = models.TextField(blank=True)

    class Meta:
        verbose_name = "Salon Info"
        verbose_name_plural = "Salon Info"

    def __str__(self):
        return self.salon_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj