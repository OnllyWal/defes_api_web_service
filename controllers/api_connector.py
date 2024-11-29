import requests
import json

def fetch_emails(endpoint_url):
    try:
        # Faz a requisição GET para o endpoint Flask
        response = requests.get(endpoint_url)
        response.raise_for_status()  # Verifica se houve erro HTTP
        emails = response.json()  # Converte a resposta JSON para um objeto Python (lista de dicionários)
        print
        return emails
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados do endpoint: {e}")
        return []

def process_emails(emails):
    # Manipula os dados recebidos conforme a necessidade
    for email in emails:
        print(f"ID: {email['id']}, Título: {email['titulo']}")
        # Exemplos de manipulação:
        # - Filtrar emails por tipo
        # - Salvar os dados em um arquivo local
        # - Processar anexos
        # - Enviar para outro sistema

def main():
    # URL do endpoint Flask
    endpoint_url = "http://<FLASK_SERVER_IP>:5000/emails"
    print("Buscando emails do servidor Flask...")

    # Busca e processa os emails
    emails = fetch_emails(endpoint_url)
    if emails:
        print(f"{len(emails)} emails recebidos. Processando...")
        process_emails(emails)
    else:
        print("Nenhum email foi recebido.")

if __name__ == "__main__":
    main()
