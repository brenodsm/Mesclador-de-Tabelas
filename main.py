import pandas as pd
import streamlit as st
from io import BytesIO

# Interface do Streamlit
st.title('Mesclagem de Tabelas')

# Campo de entrada para o nome do arquivo de saída, com valor padrão
nome_arquivo = st.text_input("Nome do arquivo de saída", "tabelas_mescladas")

# Fazer upload dos arquivos Excel
uploaded_files = st.file_uploader("Selecione os arquivos Excel", type=['xls', 'xlsx'], accept_multiple_files=True)

if uploaded_files:  # Verificar se arquivos foram carregados
    # Função para carregar arquivos Excel, considerando os dois formatos
    def carregar_arquivo(file):
        if file.name.endswith('.xls'):
            return pd.read_excel(file, engine='xlrd')
        else:
            return pd.read_excel(file, engine='openpyxl')

    # Carregar e concatenar os arquivos
    tabelas_mescladas = pd.concat([carregar_arquivo(file) for file in uploaded_files], ignore_index=True)

    # Função para salvar o DataFrame em um arquivo Excel em memória
    @st.cache_data
    def save_to_excel(df):
        output = BytesIO()  # Criar um objeto BytesIO
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
        output.seek(0)  # Retornar o ponteiro do arquivo para o início
        return output

    # Exibir o spinner enquanto o arquivo é gerado
    with st.spinner("Processando a mesclagem das tabelas..."):
        excel_data = save_to_excel(tabelas_mescladas)

    # Botão para baixar o arquivo Excel com o nome escolhido
    downloaded = st.download_button(
        label="Baixar tabela mesclada",
        data=excel_data,
        file_name=f"{nome_arquivo}.xlsx",
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    # Exibir mensagem de sucesso após o download
    if downloaded:
        st.success('Mesclagem concluída com sucesso!')
else:
    st.info("Por favor, faça o upload dos arquivos Excel.")
