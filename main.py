import openai
openai.api_key = "key"

def get_completion(prompt,model="gpt-3.5-turbo"):
    messages = [{"role":"user","content":prompt}]
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0
    )
    return response.choices[0].message["content"]

text = """Das Content Life Cyrcle beschreibt die Phasen, die der Content durchläuft (vgl. Spörrer, 2009, S. 45). Diese Phasen sind: Erstellung, Kontrolle und Freigabe, Publikation und Archivierung. Bei der Erstellung wird der Inhalt in Form von Texten, Fotos und Videos erstellt. Dieser Content wird in der zweiten Phase auf Korrektheit geprüft und bei einem positiven Ergebnis wird der Inhalt freigegeben. Danach wird der Inhalt in den vorgesehenen Kanälen und Plattformen veröffentlicht. Die letzte Phase des Content Life Cyrcle beinhaltet die Versionierung, Backups, Wiederverwendung und Archivierung des Contents. """
prompt = f"""
vereinfache den text in {text}. Der Text soll für jemanden mit den Deutschkentnissen B1 verstänlich sein. Ergebnis auf Spanisch
"""
response = get_completion(prompt)
print(response)
