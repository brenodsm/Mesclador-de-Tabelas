import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Ferramentas Pizzatto", layout="centered")
st.title("Ferramentas Pizzatto")

# Menu lateral para escolha da funcionalidade
pagina = st.sidebar.selectbox("Escolha a funcionalidade:", ["Adicionar CNPJ Pizzatto", "Mesclar Tabelas"])

# Página 1: Adicionar CNPJ
if pagina == "Adicionar CNPJ Pizzatto":
    st.header("Adicionar CNPJ à planilha")

    uploaded_file = st.file_uploader("Envie sua planilha Excel", type=["xlsx"])

    try:
        lista_cnpjs = st.secrets["cnpjs"]["lista"]
    except Exception as e:
        st.error("Erro ao carregar os CNPJs. Verifique as configurações em st.secrets.")
        lista_cnpjs = []

    if lista_cnpjs:
        cnpj_escolhido = st.selectbox("Selecione o CNPJ Pizzatto que deseja incluir:", lista_cnpjs)

        if uploaded_file and cnpj_escolhido:
            df = pd.read_excel(uploaded_file)
            df.insert(0, "CNPJ Pizzatto", cnpj_escolhido)

            st.success("Coluna adicionada com sucesso!")
            st.dataframe(df)

            output = BytesIO()
            df.to_excel(output, index=False, engine='openpyxl')
            output.seek(0)

            st.download_button(
                label="Baixar planilha com CNPJ adicionado",
                data=output,
                file_name=f"{cnpj_escolhido[-2:]}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

# Página 2: Mesclar Tabelas
elif pagina == "Mesclar Tabelas":
    st.header("Mesclagem de Tabelas Excel")

    nome_arquivo = st.text_input("Nome do arquivo de saída", "tabelas_mescladas")

    uploaded_files = st.file_uploader("Selecione os arquivos Excel", type=['xls', 'xlsx'], accept_multiple_files=True)

    if uploaded_files:
        def carregar_arquivo(file):
            if file.name.endswith('.xls'):
                return pd.read_excel(file, engine='xlrd')
            else:
                return pd.read_excel(file, engine='openpyxl')

        tabelas_mescladas = pd.concat([carregar_arquivo(file) for file in uploaded_files], ignore_index=True)

        @st.cache_data
        def save_to_excel(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False)
            output.seek(0)
            return output

        with st.spinner("Processando a mesclagem das tabelas..."):
            excel_data = save_to_excel(tabelas_mescladas)

        downloaded = st.download_button(
            label="Baixar tabela mesclada",
            data=excel_data,
            file_name=f"{nome_arquivo}.xlsx",
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

        if downloaded:
            st.success('Mesclagem concluída com sucesso!')
    else:
        st.info("Por favor, faça o upload dos arquivos Excel.")
