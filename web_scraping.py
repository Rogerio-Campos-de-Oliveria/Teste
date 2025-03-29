#Importação das bibliotecas
import urllib3
from bs4 import BeautifulSoup
import wget
from zipfile import ZipFile
import os

#1 - Web Scraping

#Definição da URL
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"


#Baixar o HTML da página
arquivo = urllib3.PoolManager()
retorno = arquivo.request('GET',url)

pagina = BeautifulSoup(retorno.data,"html.parser")


#Encontrar os links dos PDFs na página separar e salvar

dado=[]
for a in pagina.find_all("a", class_="internal-link"):
    link = a["href"]
    if "Anexo" in link and link.endswith(".pdf"):
        dado.append(a.get("href"))
       
#Criar uma pasta para armazenar os arquivos
os.mkdir("anexos")
caminho_destino = ("anexos")

for item in dado:
    url_origem = item
    wget.download(url_origem,caminho_destino)

#ZIP arquivos
zip_arquivo = "anexos.zip"
with ZipFile(zip_arquivo, "w") as zip:
    for pdf in os.listdir("anexos"):
        zip.write(os.path.join("anexos", pdf), pdf) 

