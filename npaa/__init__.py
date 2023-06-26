import requests
from requests.exceptions import JSONDecodeError

from npaa import prompt


class Message:
    def __init__(self, role: str, content: str):
        """
        The message of conversation between user and AI.

        :param role: who sent the message, can only be 'user', 'assistant', or 'system'
        :param content: the content of the message, string
        """
        self.role = role
        self.content = content

    def __str__(self):
        return f'{{"role": "{self.role}", "content": "{self.content}"}}'

    def to_dic(self):
        return {"role": self.role, "content": self.content}


class Response:
    def __init__(self, message: None | Message, data: None | dict, status: int, raw_response: requests.Response):
        """
        The response from NPAA.request.

        :param message: the response from the AI model
        :param data: the response from OpenAI
        :param status: the status code of the request
        :param raw_response: the overall response
        """
        self.message = message
        self.data = data
        self.status = status
        self.raw_response = raw_response


class NPAA:

    def __init__(self, key: str, model: str = 'gpt-3.5-turbo', temperature: float = 0.7):
        """
        Create a new NPAA (NeedPedia Ai Assistant) object.
        Used to handle message transfers.

        :param key: the OpenAI Key
        :param model: the model to use
        :param temperature: the temperature of the model
        """
        self.key = key
        self.messages: list[Message] = [Message(content=prompt.prompt, role='system')]
        self.model = model
        self.temperature = temperature

    def request(self, new_message: str, role='user') -> Response:
        """
        To make a request and get response.

        :param new_message: the message to be sent
        :param role: the role of the message sender (user, assistant, system)
        :return: a Response object
        """

        new_message = Message(role=role, content=new_message)
        send_message = Message(role=new_message.role, content=new_message.content + prompt.reminder)

        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}"
        }
        data = {
            "model": self.model,
            "messages": [each.to_dic() for each in self.messages] + [send_message.to_dic()],
            "temperature": self.temperature
        }
        response = requests.post(url=url, headers=headers, json=data)

        try:
            response_json = response.json()
        except JSONDecodeError:
            response_json = None

        response_message = None

        if response.status_code == 200:
            self.messages.append(new_message)
            self.messages.append(Message(content=response_json['choices'][0]['message']['content'],
                                         role=response_json['choices'][0]['message']['role']))
            response_message = self.messages[-1]

        return Response(message=response_message, data=response_json, status=response.status_code, raw_response=response)
