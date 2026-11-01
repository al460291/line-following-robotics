# Line Following Exercise — Robotics Academy / Unibotics

> **Status:** Starter repository. The source files are reference implementations based on the provided lecture slides. **Simulation results and screenshots must be added after running the exercise**; no completion or performance is claimed here.

## 1. Objective

Program a simulated autonomous racing car to follow the red line on the circuit using camera images, OpenCV and feedback control. The original exercise is described in [Visual Follow Line — Robotics Academy](https://jderobot.github.io/RoboticsAcademy/exercises/AutonomousCars/follow_line/).

## 2. Technologies

- Python
- OpenCV (`cv2`) for image processing
- Robotics Academy / Unibotics simulator with HAL and WebGUI
- Docker for the simulator backend, following the lecture instructions

**Important:** `HAL` and `WebGUI` are provided by the simulator. The `src/*.py` scripts are intended to be **pasted into the Follow Line web code editor**, not executed as ordinary local Python programs.

## 3. How to run

1. Install Docker and make sure the Docker engine is running.
2. Start the simulator backend using the command from the lecture slides:

   ```bash
   docker run --rm -it -p 6080-6090:6080-6090 -p 7163:7163 jderobot/robotics-backend:latest
   ```

   On Linux computers with compatible graphics acceleration, the slides also give an option using `--device /dev/dri`. For NVIDIA GPUs, see the additional instructions in the lecture slides. **Do not start multiple backends on the same ports.**
3. Visit [Unibotics — Follow Line](https://unibotics.org/academy/follow_line/) in a browser while the backend is running.
4. Open the exercise code editor. Copy and paste **one script at a time** from `src/`, in the order described below.
5. Run the exercise. Observe the camera/mask display and the simulated car.
6. Save **your own screenshots** to `screenshots/`, record outcomes in `results/experiment_log.csv`, and update the results section below.

> These steps reflect the course slides. Exact backend/browser behavior depends on your local setup; this starter has not been run in your environment.

## 4. Activities

### Activity 1 — Image acquisition and display

**File:** [`src/step_1_image_acquisition.py`](src/step_1_image_acquisition.py)

- Read the vehicle camera image with `HAL.getImage()`.
- Display it using `WebGUI.showImage()`.
- **Evidence to add:** `screenshots/01_camera.png`.

### Activity 2 — Red color filtering

**File:** [`src/step_2_color_filtering.py`](src/step_2_color_filtering.py)

- Convert the original BGR image to HSV (`cv2.cvtColor`).
- Use the color interval shown in the slides, from `(0, 125, 125)` to `(30, 255, 255)`.
- Create a binary mask using `cv2.inRange()`.
- **Evidence to add:** `screenshots/02_red_mask.png`.

**What to explain in the report:** HSV helps segment the red line; the lower and upper thresholds may need adjustment depending on the simulated lighting/colors.

### Activity 3 — Centroid of the red mask

**File:** [`src/step_3_centroid_detection.py`](src/step_3_centroid_detection.py)

- Find contours with `cv2.findContours()`.
- Select the largest contour and calculate its moments with `cv2.moments()`.
- Compute the centroid from `cx = m10 / m00`, `cy = m01 / m00` when `m00` is nonzero.
- **Evidence to add:** `screenshots/03_centroid.png` (for example, show the mask and the `cx, cy` output).

### Activity 4 — Proportional controller (P)

**File:** [`src/step_4_proportional_controller.py`](src/step_4_proportional_controller.py)

- Compute steering error: `error = (image_width / 2) - cx`.
- Set forward velocity using `HAL.setV()`.
- Set angular velocity using `HAL.setW(KP * error)`.
- Tune the proportional gain `KP` to reduce oscillations and line-loss events.
- The initial `KP = 0.01` and forward velocity `1.0` come from the slide example; **they have not been optimized for your simulation**.
- **Evidence to add:** `screenshots/04_p_controller.png`.

**Difference from the simplified slide example:** This starter checks for missing/empty contours before computing moments and stops the vehicle when the line is not detected.

### Activity 5 — Controller comparison (optional extension / as required by your instructor)

**File:** [`src/step_5_pid_experiment.py`](src/step_5_pid_experiment.py)

- **P:** Keep `KI = 0` and `KD = 0`.
- **PD:** Tune `KP` and a positive `KD`, keeping `KI = 0`.
- **PID:** Tune `KP`, `KI` and `KD`.
- Compare trajectory stability, line-loss events, completion percentage, and completion time when available.
- This is a discrete-step teaching example; derivatives and integration are not normalized to elapsed time.

The official exercise describes PID control as its goal. Check the teacher's grading instructions to decide whether the P baseline alone is sufficient.

## 5. Screenshots / evidence

Replace these placeholders with screenshots you capture **from your own execution**:

| Screenshot | Purpose | Status |
| --- | --- | --- |
| `screenshots/01_camera.png` | Original camera image | Pending |
| `screenshots/02_red_mask.png` | Segmented red mask | Pending |
| `screenshots/03_centroid.png` | Detected centroid, terminal output | Pending |
| `screenshots/04_p_controller.png` | P controller following the line | Pending |
| `screenshots/05_best_run.png` | Best run / progress / timing | Pending |

Once added, insert images into this README with Markdown, e.g.:

```markdown
![Red line detection](screenshots/02_red_mask.png)
```

## 6. Performance evaluation

**No performance has been measured yet.** Enter your actual trials in [`results/experiment_log.csv`](results/experiment_log.csv) and summarize them below.

Suggested comparison table:

| Controller | KP | KI | KD | Forward speed | Track progress (%) | Lap / run time (s) | Line lost (#) | Observations |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| P | — | 0 | 0 | — | Not measured | Not measured | Not measured | — |
| PD | — | 0 | — | — | Not measured | Not measured | Not measured | — |
| PID | — | — | — | — | Not measured | Not measured | Not measured | — |

**Evaluation questions:**

- Does the vehicle stay aligned with the red line through sharp turns?
- Does it oscillate from side to side?
- Does higher forward speed make it leave the line?
- Which gains produce the most stable progress?
- Is the result reproducible in multiple trials?

## 7. Conclusions (to complete after testing)

Describe which controller performed best, what technical problems arose, the final parameter choices, and possible improvements. Do not report untested performance as achieved results.

## 8. References

- [Robotics Academy — Visual Follow Line](https://jderobot.github.io/RoboticsAcademy/exercises/AutonomousCars/follow_line/)
- [Unibotics instructions](https://unibotics.org/instructions/)
- Course presentation: *Line Following Exercise* (provided by the instructor).
