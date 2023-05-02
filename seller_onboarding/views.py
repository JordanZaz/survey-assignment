from django.shortcuts import render, redirect
from .models import SellerOnboarding
from .forms import SellerOnboardingForm
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import uuid


def onboarding_form(request):
    if 'survey_id' not in request.session:
        request.session['survey_id'] = str(uuid.uuid4())

    survey_id = request.session['survey_id']

    try:
        seller_onboarding = SellerOnboarding.objects.get(survey_id=survey_id)
    except SellerOnboarding.DoesNotExist:
        seller_onboarding = SellerOnboarding.objects.create(
            survey_id=survey_id)

    form = SellerOnboardingForm(
        request.POST or None, instance=seller_onboarding)
    if form.is_valid():
        form.save()
        if 'next' in request.POST:
            return redirect(request.path)
        elif 'submit' in request.POST:
            return redirect('thank_you')

    return render(request, 'seller_onboarding/onboarding_form.html', {'form': form})


def thank_you(request):
    return render(request, 'seller_onboarding/thank_you.html')


def results(request):
    sellers = SellerOnboarding.objects.all()
    # print("Fetched Sellers: ", sellers)
    return render(request, 'seller_onboarding/results.html', {'sellers': sellers})


@csrf_exempt
def save_form_data(request):
    if request.method == 'POST':
        survey_id = request.POST.get('survey_id', '')
        if not survey_id:
            return JsonResponse({"success": False, "message": "No survey_id provided"})

        seller_onboarding, _ = SellerOnboarding.objects.get_or_create(
            survey_id=survey_id)

        form = SellerOnboardingForm(
            request.POST, instance=seller_onboarding)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "errors": form.errors})
    else:
        return HttpResponse(status=405)  # Method not allowed


@csrf_exempt
def clear_survey_id(request):
    if request.method == 'POST':
        if 'survey_id' in request.session:
            del request.session['survey_id']
        return JsonResponse({"success": True})
    else:
        return HttpResponse(status=405)  # Method not allowed
