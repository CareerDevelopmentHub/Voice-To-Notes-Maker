import speech_recognition as sr

# Initialize an empty list to store notes
notes = []

# Functions
def takeNotes():
    '''It takes microphone input from the user and appends it to the notes list'''

    global notes
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            note = recognizer.recognize_google(audio, language="en-in")
            notes.append(note)  # Append the note to the list
            print("Note written!")  # Print "Note written" after each note is recognized
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

def writeNotesToFile():
    '''Writing the notes to a text file'''

    global notes
    if notes:
        with open("notes.txt", "a+") as file:
            for note in notes:
                file.write(note + "\n")
        print("All notes saved to file.")

if __name__ == '__main__':
    while True:
        takeNotes()
        ask = input("Do you want to take more notes? (y/N): ")
        if ask.lower() != "y":
            writeNotesToFile()
            print("Thanks for using us!")
            break

    ask = input("Do you want to view the notes? (y/N): ")
    if ask.lower() == "y":
        # Read and display notes from the file
        with open("notes.txt", "r") as file:
            print("Your Notes:")
            for line in file:
                print(line.strip())  # Strip newline characters and print each note
