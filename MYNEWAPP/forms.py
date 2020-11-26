from django import forms
class Student(forms.Form):
    name=forms.CharField(label="name")
    list1=[( 'Male','Male'),('Female','Female')]
    gender=forms.ChoiceField(choices=list1,widget=forms.RadioSelect)
    CHOICES=[
        ('rose','rose'),
        ('lilly','lilly')
    ]
    flowers=forms.CharField(widget=forms.Select(choices=CHOICES))
class StudentDetails(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    age=forms.CharField(widget=forms.NumberInput)
    address=forms.CharField(widget=forms.Textarea)
    list1=[('Male','Male'),('Female','Female')]
    FRUIT_CHOICES = [
        ('orange', 'Oranges'),
        ('banana', 'bananas'),
        ('mango', 'Mangoes'),
        ('grape', 'grapes'),
    ]
    favorite_fruit = forms.CharField(widget=forms.Select(choices=FRUIT_CHOICES))
class Cricketplayers(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    age=forms.CharField(widget=forms.NumberInput)
    address=forms.CharField(widget=forms.TextInput)
    list1=[('Batsman','Batsman'),('Bowler','Bowler'),('Allrounder','Allrounder')]
    role=forms.ChoiceField(choices=list1,widget=forms.RadioSelect)
    COUNTRY_CHOICES=[('india','india'),('australia','australia'),('england','england')]
    COUNTRY=forms.CharField(widget=forms.Select(choices=COUNTRY_CHOICES))
    password=forms.CharField(widget=forms.PasswordInput)
    confirmpassword=forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField(widget=forms.TextInput)
    fileupload=forms.FileField()
    def clean_name(self):
        value=self.cleaned_data['name']
        if value.isupper():
            raise forms.ValidationError("please don't use uppercase")
        return value
    def clean_address(self):
        value=self.cleaned_data['address']
        if value.islower():
            raise forms.ValidationError("dont uselower case")
        return value

    def clean_email(self):
        value = self.cleaned_data['email']
        if value.endswith('@hotmail.com'):
            raise forms.ValidationError("please dont use email")
        return value

    def clean_confirmpassword(self):

        password = self.cleaned_data["password"]
        confirmpassword = self.cleaned_data["confirmpassword"]

        if password != confirmpassword:
            raise forms.ValidationError("password and confirmpassword does not match")
        return password










