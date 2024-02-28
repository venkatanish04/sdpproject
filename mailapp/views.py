import csv
from django.core.mail import send_mail
from django.shortcuts import render

def send_emails(request):
    csv_file_path = r'C:\Users\venka\OneDrive\Desktop\PSFD\pythonProject1\djangoproject\TTm\static\email.csv'
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['email']
            subject = 'Hello KLUian'  # Set your subject here
            message_body = 'Hey, Welcome to PFSD Class, Hope u have a great time with python'  # Set your email content here
            send_mail(
                subject,
                message_body,
                '2200032220cseh@gmail.com',# Change this to the sender's email address if required
                [recipient_email],
                fail_silently=False,
            )
            print(f'Sent email to {recipient_email}')
    return render(request, 'Emails_sent_successfully.html')
