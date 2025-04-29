# 🤖 Bot da FURIA (Telegram)

Este é um bot oficial da FURIA Esports feito com Python e a biblioteca `python-telegram-bot`.  
Ele oferece comandos rápidos para acessar informações sobre a organização, agenda de jogos, time e muito mais.

## 🔧 Funcionalidades

- Mensagens automáticas com comandos personalizados
- Links úteis para redes sociais, site oficial e loja
- Respostas automáticas para mensagens como “oi” ou “furia”
- Organização de código com comandos separados

## 🚀 Comandos disponíveis

| Comando         | Ação                                                                 |
|-----------------|----------------------------------------------------------------------|
| `/start`        | Inicia o bot e mostra o menu                                         |
| `/help`         | Mostra todos os comandos disponíveis                                 |
| `/sobre`        | Fala sobre a FURIA e sua história                                    |
| `/loja`         | Link para a loja oficial da FURIA                                    |
| `/agenda`       | Mostra a agenda de jogos no site Draft5                              |
| `/time`         | Mostra os jogadores do time                                          |
| `/resultados`   | Link direto para os últimos resultados                               |
| `/instagram`    | Redireciona para o Instagram oficial da FURIA                        |

## 🧪 Respostas automáticas para mensagens

| Texto na mensagem     | Resposta do bot                                               |
|-----------------------|---------------------------------------------------------------|
| `oi` ou `olá`         | Saudação personalizada                                        |
| `furia`               | "🔥 Vai FURIA! 🔥"                                             |
| `loja`                | Link direto para a loja oficial                               |
| Outro texto qualquer  | Mensagem sugerindo usar o comando `/help`                     |

## 🛠️ Instalação e uso

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/seu-usuario/bot-furia.git
   cd bot-furia
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure o token do bot:**

   Crie um arquivo `.env` e adicione sua chave:

   ```
   API_TOKEN=seu_token_do_telegram_aqui
   ```

4. **Execute o bot:**
   ```bash
   python bot.py
   ```

## 📦 Requisitos

- Python 3.10 ou superior
- `python-telegram-bot` v20+

## 🔒 Segurança

Seu token está protegido por meio do arquivo `.env`, e o projeto já inclui um `.gitignore` que impede o token de ser exposto no GitHub.

---

## 📎 Links úteis

- 🌐 [Site Oficial da FURIA](https://www.furia.gg)
- 🛒 [Loja Oficial](https://store.furia.gg)
- 📅 [Agenda da Equipe](https://draft5.gg/equipe/330-FURIA/proximas-partidas)
- 📷 [Instagram Oficial](https://www.instagram.com/furiagg/?hl=pt-br)

## 📜 Licença

Este projeto é apenas um exemplo educacional e não possui afiliação oficial com a FURIA Esports.

---

Feito com 💜 por fãs da FURIA!

