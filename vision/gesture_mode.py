import cv2
import pyautogui
import mediapipe as mp
import time
from vision.swipe_detection import detect_swipe
from actions.browser_actions import (
    open_google,
    open_youtube
)
from config.settings import (
    HOLD_TIME,
    DEAD_ZONE,
    SCROLL_MULTIPLIER
)

def gesture_mode():

    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils

    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    )

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    current_gesture = "NONE"
    gesture_start_time = time.time()
    
    gesture_locked = False
    scroll_mode = False
   
    control_y = None

    while True:

        success, img = cap.read()

        if not success:
            continue

        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        detected_gesture = "NONE"

        if results.multi_hand_landmarks:

            hand = results.multi_hand_landmarks[0]
            wrist_x = hand.landmark[0].x
            wrist_y = hand.landmark[0].y

            if scroll_mode and control_y is not None:
                delta = wrist_y - control_y
                if abs(delta) > DEAD_ZONE:
                    speed = int(abs(delta) * SCROLL_MULTIPLIER)
                    if delta > 0:
                        pyautogui.scroll(speed)
                    else:
                        pyautogui.scroll(-speed)
                    control_y = wrist_y

            swipe = detect_swipe(wrist_x)
            

            if swipe == "RIGHT":
                print("SWIPE RIGHT")

            elif swipe == "LEFT":
                print("SWIPE LEFT")
            
            mp_draw.draw_landmarks(
                img,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            landmarks = hand.landmark
            
            
            
            index_up = landmarks[8].y < landmarks[6].y
            middle_up = landmarks[12].y < landmarks[10].y
            ring_up = landmarks[16].y < landmarks[14].y
            pinky_up = landmarks[20].y < landmarks[18].y

            fingers = 0

            if landmarks[8].y < landmarks[6].y:
                fingers += 1

            if landmarks[12].y < landmarks[10].y:
                fingers += 1

            if landmarks[16].y < landmarks[14].y:
                fingers += 1

            if landmarks[20].y < landmarks[18].y:
                fingers += 1
            if fingers >= 4:
                detected_gesture = "PALM"

            elif (
                index_up
                and not middle_up
                and not ring_up
                and not pinky_up
            ):
                detected_gesture = "INDEX"

            elif (
                index_up
                and middle_up
                and not ring_up
                and not pinky_up
            ):
                detected_gesture = "PEACE"

            elif fingers == 0:
                detected_gesture = "FIST"
        now = time.time()

        if detected_gesture != current_gesture:
            current_gesture = detected_gesture
            gesture_start_time = now

        if current_gesture == "NONE":
            gesture_locked = False
        hold_time = now - gesture_start_time
        
        cv2.putText(
            img,
            f"Gesture: {current_gesture}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            img,
            "Super Powers Mode",
            (20, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2
        )
        if scroll_mode:

                cv2.putText(
                    img,
                    "SCROLL MODE",
                    (20, 150),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 255),
                    2
                )
        # Gesture confirmed only after hold
        if (
            hold_time >= HOLD_TIME
            and current_gesture != "NONE"
            and not gesture_locked
        ):
            if current_gesture == "PALM":
                print("AIR CONTROL ENABLED")
                scroll_mode = True
                control_y = wrist_y
                gesture_locked = True

            elif current_gesture == "PEACE":

                print("Opening YouTube")
                open_youtube()

                gesture_locked = True

            elif current_gesture == "INDEX":

                print("Opening Google")
                open_google()

                gesture_locked = True

            elif current_gesture == "FIST":

                if scroll_mode:

                    print("SCROLL MODE DISABLED")

                    scroll_mode = False
                    control_y = None
                    gesture_locked = False

                else:

                    print("Exiting Super Powers")

                    cap.release()
                    cv2.destroyAllWindows()

                    return "EXIT"

          
        cv2.imshow("Super Powers", img)

        if cv2.waitKey(1) & 0xFF == ord("q"):

            cap.release()
            cv2.destroyAllWindows()

            return "EXIT"