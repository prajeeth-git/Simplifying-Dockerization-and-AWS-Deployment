from django import forms

from .validators import validate_dot_com,validate_url


class submiturlform(forms.Form):
    url=forms.CharField(label='',
    validators=[validate_url],
    widget=forms.TextInput(
        attrs={
            "placeholder":"Enter your long URL here",
            "class":"form-control"}
    )
 
    )

    # def clean(self):
    #     cleaned_data=super(submiturlform, self).clean()
    #     print(cleaned_data,'jjj')
    #     url = cleaned_data.get('url')
    #     url_validator=URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL")
    #     return url
    

    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     if "http" in url:
    #         return url
    #     return "http://"