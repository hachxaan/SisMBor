# from msilib.schema import CheckBox

from django import forms
from django.forms import Select, ModelForm, TextInput, Textarea

from appMainSite.const import *
from .models import Unidad, Cliente, Concepto, ConceptoCategoria, Personal, ConceptoTipoMarca, UnidadMedida


class ClienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():

        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['cve_usu_alta'].widget = forms.HiddenInput()
        self.fields['fh_registro'].widget = forms.HiddenInput()
        self.fields['rup'].widget.attrs['autofocus'] = True
        self.fields['telefono_contacto'].required = True
        self.fields['nombre_empresa'].required = True
        self.fields['celular_contacto'].required = True
        self.fields['direccion'].required = True
        self.fields['nombre'].required = True
        self.fields['apellido'].required = True
        self.fields['correo_electronico'].required = True

    class Meta:
        model = Cliente
        fields = ['cve_usu_alta', 'fh_registro', 'id_cliente', 'rup', 'nombre_empresa', 'telefono_contacto',
                  'celular_contacto', 'correo_electronico', 'direccion', 'nombre', 'apellido']
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
        self.fields['id_cliente'].label = "Cliente"
        self.fields['marca'].required = True
        self.fields['modelo'].required = True
        self.fields['motor'].required = True
        self.fields['chasis'].required = True

    class Meta:
        model = Unidad
        fields = '__all__'
        widgets = {
            'id_cliente': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
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
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ManobraForm(forms.ModelForm):
    id_categoria = forms.ModelChoiceField(queryset=ConceptoCategoria.objects.filter(id_tipo_concepto=TCONCEPTO_MANOBRA))

    def clean_name(self):
        if not self['id_tipo_concepto'].html_name in self.data:
            return self.fields['id_tipo_concepto'].initial
        return self.cleaned_data['id_tipo_concepto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cve_concepto'].widget.attrs['autofocus'] = True
        self.fields['id_tipo_concepto'].widget.attrs['value'] = TCONCEPTO_MANOBRA
        self.fields['id_tipo_concepto'].widget = forms.HiddenInput()
        self.fields['b_numero_serie'].widget = forms.HiddenInput()
        self.fields['precio_compra'].widget = forms.HiddenInput()
        self.fields['stock'].widget = forms.HiddenInput()
        self.fields['stock'].widget.attrs['value'] = 0
        self.fields['b_nserie_obligatorio'].widget = forms.HiddenInput()
        self.fields['b_nserie_obligatorio'].widget.attrs['value'] = 0
        self.fields['desc_concepto'].label = "Descripción de la Mano de Obra"
        self.fields['cve_concepto'].label = "Clave la Mano de Obra"
        self.fields['id_categoria'].label = "Categoría"
        self.fields['id_tipo_servicio'].label = "Tipo de servicio"
        self.fields['id_periodo_km'].label = "Kilometraje sugerido"
        self.fields['hora_hombre'].required = True
        self.fields['precio_venta'].required = True
        self.fields['id_tipo_servicio'].required = True
        self.fields['id_periodo_km'].required = True

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
                  'b_nserie_obligatorio',
                  'precio_compra',
                  'stock',
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
            ),

            'precio_venta': TextInput(
                attrs={
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'value': "0"
                }
            ),

            'hora_hombre': TextInput(
                attrs={
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'value': "0"
                }
            )

            # 'id_categoria': floppyforms.widgets.Input( datalist=ConceptoCategoria.objects.filter(id_tipo_concepto = 2) )

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


