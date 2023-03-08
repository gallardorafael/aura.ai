from aura.hear import AudioRecorder

# TODO: move this, should not be global
recorder = AudioRecorder()

def start_recording():
    print("Starting...")
    print(f"Working with event {recorder.event_uuid}.")
    recorder.start()

def stop_recording():
    print("Stopping...")
    print(f"Saving records from event {recorder.event_uuid}, in folder: {recorder.root_path}.")
    recorder.stop()
    recorder.join()

def main():
    while True:
        user_input = input("Enter a command (start/stop/q): ")
        if user_input == "start":
            if not recorder.is_alive():
                start_recording()
        elif user_input == "stop":
            if recorder.is_alive():
                stop_recording()
        elif user_input == "q":
            if recorder.is_alive():
                stop_recording()
            exit()
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()