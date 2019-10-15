from django import forms

class MovieForm(forms.Form):
    title = forms.CharField(max_length=100)
    title_en = forms.CharField(
                    max_length=100,
                    label="영문제목",
                    widget=forms.TextInput(
                        attrs={
                            'placeholder': '영문제목을 입력해주세요'
                        }
                    )
                )
    audience = forms.IntegerField()
    open_date = forms.DateField(
                    widget=forms.DateInput(
                        attrs={
                            'type': 'date'
                        }
                    )
                )
    genre = forms.CharField(max_length=100)
    watch_grade = forms.CharField(max_length=100)
    score = forms.FloatField()
    poster_url = forms.CharField(widget=forms.Textarea) # 다른 형태로 바꾸려면 widget으로 수정해야한다.
    description = forms.CharField(widget=forms.Textarea)