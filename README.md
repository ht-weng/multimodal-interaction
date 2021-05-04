# Does a fusion of natural interaction technologies effectively improve a GUI?

## Dependencies

[mediapipe](https://github.com/google/mediapipe)

```sh
pip install mediapipe
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

## Host the PoC webpage
Run `python -m http.server` in the `web/` directory and visit `localhost:8000/index.html`

## Haptic feedback for MacBook with Touch Bar

### Build
We need the latest version of Xcode.
Simply use `make` to install all dependencies, build application binary, then archive it in `build/HapticKey.xcarchive/Products/`.
