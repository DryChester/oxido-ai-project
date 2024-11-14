
# TXT to HTML generator with AI

[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)
[![GitHub](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)

Niewielkie narzędzie generujące stronę HTML z wybranego pliku tekstowego. Stworzone w Pythonie. Używa modelu GPT-4. Wygenerowany plik może być wstawiony bezpośrednio do sekcji `<body>`

# Instalacja

### 1. Klonowanie repozytorium

Można to zrobić bezpośrednio na stronie repozytorium lub użyć komendy:

```shell
git clone https://github.com/DryChester/oxido-ai-project
```

### 2. Ustawienie klucza API OpenAI jako zmiennej środowiskowej

Można to zrobić na **dwa** sposoby:

1) Wpisać w terminalu komendę:

>Linux/Mac:
```shell 
export OPENAI_API_KEY='Twój_Klucz_API'
```
>Windows:
```shell 
setx OPENAI_API_KEY 'Twój_Klucz_API'
```

2) Stworzyć w skopiowanym repozytorium plik .env i umieścić tam następujący kod:

```shell
OPENAI_API_KEY='Twój_Klucz_API'
```
W miejscu 'Twój_Klucz_API' wklejasz swój prywatny klucz OpenAI API. 

### 3. Zainstaluj bibliotekę OpenAI w Pythonie
Jeżeli nie masz zainstalowanej biblioteki OpenAI (można to sprawdzić wpisując w Terminalu:)
```shell
openai --version
```  
to zainstalujesz ją w następujący sposób:
```python
pip install openai
```
### 4. Uruchom skrypt
Do uruchomienia skryptu wystarczy wpisanie komendy w Terminalu:
```python
python main.py
```
Po dłuższej chwili, powinien pojawić się następujący komunikat:
>HTML article generated and saved to artykuł.html



# Dodatkowe informacje

Skrypt można edytować do swoich potrzeb. 

1) Aby zmienić tekst znajdujący się w pliku `article.txt` wystarczy otworzyć go w dowolnym edytorze tekstowym. Można zmienić też jego nazwę, lecz należy wówczas dokonać odpowiednich edycji w kodzie:
```python
#funkcja 'main'
def main():

    file_content = read_file("article.txt") #tu zmieniasz nazwę pliku
```
2) W podobny sposób można edytować kod, tak, by stworzył plik .html o innej nazwie:
```python
    output_file = "artykuł.html" #tutaj również nazwa może zostać zmieniona, jednak rozszerzenie musi pozostać takie samo
    write_to_html(output_file, generated_content)
    print(f"HTML article generated and saved to {output_file}")
```


# Licencja
[MIT license](./LICENSE)


