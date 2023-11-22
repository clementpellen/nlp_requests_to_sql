from openai import OpenAI
from dotenv import load_dotenv
import os

from database import get_column_names

def generate_sql_query(client, natural_language_query):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": natural_language_query,
                }
            ],
            model="gpt-3.5-turbo",
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

def main():
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    intro = "Tu es le chatbot de la base de données de l'équipe. Tu dois convertir les requêtes en langage naturel en requêtes SQL. Tu répondras uniquement sous forme de code avce la requête demandée."
    natural_query = "Quelle est le pays le plus représenté dans la base de données ?"
    prompt = intro + get_column_names() + natural_query
    sql_query = generate_sql_query(client, prompt)
    print(sql_query)

if __name__ == "__main__":
    main()

