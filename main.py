from instagrapi import Client
import time

# Авторизация
username = str(input("Instanick: "))
password = input("Password: ")
cl = Client()
cl.login(username, password)

# Получение подписчиков и подписок
followers = cl.user_followers(cl.user_id)
following = cl.user_following(cl.user_id)

for user_id, user_info in following.items():
    if user_id in followers:
        print(f"Пропускаем: {user_info.username} (Подписан на вас)")
    else:
        print(f"Отписка от: {user_info.username}")
        try:
            cl.user_unfollow(user_id)
            print(f"Успешно отписались от {user_info.username}")
        except Exception as e:
            print(f"Ошибка при обработке {user_info.username}: {e}")
        time.sleep(5)  # Добавляем паузу между запросами