class MantenimientoForm(forms.ModelForm):
    # id_categoria = forms.ModelChoiceField(
    #     queryset=ConceptoCategoria.objects.filter(id_tipo_concepto=TCONCEPTO_MANTENIMIENTO))
    b_agrega_conceptos = forms.BooleanField()
    def clean_name(self):
        if not self['id_tipo_concepto'].html_name in self.data:
            return self.fields['id_tipo_concepto'].initial
        return self.cleaned_data['id_tipo_concepto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cve_concepto'].widget.attrs['autofocus'] = True
        self.fields['id_tipo_concepto'].widget.attrs['value'] = TCONCEPTO_MANOBRA
        self.fields['b_numero_serie'].widget.attrs['value'] = 0
        self.fields['b_nserie_obligatorio'].widget.attrs['value'] = 0
        self.fields['precio_compra'].widget.attrs['value'] = 0
        self.fields['id_periodo_km'].widget.attrs['value'] = 0
        self.fields['stock'].widget.attrs['value'] = 0
        self.fields['id_tipo_servicio'].widget.attrs['value'] = 2
        self.fields['id_tipo_concepto'].widget = forms.HiddenInput()
        self.fields['b_numero_serie'].widget = forms.HiddenInput()
        self.fields['id_periodo_km'].widget = forms.HiddenInput()
        self.fields['precio_compra'].widget = forms.HiddenInput()
        self.fields['id_tipo_servicio'].widget = forms.HiddenInput()
        self.fields['b_nserie_obligatorio'].widget = forms.HiddenInput()
        self.fields['id_categoria'].widget = forms.HiddenInput()
        self.fields['id_periodo_km'].widget = forms.HiddenInput()
        self.fields['stock'].widget = forms.HiddenInput()
        self.fields['precio_venta'].required = True
        self.fields['hora_hombre'].required = True
        self.fields['b_agrega_conceptos'].required = False
        self.fields['id_categoria'].required = False
        self.fields['desc_concepto'].label = "Descripción del Mantenimiento"
        self.fields['cve_concepto'].label = "Clave del Mantenimiento"

        # self.fields['id_tipo_servicio'].label="Tipo de servicio"
        # self.fields['id_periodo_km'].label="Kilometraje sugerido"

    class Meta:
        model = Concepto
        fields = ['cve_concepto',
                  'desc_concepto',
                  'id_categoria',
                  'precio_venta',
                  'hora_hombre',
                  'stock',
                  'id_tipo_servicio',
                  'id_periodo_km',
                  'id_tipo_concepto',
                  'b_numero_serie',
                  'precio_compra',
                  'b_nserie_obligatorio',
                  'b_agrega_conceptos'
                  ]
        widgets = {

            'b_agrega_conceptos': TextInput(
                attrs={
                    'class': 'd-inline-flex p-2',
                    'type': "checkbox",
                    'min': "0",
                    'step': "any"

                }
            ),
            'precio_venta': TextInput(
                attrs={
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'value': "0.00"

                }
            ),
            'hora_hombre': TextInput(
                attrs={
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'value': "0"

                }
            ),

            # 'id_categoria': floppyforms.widgets.Input( datalist=ConceptoCategoria.objects.filter(id_tipo_concepto = 2) )

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


class InventarioForm(forms.ModelForm):
    id_categoria = forms.ModelChoiceField(
        queryset=ConceptoCategoria.objects.filter(id_tipo_concepto=TCONCEPTO_REPUESTOS))
    id_unidad_medida = forms.ModelChoiceField(queryset=UnidadMedida.objects.all())
    id_marca = forms.ModelChoiceField(
        queryset=ConceptoTipoMarca.objects.filter(id_tipo_concepto=TCONCEPTO_REPUESTOS))

    b_numero_serie = forms.BooleanField()
    b_nserie_obligatorio = forms.BooleanField()

    def clean_name(self):
        if not self['id_tipo_concepto'].html_name in self.data:
            return self.fields['id_tipo_concepto'].initial
        return self.cleaned_data['id_tipo_concepto']

    def __init__(self, *args, **kwargs):

        initial = kwargs.get('initial', {})
        initial['stock'] = '0'
        initial['id_tipo_servicio'] = '1'
        initial['b_numero_serie'] = False
        initial['b_nserie_obligatorio'] = False
        initial['vida_util_km'] = '0'
        initial['vida_util_hr'] = '0'
        initial['precio_venta'] = '0.00'
        initial['precio_compra'] = '0.00'
        # initial['id_tipo_concepto']=TCONCEPTO_REPUESTOS
        kwargs['initial'] = initial
        super(InventarioForm, self).__init__(*args, **kwargs)

        # super().__init__(*args, **kwargs)
        self.fields['cve_concepto'].widget.attrs['autofocus'] = True
        self.fields['id_tipo_concepto'].widget.attrs['value'] = TCONCEPTO_REPUESTOS
        self.fields['id_tipo_servicio'].widget.attrs['value'] = 0

        self.fields['id_tipo_concepto'].widget = forms.HiddenInput()
        self.fields['id_tipo_servicio'].widget = forms.HiddenInput()

        self.fields['id_categoria'].label = "Categoría"
        self.fields['id_marca'].label = "Marca"
        self.fields['id_unidad_medida'].label = "Unidad de Medida"
        self.fields['id_periodo_km'].label = "Kilometraje sugerido"
        self.fields['b_numero_serie'].label = "Registra número de serie"
        self.fields['b_nserie_obligatorio'].label = "Obligartorio agregar número de serie"
        self.fields['stock'].label = "Stock Inicial"
        self.fields['cve_concepto'].label = "Clave del Repuesto"
        self.fields['desc_concepto'].label = "Descripción del Repuesto"
        self.fields['stock'].required = True
        self.fields['precio_venta'].required = True
        self.fields['precio_compra'].required = True
        self.fields['vida_util_km'].required = True
        self.fields['vida_util_hr'].required = True
        self.fields['b_numero_serie'].required = False
        self.fields['b_nserie_obligatorio'].required = False


    class Meta:
        model = Concepto
        fields = ['cve_concepto',
                  'desc_concepto',
                  'stock',
                  'precio_compra',
                  'precio_venta',
                  'id_categoria',
                  'id_marca',
                  'id_unidad_medida',
                  'vida_util_km',
                  'vida_util_hr',
                  'id_periodo_km',
                  'id_tipo_concepto',
                  'b_numero_serie',
                  'b_nserie_obligatorio',
                  'id_tipo_servicio'
                  ]
        widgets = {

            'id_periodo_km': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'id_unidad_medida': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),

            'stock': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "1",
                }
            ),
            'precio_compra': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'data-class_custom': 'col col-md-4 col-sm-12'
                }
            ),
            'precio_venta': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'data-class_custom': 'col col-md-4 col-sm-12'
                }
            ),
            'vida_util_km': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'data-class_custom': 'col col-md-4 col-sm-12'
                }
            ),
            'vida_util_hr': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'data-class_custom': 'col col-md-4 col-sm-12'
                }
            ),
            'b_numero_serie': TextInput(
                attrs={
                    'class': 'd-inline-flex p-2',
                    'type': "checkbox",
                    'min': "0",
                    'step': "any"

                }
            ),
            'b_nserie_obligatorio': TextInput(
                attrs={
                    'class': 'd-inline-flex p-2',
                    'type': "checkbox",
                    'min': "0",
                    'step': "any"

                }
            ),
            # 'id_categoria': floppyforms.widgets.Input( datalist=ConceptoCategoria.objects.filter(id_tipo_concepto = 2) )

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


