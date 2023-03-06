import argparse

from aura.hear import AudioRecorder

# TODO: move this, should not be global
recorder = AudioRecorder()

def start(args):
    print("Starting...")
    print(f"Working with event {recorder.event_uuid}, in folder: {recorder.root_path}")
    recorder.run()

def stop(args):
    print("Stopping...")
    recorder.stop()

def finish(args):
    print("Finishing...")
    exit()

def setup_argparser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # start command
    start_parser = subparsers.add_parser("start")
    start_parser.set_defaults(func=start)

    # stop command
    stop_parser = subparsers.add_parser("stop")
    stop_parser.set_defaults(func=stop)

    # finish command
    finish_parser = subparsers.add_parser("finish")
    finish_parser.set_defaults(func=finish)

    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()