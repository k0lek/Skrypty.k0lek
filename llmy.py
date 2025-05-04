from langchain_ollama import OllamaLLM

# Inicjalizacja modelu
llm = OllamaLLM(model="llama3.1:8b", temperature=0.7, max_tokens=150, top_p=0.95)

# Liczba odpowiedzi do wygenerowania
num_responses = 3

# Generowanie odpowiedzi w pętli
responses = []
for _ in range(num_responses):
    response = llm.invoke("Where is 'Smok Wawelski'?")
    responses.append(response)

# Wyświetlanie odpowiedzi
for idx, response in enumerate(responses):
    print(f"Response {idx + 1}: {response}")

