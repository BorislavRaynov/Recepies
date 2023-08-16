from django import forms
from .models import Recepie


class BaseRecepieForm(forms.ModelForm):
    class Meta:
        model = Recepie
        fields = '__all__'


class CreateRecepieForm(BaseRecepieForm):
    pass


class EditRecepieForm(BaseRecepieForm):
    pass


class DeleteRecepieForm(BaseRecepieForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