class InventarioFormEdit(forms.ModelForm):
    id_categoria = forms.ModelChoiceField(
        queryset=ConceptoCategoria.objects.filter(id_tipo_concepto=TCONCEPTO_REPUESTOS))
    id_unidad_medida = forms.ModelChoiceField(queryset=UnidadMedida.objects.all())
    id_marca = forms.ModelChoiceField(
        queryset=ConceptoTipoMarca.objects.filter(id_tipo_concepto=TCONCEPTO_REPUESTOS))

    b_numero_serie = forms.BooleanField()
    b_nserie_obligatorio = forms.BooleanField()

    def clean_name(self):
        if not self['id_tipo_concepto'].html_name in self.data:
            return self.fields['id_tipo_concepto'].initial
        return self.cleaned_data['id_tipo_concepto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # super().__init__(*args, **kwargs)
        self.fields['cve_concepto'].widget.attrs['autofocus'] = True
        self.fields['id_tipo_concepto'].widget.attrs['value'] = TCONCEPTO_REPUESTOS
        self.fields['id_tipo_servicio'].widget.attrs['value'] = 0

        self.fields['id_tipo_concepto'].widget = forms.HiddenInput()
        self.fields['id_tipo_servicio'].widget = forms.HiddenInput()

        self.fields['id_categoria'].label = "Categoría"
        self.fields['id_marca'].label = "Marca"
        self.fields['id_unidad_medida'].label = "Unidad de Medida"
        self.fields['id_periodo_km'].label = "Kilometraje sugerido"
        self.fields['b_numero_serie'].label = "Registra número de serie"
        self.fields['b_nserie_obligatorio'].label = "Obligartorio agregar número de serie"
        self.fields['stock'].label = "Stock"
        self.fields['cve_concepto'].label = "Clave del Repuesto"
        self.fields['desc_concepto'].label = "Descripción del Repuesto"
        self.fields['stock'].required = True
        self.fields['precio_venta'].required = True
        self.fields['precio_compra'].required = True
        self.fields['vida_util_km'].required = True
        self.fields['vida_util_hr'].required = True
        self.fields['b_numero_serie'].required = False
        self.fields['b_nserie_obligatorio'].required = False

    class Meta:
        model = Concepto
        fields = ['cve_concepto',
                  'desc_concepto',
                  'stock',
                  'precio_compra',
                  'precio_venta',
                  'id_categoria',
                  'id_marca',
                  'id_unidad_medida',
                  'vida_util_km',
                  'vida_util_hr',
                  'id_periodo_km',
                  'id_tipo_concepto',
                  'b_numero_serie',
                  'b_nserie_obligatorio',
                  'id_tipo_servicio'
                  ]
        widgets = {

            'id_periodo_km': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'id_unidad_medida': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),

            'stock': TextInput(
                attrs={
                    'readonly': 'readonly',
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "1",
                }
            ),
            'precio_compra': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'data-class_custom': 'col col-md-4 col-sm-12'
                }
            ),
            'precio_venta': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'data-class_custom': 'col col-md-4 col-sm-12'
                }
            ),
            'vida_util_km': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'data-class_custom': 'col col-md-4 col-sm-12'
                }
            ),
            'vida_util_hr': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'data-class_custom': 'col col-md-4 col-sm-12'
                }
            ),
            'b_numero_serie': TextInput(
                attrs={
                    'class': 'd-inline-flex p-2',
                    'type': "checkbox"
                }
            ),
            'b_nserie_obligatorio': TextInput(
                attrs={
                    'class': 'd-inline-flex p-2',
                    'type': "checkbox"
                }
            ),
            # 'id_categoria': floppyforms.widgets.Input( datalist=ConceptoCategoria.objects.filter(id_tipo_concepto = 2) )

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




