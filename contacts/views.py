from django.core.urlresolvers import reverse_lazy, reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from contacts.models import PersonContact, ContactService


def index(request):

    # if request.user.has_perm('contacts.view_contact'):
    #     print('yey')
    # else:
    #     print('nope')

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

    if request.user.has_perm('contacts.view_contact'):
        contact = get_object_or_404(PersonContact, pk=contact_id)

        return render(
            request,
            'contacts/showContact.html',
            {
                'contact': contact
            }
        )
    else:
        return HttpResponseRedirect(
            reverse('index')
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
        name__icontains=query
    )
    return render(
        request,
        'contacts/search_result.html',
        {
            'contacts': contacts
        }
    )
