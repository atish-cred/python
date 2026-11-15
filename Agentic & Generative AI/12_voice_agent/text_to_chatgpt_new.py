
from openai import OpenAI, AsyncOpenAI
from dotenv import load_dotenv
from openai.helpers import LocalAudioPlayer

import speech_recognition as sr
import asyncio


load_dotenv()

client = OpenAI()


# Text to Speech
async def tts(async_client: AsyncOpenAI, speech: str):

    async with async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input=speech,
        instructions="Always speak in a cheerful manner, full of delight and happiness.",
        response_format="pcm"
    ) as response:

        await LocalAudioPlayer().play(response)


# Speech to Text
def stt(recognizer, source):

    print("\nSpeak something...")

    try:
        audio = recognizer.listen(source)

        print("Processing Audio... (STT)")

        text = recognizer.recognize_google(audio)

        print("You said:", text)

        return text

    except sr.UnknownValueError:
        print("Sorry, I could not understand your voice.")
        return None

    except sr.RequestError as e:
        print("Speech recognition error:", e)
        return None


# ChatGPT
def chat(user_input, messages):

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    ai_response = response.choices[0].message.content

    # Important: Save assistant response in conversation history
    messages.append({
        "role": "assistant",
        "content": ai_response
    })

    print("\nAI Response:", ai_response)

    return ai_response


# Main asynchronous function
async def main():

    recognizer = sr.Recognizer()

    recognizer.pause_threshold = 2

    SYSTEM_PROMPT = """
    You are an expert voice agent.

    You are given the transcript of what the user has said using voice.

    Respond naturally and conversationally, as if you are
    speaking directly to the user.

    Keep responses clear and suitable for voice output.
    """

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    # Create one async client for the entire application
    async with AsyncOpenAI() as async_client:

        with sr.Microphone() as source:

            print("Calibrating microphone...")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            print("Voice agent is ready!")

            try:

                while True:

                    user_input = stt(recognizer, source)

                    if not user_input:
                        continue

                    if user_input.lower().strip() in ["exit", "quit", "stop"]:
                        print("Voice agent stopped.")
                        break

                    # Get response from ChatGPT
                    response = chat(user_input, messages)

                    # Convert response to speech
                    await tts(async_client, response)

            except KeyboardInterrupt:
                print("\nVoice agent stopped.")


if __name__ == "__main__":
    asyncio.run(main())
