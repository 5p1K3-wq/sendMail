import smtplib
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

email_from = os.getenv("EMAIL_FROM")
email_from_login = os.getenv("EMAIL_FROM_LOGIN")
email_from_pass = os.getenv("EMAIL_FROM_PASS")
email_to = os.getenv("EMAIL_TO")
text_email = """
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""

text_email = text_email.replace('%website%', 'https://dvmn.org')
text_email = text_email.replace('%friend_name%', 'Егор')
text_email = text_email.replace('%my_name%', 'Константин')

message = 'From: {0}\nTo: {1}\nSubject: Invite\nContent-Type: text/plain; charset="UTF-8";\n\n\n{2}'.format(
    email_from, email_to, text_email).encode("UTF-8")

# send mail
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(email_from_login, email_from_pass)
server.sendmail(email_from, email_to, message)
server.quit()
