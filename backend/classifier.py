import spacy

nlp = spacy.load("pt_core_news_sm")

def classify_feedback(message: str) -> str:
    # Define keywords for compliments and complaints
    compliments = ["ótimo", "excelente", "gostei", "bom", "maravilhoso", "parabéns", "incrível"]
    complaints = ["ruim", "horrível", "péssimo", "reclamação", "lento", "demorado", "problema", "erro"]

    lower_message = message.lower()

    # Check if the message contains any compliment or complaint keywords
    if any(word in lower_message for word in compliments):
        return "compliment"
    elif any(word in lower_message for word in complaints):
        return "complaint"
    else:
        return "neutral"
