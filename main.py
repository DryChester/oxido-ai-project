import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# ustawienie klucza API OpenAI
client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)
#funkcja odczytująca plik z artykułem
def read_file(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return content    

#funkcja generująca odpowiedź z pomocą ChatGPT
def generate_response(prompt, file_content):
    
    response = client.chat.completions.create(
        model="gpt-4",
        max_tokens=5000,
        temperature=0.6,
        messages=[
    {"role": "system", "content": prompt},
    {"role": "user", "content": file_content}
        ]
    )
    return response.choices[0].message.content

#funkcja zmieniająca odpowiedź w plik HTML
def write_to_html(output_path, content):

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)

#funkcja 'main'
def main():

    file_content = read_file("article.txt")

    prompt = "Przekształć poniższy artykuł na kod HTML do wstawienia pomiędzy tagami <body> i </body>,\n " \
        "stosując następujące wytyczne:\n" \
        "• Użyj odpowiednich tagów HTML (np. <h1>, <h2>, <p>) do strukturyzacji nagłówków i paragrafów." \
        "Nie dołączaj znaczników <html>, <head> ani <body>"\
        "• W miejscach, gdzie warto wstawić grafikę, dodaj tag <img> z atrybutem src='image_placeholder.jpg'" \
        "oraz opisowy atrybut alt, który będzie pełnił rolę promptu do wygenerowania grafiki.\n" \
        "• Dodaj podpisy pod obrazkami używając tagu <figcaption>, umieszczonego w kontenerze <figure>.\n" \
        "• Nie stosuj żadnego stylowania CSS ani JavaScript – tylko czysty HTML.\n\n"
    generated_content = generate_response(prompt, file_content)

    output_file = "artykuł.html"
    write_to_html(output_file, generated_content)
    print(f"HTML article generated and saved to {output_file}")

if __name__ == "__main__":
    main()