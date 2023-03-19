from aura.hear import AudioRecorder

# TODO: move this, should not be global
recorder = AudioRecorder()

def start_recording():
    print("Starting...")
    print(f"Working with event {recorder.event_uuid}.")
    recorder.start_recording()

def stop_recording():
    print("Stopping...")
    print(f"Saving records from event {recorder.event_uuid}, in folder: {recorder.root_path}.")
    recorder.stop_recording()

def main():
    while True:
        user_input = input("Enter a command (start/stop/q): ")
        if user_input == "start":
            if not recorder.recording:
                start_recording()
        elif user_input == "stop":
            if recorder.recording:
                stop_recording()
        elif user_input == "q":
            if recorder.recording:
                stop_recording()
            exit()
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()