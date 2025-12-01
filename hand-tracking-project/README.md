# Hand Tracking Project 🖐️

A real-time hand tracking application built with Python, OpenCV, and MediaPipe. Track your hands, draw in the air, recognize gestures, and more!

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/opencv-4.8+-green.svg)
![MediaPipe](https://img.shields.io/badge/mediapipe-0.10+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

### 🎯 Four Interactive Modes

1. **Basic Tracking Mode** - Real-time hand detection with finger counting
2. **Drawing Mode** - Draw in the air with your index finger
3. **Gesture Recognition** - Detects thumbs up, peace sign, fist, OK sign, and more
4. **Distance Meter** - Measures distance between thumb and index finger

### 🎨 Key Capabilities

- ✅ Track up to 2 hands simultaneously
- ✅ 21 landmark points per hand
- ✅ Real-time FPS display
- ✅ Left/right hand detection
- ✅ Multiple drawing colors
- ✅ Gesture-based interactions
- ✅ Smooth physics and animations

## 🚀 Quick Start

### Option 1: Run with Docker (Recommended)

**Prerequisites:**
- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- Webcam connected
- X11 display (Linux/macOS)

**Build and run:**
```bash
# Clone the repository
git clone https://github.com/yourusername/hand-tracking-project.git
cd hand-tracking-project

# Build Docker image
docker build -t hand-tracker .

# Run on Linux
xhost +local:docker
docker run -it --rm \
  --device=/dev/video0:/dev/video0 \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  hand-tracker

# Or use docker-compose
docker-compose up
```

**Run on macOS:**
```bash
# Install XQuartz first
brew install --cask xquartz

# Start XQuartz and allow connections
open -a XQuartz
# In XQuartz preferences: Security > "Allow connections from network clients"

# Get your IP
IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')

# Allow X11 forwarding
xhost + $IP

# Run container
docker run -it --rm \
  --device=/dev/video0:/dev/video0 \
  -e DISPLAY=$IP:0 \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  hand-tracker
```

**Run on Windows:**
```bash
# Install VcXsrv or Xming first
# Start VcXsrv with "Disable access control" checked

# Run container
docker run -it --rm ^
  --device=/dev/video0:/dev/video0 ^
  -e DISPLAY=host.docker.internal:0.0 ^
  hand-tracker
```

### Option 2: Run Locally

**Prerequisites:**
- Python 3.8 or higher
- Webcam

**Install and run:**
```bash
# Clone the repository
git clone https://github.com/yourusername/hand-tracking-project.git
cd hand-tracking-project

# Install dependencies
pip install -r requirements.txt

# Run basic version
python hand_tracker.py

# Or run enhanced version with all features
python hand_tracker_enhanced.py
```

## 🎮 Controls

| Key | Action |
|-----|--------|
| `1` | Basic Tracking Mode |
| `2` | Drawing Mode |
| `3` | Gesture Recognition Mode |
| `4` | Distance Meter Mode |
| `r` | Red color (drawing) |
| `g` | Green color (drawing) |
| `b` | Blue color (drawing) |
| `c` | Clear canvas |
| `q` | Quit |

## 📁 Project Structure

```
hand-tracking-project/
│
├── hand_tracker.py           # Basic hand tracking
├── hand_tracker_enhanced.py  # Full-featured version
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose setup
├── .dockerignore           # Docker ignore rules
├── .gitignore              # Git ignore rules
├── README.md               # This file
├── README_ENHANCED.md      # Detailed feature guide
└── LICENSE                 # MIT License
```

## 🛠️ Technologies Used

- **Python 3.11** - Programming language
- **OpenCV** - Computer vision and image processing
- **MediaPipe** - Hand tracking and landmark detection
- **NumPy** - Numerical computations
- **Docker** - Containerization

## 📖 How It Works

1. **Capture**: OpenCV captures video from your webcam
2. **Process**: MediaPipe detects hands and 21 landmarks per hand
3. **Analyze**: Custom algorithms interpret landmarks for gestures and interactions
4. **Visualize**: OpenCV draws landmarks, connections, and UI elements
5. **Interact**: Real-time response to hand movements and gestures

## 🎯 Use Cases

- **Education**: Learn computer vision and hand tracking
- **Accessibility**: Touchless interfaces
- **Gaming**: Gesture-based game controls
- **Presentations**: Hand-controlled slides
- **Art**: Virtual drawing and painting
- **Sign Language**: Recognition systems

## 🔧 Configuration

Edit these constants in the code to customize:

```python
# In hand_tracker_enhanced.py

# Hand detection sensitivity
hands = mp_hands.Hands(
    max_num_hands=2,                    # Track 1-2 hands
    min_detection_confidence=0.7,       # Lower = more sensitive
    min_tracking_confidence=0.7         # Tracking smoothness
)

# Drawing settings
brush_thickness = 10                    # Brush size
draw_color = (0, 255, 0)               # Default color (BGR)
```

## 🐛 Troubleshooting

### Camera not detected in Docker
```bash
# Check camera device
ls -la /dev/video*

# Try different device
docker run ... --device=/dev/video1:/dev/video1 ...
```

### Display issues on Linux
```bash
# Allow X11 connections
xhost +local:docker

# Check DISPLAY variable
echo $DISPLAY
```

### Low FPS
- Close other applications using the camera
- Reduce `max_num_hands` to 1
- Lower detection confidence values

### Hands not detected
- Ensure good lighting
- Keep hands in frame
- Try adjusting confidence thresholds

## 🚀 Future Enhancements

- [ ] Add more gesture types
- [ ] Implement gesture macros
- [ ] Add sound effects
- [ ] Save/load drawings
- [ ] Multi-user support
- [ ] Web interface
- [ ] Mobile app version
- [ ] 3D hand tracking
- [ ] Sign language recognition
- [ ] Virtual keyboard

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- [MediaPipe](https://google.github.io/mediapipe/) - Google's ML solutions
- [OpenCV](https://opencv.org/) - Computer vision library
- [Python](https://python.org/) - Programming language

## 📧 Contact

Have questions? Feel free to reach out or open an issue!

---

⭐ Star this repo if you find it helpful!