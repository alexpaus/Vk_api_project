import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(
    token='870b2c84cc4b80a88973841f55313ecabe6bb561737bf37726129396955f01512870aaacea5248cf1760a')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '203962283')


def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})


def add(day, rasp, id):
    print(day, rasp)


def show(id, day):
    pass


def main():
    week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_chat:

                id = event.chat_id

                msg = event.object.message['text'].lower()

                if msg == 'привет':
                    sender(id, 'Приветствую))')

                if msg == 'показать расписание':
                    sender(id, 'Введите день недели')
                    f = 'show'
                if msg in week and f == 'show':
                    sender(id, 'Расписание на {}:'.format(msg))

                if msg == 'помощь':
                    pass
                if msg == 'изменить расписание':
                    sender(id, 'Введите день недели')
                    f = 'change'
                if msg in week and f == 'change':
                    sender(id, 'Вводите уроки (каждый с новой строки)')
                    day = msg

                    f = 'add'
                if f == 'add':
                    rasp = msg.split()

                    add(day, rasp, id)


if __name__ == '__main__':
    main()
