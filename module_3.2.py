def send_email(message, recipient, sender="university.help@gmail.com"):
    valid_domains = ('.com', '.ru', '.net')

    def is_valid_email(email):
        return '@' in email and str(email).endswith(valid_domains)

    if not is_valid_email(sender) or not is_valid_email(recipient):
        return f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}"
    if sender == recipient:
        return 'Нельзя отправить письмо самому себе!'
    if sender == 'university.help@gmail.com':
        return f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.'
    else:
        return f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}'

print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))


# def send_mail(message, recipient, sender='university.help@gmail.com'):
#     valid_domains = ('.com', '.ru', '.net')
#
#     def is_valid_email(email):
#         return '@' in email and str(email).endswith(valid_domains)
#
#     if not is_valid_email(sender) or not is_valid_email(recipient):
#         print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
#
#     if recipient == sender:
#         print('Нельзя отправить письмо самому себе!')

