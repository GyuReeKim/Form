from django import forms
from .models import Movie, Comment

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

# Model과 관련있는 form 생성
class MovieModelForm(forms.ModelForm):
    # 원래의 정보를 수정하거나 확장할 수 있다.
    open_date = forms.DateField(
                    widget=forms.DateInput(
                        attrs={
                            'type': 'date'
                        }
                    )
                )
    # 추가적인 데이터는 Meta에 저장된다.
    class Meta:
        model = Movie
        fields = '__all__'

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)