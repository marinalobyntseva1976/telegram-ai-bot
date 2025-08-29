import os
from bot import bot

# Для совместимости с различными платформами
if __name__ == "__main__":
    print("🤖 Бот AI-Adminpriority запущен!")
    print("📝 Для остановки нажмите Ctrl+C")
    
    try:
        bot.polling(none_stop=True, interval=0)
    except KeyboardInterrupt:
        print("\n🛑 Бот остановлен")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

