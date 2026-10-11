
import webbrowser
import datetime
import urllib.parse
import subprocess
import platform

ASSISTANT_NAME = "ROSHAN AI"
OWNER_NAME = "Roshan"


def speak(message):
    """Display the assistant's message."""
    print(f"\n{ASSISTANT_NAME}: {message}")


def open_youtube():
    webbrowser.open("https://www.youtube.com")
    speak("Opening YouTube for you, Roshan!")


def play_song():
    song = input("Enter the song name: ").strip()

    if song:
        query = urllib.parse.quote_plus(song)
        url = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(url)
        speak(f"Searching YouTube for {song}!")


def open_google():
    webbrowser.open("https://www.google.com")
    speak("Google is opening!")


def tell_time():
    now = datetime.datetime.now()
    speak("The current time is " + now.strftime("%I:%M %p"))


def tell_date():
    today = datetime.datetime.now()
    speak("Today's date is " + today.strftime("%d %B %Y"))


def open_calculator():
    try:
        if platform.system() == "Windows":
            subprocess.Popen(["calc.exe"])
            speak("Calculator opened!")
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", "-a", "Calculator"])
            speak("Calculator opened!")
        else:
            subprocess.Popen(["gnome-calculator"])
            speak("Calculator opened!")
    except (FileNotFoundError, OSError):
        speak("Sorry, I could not open the calculator.")


def process_command(command):
    command = command.lower().strip()

    if not command:
        speak("Please type a command.")
        return True

    if command in ["exit", "quit", "bye", "stop"]:
        speak("Goodbye Roshan! See you again.")
        return False

    elif any(word in command for word in [
        "hello", "hi", "hey", "namaste", "नमस्ते"
    ]):
        speak("Hello Roshan! How can I help you today?")

    elif "who are you" in command:
        speak("I am ROSHAN AI, your personal assistant.")

    elif "youtube" in command:
        if any(word in command for word in [
            "song", "music", "play", "गाना"
        ]):
            play_song()
        else:
            open_youtube()

    elif any(word in command for word in [
        "play song", "play music", "गाना चलाओ", "गाना बजाओ"
    ]):
        play_song()

    elif "google" in command:
        open_google()

    elif "time" in command or "समय" in command:
        tell_time()

    elif "date" in command or "तारीख" in command:
        tell_date()

    elif "calculator" in command or "कैलकुलेटर" in command:
        open_calculator()

    elif any(word in command for word in [
        "how are you", "कैसे हो"
    ]):
        speak("I am working perfectly, Roshan!")

    elif "help" in command:
        speak(
            "Try: hello, open YouTube, play song, "
            "open Google, time, date, calculator, or exit."
        )

    else:
        speak(
            "I don't know that command yet. "
            "Type help to see what I can do."
        )

    return True


def main():
    print("=" * 42)
    print("       WELCOME TO ROSHAN AI")
    print("       Your Personal Assistant")
    print("=" * 42)

    speak(f"Hello {OWNER_NAME}! I am ready to help you.")
    speak("Type 'help' to see available commands.")

    running = True

    while running:
        try:
            command = input("\nYou: ")
            running = process_command(command)
        except (KeyboardInterrupt, EOFError):
            print()
            speak("Goodbye Roshan!")
            break


if __name__ == "__main__":
    main()
