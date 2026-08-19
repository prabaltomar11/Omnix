import sys
import subprocess
import tempfile
import os

PIPER_MODEL = "tts/models/en/en_US-ryan-medium.onnx"
PITCH = 0.89


def speak(text):
    raw_file = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    )

    processed_file = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    )

    raw_path = raw_file.name
    processed_path = processed_file.name

    raw_file.close()
    processed_file.close()

    try:
        piper_command = [
            sys.executable,
            "-m",
            "piper",
            "-m",
            PIPER_MODEL,
            "-f",
            raw_path
        ]

        subprocess.run(
            piper_command,
            input=text,
            text=True,
            check=True
        )

        ffmpeg_command = [
            "ffmpeg",
            "-y",
            "-i",
            raw_path,
            "-af",
            f"rubberband=pitch={PITCH}",
            processed_path
        ]

        subprocess.run(
            ffmpeg_command,
            check=True
        )

        play_command = [
            "aplay",
            processed_path
        ]

        subprocess.run(
            play_command,
            check=True
        )

    finally:
        for path in (raw_path, processed_path):
            if os.path.exists(path):
                os.remove(path)
