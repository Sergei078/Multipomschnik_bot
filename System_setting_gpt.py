from transformers import AutoTokenizer
from config import MODEL

assistant_content = ("Continue your answer, based on the previous answers that I will now provide you, "
                     "you need to continue the answer strictly on the topic that is given in the previous answers.")


max_tokens_in_task = 300


def count_tokens(text):
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    return len(tokenizer.encode(text))


def system(sub, lev):
    system_content = (f"You are a teacher in the subject: {sub}, you need to explain the "
                      f"questions that the user will ask as informatively as possible, the "
                      f"user has a certain level of knowledge: {lev}")
    return system_content

