from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, required=False, label='name',
                           widget=forms.TextInput(attrs={'placeholder': 'name'}))
    email = forms.CharField(required=False, label='email',
                             widget=forms.TextInput(attrs={'placeholder': 'email'}))
    comment = forms.CharField(required=True,
                              widget=forms.Textarea(
                                  attrs={'placeholder': 'please share your comment in any language you prefer ...'}),
                              label='please comment me in any language you prefer ...',
                              )
