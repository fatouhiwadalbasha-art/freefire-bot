import os
import random
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# تحميل المتغيرات السرية من ملف .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# دالة الترحيب وعرض الأزرار
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📱 هاتف ضعيف (Weak)", callback_data='weak')],
        [InlineKeyboardButton("⚡ هاتف متوسط (Medium)", callback_data='medium')],
        [InlineKeyboardButton("🔥 هاتف قوي (Strong)", callback_data='strong')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "أهلاً بك في أداة الحساسية الذكية! 🎯\n"
        "الرجاء اختيار فئة هاتفك لتوليد أفضل إعدادات تلقائية للهيدشوت:",
        reply_markup=reply_markup
    )

# دالة معالجة الضغط على الأزرار وحساب الحساسية
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    device_type = query.data
    
    if device_type == 'weak':
        title = "📱 إعدادات الهواتف الضعيفة"
        general = random.randint(95, 100)
        red_dot = random.randint(90, 95)
        scope2 = random.randint(85, 92)
        scope4 = random.randint(80, 88)
        fire_button = random.randint(50, 55)
    elif device_type == 'medium':
        title = "⚡ إعدادات الهواتف المتوسطة"
        general = random.randint(90, 96)
        red_dot = random.randint(85, 92)
        scope2 = random.randint(80, 88)
        scope4 = random.randint(75, 85)
        fire_button = random.randint(45, 50)
    else:
        title = "🔥 إعدادات الهواتف القوية"
        general = random.randint(85, 92)
        red_dot = random.randint(80, 86)
        scope2 = random.randint(75, 82)
        scope4 = random.randint(70, 78)
        fire_button = random.randint(40, 46)

    result_text = (
        f"🎯 **{title}** 🎯\n\n"
        f"🔹 الحساسية العامة (General): `{general}`\n"
        f"🔹 النقطة الحمراء (Red Dot): `{red_dot}`\n"
        f"🔹 عدسة 2X (Scope 2x): `{scope2}`\n"
        f"🔹 عدسة 4X (Scope 4x): `{scope4}`\n"
        f"🔘 حجم زر الإطلاق (Fire Button): `{fire_button}%`\n\n"
        f"💡 _تم حساب القيم برمجياً لتناسب جهازك دون الحاجة لتعديل DPI._"
    )
    
    await query.edit_message_text(text=result_text, parse_mode="Markdown")

def main():
    print("جاري تشغيل البوت بأمان... اضغط CTRL+C لإيقافه.")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CallbackQueryHandler(button_click))
    app.run_polling()

if __name__ == "__main__":
    main()
