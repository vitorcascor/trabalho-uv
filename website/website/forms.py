from django import forms

from skins.models import Produto

class SkinForm(forms.ModelForm):

  class Meta:
    model = Produto
    fields = ('nome','imagem','preco')
