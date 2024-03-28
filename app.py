import openai

# Configuration de la clé
openai.api_key = 'key'

def obtenir_sites_touristiques(ville):
    
    prompt = f"Quels sont les sites touristiques à visiter à {ville} ?"
    response = openai.chat.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def main():
    print("Bienvenue dans le chatbot des sites touristiques !")
    while True:
        ville = input("Vous désirez visiter les sites touristiques de quelle ville ? (tapez 'exit' pour quitter) ")
        if ville.lower() == 'exit':
            print("Au revoir !")
            break
        else:
            try:
                sites_touristiques = obtenir_sites_touristiques(ville)
                print(f"Voici les sites touristiques à visiter à {ville}:")
                print(sites_touristiques)
            except Exception as e:
                print("Une erreur s'est produite lors de la récupération des sites touristiques.")
                print("Veuillez réessayer ou contacter l'administrateur.")
                print("Erreur:", str(e))

if __name__ == "__main__":
    main()


