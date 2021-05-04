# Does a fusion of natural interaction technologies effectively improve a GUI?

## Dependencies

[mediapipe](https://github.com/google/mediapipe), SpeechRecognition, PyAudio, portaudio, tensorflow, cv2.

```sh
brew install portaudio
pip install mediapipe SpeechRecognition PyAudio tensorflow opencv-python
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

### Emotion Recognition

```sh
cd emotion-recognition
python video_realtime.py
```

## Host the PoC webpage

Run `python -m http.server` in the `web/` directory and visit `localhost:8000/index.html`

## Haptic feedback for MacBook with Touch Bar

### Build
We need the latest version of Xcode.
Simply use `make` in the `HapticKey` directory to install all dependencies, build application binary, then archive it in `build/HapticKey.xcarchive/Products/`.
