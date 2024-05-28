from django import forms
from inicio.models import Equipo, OrdenServicio
from django.contrib.auth.models import User


class FormEquipo(forms.ModelForm):
    
    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'serial_number': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Numero de serie', 'required': False}
            ),
            'cliente_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Nombre del cliente', 'required': True}
            ),
            'telefono_cliente': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Telefono del cliente', 'required': True}
            ),'tipo_equipo': forms.Select(
                attrs={'class':'form-control','placeholder':'Tipo de equipo', 'required': False}
            ),
            'marca_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Marca', 'required': True}
            ),
            'modelo_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Modelo', 'required': True}
            ),
            'accesorios_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Accesorios', 'required': False}
            ),
            'contraseña_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Contraseña del equipo', 'required': False}
            ),
            'sistema_operativo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Sistema Operativo', 'required': True}
            ),
        }
        
class FormServicio(forms.ModelForm):
    
    class Meta:
        model = OrdenServicio
        fields = '__all__'
        exclude = ['servicio_realizado','notas_finales','partes','fecha_entrega','costo_final','observaciones_notas','encargado']
        widgets = {
            'id_orden': forms.NumberInput(
                attrs={'class':'form-control','placeholder':'Numero de orden', 'required': True}
            ),
            'fecha_orden': forms.DateInput(
                attrs={'class':'form-control','placeholder':'dd/mm/aaaa',"required": True}
            ),    
            'cotizacion': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Cotizacion', 'required': False}
            ),
            'tipo_servicio': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Tipo de servicio', 'required': True}
            ),'equipo': forms.Select(
                attrs={'class':'form-control','placeholder':'equipo', 'required': False}
            ),
            'indicaciones_adicionales': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Incicaciones', 'required': True}
            ),
            'falla_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Falla', 'required': True}
            ),
            
        }
      
class UserForm(forms.ModelForm):
    re_pass = forms.CharField(
        label='Confirma contraseña',
        widget=forms.PasswordInput(),
        required=True
    )
    
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(),
        required=True
    )
    class Meta:
        model = User
        fields = ['username','email','password','re_pass']
        # fields = '__all__'

    def clean_password(self, *args, **kwargs):
        if self.data['password'] != self.data['re_pass']:
            raise forms.ValidationError('Las contraseñas no son iguales', code='passwords_not_equals')
        return self.data['password']
    
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class FormEditarOrden(forms.ModelForm):
    class Meta:
        model = OrdenServicio
        exclude = ['id_orden','fecha_orden','equipo']
        widgets = {
            'fecha_entrega':forms.DateInput(
                attrs={'class':'form-control','placeholder':'dd/mm/aaaa',"required": False}
            ),  
            'cotizacion': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Cotizacion', 'required': False}
            ),
            'costo_final': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Costo final', 'required': False}
            ),
            'tipo_servicio': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Tipo de servicio', 'required': True}
            ),
            'indicaciones_adicionales': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Incicaciones', 'required': True}
            ),
            'servicio_realizado': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Servicio realizado', 'required': False}
            ),
            'notas_finales': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Notas Finales', 'required': False}
            ),
            'encargado': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Encargado', 'required': False}
            ),
            'observaciones_notas': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Observaciones', 'required': False}
            ),
            'falla_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Falla', 'required': True}
            ),
            'partes': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Partes', 'required': False}
            ),

        }


class FormEditarEquipo(forms.ModelForm):
    class Meta:
        model = Equipo
        exclude = ['serial_number']
        widgets = {
            
            'cliente_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Nombre del cliente', 'required': True}
            ),
            'telefono_cliente': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Telefono del cliente', 'required': True}
            ),'tipo_equipo': forms.Select(
                attrs={'class':'form-control','placeholder':'Tipo de equipo', 'required': False}
            ),
            'marca_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Marca', 'required': True}
            ),
            'modelo_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Modelo', 'required': True}
            ),
            'accesorios_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Accesorios', 'required': False}
            ),
            'contraseña_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Contraseña del equipo', 'required': False}
            ),
            'sistema_operativo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Sistema Operativo', 'required': True}
            ),

        }

