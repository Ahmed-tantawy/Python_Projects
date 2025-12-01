import cv2
import mediapipe as mp
import time
import math
import numpy as np

# Initialize MediaPipe hands solution
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Initialize the Hands object
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Get frame dimensions
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Variables for FPS calculation
prev_time = 0

# Drawing canvas
canvas = None

# Mode selection (1: Basic, 2: Drawing, 3: Gestures, 4: Distance)
current_mode = 1

# Color for drawing
draw_color = (0, 255, 0)  # Green
brush_thickness = 10

# Drawing history for clearing
prev_x, prev_y = 0, 0

print("=" * 50)
print("ENHANCED HAND TRACKING")
print("=" * 50)
print("Controls:")
print("  'q' - Quit")
print("  '1' - Basic Mode (hand tracking)")
print("  '2' - Drawing Mode (draw with index finger)")
print("  '3' - Gesture Recognition Mode")
print("  '4' - Distance Meter Mode")
print("  'c' - Clear canvas (in drawing mode)")
print("  'r' - Red color")
print("  'g' - Green color")
print("  'b' - Blue color")
print("=" * 50)


def count_fingers(hand_landmarks, handedness):
    """Count the number of fingers that are up"""
    fingers = []
    
    # Thumb (different logic for left/right hand)
    if handedness == "Right":
        if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
            fingers.append(1)
        else:
            fingers.append(0)
    else:
        if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
            fingers.append(1)
        else:
            fingers.append(0)
    
    # Other fingers (compare tip with pip joint)
    finger_tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky
    finger_pips = [6, 10, 14, 18]
    
    for tip, pip in zip(finger_tips, finger_pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            fingers.append(1)
        else:
            fingers.append(0)
    
    return fingers, sum(fingers)


def calculate_distance(point1, point2, frame_shape):
    """Calculate Euclidean distance between two landmarks"""
    h, w, c = frame_shape
    x1, y1 = int(point1.x * w), int(point1.y * h)
    x2, y2 = int(point2.x * w), int(point2.y * h)
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance, (x1, y1), (x2, y2)


def detect_gesture(fingers, hand_landmarks):
    """Detect specific hand gestures"""
    # Fist: all fingers down
    if sum(fingers) == 0:
        return "Fist"
    
    # Thumbs up: only thumb up
    if fingers == [1, 0, 0, 0, 0]:
        return "Thumbs Up"
    
    # Peace sign: index and middle up
    if fingers == [0, 1, 1, 0, 0]:
        return "Peace Sign"
    
    # OK sign: thumb and index forming circle
    thumb_tip = hand_landmarks.landmark[4]
    index_tip = hand_landmarks.landmark[8]
    distance = math.sqrt((thumb_tip.x - index_tip.x)**2 + (thumb_tip.y - index_tip.y)**2)
    if distance < 0.05 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
        return "OK Sign"
    
    # Open hand: all fingers up
    if sum(fingers) == 5:
        return "Open Hand"
    
    # Pointing: only index finger up
    if fingers == [0, 1, 0, 0, 0]:
        return "Pointing"
    
    return None


while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        print("Failed to grab frame")
        break
    
    # Initialize canvas if needed
    if canvas is None:
        canvas = np.zeros_like(frame)
    
    # Flip the frame horizontally for mirror view
    frame = cv2.flip(frame, 1)
    
    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame
    results = hands.process(rgb_frame)
    
    # Calculate FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    
    # Draw hand landmarks if detected
    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            # Get hand label (Left/Right)
            hand_label = handedness.classification[0].label
            
            # Draw landmarks
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )
            
            # Mode 1: Basic tracking with finger counting
            if current_mode == 1:
                fingers, finger_count = count_fingers(hand_landmarks, hand_label)
                
                # Get wrist position for text
                h, w, c = frame.shape
                wrist_x = int(hand_landmarks.landmark[0].x * w)
                wrist_y = int(hand_landmarks.landmark[0].y * h)
                
                cv2.putText(frame, f'{hand_label}: {finger_count} fingers', 
                           (wrist_x - 50, wrist_y - 20),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
            
            # Mode 2: Drawing mode
            elif current_mode == 2:
                fingers, finger_count = count_fingers(hand_landmarks, hand_label)
                
                # Get index finger tip position
                h, w, c = frame.shape
                index_x = int(hand_landmarks.landmark[8].x * w)
                index_y = int(hand_landmarks.landmark[8].y * h)
                
                # Draw if only index finger is up
                if fingers[1] == 1 and fingers[2] == 0:
                    cv2.circle(frame, (index_x, index_y), brush_thickness, draw_color, -1)
                    
                    if prev_x == 0 and prev_y == 0:
                        prev_x, prev_y = index_x, index_y
                    
                    cv2.line(canvas, (prev_x, prev_y), (index_x, index_y), 
                            draw_color, brush_thickness)
                    prev_x, prev_y = index_x, index_y
                else:
                    prev_x, prev_y = 0, 0
                
                # Show indicator
                cv2.circle(frame, (index_x, index_y), 10, (255, 0, 255), 2)
            
            # Mode 3: Gesture recognition
            elif current_mode == 3:
                fingers, finger_count = count_fingers(hand_landmarks, hand_label)
                gesture = detect_gesture(fingers, hand_landmarks)
                
                if gesture:
                    h, w, c = frame.shape
                    cv2.putText(frame, f'{hand_label}: {gesture}', 
                               (50, 150 if hand_label == "Left" else 200),
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)
            
            # Mode 4: Distance meter
            elif current_mode == 4:
                # Measure distance between thumb and index finger
                thumb_tip = hand_landmarks.landmark[4]
                index_tip = hand_landmarks.landmark[8]
                
                distance, (x1, y1), (x2, y2) = calculate_distance(
                    thumb_tip, index_tip, frame.shape
                )
                
                # Draw line between thumb and index
                cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)
                cv2.circle(frame, (x1, y1), 10, (255, 0, 0), -1)
                cv2.circle(frame, (x2, y2), 10, (255, 0, 0), -1)
                
                # Draw midpoint with distance
                mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
                cv2.putText(frame, f'{int(distance)}px', (mid_x - 30, mid_y - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
    
    # Overlay canvas on frame in drawing mode
    if current_mode == 2:
        gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray_canvas, 20, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        frame_bg = cv2.bitwise_and(frame, frame, mask=mask_inv)
        canvas_fg = cv2.bitwise_and(canvas, canvas, mask=mask)
        frame = cv2.add(frame_bg, canvas_fg)
    
    # Display mode and info
    mode_names = {1: "Basic Tracking", 2: "Drawing Mode", 3: "Gesture Recognition", 4: "Distance Meter"}
    cv2.putText(frame, f'Mode: {mode_names[current_mode]}', (10, 30),
               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 70),
               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # Show number of hands
    num_hands = len(results.multi_hand_landmarks) if results.multi_hand_landmarks else 0
    cv2.putText(frame, f'Hands: {num_hands}', (10, 110),
               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow('Enhanced Hand Tracking', frame)
    
    # Key controls
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
    elif key == ord('1'):
        current_mode = 1
        print("Switched to: Basic Tracking Mode")
    elif key == ord('2'):
        current_mode = 2
        print("Switched to: Drawing Mode")
    elif key == ord('3'):
        current_mode = 3
        print("Switched to: Gesture Recognition Mode")
    elif key == ord('4'):
        current_mode = 4
        print("Switched to: Distance Meter Mode")
    elif key == ord('c'):
        canvas = np.zeros_like(frame)
        print("Canvas cleared!")
    elif key == ord('r'):
        draw_color = (0, 0, 255)
        print("Color: Red")
    elif key == ord('g'):
        draw_color = (0, 255, 0)
        print("Color: Green")
    elif key == ord('b'):
        draw_color = (255, 0, 0)
        print("Color: Blue")

# Cleanup
cap.release()
cv2.destroyAllWindows()
hands.close()
print("\nHand Tracking Stopped!")