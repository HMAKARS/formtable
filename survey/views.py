from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import SurveyForm
from django.conf import settings

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST, request.FILES)

        if form.is_valid():
                data = form.cleaned_data
                subject = f"[소개팅 신청서] {data['name']}님의 신청"
                message = f"""
📥 소개팅 신청서

성별: {data['gender']}
나이: {data['age']}
직업/분야: {data['job_field']}
이름: {data['name']}
연락처: {data['phone']}
"""

                email = EmailMessage(
                    subject, message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=['tableparty58@gamil.com']  # 수신자 주소 수정
                )


                email.send()
                return redirect('thanks')
    else:
        form = SurveyForm()

    return render(request, 'survey/survey.html', {'form': form})

def thanks_view(request):
    return render(request, 'survey/thanks.html')
