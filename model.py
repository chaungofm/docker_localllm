from transformers import pipeline

qa_model = pipeline("question-answering", "deepset/roberta-base-squad2")
# question = "Where do I live?"
# context = "My name is Tim and I live in Sweden."

def question_anwser(question: str, context: str):
    return qa_model(question = question, context = context)

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summary_pipline(ARTICLE: str):
    return summarizer(ARTICLE, max_length=500, min_length=100)