from django.forms import ModelForm, TextInput, Select
from django import forms
from tempus_dominus.widgets import DatePicker

from OBTaller.models import UnidadCombustible, UnidadPeaje


class UnidadCombustibleForm(ModelForm):

    # fh_ticket = forms.DateField(widget=DatePicker())
    fh_ticket = forms.DateField(
        # input_formats=['%d/%m/%Y'],
        # widget=forms.DateInput(attrs={
        widget=DatePicker(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#id_fh_ticket',
            'data-toggle': "datetimepicker"
        })
    )
    test = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_unidad_asigna'].widget=forms.HiddenInput()
        # self.fields['fh_registro'].widget=forms.HiddenInput()
        self.fields['tx_referencia'].required=True
        self.fields['fh_ticket'].required=True
        self.fields['imp_ticket'].required=True
        self.fields['cantidad'].required=True
        self.fields['img_ticket'].required=True


        self.fields['tx_referencia'].label = "Nombre/Titulo/Referencia"
        self.fields['fh_ticket'].label = "Fecha del ticket"
        self.fields['imp_ticket'].label = "Importe total"
        self.fields['cantidad'].label = "unida_medida_combustible"
        self.fields['img_ticket'].label = "Fotografia del ticket"

        self.fields['tx_referencia'].widget.attrs['autofocus'] = True

        # if kwargs['instance']:
        #
        #     ticket = kwargs['instance']
        #     self.test = ticket.fh_ticket.strftime("%d/%m/%Y")
        #     self.fields['fh_ticket'].initial = ticket.fh_ticket.strftime("%d/%m/%Y")
        #     self.fields['fh_ticket'].initial = ticket.fh_ticket.strftime("%d/%m/%Y")
        #     self.test = ticket.fh_ticket
        # else:
        #     self.test = 1

    class Meta:
        model = UnidadCombustible
        fields = ['tx_referencia', 'fh_ticket', 'imp_ticket', 'cantidad', 'img_ticket', 'id_unidad_asigna']
        widgets = {
            'tx_referencia': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre o referencia',
                }
            ),
            'fh_ticket': forms.DateTimeInput(attrs={
                        'class': 'form-control datetimepicker-input',
                        'data-target': '#id_fh_ticket',
                        'data-toggle' : "datetimepicker"
                    }),
            'imp_ticket':    TextInput(
                attrs={
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'value': "0.00"
                }
            ),
            'cantidad': TextInput(
                attrs={
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'value': "0.00"
                }
            )

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data = {}
                data['error'] = form.errors
        except Exception as e:
            data = {}
            data['error'] = str(e)
        return data


class UnidadPeajeForm(ModelForm):

    # fh_ticket = forms.DateField(widget=DatePicker())
    fh_ticket = forms.DateField(
        # input_formats=['%d/%m/%Y'],
        # widget=forms.DateInput(attrs={
        widget=DatePicker(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#id_fh_ticket',
            'data-toggle': "datetimepicker",
             'dateFormat' : 'dd/mm/yy'
        })
    )
    test = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_unidad_asigna'].widget=forms.HiddenInput()
        self.fields['id_unidad'].widget=forms.HiddenInput()
        # self.fields['fh_registro'].widget=forms.HiddenInput()
        self.fields['tx_referencia'].required=True
        self.fields['fh_ticket'].required=True
        self.fields['imp_ticket'].required=True

        self.fields['img_ticket'].required=True


        self.fields['tx_referencia'].label = "Nombre/Titulo/Referencia"
        self.fields['fh_ticket'].label = "Fecha del ticket"
        self.fields['imp_ticket'].label = "Importe total"

        self.fields['img_ticket'].label = "Fotografia del ticket"

        self.fields['tx_referencia'].widget.attrs['autofocus'] = True

        # if kwargs['instance']:
        #
        #     ticket = kwargs['instance']
        #     self.test = ticket.fh_ticket.strftime("%d/%m/%Y")
        #     self.fields['fh_ticket'].initial = ticket.fh_ticket.strftime("%d/%m/%Y")
        #     self.fields['fh_ticket'].initial = ticket.fh_ticket.strftime("%d/%m/%Y")
        #     self.test = ticket.fh_ticket
        # else:
        #     self.test = 1

    class Meta:
        model = UnidadPeaje
        fields = ['id_unidad', 'tx_referencia', 'fh_ticket', 'imp_ticket', 'img_ticket', 'id_unidad_asigna']
        widgets = {
            'tx_referencia': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre o referencia',
                }
            ),
            # 'fh_ticket': forms.DateTimeInput(attrs={
            #             'class': 'form-control datetimepicker-input',
            #             'data-target': '#id_fh_ticket',
            #             'data-toggle' : "datetimepicker"
            #         }),
            'imp_ticket':    TextInput(
                attrs={
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'value': "0.00"
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data = {}
                data['error'] = form.errors
        except Exception as e:
            data = {}
            data['error'] = str(e)
        return data