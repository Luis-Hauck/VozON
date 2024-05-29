import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

# Sua chave da API Generative AI do Google
google_api_key = 'AIzaSyBt0yN_f8_XdGtsrYsY0qaHcqcF9AtZv5A'
# Configura a API Generative AI com sua chave
genai.configure(api_key=google_api_key)

generation_config = {
    'candidate_count': 1,
    'temperature': 0.5,
}

# Configurações para gerar texto com o modelo Gemini 1.0 Pro

model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                              generation_config=generation_config
                              )

# Carrega o modelo Gemini 1.0 Pro com as configurações definidas
chat = model.start_chat(history=[])

# Inicializa o mecanismo de sistese de voz.
motor_de_sistese_de_fala = pyttsx3.init()

# Obtém todas as vozes disponíveis no sistema
voices = motor_de_sistese_de_fala.getProperty('voices')

# Define a voz a ser usada pelo robô como a segunda voz
motor_de_sistese_de_fala.setProperty('voice', voices[0].id)


# Usa o motor de síntese de fala para falar
def falar(frase):
    motor_de_sistese_de_fala.say(frase)
    motor_de_sistese_de_fala.runAndWait()
    motor_de_sistese_de_fala.stop()


# Remove os caracteres especiais do texto gerado
def remover_caracteres_especiais(texto):
    texto_sem_asteriscos = ""
    for caractere in texto:
        if caractere not in "*!@$%&''-+.*/=+-_":
            texto_sem_asteriscos += caractere
    return texto_sem_asteriscos


# Define uma função para reconhecer a fala do usuário.
def reconhecer_fala():
    # Inicializa o reconhecedor de fala.
    microfone = sr.Recognizer()

    # Configura o microfone como fonte de áudio.
    with sr.Microphone() as source:
        # Ajusta o reconhecimento para o ruído ambiente.
        microfone.adjust_for_ambient_noise(source)

        # Fala uma mensagem para o usuário.
        falar('Sobre o que você quer conversar? ')

        # Escuta o áudio do microfone.
        audio = microfone.listen(source)

        # Tenta reconhecer a fala 5 vezes.

        for _ in range(5):
            try:
                # Reconhece a fala do usuário usando o Google Speech Recognition.
                frase_reconhecida = microfone.recognize_google(audio, language='pt')

                # Fala a frase reconhecida ao usuário.
                falar('Você disse: '), falar(frase_reconhecida)

                # Retorna a frase reconhecida.

                return frase_reconhecida

            except sr.UnknownValueError:
                falar('Não entendi o que você disse, vou encerrar a conversa.')
                break
            except sr.RequestError as e:
                falar(f'Ocorreu um erro ao reconhecer a fala: {e}')
                break

    return None


# Saudação inicial
falar('Seja bem vindo ao VozON')
falar('Para encerrar a conversa diga FIM')


# Loop principal da conversa
def iniciar_conversa():
    prompt = reconhecer_fala()
    while prompt != 'fim':
        # Envia a fala do usuário para o modelo gerar uma resposta
        response = chat.send_message(prompt)
        # Remove caracteres especiais da resposta do modelo (opcional)
        falar(remover_caracteres_especiais(response.text))
        # Obtém a próxima fala do usuário
        prompt = reconhecer_fala()
    falar('Você encerrou a conversa')


iniciar_conversa()