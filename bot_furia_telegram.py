




import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Olá, eu sou o Bot da FURIA!\n\n"
        "Use /help para ver o que eu posso fazer."
    )

# Comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📜 Comandos disponíveis:\n"
        "/start - Iniciar o bot\n"
        "/help - Mostrar esta mensagem de ajuda\n"
        "/sobre - Saiba mais sobre a FURIA\n"
        "/instagram - Acompanhe a gente nas redes sociais\n"
        "/loja - Link para a loja oficial\n"
        "/agenda - Ver a agenda de jogos\n"
        "/time - Ver os jogadores da Furia\n"
        "/resultados - Ver os resultados dos nossos jogos"
    )

# Outros comandos
async def sobre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 A FURIA é uma organização de esports brasileira conhecida mundialmente!\n"
        "Saiba mais sobre nós: https://www.furia.gg/quem-somos"
    )

async def loja(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛒 Confira nossa loja oficial: https://www.furia.gg/produtos")

async def agenda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🗓️ Veja nossa agenda de jogos: https://draft5.gg/equipe/330-FURIA/proximas-partidas")

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👥 Veja nossa equipe de CS: https://draft5.gg/equipe/330-FURIA")

async def resultados(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Veja o resultado de nossos jogos: https://draft5.gg/equipe/330-FURIA/resultados")

async def instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📸 Acompanhe a gente no Instagram: https://www.instagram.com/furiagg/?hl=pt-br")

# Resposta a mensagens normais
async def mensagem_normal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()
    if "furia" in texto:
        await update.message.reply_text("🔥 Vai FURIA! 🔥")
    elif "oi" in texto or "olá" in texto:
        await update.message.reply_text("👋 Olá! Seja bem-vindo ao Bot da FURIA!")
    elif "loja" in texto:
        await update.message.reply_text("🛒 Nossa loja oficial: https://store.furia.gg")
    else:
        await update.message.reply_text("❓ Não entendi... Use /help para ver os comandos disponíveis.")


# Main
def main():
    app = Application.builder().token(API_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("sobre", sobre))
    app.add_handler(CommandHandler("loja", loja))
    app.add_handler(CommandHandler("agenda", agenda))
    app.add_handler(CommandHandler("time", time))
    app.add_handler(CommandHandler("resultados", resultados))
    app.add_handler(CommandHandler("instagram", instagram))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensagem_normal))

    app.run_polling()

if __name__ == "__main__":
    main()
