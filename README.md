# face-direction-heuristic

This repository presents a simple, explainable heuristic approach
for estimating head direction (LEFT / FORWARD / RIGHT) using
facial landmarks.

The project is designed as a baseline computer vision pipeline
and focuses on geometric reasoning rather than machine learning.

---

## Overview

The system processes real-time webcam input and:

- Detects a face using MediaPipe Face Mesh
- Extracts facial landmarks
- Uses the nose landmark as a reference point
- Estimates head direction based on horizontal displacement

This approach prioritizes interpretability and modularity.

---

## Pipeline

Camera Input  
→ Face Detection & Landmark Extraction  
→ Landmark-to-Pixel Conversion  
→ Heuristic Decision Logic  
→ Visualization

---

## Heuristic Logic

- If the nose position shifts significantly left of the screen center → LEFT
- If it shifts significantly right → RIGHT
- Otherwise → FORWARD

A tolerance margin is used to prevent jitter caused by small movements
or landmark noise.

---

## Technologies

- Python
- OpenCV
- MediaPipe

- ## Execution

```bash
python face-direction-heuristic.py

---

```md

## Expected Output

- A green dot indicating the nose landmark
- On-screen text showing head direction:
  - LEFT
  - FORWARD
  - RIGHT



