from django import forms
from django.forms import Select, ModelForm, TextInput, Textarea
from floppyforms.templatetags import floppyforms

from .models import Unidad, Cliente, Concepto, ConceptoCategoria, Personal


class ClienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['rup'].widget.attrs['autofocus'] = True

    class Meta:
        model = Cliente
        fields = ['id_cliente','rup','nombre_empresa','telefono_contacto','celular_contacto','correo_electronico','direccion','nombre','apellido']
        widgets = {
            'rup': TextInput(
                attrs={
                    'placeholder': 'Ingrese el Registro Unico de Proponentes',
                }
            ),
            'nombre_empresa': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de la empresa'
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
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data



class UnidadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['placa'].widget.attrs['autofocus'] = True
        self.fields['id_cliente'].label="Cliente"

    class Meta:
        model = Unidad
        fields = '__all__'
        widgets={
            'id_cliente': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            )
        }

    def save(self, commit=True):
        data={}
        form=super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error']=form.errors
        except Exception as e:
            data['error']=str( e )
        return data


class ManobraForm(forms.ModelForm):
    # id_tipo_concepto=forms.IntegerField( required=False)
    id_categoria=forms.ModelChoiceField( queryset=ConceptoCategoria.objects.filter(id_tipo_concepto = 2))
    # cat = ConceptoCategoria.objects.filter(id_tipo_concepto = 2)
    #-> id_categoria=forms.ChoiceField( choices=[[1000, 'Nueva categoría']] + [[0, 'Selecciona una categoría']] + [[r.id_categoria, r.desc_categoria] for r in ConceptoCategoria.objects.filter(id_tipo_concepto = 2)] )
    def clean_name(self):
        if not self['id_tipo_concepto'].html_name in self.data:
            return self.fields['id_tipo_concepto'].initial
        return self.cleaned_data['id_tipo_concepto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cve_concepto'].widget.attrs['autofocus'] = True
        self.fields['id_tipo_concepto'].widget.attrs['value']=2
        self.fields['id_tipo_concepto'].widget=forms.HiddenInput()
        self.fields['b_numero_serie'].widget=forms.HiddenInput()
        self.fields['precio_compra'].widget=forms.HiddenInput()
        self.fields['id_categoria'].label = "Categoría"
        self.fields['id_tipo_servicio'].label="Tipo de servicio"
        self.fields['id_periodo_km'].label="Kilometraje sugerido"


    class Meta:
        model = Concepto
        fields = ['cve_concepto',
                  'desc_concepto',
                  'id_categoria',
                  'precio_venta',
                  'hora_hombre',
                  'id_tipo_servicio',
                  'id_periodo_km',
                  'id_tipo_concepto',
                  'b_numero_serie',
                  'precio_compra'
                  ]
        widgets = {
            # 'id_categoria': TextInput( attrs={'style': 'width:20px'} ),
            'id_tipo_servicio': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'id_periodo_km': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'desc_concepto': TextInput(
                attrs={
                    'style': 'width: 50%'
                }
            )

            # 'id_categoria': floppyforms.widgets.Input( datalist=ConceptoCategoria.objects.filter(id_tipo_concepto = 2) )


        }
    def save(self, commit=True):
        data={}
        form=super()

        try:
            # _mutable=self.data._mutable
            #
            # # set to mutable
            # self.data._mutable=True
            #
            # # сhange the values you want
            # self.data['id_tipo_concepto'] = 2
            # self.data['b_numero_serie']=0
            # self.data['precio_compra']=0
            # # set mutable flag back
            # self.data._mutable=_mutable


            if form.is_valid():
                form.save()
            else:
                data['error']=form.errors
        except Exception as e:
            data['error']=str( e )
        return data



class PersonalForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['cve_usu_alta'].widget=forms.HiddenInput()
        # self.fields['fh_registro'].widget=forms.HiddenInput()
        # self.fields['fh_registro'].required=False
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Personal
        fields = ['nombre', 'apellido']
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de la persona',
                }
            ),
            'apellido': TextInput(
                attrs={
                    'placeholder': 'Ingrese el apellido de la persona'
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
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data