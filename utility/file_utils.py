import os

@staticmethod
def simulate_send_email(email_address, subject, message):
        """
        Sends a 'simulated' email in the form of adding an email message 
        to a text file.  The message will appear in the 'observer_emails.txt' 
        file within the 'output' directory of the current project directory.
        Args:
            email_address (str):  The email address to which the 'simulated' message is sent.
            subject (str):  The subject line for the 'simulated' message.
            message (str): The message body for the 'simulated' message.
        """
        directory = "output"
        filename = "observer_emails.txt"
        path = os.path.join(directory, filename)
        os.makedirs(directory, exist_ok=True)
        with open(path, "a") as file:
            file.write(f"---\nTo: {email_address}\nSubject: {subject}\nMessage: {message}\n---\n")