from django import forms
from django.core.validators import RegexValidator

class SurveyForm(forms.Form):
    GENDER_CHOICES = [
        ('남성', '남성'),
        ('여성', '여성'),
    ]

    gender = forms.ChoiceField(
        label="본인의 성별을 선택해주세요",
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )
    age = forms.IntegerField(
        label="본인의 만나이를 알려주세요",
        min_value=25, max_value=32,
        widget=forms.NumberInput(attrs={'placeholder': '25 ~ 32'}),
        required=True
    )
    job_field = forms.CharField(
        label="현재 종사하시는 분야에 대해 간단히 적어주세요",
        widget=forms.TextInput()
    )
    """
    photos = forms.FileField(
        label="본인의 6개월 이내 사진을 2~3장 첨부해주세요",
        widget=forms.ClearableFileInput(),
        required=True
    )
    """
    name = forms.CharField(
        label="성함을 적어주세요",
        widget=forms.TextInput(),
        required=True
    )

    phone = forms.CharField(
        label="모임 이용을 위한 연락처를 입력해주세요. 참가자 선정이 되면 개별 연락으로 참가안내를 드립니다.",
        max_length=11,
        min_length=11,
        validators=[
            RegexValidator(r'^\d{11}$', message='숫자 11자리를 입력해주세요 (예: 01012345678)')
        ],
        widget=forms.TextInput(attrs={
            'inputmode': 'numeric'
        }),
        required=True
    )
    agree = forms.BooleanField(
        label="위 약관 내용을 모두 확인하였으며 동의합니다.",
        required=True
    )
