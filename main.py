import openai

openai.api_key = "SUA_CHAVE_DE_API_AQUI"

def traduzir_texto(texto, idioma_alvo):
	resposta = openai.Completion.create(
    	engine="text-davinci-002", 
        prompt=f"Traduza o seguinte texto para {idioma_alvo}: {texto}\n", 
        max_tokens=60, 
        n=1, 
        stop=None, 
        temperature=0.7, 
	) 
	return resposta.choices[0].text.strip()

texto = "Olá, mundo!"
idioma_alvo = "es" # Espanhol
traducao = traduzir_texto(texto, idioma_alvo)
print(traducao) # ¡Hola mundo!
