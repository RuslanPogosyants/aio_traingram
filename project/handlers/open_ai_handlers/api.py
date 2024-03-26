from project.config import gigachat_token
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

chat = GigaChat(credentials=gigachat_token, verify_ssl_certs=False)


def request_answer(promt: str) -> str:
    role = [SystemMessage(content='Ты эксперт в таких областях как ЛФК, здоровое питание, физические упражнения. Ты помощник-тренер, отвечай только на вопросы по этим темам.')]
    messages = role
    messages.append(HumanMessage(content=promt))
    result = chat(messages)
    return result.content


if __name__ == "__main__":
    print(request_answer("Что такое протеин?"))
