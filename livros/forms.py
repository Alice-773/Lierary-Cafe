from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'
        
        
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full p-3 bg-[#FDFBF7] border border-[#E6DEC9] rounded-xl text-sm text-[#2C1810] focus:outline-none focus:border-[#A0785A] transition-all',
                'placeholder': 'Ex: O Hobbit'
            }),
            'autor': forms.TextInput(attrs={
                'class': 'w-full p-3 bg-[#FDFBF7] border border-[#E6DEC9] rounded-xl text-sm text-[#2C1810] focus:outline-none focus:border-[#A0785A] transition-all',
                'placeholder': 'Ex: J.R.R. Tolkien'
            }),
            'categoria': forms.Select(attrs={
                'class': 'w-full p-3 bg-[#FDFBF7] border border-[#E6DEC9] rounded-xl text-sm text-[#2C1810] focus:outline-none focus:border-[#A0785A] transition-all'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'w-full p-3 bg-[#FDFBF7] border border-[#E6DEC9] rounded-xl text-sm text-[#2C1810] focus:outline-none focus:border-[#A0785A] transition-all',
                'placeholder': 'Ex: 978-3-16-148410-0'
            }),
            'ano': forms.NumberInput(attrs={
                'class': 'w-full p-3 bg-[#FDFBF7] border border-[#E6DEC9] rounded-xl text-sm text-[#2C1810] focus:outline-none focus:border-[#A0785A] transition-all',
                'placeholder': 'Ex: 1937'
            }),
            'quantidade': forms.NumberInput(attrs={
                'class': 'w-full p-3 bg-[#FDFBF7] border border-[#E6DEC9] rounded-xl text-sm text-[#2C1810] focus:outline-none focus:border-[#A0785A] transition-all',
                'min': '1'
            }),
            'disponivel': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-[#6F4E37] border-[#E6DEC9] rounded focus:ring-[#A0785A] bg-[#FDFBF7]'
            }),
            
           
            'emprestado_para': forms.TextInput(attrs={
                'class': 'w-full p-3 bg-[#FDFBF7] border border-[#E6DEC9] rounded-xl text-sm text-[#2C1810] focus:outline-none focus:border-[#A0785A] transition-all',
                'placeholder': 'Nome da pessoa que pegou o livro'
            }),
            'data_emprestimo': forms.DateInput(attrs={
                'class': 'w-full p-3 bg-[#FDFBF7] border border-[#E6DEC9] rounded-xl text-sm text-[#2C1810] focus:outline-none focus:border-[#A0785A] transition-all',
                'type': 'date'
            }),
        }