import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")


def main_menu():
    keyboard = [
        [InlineKeyboardButton("⚡ TÖVSİYƏ: AUD/JPY (5M)", callback_data="recommend")],
        [
            InlineKeyboardButton("🎯 Canlı Analiz", callback_data="live"),
            InlineKeyboardButton("🌐 Bazar", callback_data="market"),
        ],
        [
            InlineKeyboardButton("📡 Bazar Nəbzi", callback_data="pulse"),
            InlineKeyboardButton("👑 VIP Siqnallar", callback_data="vip"),
        ],
        [InlineKeyboardButton("➡️ Növbəti", callback_data="next")],
    ]

    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 *NEXORA AI SIGNAL*\n\n"
        "🤖 AI əsaslı siqnal sistemi\n"
        "📊 Bazar analizləri və siqnallar\n\n"
        "Aşağıdakı menyudan seçim edin:",
        parse_mode="Markdown",
        reply_markup=main_menu(),
    )


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "recommend":
        text = (
            "⚡ *TÖVSİYƏ*\n\n"
            "AUD/JPY OTC\n"
            "⏱ 5 dəqiqə\n\n"
            "📊 Analiz hazırlanır..."
        )

    elif query.data == "live":
        text = (
            "🎯 *CANLI ANALİZ*\n\n"
            "Canlı analiz modulu hazırlanır."
        )

    elif query.data == "market":
        text = (
            "🌐 *BAZAR*\n\n"
            "AUD/USD\n"
            "EUR/USD\n"
            "GBP/USD\n"
            "USD/JPY"
        )

    elif query.data == "pulse":
        text = (
            "📡 *BAZAR NƏBZİ*\n\n"
            "Bazar məlumatları hazırlanır."
        )

    elif query.data == "vip":
        text = (
            "👑 *VIP SİQNALLAR*\n\n"
            "VIP bölməsi hazırlanır."
        )

    else:
        text = "➡️ Növbəti bölmə hazırlanır."

    await query.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=main_menu(),
    )


def run():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN təyin edilməyib.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_callback))

    print("NEXORA AI SIGNAL BOT işləyir...")
    app.run_polling()


if __name__ == "__main__":
    run()
