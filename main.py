from controllers.api_connector import get_emails,process_email, update_email

def main():
    # URL do endpoint Flask
    endpoint_url = "http://172.19.113.12:5000/emails?status=Armazenado&tipo=defesa"
    print("Buscando emails do servidor Flask...")

    # Busca e processa os emails
    emails = get_emails(endpoint_url)
    if emails:
        for email in emails:
            print(f"{len(emails)} emails recebidos. Processando...")
            email = process_email
            update_email(email, endpoint_url)

    else:
        print("Nenhum email foi recebido.")


if __name__ == "__main__":
    main()