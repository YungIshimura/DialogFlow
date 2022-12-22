import random
import logging

from environs import Env

from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api as vk
from dialogflow_tools import detect_intent


logger = logging.getLogger('dialog_bot_logger')


def get_answer(event, vk_api, project_id):
    answer = detect_intent(
        project_id=project_id,
        session_id=event.user_id,
        text=event.text
    )
    if not answer.query_result.intent.is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer.query_result.fulfillment_text,
            random_id=random.randint(1, 1000)
        )


def main():
    env = Env()
    env.read_env()

    vk_api_key = env('VK_API_KEY')
    gcloud_project_id = env('GOOGLE_CLOUD_PROJECT_ID')

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    try:
        vk_session = vk.VkApi(token=vk_api_key)
        longpoll = VkLongPoll(vk_session)
        vk_api = vk_session.get_api()
        logger.info("Диалоговый VK бот запущен!")

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                get_answer(event, vk_api, gcloud_project_id)
    except Exception as err:
        logger.exception('VK бот упал с ошибкой', exc_info=err)


if __name__ == '__main__':
    main()
