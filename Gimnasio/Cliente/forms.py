from django import forms
from .models import ReservaTurno

class ReservaTurnoForm(forms.ModelForm):
    class Meta:
        model = ReservaTurno
        fields = ['fecha', 'hora']

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha < datetime.date.today():
            raise forms.ValidationError("La fecha no puede ser en el pasado.")
        return fecha