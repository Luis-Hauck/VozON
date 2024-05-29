# Documentação para o código VozON

## Introdução
O VozON é um programa que utiliza a API Generative AI do Google para gerar respostas de voz a partir de entradas de fala do usuário. Ele também inclui funcionalidades para reconhecimento de fala e síntese de voz.

## Configuração
Antes de usar o VozON, você precisa configurar algumas coisas:

1. **Chave da API Generative AI do Google:**
   - Você deve obter uma chave de API válida para acessar a API Generative AI do Google.
   - Substitua `'SUA_CHAVE_AQUI'` pela sua chave no código.

2. **Configurações do modelo Gemini 1.0 Pro:**
   - O VozON utiliza o modelo Gemini 1.0 Pro para gerar respostas.
   - Você pode ajustar as configurações de geração, como o número de candidatos e a temperatura.

3. **Instalação das seguintes bibliotecas:**
   - `google.generativeai` Para usar a Gemini.
   - `speech_recognition` para reconhecer a fala do usuário.
   - `pyttsx3` para sintetizar a resposta gerada.
## Funcionalidades principais
O VozON oferece as seguintes funcionalidades:

1. **Geração de respostas:**
   - O usuário fornece uma entrada de fala.
   - O VozON envia essa entrada para o modelo Gemini 1.0 Pro.
   - O modelo gera uma resposta de voz.
   - A resposta é sintetizada e reproduzida para o usuário.

2. **Reconhecimento de fala:**
   - O VozON utiliza a biblioteca `speech_recognition` para reconhecer a fala do usuário.
   - O usuário pode falar sobre qualquer tópico.
   - O VozON tenta reconhecer a fala do usuário e gera uma resposta.

3. **Síntese de voz:**
   - O VozON utiliza a biblioteca `pyttsx3` para sintetizar a resposta gerada.
   - A voz do robô pode ser configurada para diferentes vozes disponíveis no sistema.

## Como usar
1. Execute o código.
2. O VozON dará as boas-vindas e pedirá ao usuário para falar sobre o que deseja conversar.
3. O usuário pode falar livremente.
4. O VozON reconhecerá a fala do usuário, gerará uma resposta e a reproduzirá.
5. O usuário pode continuar a conversa ou dizer "FIM" para encerrar.

## Encerramento
Obrigado por usar o VozON! Se você tiver mais perguntas ou precisar de assistência, basta falar.
