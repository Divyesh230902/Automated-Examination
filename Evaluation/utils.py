from collections import defaultdict
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER

def send_results(results,exam,year):
    for student in results:
        subject = f"Result For Your {exam} Exam {year}"
        msg = f"Name: {student.fullname}\n\n"
        for sub in results[student]:
            msg += f"{sub}: {results[student][sub]}\n"
        send_mail(subject,msg,EMAIL_HOST_USER,[student.email])

def sort_answersheets(answersheets,exam,year):
    results = defaultdict(dict)
    for ans_sheet in answersheets:
        try:
            student = ans_sheet.student
            subject = ans_sheet.exam.subject.name
            marks = ans_sheet.evaluation.get().marks
            results[student][subject] = marks
        except:
            pass
    print(results)
    send_results(results,exam,year)
    