# birthday/forms.py
from django import forms

# Импортируем класс модели Birthday.
from .models import Birthday


# Для использования формы с моделями меняем класс на forms.ModelForm.
class BirthdayForm(forms.ModelForm):
    # Удаляем все описания полей.

    # Все настройки задаём в подклассе Meta.
    class Meta:
       
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        fields = '__all__'
        widgets = {'birthday': forms.DateInput(attrs={'type': 'date'})}




# Создание класса Forms версия 1 .
# class BirthdayForm(forms.Form):
#    first_name = forms.CharField(label='Имя', max_length=20)
#    last_name = forms.CharField(
#        label ='Фамилия', required=False, help_text='Необязательное поле'
#    )
#    birthday = forms.DateField(
#        label='Дата рождения',
#        # Указываем, что виджет для ввода даты должен быть с типом date.
#        widget = forms.DateInput(attrs={'type': 'date'})
#    )
