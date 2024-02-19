from transformers import AutoTokenizer

assistant_content = ("Continue your answer, based on the previous answers that I will now provide you, "
                     "you need to continue the answer strictly on the topic that is given in the previous answers.")

system_content = "You are a friendly assistant who talks about the sights of the world, countries and cities."


max_tokens_in_task = 100


def count_tokens(text):
    tokenizer = AutoTokenizer.from_pretrained("rhysjones/phi-2-orange")
    return len(tokenizer.encode(text))

