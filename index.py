import time
import smtplib
from email.message import EmailMessage
from colorama import Fore, init

# Initialiserer fargene
init(autoreset=True)

def main():
    #Dekorere terminal
    print(Fore.YELLOW + "=" * 60)
    print(Fore.CYAN + "  Velkommen til Konstant Spam-Mail programmet  ")
    print(Fore.MAGENTA + "          Laget av Thor A. Å.          ")
    print(Fore.GREEN + "               20.03.2025              ")
    print(Fore.YELLOW + "=" * 60)
    print("")

    innhold = input("Skriv et ord: ") #Spør om ord.
    #Spør hvor mange jeg vil sende:
    antall_mails = int(input(Fore.CYAN + "Hvor mange mails ønsker du sende? ").strip())
    email_receiver = input(Fore.CYAN + "Til: ")
    
    send_bulk_emails(innhold, antall_mails, email_receiver)

def send_bulk_emails(content, count, email_receiver):
    email_sender = '' #Her må du skrive mailen din!
    email_password = ''  # Her må du skrive app-passordet du opprettet!

    for i in range(count):
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = f"Spam-mail {i + 1}" #Tittel på eposten.
        em.set_content(content)

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            print(Fore.GREEN + f"E-post {i + 1} sendt!")
        except Exception as e:
            print(Fore.RED + f"Feil ved sending av epost {i + 1}: {e}")
        
        if i < count - 1:
            time.sleep(0)  # Pause i sekunder mellom sendingene, dette kan du redigere.

if __name__ == "__main__":
    main()