class InventarioNeumaticosForm(forms.ModelForm):
    id_categoria = forms.ModelChoiceField(
        queryset=ConceptoCategoria.objects.filter(id_tipo_concepto=TCONCEPTO_NEUMATICOS))
    # id_unidad_medida = forms.ModelChoiceField(queryset=UnidadMedida.objects.all())
    id_marca = forms.ModelChoiceField(
        queryset=ConceptoTipoMarca.objects.filter(id_tipo_concepto=TCONCEPTO_NEUMATICOS))

    b_numero_serie = forms.BooleanField()
    b_nserie_obligatorio = forms.BooleanField()

    def clean_name(self):
        if not self['id_tipo_concepto'].html_name in self.data:
            return self.fields['id_tipo_concepto'].initial
        return self.cleaned_data['id_tipo_concepto']

    def __init__(self, *args, **kwargs):

        initial = kwargs.get('initial', {})
        initial['stock'] = '0'
        initial['id_tipo_servicio'] = '1'
        initial['b_numero_serie'] = False
        initial['b_nserie_obligatorio'] = False
        initial['vida_util_km'] = '0'
        initial['vida_util_hr'] = '0'
        initial['precio_venta'] = '0.00'
        initial['precio_compra'] = '0.00'
        # initial['id_tipo_concepto']=TCONCEPTO_REPUESTOS
        kwargs['initial'] = initial
        super(InventarioNeumaticosForm, self).__init__(*args, **kwargs)

        # super().__init__(*args, **kwargs)
        self.fields['cve_concepto'].widget.attrs['autofocus'] = True
        self.fields['id_tipo_concepto'].widget.attrs['value'] = TCONCEPTO_NEUMATICOS
        self.fields['id_tipo_servicio'].widget.attrs['value'] = 0

        self.fields['id_tipo_concepto'].widget = forms.HiddenInput()
        self.fields['id_tipo_servicio'].widget = forms.HiddenInput()

        self.fields['id_categoria'].label = "Categoría"
        self.fields['id_marca'].label = "Marca"
        # self.fields['id_unidad_medida'].label = "Unidad de Medida"
        # self.fields['id_unidad_medida'].widget = forms.HiddenInput()
        # self.fields['id_periodo_km'].label = "Kilometraje sugerido"
        self.fields['b_numero_serie'].label = "Registra número de serie"
        self.fields['b_nserie_obligatorio'].label = "Obligartorio agregar número de serie"
        self.fields['stock'].label = "Stock Inicial"
        self.fields['cve_concepto'].label = "Clave de Neumático"
        self.fields['desc_concepto'].label = "Descripción del Neumático"
        self.fields['stock'].required = True
        self.fields['precio_venta'].required = True
        self.fields['precio_compra'].required = True
        self.fields['vida_util_km'].required = True
        # self.fields['vida_util_hr'].required = False
        self.fields['b_numero_serie'].required = False
        self.fields['b_nserie_obligatorio'].required = False

    class Meta:
        model = Concepto
        fields = ['cve_concepto',
                  'desc_concepto',
                  'stock',
                  'precio_compra',
                  'precio_venta',
                  'id_categoria',
                  'id_marca',
                  # 'id_unidad_medida',
                  'vida_util_km',
                  # 'vida_util_hr',
                  # 'id_periodo_km',
                  'id_tipo_concepto',
                  'b_numero_serie',
                  'b_nserie_obligatorio',
                  'id_tipo_servicio'
                  ]
        widgets = {

            'id_periodo_km': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),


            'stock': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "1",
                }
            ),
            'precio_compra': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'data-class_custom': 'col col-md-4 col-sm-12'
                }
            ),
            'precio_venta': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'data-class_custom': 'col col-md-4 col-sm-12'
                }
            ),
            'vida_util_km': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'data-class_custom': 'col col-md-4 col-sm-12'
                }
            ),
            'b_numero_serie': TextInput(
                attrs={
                    'class': 'd-inline-flex p-2',
                    'type': "checkbox",
                    'min': "0",
                    'step': "any"

                }
            ),
            'b_nserie_obligatorio': TextInput(
                attrs={
                    'class': 'd-inline-flex p-2',
                    'type': "checkbox",
                    'min': "0",
                    'step': "any"

                }
            ),
            # 'id_categoria': floppyforms.widgets.Input( datalist=ConceptoCategoria.objects.filter(id_tipo_concepto = 2) )

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


