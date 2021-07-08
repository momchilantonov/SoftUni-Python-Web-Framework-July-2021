from media_demo.phones.forms import PhoneForm
from media_demo.phones.models import Phone
from django.shortcuts import redirect, render


def index(req):
    phones = Phone.objects.all()
    for phone in phones:
        phone.selected_image = phone.phoneimage_set.filter(is_selected=True).first()
    form = PhoneForm()
    context = {
        'phones': phones,
        'form': form,
    }
    return render(req, 'index.html', context)


def create_phone(req):
    form = PhoneForm(req.POST, req.FILES)
    if form.is_valid():
        form.save()
        return redirect('index')