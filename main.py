from openai import OpenAI
from dotenv import load_dotenv
import os

from database import create_db, get_column_names, execute_sql_query

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
            temperature=0.1,
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

def ask_request():
    return input("Quelle est la requête que vous souhaitez effectuer ?\n")

def remove_carriage_return(string):
    return string.replace('\n', ' ')


def main():
    load_dotenv()
    temp_db = create_db()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    intro = "Tu es le chatbot de la base de données de l'équipe. Tu dois convertir les requêtes en langage naturel en requête SQL. Tu répondras uniquement sous forme de code avce la requête demandée. Utilise la table cars suivante qui ne contient pas d'index"
    natural_query = ask_request()
    prompt = intro + get_column_names(temp_db) + natural_query
    sql_query = generate_sql_query(client, prompt)
    print("\nRequête SQL générée :\n", sql_query)
    if input("\nSouhaitez-vous l'exécuter ?\n") == 'oui':
        print("\nRésultat de la requête :\n", execute_sql_query(temp_db, remove_carriage_return(sql_query)))

if __name__ == "__main__":
    main()

# Requêtes à effectuer :

#   Quelle est la moyenne des prix des voitures dans la base de données ?
#   SELECT AVG(price) FROM data

#   Quelle est la médiane des prix parmi les 35 derniers modèles de voiture sortis ?
#   WITH RankedCars AS (SELECT price, ROW_NUMBER() OVER (ORDER BY year DESC, model DESC) as rn FROM cars LIMIT 35) SELECT price FROM RankedCars WHERE rn = (35 + 1) / 2;