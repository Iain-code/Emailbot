import smtplib
import getpass


def send_email():
    host = "smtp-mail.outlook.com"
    port = 587

    sender = "reallywtf987@hotmail.com"
    receiver = "iainvirgo1010@live.co.uk"
    password = getpass.getpass("Password: ")
    subject = "Python email test"
    body = "I wrote an email...hope this works"


    message = f"""From: {sender}
    To: {receiver}
    Subject: {subject}\n
    {body}
    """
    try:
        # Connect to the SMTP server
        smtp = smtplib.SMTP(host, port, local_hostname='localhost')
        smtp.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        smtp.ehlo()  # Identify this client to the server
        smtp.login(sender, password)  # Log in to your email account
        smtp.sendmail(sender, receiver, message)  # Send the email
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        smtp.quit()  # Close the connection

if __name__ == "__main__":
    send_email()







    
