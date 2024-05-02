def generate_html(name):
    # HTML-Code für die Animation
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Happy Birthday</title>
        <style>
            body {{
                background-color: #ff4500;
                text-align: center;
            }}
            h1 {{
                color: #ff4500;
            }}
            #cake {{
                width: 300px;
                margin: 50px auto;
            }}
        </style>
    </head>
    <body>
        <h1>Happy Birthday, {name}!</h1>
        <img id="cake" src="Birthdaycake.jpeg" alt="Birthday Cake">
        <p>HIER NOCHMAL IN NERD LANGUAGE; ALLES GUTE ZUM BDAY!</p>
    </body>
    </html>
    """

    # HTML-Datei erstellen und öffnen
    with open("happy_birthday.html", "w") as file:
        file.write(html_content)

    print("Happy Birthday HTML-Datei wurde erstellt und geöffnet.")

if __name__ == "__main__":
    name = input("Gib den Namen ein: ")
    generate_html(name)