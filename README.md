Perfeito! Aqui está um **README.md atualizado, organizado e pronto para seu projeto Feedback Assistant com Proxy para Verbeux FeedAI:**

---

# 📢 Feedback Assistant – Verbeux API Integration

## ✅ Visão Geral

Este projeto é um assistente de feedback de clientes desenvolvido com **FastAPI**. Ele permite **coletar**, **classificar** e **armazenar feedbacks** de forma simples, além de incluir um **proxy HTTP** que conecta seu backend à **Generative API da Verbeux (FeedAI)**.

Este projeto faz parte de um **desafio técnico para a vaga de Estágio na Verbeux**.

---

## 🚀 Funcionalidades

* ✅ Envio de feedbacks (Elogio, Reclamação ou Neutro)
* ✅ Classificação automática de mensagens por palavras-chave
* ✅ Armazenamento de feedbacks em **SQLite**
* ✅ Exibição de todos os feedbacks via **API JSON** e via **página HTML**
* ✅ **Proxy `/chat`** para integração com a **Verbeux FeedAI Generative API**
* ✅ Configuração de **CORS** para comunicação com seu frontend (se desejar)

---

## 📂 Estrutura do Projeto

```
feedback-assistant/
├── src/
│   ├── main.py          # FastAPI principal (rotas de feedback + inclusão da proxy)
│   ├── proxy.py         # Proxy para a API Generative da Verbeux
│   ├── database.py      # Configuração do banco (SQLAlchemy + SQLite)
│   └── classifier.py    # Lógica simples para classificar feedbacks
├── data/
│   └── feedbacks.json   # Backup opcional de feedbacks
├── templates/
│   └── index.html       # Página HTML com listagem de feedbacks
├── static/
│   └── style.css        # Estilo da página web
├── requirements.txt     # Dependências Python
└── README.md            # Instruções e documentação
```

---

## ⚙️ Como Executar Localmente

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Inicie o servidor FastAPI:

```bash
uvicorn src.main:app --reload
ou
python -m uvicorn main:app --reload
```

3. Acesse o sistema no navegador:

```
http://127.0.0.1:8000
```

---

## 🧑‍💻 Endpoints Disponíveis

| Endpoint      | Método | Função                                          |
| ------------- | ------ | ----------------------------------------------- |
| `/submit/`    | POST   | Envia um novo feedback                          |
| `/feedbacks/` | GET    | Lista todos os feedbacks salvos                 |
| `/`           | GET    | Página HTML com feedbacks                       |
| `/chat`       | POST   | Proxy que envia mensagens para o FeedAI Verbeux |

---

## 🔑 Configuração da Proxy Verbeux (FeedAI)

Antes de testar o endpoint `/chat`, **você precisa editar o arquivo `src/proxy.py` e definir:**

* ✅ Sua **API KEY oficial da Verbeux**:

```python
API_KEY = "SUA_API_KEY_AQUI"
```

* ✅ O **UUID do seu Assistente Generative da Verbeux**:

```python
ASSISTANT_ID = "UUID_DO_SEU_ASSISTENTE"
```

👉 Se ainda não tiver esse UUID, peça ao suporte ou ao dev da Verbeux.

---

## ✅ Exemplos de Uso da Proxy (`/chat`)

**Exemplo de requisição POST:**

URL:

```
POST http://127.0.0.1:8000/chat
```

Body JSON:

```json
{
  "message": "Olá, quero fazer um pedido"
}
```

---

## 📝 Observações Importantes

* O UUID usado deve ser de um **Assistente habilitado na Generative API da Verbeux**, senão o endpoint vai dar erro 404.
* Lembre-se de não compartilhar sua **API Key segura**.
* O projeto usa **SQLite** para simplificar o armazenamento local.

---
