# Mesclagem de Tabelas Excel

Este projeto é uma aplicação desenvolvida com **Streamlit** e **Pandas** para mesclar múltiplos arquivos Excel em um único arquivo consolidado.

## 🚀 Funcionalidades
- Upload de múltiplos arquivos Excel (`.xls` e `.xlsx`)
- Mesclagem automática das tabelas em um único DataFrame
- Download do arquivo consolidado em formato `.xlsx`
- Opção de personalizar o nome do arquivo de saída
- Interface interativa e intuitiva

## 📦 Requisitos
Antes de executar o projeto, certifique-se de ter os seguintes pacotes instalados:

```bash
pip install streamlit pandas openpyxl xlrd
```

## ▶ Como Executar
1. Salve o código principal em um arquivo Python, por exemplo, `app.py`.
2. Execute o Streamlit para iniciar a aplicação:

```bash
streamlit run app.py
```

3. Acesse o link exibido no terminal para interagir com a aplicação no navegador.

## 📝 Como Usar
1. Faça o upload de um ou mais arquivos Excel.
2. Aguarde a mesclagem dos arquivos.
3. Baixe o arquivo consolidado com o nome personalizado.

## 📌 Observações
- O programa suporta arquivos nos formatos **.xls** e **.xlsx**.
- As tabelas devem ter colunas compatíveis para a correta mesclagem.
- Se os arquivos contêm colunas diferentes, o resultado pode conter valores `NaN` em colunas não existentes em todos os arquivos.

## 📄 Licença
Este projeto é de código aberto e pode ser usado e modificado livremente.

