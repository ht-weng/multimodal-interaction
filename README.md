# Collection of vision-based sensing tools  

## Dependencies

[mediapipe](https://github.com/google/mediapipe)

```sh
pip install mediapipe
```

## How to get started

### Detect face mesh or hand gesture

`cd mediapipe/`, then `python face-mesh.py` or `python hands.py`.

### Use holistic model to detect and output index fingers' coordinates

```sh
cd mediapipe/
python holistic.py
```

The output csv files are in the `data/` folder.
