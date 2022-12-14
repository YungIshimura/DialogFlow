# Telegram и VK бот для службы поддержки

Чат боты для службы поддержки с использованием ```DialogFlow```. 

## Как установить?
Во-первых, вам необходимо скачать этот репозиторий. Для этого нажмите зелёную кнопку Code в правом верхнем углу и выберите удобный для вас метод скачивания.
![Скачивание репозитория](https://user-images.githubusercontent.com/83189636/209101669-cb4135c6-73b9-4b69-9a52-e953452f550a.gif)
Во-вторых, создайте .env файл в папке проекта, в него нужно записать следующее:
**TG_BOT_API_KEY**. Далее необходимо создать телеграм бота в [BotFather](https://telegram.me/BotFather) и получать API-ключ бота. Для этого папаше ботов нужно прописать команду ```/newbot ``` и придумать боту название и логин, заканчивающийся на bot. Записать его в ```.env``` аналогичным образом.
```python
TG_BOT_API_KEY = 'Ваш API-ключ'
```

**TG_CHAT_ID**. Для получения вашего chat id нужно перейти [@userinfobot](https://telegram.me/userinfobot), достаточно просто запустить его и он отправит вам всё необходимое. Его нужно также записать в ```.env``` файл.
```python
TG_CHAT_ID = 'Ваш chat id '
```
**VK_API_KEY**. Создайте группу в [VK](https://vk.com/groups?tab=admin) и перейдите к настройкам сообщества (раздел ```управлениe```). Далее выберите раздел *Работа с API* и создайте ключ. Его нужно записать в ```.env``` файл.`
```python
VK_API_KEY = 'Ваш API-ключ'
```
**GOOGLE_CLOUD_PROJECT_ID**. Также вам необходимо создать проект в [DialogFlow](https://cloud.google.com/dialogflow/es/docs/quick/setup) и [Агента](https://cloud.google.com/dialogflow/es/docs/quick/build-agent). В настройках проекта будет ```Project ID```, как раз его и нужно записать в ```.env``` файл.
```python
GOOGLE_CLOUD_PROJECT_ID = 'Ваш project id'
```
**GOOGLE_APPLICATION_CREDENTIALS** получите JSON файл с ключем доступа по [инструкции](https://cloud.google.com/docs/authentication/getting-started).
```python
GOOGLE_APPLICATION_CREDENTIALS = 'Путь до .env-файла'
```

В проекте используется пакет [environs](https://pypi.org/project/environs/). Он позволяет загружать переменные окружения из файла ```.env``` в корневом каталоге приложения.
Этот ```.env``` файл можно использовать для всех переменных конфигурации.
Ну и естественно Python3 должен быть уже установлен. Затем используйте pip (или pip3,если есть конфликт с Python2) для установки зависимостей:
```python
pip install -r requirements.txt
```

## Как пользоваться 

Достаточно просто запустить необходимый скрипт при помощи команд:

**Telegram**
```bash 
python3 dialogflow_tg_bot.py
```
и запустить бота, отправив ему команду ```/start``` или нажать на кнопку ```start``` при первом запуске. Когда преподаватель проверит работу, то вам бот отправит вам уведомление о том принял ли он работу, или же нет.

**VK**
```bash 
python3 dialogflow_vk_bot.py
```
и отправить сообщение в группу.

## Пример работы

**Telegram**

![2](https://user-images.githubusercontent.com/83189636/209107248-9f100227-daaa-4ec2-93b3-85c9b2b12c3c.gif)


**VK**

![3](https://user-images.githubusercontent.com/83189636/209107290-2a224237-8ee7-4cfd-a00f-3e070372580f.gif)


## Тренировка бота
Для тренировки бота запустите файл ```bot_trainer.py```, указав путь к JSON файлу. Пример данных для тренировки:
```JSON
{
  "Устройство на работу": {
    "questions": [
      "Как устроиться к вам на работу?",
      "Как устроиться к вам?",
      "Как работать у вас?",
      "Хочу работать у вас",
      "Возможно-ли устроиться к вам?",
      "Можно-ли мне поработать у вас?",
      "Хочу работать редактором у вас"
    ],
    "answer": "Если вы хотите устроиться к нам, напишите на почту game-of-verbs@gmail.com мини-эссе о себе и прикрепите ваше портфолио."
  }
}
```
