import requests
import logging
from System_setting_gpt import assistant_content, system_content

SERVER = input('Введи сервер:')


class Continue_text_gpt:
    def gpt(self, promt1):
        try:
            resp = requests.post(
                    SERVER,
                    headers={"Content-Type": "application/json"},
                    json={
                        "messages": [
                            {"role": "system", "content": system_content},
                            {"role": "assistant", "content": f'{assistant_content} {promt1}'},
                        ],
                        "temperature": 1,
                        "max_tokens": 50
                    }
                )
            data = resp.json()
            if resp.status_code < 200 or resp.status_code >= 300:
                error = 'Произошла ошибка'
                logging.error(str(resp.status_code))
                return error
            if 'error' in data:
                error1 = 'Произошла ошибка на стороне сервера.'
                logging.error(str(f'{data["error"]}'))
                return error1
            else:
                n = data['choices'][0]['message']['content']
                return n

        except Exception as e:
            error_gpt = 'Произошла неизвестная ошибка!'
            logging.error(str(e))
            return error_gpt


class Question_gpt2:
    def promt(self, result1):
        try:
            resp = requests.post(
                SERVER,

                headers={"Content-Type": "application/json"},

                json={
                    "messages": [
                        {"role": "system", "content": system_content},
                        {"role": "user", "content": f'{result1.text}'},
                    ],
                    "temperature": 1,
                    "max_tokens": 50
                }
            )
            data = resp.json()
            print(data)
            if resp.status_code < 200 or resp.status_code >= 300:
                error = 'Произошла ошибка'
                logging.error(str(resp.status_code))
                return error
            if 'error' in data:
                error1 = 'Произошла ошибка на стороне сервера.'
                logging.error(str(f'{data["error"]}'))
                return error1
            else:
                n = data['choices'][0]['message']['content']
                return n
        except Exception as e:
            error_gpt1 = 'Произошла неизвестная ошибка!'
            logging.error(str(e))
            return error_gpt1