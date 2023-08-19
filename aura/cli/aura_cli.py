from aura.brain.hear import SoundcardAudioRecorder as Recorder


def start_recording(recorder):
    print("Starting...")
    print(f"Working with event {recorder.event_uuid}.")
    recorder.start_recording()


def stop_recording(recorder):
    print("Stopping...")
    print(f"Saving records from event {recorder.event_uuid}, in folder: {recorder.root_path}.")
    recorder.stop_recording()


def main():
    recorder = None
    while True:
        user_input = input("Enter a command (start/stop/q): ")
        if user_input == "start":
            if recorder is None:
                recorder = Recorder()
                start_recording(recorder)
            else:
                print("Aura is already recording.")
        elif user_input == "stop":
            if recorder is not None:
                if recorder.recording:
                    stop_recording(recorder)
                    recorder = None
            else:
                print("Aura is not recording.")
        elif user_input == "q":
            if recorder is not None:
                if recorder.recording:
                    stop_recording(recorder)
                    recorder = None
            exit()
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
