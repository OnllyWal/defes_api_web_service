from controllers.api_connector import get_emails,process_email, update_email
import time

def main():
    # URL do endpoint Flask
    endpoint_url = "http://172.19.113.12:5000/emails"
    print("Buscando emails do servidor Flask...")

    # Busca e processa os emails
    while True:
        emails = get_emails(endpoint_url)
        if emails:
            for email in emails:
                if email['status'] == "Armazenado":
                    #print(email)
                    print(f"{len(emails)} emails recebidos. Processando...")
                    email, id = process_email(email)
                    update_email(email, id)
        else:
            print("Nenhum email foi recebido.")
        time.sleep(60)


if __name__ == "__main__":
    main()