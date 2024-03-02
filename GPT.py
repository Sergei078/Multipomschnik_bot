import requests
import logging
from ERROR import error_gpt, error
from config import SERVER
from System_setting_gpt import assistant_content


class Question_gpt2:
    def __init__(self):
        self.temperature = 1.2
        self.max_tokens = 60
        self.server = SERVER

    def promt(self, result1, system_content):
        try:
            resp = requests.post(
                self.server,
                headers={"Content-Type": "application/json"},
                json={
                    "messages": [
                        {"role": "system", "content": f'{system_content}'},
                        {"role": "user", "content": f'{result1.text}'},
                    ],
                    "temperature": self.temperature,
                    "max_tokens": self.max_tokens
                }
            )
            data = resp.json()
            error_gpt(resp, data)
            answer = data['choices'][0]['message']['content']
            return answer

        except Exception as e:
            error_gpt1 = error
            logging.error(str(e))
            return error_gpt1


class Continue_text_gpt:
    def __init__(self):
        self.temperature = 1.2
        self.max_tokens = 60
        self.server = SERVER
        self.assistant = assistant_content

    def gpt(self, promt1, system_content):
        try:
            resp = requests.post(
                    self.server,
                    headers={"Content-Type": "application/json"},
                    json={
                        "messages": [
                            {"role": "system", "content": f'{system_content}'},
                            {"role": "assistant", "content": f'{self.assistant} {promt1}'},
                        ],
                        "temperature": self.temperature,
                        "max_tokens": self.max_tokens
                    }
                )
            data = resp.json()
            error_gpt(resp, data)
            continuation = data['choices'][0]['message']['content']
            return continuation

        except Exception as e:
            error1 = error
            logging.error(str(e))
            return error1