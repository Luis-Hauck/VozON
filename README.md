# Introdução

Este script Python utiliza a API Generative AI do Google para criar um chatbot que interage com o usuário por meio de voz. O chatbot reconhece a fala do usuário usando a biblioteca Speech Recognition e responde com texto gerado pelo modelo Gemini 1.0 Pro. A fala do chatbot é sintetizada pela biblioteca Pyttsx3.

## Funcionalidades

- **Interação por voz:** O chatbot pode ser controlado por comandos de voz.
- **Geração de texto:** O chatbot utiliza o modelo Gemini 1.0 Pro para gerar respostas relevantes e interessantes às perguntas do usuário.
- **Síntese de voz:** O chatbot pode falar suas respostas usando a biblioteca Pyttsx3.

## Implementação

O script Python está dividido em três partes principais:

1. **Importação de bibliotecas:** As bibliotecas `google.generativeai`, `speech_recognition` e `pyttsx3` são importadas para realizar as funcionalidades do chatbot.
2. **Configuração da API Generative AI:** A chave da API do Google é definida e a configuração do modelo Gemini 1.0 Pro é especificada.
3. **Loop principal:**
   - A função `iniciar_conversa` é chamada para inicializar o chatbot.
   - Um loop infinito é executado enquanto a frase do usuário não for "FIM".
   - A função `reconhecer_fala` é usada para capturar a fala do usuário.
   - A frase reconhecida é enviada para o chatbot usando a função `enviar_mensagem`.
   - A resposta do chatbot é recebida e a função `remover_caracteres_especiais` é usada para remover caracteres especiais.
   - A resposta do chatbot é falada para o usuário usando a função `falar`.
   - A próxima frase do usuário é capturada.
   - A função `encerrar_conversa` é chamada para finalizar o chatbot.

## Funções

- `iniciar_conversa()`: Inicializa o chatbot, configurando o modelo e o motor de síntese de voz.
- `reconhecer_fala()`: Captura a fala do usuário usando o Speech Recognition e retorna a frase reconhecida.
- `enviar_mensagem(frase)`: Envia a frase para o chatbot e retorna a resposta.
- `remover_caracteres_especiais(texto)`: Remove caracteres especiais do texto.
- `falar(frase)`: Sintetiza a frase em voz alta usando o Pyttsx3.
- `encerrar_conversa()`: Finaliza o chatbot, liberando recursos.

## Exemplo de uso

Para usar o script, basta salvá-lo como um arquivo Python e executá-lo no terminal. O chatbot estará pronto para interagir com você por voz e texto.

**Observações:**

- Este script é apenas um exemplo e pode ser adaptado para atender às suas necessidades específicas.
- Certifique-se de ter as bibliotecas `google.generativeai`, `speech_recognition` e `pyttsx3` instaladas em seu sistema.
- A chave da API do Google é necessária para usar a API Generative AI. Você pode obter uma chave gratuita em https://aistudio.google.com/
