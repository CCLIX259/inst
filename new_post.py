import time

import instaloader
from pyrogram import Client


bot = instaloader.Instaloader()
TELEGRAM_CHANNEL_ID = -1001951565322
API_ID = 15354199
API_HASH = "4b42c4babb1f7866c005b8c5a967add7"

bot.load_session_from_file("botforern2", filename="./session-botforern2")


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
    while True:
        posts = instaloader.Profile.from_username(bot.context, "ernest_kuhni").get_posts()
        for i in posts:
            post_ = i
            break
        time.sleep(180)
        while True:
            posts = instaloader.Profile.from_username(bot.context, "ernest_kuhni").get_posts()
            for i in posts:
                if post_ != i:
                    send_message(posts[0])
                    post_ = i
                else:
                    break
