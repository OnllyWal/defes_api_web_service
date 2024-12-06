import requests
import os
from defesa_api.pre_process import start_doc_process, txt_edit_6lines
from defesa_api.text_chamado import text_chamado

def get_emails(endpoint_url):
    try:
        # Faz a requisição GET para o endpoint Flask
        response = requests.get(endpoint_url)
        response.raise_for_status()  # Verifica se houve erro HTTP
        emails = response.json()  # Converte a resposta JSON para um objeto Python (lista de dicionários)
        return emails
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados do endpoint: {e}")
        return []
    

def post_anexos(anexos, upload_url):
    files = [("file", (anexo.split("/")[-1], open(anexo, "rb"))) for anexo in anexos]

    response = requests.post(upload_url, files = files)
    if response.status_code != 200:
        print(f"Erro ao enviar anexos: {response.status_code} - {response.text}")
        return
    
    uploaded_urls = response.json().get("urls", [])
    print(f"Anexos enviados: {uploaded_urls}")

    return uploaded_urls

def process_email(email):
    # Manipula os dados recebidos conforme a necessidade
    txt = txt_edit_6lines(email['corpo'])
    docs = start_doc_process(email, txt)
    urls = post_anexos(docs, upload_url="http://172.19.113.12:5000/upload")
    chamado = text_chamado(txt)
    id = int(email['id'])

    email['corpo'] = f"{chamado} \n Atenciosamente, \n Equipe PPComp"
    email['anexos'] = urls
    email['status'] = "Processado"
    print(email)
    
    return email, id

def update_email(email,id):
    response = requests.put(f"http://172.19.113.12:5000/emails/{id}", json=email)
    print(response.json)
    remove_docs("/home/wal/defes_api_web_service/defesa_api/output")

def remove_docs(path):
    for arq in os.listdir(path):
        arq_path = os.path.join(path, arq)

        if os.path.isfile(arq_path):
            os.remove(arq_path)