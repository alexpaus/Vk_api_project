import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(
    token='870b2c84cc4b80a88973841f55313ecabe6bb561737bf37726129396955f01512870aaacea5248cf1760a')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '203962283')


def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})


def main():
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_chat:
                id = event.chat_id
                msg = event.object.message['text'].lower()
                if msg == 'привет':
                    sender(id, 'Приветствую))')
                print(msg)


if __name__ == '__main__':
    main()
