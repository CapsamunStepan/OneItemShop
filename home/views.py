from django.shortcuts import render
from home.forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def home(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            subject = "Заказ"
            message = f'{name} хочет заказать у вас камеру с солнечной панелью\n {phone}'
            email = 'recepientmsg@gmail.com'
            password = 'wmec epqq zbph pmbq'
            recipient_email = 'popovvalentina189@gmail.com'
            send_mail(subject=subject,
                      message=message,
                      from_email=email,
                      recipient_list=[recipient_email],
                      auth_user=email,
                      auth_password=password)
            sent = True
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form, 'sent': sent})
