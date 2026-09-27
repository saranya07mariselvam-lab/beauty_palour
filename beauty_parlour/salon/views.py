from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Service, Testimonial, SalonInfo
from .forms import EnquiryForm,FeedbackForm


def home(request):
    salon = SalonInfo.get_solo()
    featured_services = Service.objects.filter(is_active=True, is_featured=True)[:6]
    testimonials = Testimonial.objects.filter(is_active=True)[:6]
    context = {
        'salon': salon,
        'featured_services': featured_services,
        'testimonials': testimonials,
    }
    return render(request, 'salon/home.html', context)


def services(request):
    salon = SalonInfo.get_solo()
    category = request.GET.get('category', 'all')
    gender = request.GET.get('gender', 'all')

    service_list = Service.objects.filter(is_active=True)
    if category != 'all':
        service_list = service_list.filter(category=category)
    if gender != 'all':
        service_list = service_list.filter(for_gender__in=[gender, 'unisex'])

    context = {
        'salon': salon,
        'services': service_list,
        'categories': Service.CATEGORY_CHOICES,
        'selected_category': category,
        'selected_gender': gender,
    }
    return render(request, 'salon/services.html', context)


def service_detail(request, pk):
    salon = SalonInfo.get_solo()
    service = get_object_or_404(Service, pk=pk, is_active=True)
    related = Service.objects.filter(category=service.category, is_active=True).exclude(pk=pk)[:3]
    context = {'salon': salon, 'service': service, 'related': related}
    return render(request, 'salon/service_detail.html', context)


def pricing(request):
    salon = SalonInfo.get_solo()
    women_services = Service.objects.filter(is_active=True, for_gender__in=['women', 'unisex'])
    men_services = Service.objects.filter(is_active=True, for_gender__in=['men', 'unisex'])
    context = {'salon': salon, 'women_services': women_services, 'men_services': men_services}
    return render(request, 'salon/pricing.html', context)


def about(request):
    salon = SalonInfo.get_solo()
    return render(request, 'salon/about.html', {'salon': salon})


def contact(request):
    salon = SalonInfo.get_solo()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! We've received your enquiry and will contact you shortly.")
            return redirect('salon:contact')
    else:
        form = EnquiryForm()
    return render(request, 'salon/contact.html', {'salon': salon, 'form': form})

def feedback(request):
    salon = SalonInfo.get_solo()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your feedback! It will be reviewed and posted shortly.")
            return redirect('salon:feedback')
    else:
        form = FeedbackForm()
    return render(request, 'salon/feedback.html', {'salon': salon, 'form': form})
