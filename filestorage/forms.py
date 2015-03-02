from django import forms


class SearchForm(forms.Form):
    searchQuery = forms.CharField(
        label='Строка поиска',
        max_length=10,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Что ищем?'
            }
        )
    )