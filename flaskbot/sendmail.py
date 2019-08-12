from tokens import SENDGRID_API_KEY
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileType, FileName, Disposition, ContentId
import base64

# bumblebees-flowers.jpg

def send_simple_mail(subj='Sending with Twilio SendGrid is Fun'):
    message = Mail(
        from_email='from_email@example.com',
        to_emails='cagedev@gmail.com',
        subject=subj,
        html_content='<strong>and easy to do anywhere, even with Python</strong>')

    import os
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(THIS_FOLDER, 'bumblebees-flowers.jpg')
    # file_path = 'bumblebees-flowers.jpg'
    with open(file_path, 'rb') as f:
        data = f.read()
        f.close()
    encoded = base64.b64encode(data).decode()
    attachment = Attachment()
    attachment.file_content = FileContent(encoded)
    attachment.file_type = FileType('application/jpeg')
    attachment.file_name = FileName('bumblebees-flowers.jpg')
    attachment.disposition = Disposition('attachment')
    attachment.content_id = ContentId('Example Content ID')
    message.attachment = attachment


    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)