from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите ваше имя'
        self.fields['phone'].widget.attrs['placeholder'] = 'Введите ваш номер телефона'
