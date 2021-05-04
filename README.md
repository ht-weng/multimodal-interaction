# Does a fusion of natural interaction technologies effectively improve a GUI?

## Dependencies

[mediapipe](https://github.com/google/mediapipe), SpeechRecognition, PyAudio, portaudio.

```sh
brew install portaudio
pip install mediapipe SpeechRecognition PyAudio
```

## How to get started

### Detect face mesh or hand gesture

`cd mediapipe/`, then `python face_mesh.py` or `python hands.py`.

### Use holistic model to detect and output index fingers' coordinates

```sh
cd mediapipe/
python holistic.py
```

The output csv files are in the `data/` folder.

### Speech Recognition

Desktop version

```sh
cd speech-recognition/
python microphone_realtime.py
```

Web version

```sh
cd speech-recognition/
python -m http.server
```

Visit `localhost:8000`.

## Host the PoC webpage

Run `python -m http.server` in the `web/` directory and visit `localhost:8000/index.html`
