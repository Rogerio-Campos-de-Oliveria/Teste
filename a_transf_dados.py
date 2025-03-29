#Importação das bibliotecas
from zipfile import ZipFile
import os
import tabula
import pandas as pd



#2 - Transformação de Dados

# Extrair dados do pdf
arquivo = tabula.read_pdf("anexos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",pages='3-181', multiple_tables=True)
            
# Concatenar todas as tabelas extraídas
tabela_df = pd.concat(arquivo, ignore_index=True)

# Substituir abreviações OO e AMB
tabela_df.replace({"OD": "Odontológico", "AMB": "Ambulatorial"}, inplace=True)

# Salvar arquivo em CSV
os.makedirs("CSV")

csv_path = os.path.join("CSV","RogerioC_Oliceira.csv")
tabela_df.to_csv(csv_path, sep=";" , decimal="." , index=False)

#ZIP arquivo CSV
zip_arquivo = "CSV.zip"
with ZipFile(zip_arquivo, "w") as zip:
    for csv in os.listdir("CSV"):
        zip.write(os.path.join("CSV", csv), csv) 