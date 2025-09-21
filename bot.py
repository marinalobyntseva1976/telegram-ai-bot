import telebot
from telebot import types
import json
import os
from datetime import datetime

from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Токен вашего бота (замените на ваш)

bot = telebot.TeleBot(TOKEN)

# Данные о курсах AI-Adminpriority
COURSES_DATA = {
    "greeting": "👋 Привет! Добро пожаловать в AI-Adminpriority!\n\nЯ помогу вам узнать о наших курсах по работе с искусственным интеллектом для административных директоров и HR-специалистов, и других сотрудников.\n\nВыберите интересующий вас раздел:",
    
    "courses": {
        "gpt_express": {
            "name": "GPT-экспресс",
            "description": "Базовый вечерний курс по применению ChatGPT для повседневных задач:\n• Составление договоров, положений, командировок\n• Сценарии мероприятий\n• Анализ данных\n• И многое другое"
        },
        "ai_visuals": {
            "name": "AI-визуалы и GPT 2.0",
            "description": "Расширенный курс по созданию изображений и презентаций:\n• Работа с нейросетевыми инструментами (Gamma, Leonardo, Stable Diffusion)\n• Продвинутый уровень работы с GPT\n• Создание профессиональных визуалов"
        }
    },
    
    "format": "📅 Формат и условия проведения:\n\n• Формат: только офлайн (Москва)\n• Начало: 18:00\n• Продолжительность: ~3,5 часа\n• Перерыв: 30 минут\n• Место: удобная площадка в Москве (адрес присылается после регистрации)",
    
    "experience": "❓ Нужен ли опыт работы с нейросетями?\n\nНет! Обучение начинается с базовых шагов:\n• Регистрация в сервисах\n• Установка VPN (при необходимости)\n• Настройка\n• Отправка первых запросов\n\nВсё показывается пошагово на экране. Даже если вы никогда не работали с AI, вы быстро разберётесь.",
    
    "benefits": "🎯 Что вы получите на курсе?\n\n• Готовые шаблоны запросов (промптов) для ежедневных задач\n• Навык работы с AI для ускорения рутинных процессов\n• Созданные своими руками AI-визуалы и презентации\n• Понимание, как интегрировать искусственный интеллект в рабочие процессы для экономии времени и ресурсов",
    
    "teacher": "👩‍🏫 Кто преподаёт?\n\nКурсы ведёт Марина Лобынцева — основатель и руководитель платформы AI-Adminpriority, бывший административный директор hh.ru, эксперт в оптимизации офисных процессов, внедрении ESG-инициатив и нематериальной мотивации персонала.\n\nМарина — практик, который обучает работе с AI на примерах реальных задач административных директоров и HR.",
    
    "pricing": "💰 Стоимость:\n\n• Стандарт: 2 500 ₽\n• Для подписчиков журнала «Административный директор»: 1 500 ₽\n• Для партнёров, которые не являются административными специалистами и HR: стоимость по запросу",
    
    "registration": "📝 Как зарегистрироваться?\n\nОтправьте письмо на team@adminpriority.ru с:\n• Названием курса\n• Датой проведения\n\nВ ответ получите подтверждение и детали.",
    
    "contacts": "📞 Контакты:\n\n• Telegram: @marnlo\n• Email: team@adminpriority.ru\n• Регистрация: info@admdir.ru"
}

# Создание главного меню
def create_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('📚 Курсы')
    btn2 = types.KeyboardButton('📅 Формат обучения')
    btn3 = types.KeyboardButton('❓ Нужен ли опыт?')
    btn4 = types.KeyboardButton('🎯 Что получите?')
    btn5 = types.KeyboardButton('👩‍🏫 Преподаватель')
    btn6 = types.KeyboardButton('💰 Стоимость')
    btn7 = types.KeyboardButton('📝 Регистрация')
    btn8 = types.KeyboardButton('📞 Контакты')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    return markup

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    welcome_text = f"👋 Привет, {user_name}!\n\n" + COURSES_DATA["greeting"]
    bot.reply_to(message, welcome_text, reply_markup=create_main_menu())

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "🤖 Доступные команды:\n\n/start - Главное меню\n/help - Помощь\n/courses - Информация о курсах\n/contacts - Контакты"
    bot.reply_to(message, help_text)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    text = message.text.lower()
    
    if 'курс' in text:
        show_courses(message)
    elif 'формат' in text or 'обучен' in text:
        bot.reply_to(message, COURSES_DATA["format"])
    elif 'опыт' in text or 'нужен' in text:
        bot.reply_to(message, COURSES_DATA["experience"])
    elif 'получите' in text or 'что' in text:
        bot.reply_to(message, COURSES_DATA["benefits"])
    elif 'преподаватель' in text or 'кто' in text:
        bot.reply_to(message, COURSES_DATA["teacher"])
    elif 'стоимость' in text or 'цена' in text or 'рубл' in text:
        bot.reply_to(message, COURSES_DATA["pricing"])
    elif 'регистрация' in text or 'записаться' in text:
        bot.reply_to(message, COURSES_DATA["registration"])
    elif 'контакт' in text:
        bot.reply_to(message, COURSES_DATA["contacts"])
    else:
        # Если не распознали команду, показываем главное меню
        bot.reply_to(message, "Выберите интересующий вас раздел из меню ниже:", reply_markup=create_main_menu())

def show_courses(message):
    courses_text = "📚 Наши курсы:\n\n"
    
    for key, course in COURSES_DATA["courses"].items():
        courses_text += f"🎓 {course['name']}\n{course['description']}\n\n"
    
    courses_text += "Оба курса рассчитаны на 3,5 часа, проходят в вечернее время, материал подаётся простым языком, чтобы даже новички легко включились в работу."
    
    bot.reply_to(message, courses_text)

# Обработчик команды /courses
@bot.message_handler(commands=['courses'])
def send_courses(message):
    show_courses(message)

# Обработчик команды /contacts
@bot.message_handler(commands=['contacts'])
def send_contacts(message):
    bot.reply_to(message, COURSES_DATA["contacts"])

# Логирование
def log_message(message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    text = message.text
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"[{timestamp}] User: {user_id} (@{username}) {first_name}: {text}\n"
    
    with open('bot_log.txt', 'a', encoding='utf-8') as f:
        f.write(log_entry)

# Запуск бота
if __name__ == "__main__":
    print("🤖 Бот AI-Adminpriority запущен!")
    print("📝 Для остановки нажмите Ctrl+C")
    
    try:
        bot.polling(none_stop=True, interval=0)
    except KeyboardInterrupt:
        print("\n🛑 Бот остановлен")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
