def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if not('@' in message + recipient and recipient.endswith((".com", ".ru", ".net")) and sender.endswith((".com", ".ru", ".net"))):
        rezult = f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}."
    elif sender == recipient:
        rezult = "Нельзя отправить письмо самому себе!"
    elif recipient == "niversity.help@gmail.com":
        rezult = f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}."
    else:
        rezult = f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}."
    print(rezult)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')







