from django import forms
class gforms(forms.Form):
     title=forms.CharField()
     Des= forms.CharField(widget= forms.Textarea(attrs={"rows":10,"column":10


     })


     )
