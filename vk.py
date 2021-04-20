import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from main import add_id, show, change
from test1 import create_table

vk_session = vk_api.VkApi(
    token='870b2c84cc4b80a88973841f55313ecabe6bb561737bf37726129396955f01512870aaacea5248cf1760a')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '203962283')


def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})


def main():
    try:
        week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.from_chat:
                    id = event.chat_id
                    add_id(id)
                    create_table()

                    msg = event.object.message['text'].lower()

                    if msg == 'привет':
                        sender(id, 'Приветствую))')

                    if msg == 'показать расписание':
                        sender(id, 'Введите день недели')
                        f = 'show'
                    if msg in week and f == 'show':
                        ms = ''
                        if msg == 'среда':
                            ms = 'среду'
                        elif msg == 'пятница':
                            ms = 'пятницу'
                        elif msg == 'суббота':
                            ms = 'субботу'
                        else:
                            ms = msg

                        sender(id, 'Расписание на {}: \n{}'.format(ms, show(id, week.index(msg))))

                    if msg == 'изменить расписание':
                        sender(id, 'Введите день недели')
                        f = 'change'
                    if msg in week and f == 'change':
                        sender(id, 'Вводите уроки (каждый с новой строки)')
                        day = msg
                        f = 'add'

                    if f == 'add':
                        rasp = msg.split()
                        change(id, week.index(day), rasp)
                        da = ''
                        if day == 'среда':
                            da = 'среду'
                        elif day == 'пятница':
                            da = 'пятницу'
                        elif day == 'суббота':
                            da = 'субботу'
                        else:
                            da = day
                        if len(rasp) > 1:
                            sender(id, "Расписание на {} обновлено✅ ".format(da))
    except:
        main()

if __name__ == '__main__':
    main()
