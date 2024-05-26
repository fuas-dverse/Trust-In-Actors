import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Mapping of Docker container namespaces to owner emails
owner_emails = {
    "Bob/Booking-Searcher": "bob@test.com",
    # Add more mappings here
}

def send_email(receiver_email, subject, container_namespace):
    sender_email = "info@test.com"    

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Specify the email body
    body = f"""
Dear User,

I hope this message finds you well. 
We are writing to inform you about an important issue regarding your Docker container, `{container_namespace}`.

Our monitoring systems have detected that your Docker container has exceeded the allowed data limit of 100,000 bytes per minute. 
This is in violation of our usage policy, which is designed to ensure fair resource distribution among all users and 
maintain the overall health of our system.

As a result of this breach, we have temporarily halted the operation of your container/image. 
Please note that it will not be allowed to resume until its data usage falls below the prescribed limit or a special exception is granted.

We understand that this situation may cause some inconvenience, and we apologize for that. 
However, these measures are necessary to maintain the integrity and performance of our system, which ultimately benefits all users.

To resolve this issue, we kindly ask you to review the operations of your Docker container and 
take the necessary actions to bring its data usage within the allowed limit. 
This could involve optimizing your processes, reducing non-essential operations, 
or applying for a special exception if your container requires higher data usage for legitimate reasons.

If you need any assistance or have any questions regarding this matter, 
please do not hesitate to contact us. Our team is ready to provide you with the necessary support and guidance.

Thank you for your understanding and cooperation in this matter. We appreciate your prompt attention to this issue.

Best Regards,
Your DVerse Management Team

---

Note: This is an automated email. Please do not reply. For assistance, contact `support@dverse.com`. Thank you for your understanding.
    """

    text = MIMEText(body, "plain")
    message.attach(text)

    # context = ssl.create_default_context()
    # with smtplib.SMTP_SSL("localhost", 2525, context=context) as server:
    with smtplib.SMTP("localhost", 2525) as server: # Unsecure
        # server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


def notify_owner(container_namespace):
    if container_namespace in owner_emails:
        send_email(
            owner_emails[container_namespace],
            "Urgent Attention Required: Docker Container Usage Limit Exceeded",
            container_namespace
        )
    else:
        print(f"No owner email found for {container_namespace}")

# Use the function
notify_owner("Bob/Booking-Searcher")