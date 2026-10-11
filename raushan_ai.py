
import speech_recognition as sr
import pyttsx3
import webbrowser

engine = pyttsx3.init()
recognizer = sr.Recognizer()


def speak(text):
    print("ROSHAN AI:", text)
    engine.say(text)
    engine.runAndWait()


def main():
    speak("Hello Roshan! I am ready for voice commands.")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening... Speak now!")
                recognizer.adjust_for_ambient_noise(
                    source, duration=0.5
                )
                audio = recognizer.listen(
                    source, timeout=7, phrase_time_limit=8
                )

            command = recognizer.recognize_google(
                audio, language="hi-IN"
            ).lower()

            print("You said:", command)

            if any(word in command for word in [
                "बंद करो", "बंद हो जाओ", "exit", "goodbye"
            ]):
                speak("Goodbye Roshan!")
                break

            elif "youtube" in command or "यूट्यूब" in command:
                webbrowser.open("https://www.youtube.com")
                speak("Opening YouTube.")

            elif "google" in command or "गूगल" in command:
                webbrowser.open("https://www.google.com")
                speak("Opening Google.")

            else:
                speak("Sorry Roshan, please try another command.")

        except sr.WaitTimeoutError:
            print("No voice detected. Try again.")
        except sr.UnknownValueError:
            speak("I could not understand. Please repeat.")
        except sr.RequestError:
            speak("Please check your internet connection.")
        except OSError as error:
            speak("Microphone error. Check your microphone.")
            print(error)
            break


if __name__ == "__main__":
    main()
