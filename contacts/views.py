from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from contacts.models import PersonContact, ContactService


def index(request):
    services = ContactService.objects.all()
    return render(
        request,
        'contacts/index.html',
        {
            'services': services
        })

def viewServices(request):
    return HttpResponse("Services page")

def viewContact(request, contact_id):

    contact = get_object_or_404(PersonContact, pk=contact_id)

    return render(
        request,
        'contacts/showContact.html',
        {
            'contact': contact
        }
    )

def viewService(request, service_id):
    service = get_object_or_404(ContactService, pk=service_id)

    return render(
        request,
        'contacts/showService.html',
        {
            'service': service
        }
    )

def searchContact(request):
    query = request.POST['contact_search_query']
    contacts = PersonContact.objects.filter(
        name__contains=query
    )
    return render(
        request,
        'contacts/search_result.html',
        {
            'contacts': contacts
        }
    )
