import time

import instaloader
from pyrogram import Client


bot = instaloader.Instaloader()
TELEGRAM_CHANNEL_ID = -1001951565322
API_ID = 15354199
API_HASH = "4b42c4babb1f7866c005b8c5a967add7"

bot.load_session_from_file("botforern2", filename="./session-botforern2")
posts = instaloader.Profile.from_username(bot.context, "ernest_kuhni").get_posts()


def send_message(post):
    try:
        if post.is_video:
            app.send_video(TELEGRAM_CHANNEL_ID, post.video_url, caption=post.caption)
        else:
            app.send_photo(TELEGRAM_CHANNEL_ID, post.url, caption=post.caption)
    except Exception as e:
        print(f"[-] Пост не отправился\nОшибка: {e}")
        print(post.video_url if post.is_video else post.url)


with Client("my_acc", API_ID, API_HASH) as app:
    print("Собираю посты, ждите...")
    posts_ = []
    for i in posts:
        posts_.append(i)

    print("Отправляю посты...")

    for post in posts_[::-1]:
        send_message(post)
        print("Пост отправлен!")
        time.sleep(10)
