import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

google_api_key = ''
genai.configure(api_key=google_api_key)

generation_config = {
    'candidate_count': 1,
    'temperature': 0.5,
}

safety_config = {
    'Harassment': 'BLOCK_SOME',
    'Hate': 'BLOCK_SOME',
    'Sexual': 'BLOCK_SOME',
}

model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                              generation_config=generation_config
                              )

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


def remover_asteriscos(texto):
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

        # Tenta reconhecer a fala três vezes.
        for _ in range(5):
            try:
                # Reconhece a fala do usuário usando o Google Speech Recognition.
                frase_reconhecida = microfone.recognize_google(audio, language='pt')

                # Fala a frase reconhecida ao usuário.
                falar('Você disse: '), falar(frase_reconhecida)

                # Retorna a frase reconhecida.

                return frase_reconhecida

            except sr.UnknownValueError:
                falar('Não entendi o que você disse.')
            except sr.RequestError as e:
                falar('Ocorreu um erro ao reconhecer a fala: {0}'.format(e))

    return None


falar('Seja bem vindo ao VozON')
falar('Para encerrar a conversa diga FIM')

prompt = reconhecer_fala()

while prompt != 'fim':
    response = chat.send_message(prompt)
    falar(remover_asteriscos(response.text))
    prompt = reconhecer_fala()

falar('Você encerrou a conversa')
