import os
import ptbot
from dotenv import load_dotenv
from pytimeparse import parse

def reply(chat_id, text):
    sec = parse(text)
    message_id = bot.send_message(chat_id, "Запускаю таймер...")
    bot.create_timer(sec + 1, notify, chat_id=chat_id)
    bot.create_countdown(sec, notify_progress, chat_id=chat_id, message_id=message_id, sec=sec)


def notify(chat_id):
    bot.send_message(chat_id, "Время вышло")

    
def notify_progress(secs_left, chat_id, message_id, sec):
    bot.update_message(chat_id, message_id, "Осталось {} секунд(ы) \n {}".format(secs_left, render_progressbar(sec, sec-secs_left)))


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


if __name__ == '__main__':
    load_dotenv()
    TG_TOKEN = os.getenv('BOT_TOKEN')
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(reply)
    bot.run_bot()
