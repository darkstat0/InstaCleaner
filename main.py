from instagrapi import Client
import time
import getpass  # Для безопасного ввода пароля

# Приветственное сообщение
def show_banner():
    print("=" * 50)
    print(" " * 15 + "InstaCleaner")
    print("=" * 50)
    print("Инструмент для управления подписками Instagram")
    print("Автор: darkstar")
    print("=" * 50)

# Запуск программы
show_banner()

# Авторизация
username = str(input("Введите ваш Instanick: "))
password = getpass.getpass("Введите ваш пароль: ")  # Скрытие ввода пароля
cl = Client()
try:
    cl.login(username, password)
    print("\n[✓] Успешный вход в аккаунт!")
except Exception as e:
    print(f"\n[!] Ошибка авторизации: {e}")
    exit()

# Получение подписчиков и подписок
print("\n[~] Получаем данные подписчиков и подписок...")
try:
    followers = cl.user_followers(cl.user_id)
    following = cl.user_following(cl.user_id)
except Exception as e:
    print(f"[!] Ошибка при получении данных: {e}")
    exit()

print("\n[~] Начинаем обработку...")
for user_id, user_info in following.items():
    if user_id in followers:
        print(f"[=] Пропускаем: {user_info.username} (Подписан на вас)")
    else:
        print(f"[x] Отписка от: {user_info.username}")
        try:
            cl.user_unfollow(user_id)
            print(f"    [✓] Успешно отписались от {user_info.username}")
        except Exception as e:
            print(f"    [!] Ошибка при обработке {user_info.username}: {e}")
        time.sleep(5)  # Добавляем паузу между запросами
print("\n[✓] Обработка завершена!")
