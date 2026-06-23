from collections import deque

positions = deque(maxlen=10)

def detect_swipe(wrist_x):

    positions.append(wrist_x)

    if len(positions) < 10:
        return None

    movement = positions[-1] - positions[0]

    if movement > 0.25:
        positions.clear()
        return "RIGHT"

    elif movement < -0.25:
        positions.clear()
        return "LEFT"

    return None