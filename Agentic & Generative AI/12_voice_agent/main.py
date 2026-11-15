
import speech_recognition as sr

def main():
    r = sr.Recognizer()  # Speech to text

    # Access microphone
    with sr.Microphone() as source: # Mic access --> Access the microphone of the user
        r.adjust_for_ambient_noise(source) # adjust the noice cancellation
        r.pause_threshold = 2 # when we need to recognization? when user pauses for 2 seconds then take it

        print("Speak something...")

        audio = r.listen(source)

        print("Processing Audio... (STT)")

        stt = r.recognize_google(audio)

        print("You said:", stt)


if __name__ == "__main__":
    main()
