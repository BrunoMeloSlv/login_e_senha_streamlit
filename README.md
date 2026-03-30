# 📊 Dashboard de Vendas com Login | Streamlit

Este projeto consiste na construção de um **dashboard interativo de vendas com autenticação de usuários**, desenvolvido utilizando **Python + Streamlit**.

A aplicação permite que cada vendedor acesse apenas suas próprias vendas, garantindo uma experiência personalizada e mais próxima de um cenário real de negócio.

---

## 🚀 Funcionalidades

- 🔐 Sistema de login com usuário e senha  
- 👤 Controle de sessão com `st.session_state`  
- 📊 Dashboard individual por vendedor  
- 📋 Visualização de dados em tabela interativa  
- 📈 Métricas principais:
  - Total vendido  
  - Quantidade de vendas  
- 🚪 Funcionalidade de logout  

---

## 🛠️ Tecnologias utilizadas

- Python  
- Streamlit  
- Pandas  

---

## 📁 Estrutura dos dados

O projeto utiliza dois arquivos:

### 👥 `usuarios.txt`
Arquivo responsável pela autenticação dos usuários.

**Exemplo:**

usuario,senha,vendedor
admin,123,Bruno
joao,456,João Silva


---

### 💰 `vendas.xlsx`
Base de dados contendo as vendas realizadas.

**Exemplo de colunas:**
- vendedor  
- valor  
- data  
- produto  

usuarios = pd.read_csv("caminho/usuarios.txt")
vendas = pd.read_excel("caminho/vendas.xlsx")
