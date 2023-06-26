from npaa import *


def repl(key: str, role: str):
    """
    Call this function to start a REPL environment.
    The role is the user ID used for the AI to indentify user.
    In production, multiple roles will be used, to handle different user inputs.
    However, since this function is for debugging purposes only, the only way to change the role inside
    the REPL environment is through a debugger.

    :param key: the OpenAI key
    :param role: the initial role of the user
    :return:
    """
    na = NPAA(key=key, temperature=1)
    while True:
        user_input = input(">> ")
        user_input = str({'role': role, 'message': user_input})
        response = na.request(user_input)
        if response:
            print(response.message.content)
        else:
            print(response.status)
            print(response.raw_response)