class InventarioNeumaticosFormEdit(forms.ModelForm):
    id_categoria = forms.ModelChoiceField(
        queryset=ConceptoCategoria.objects.filter(id_tipo_concepto=TCONCEPTO_NEUMATICOS))
    id_unidad_medida = forms.ModelChoiceField(queryset=UnidadMedida.objects.all())
    id_marca = forms.ModelChoiceField(
        queryset=ConceptoTipoMarca.objects.filter(id_tipo_concepto=TCONCEPTO_NEUMATICOS))

    b_numero_serie = forms.BooleanField()
    b_nserie_obligatorio = forms.BooleanField()

    def clean_name(self):
        if not self['id_tipo_concepto'].html_name in self.data:
            return self.fields['id_tipo_concepto'].initial
        return self.cleaned_data['id_tipo_concepto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # super().__init__(*args, **kwargs)
        self.fields['cve_concepto'].widget.attrs['autofocus'] = True
        self.fields['id_tipo_concepto'].widget.attrs['value'] = TCONCEPTO_NEUMATICOS
        self.fields['id_tipo_servicio'].widget.attrs['value'] = 0

        self.fields['id_tipo_concepto'].widget = forms.HiddenInput()
        self.fields['id_tipo_servicio'].widget = forms.HiddenInput()

        self.fields['id_categoria'].label = "Categoría"
        self.fields['id_marca'].label = "Marca"
        self.fields['id_unidad_medida'].label = "Unidad de Medidas"
        self.fields['id_periodo_km'].label = "Kilometraje sugerido"
        self.fields['b_numero_serie'].label = "Registra número de serie"
        self.fields['b_nserie_obligatorio'].label = "Obligartorio agregar número de serie"
        self.fields['stock'].label = "Stock"
        self.fields['cve_concepto'].label = "Clave de Neumático"
        self.fields['desc_concepto'].label = "Descripción del Neumático"
        self.fields['stock'].required = True
        self.fields['precio_venta'].required = True
        self.fields['precio_compra'].required = True
        self.fields['vida_util_km'].required = True
        self.fields['vida_util_hr'].required = True
        self.fields['b_numero_serie'].required = False
        self.fields['b_nserie_obligatorio'].required = False

    class Meta:
        model = Concepto
        fields = ['cve_concepto',
                  'desc_concepto',
                  'stock',
                  'precio_compra',
                  'precio_venta',
                  'id_categoria',
                  'id_marca',
                  'id_unidad_medida',
                  'vida_util_km',
                  'vida_util_hr',
                  'id_periodo_km',
                  'id_tipo_concepto',
                  'b_numero_serie',
                  'b_nserie_obligatorio',
                  'id_tipo_servicio'
                  ]
        widgets = {

            'id_periodo_km': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'id_unidad_medida': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),

            'stock': TextInput(
                attrs={
                    'readonly': 'readonly',
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "1",
                }
            ),
            'precio_compra': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'data-class_custom': 'col col-md-4 col-sm-12'
                }
            ),
            'precio_venta': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'data-class_custom': 'col col-md-4 col-sm-12'
                }
            ),
            'vida_util_km': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'data-class_custom': 'col col-md-4 col-sm-12'
                }
            ),
            'vida_util_hr': TextInput(
                attrs={
                    'class': 'col col-md-4 col-sm-12',
                    'type': "number",
                    'min': "0",
                    'step': "any",
                    'data-class_custom': 'col col-md-4 col-sm-12'
                }
            ),
            'b_numero_serie': TextInput(
                attrs={
                    'class': 'd-inline-flex p-2',
                    'type': "checkbox"
                }
            ),
            'b_nserie_obligatorio': TextInput(
                attrs={
                    'class': 'd-inline-flex p-2',
                    'type': "checkbox"
                }
            ),
            # 'id_categoria': floppyforms.widgets.Input( datalist=ConceptoCategoria.objects.filter(id_tipo_concepto = 2) )

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