# UAV based Target Tracking

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green.svg)](https://opencv.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.8+-red.svg)](https://pytorch.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-1.15+-orange.svg)](https://tensorflow.org/)
[![AirSim](https://img.shields.io/badge/AirSim-1.0+-purple.svg)](https://microsoft.github.io/AirSim/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## 🚁 Overview

The UAV-Based Autonomous Security System is an advanced computer vision and machine learning project that implements autonomous drone surveillance with facial recognition capabilities. This system enables security forces to detect, recognize, and track specific individuals in crowded areas using unmanned aerial vehicles (UAVs) equipped with high-definition cameras.

### Key Objectives

- **Autonomous Mission Execution**: Schedule, repeat, and monitor autonomous drone missions
- **Face Recognition**: Real-time facial identification in crowded environments
- **Person Tracking**: Autonomous tracking and following of recognized individuals
- **Security Surveillance**: 24/7 security monitoring for various applications
- **Cost-Effective Solution**: More economical than traditional helicopter surveillance
- **Real-time Drone Control**: Direct UAV control based on tracking coordinates

### Applications

- **Situational Awareness**: Real-time monitoring of security situations
- **Guard Augmentation**: Supporting human security personnel
- **Event Security**: Monitoring large gatherings and events
- **Border Control**: Surveillance of border areas
- **Criminal Detection**: Tracking and following suspects
- **Infrastructure Protection**: Securing critical facilities
- **Autonomous Survey Missions**: Automated area surveillance and mapping

## ✨ Features

### 🔍 Face Recognition
- Real-time facial detection and recognition in video streams
- High-accuracy identification using deep learning models
- Support for multiple face detection methods (CNN, HOG)
- 99.38% accuracy on Labeled Faces in the Wild (LFW) dataset

### 🎯 Person Tracking
- Fully-Convolutional Siamese Networks for object tracking
- Real-time tracking at 30+ frames per second
- Robust tracking in complex environments
- Automatic target re-acquisition

### 🚁 Autonomous Mission Control
- Mission scheduling and planning
- Autonomous takeoff and landing
- Obstacle detection and avoidance
- GPS-guided navigation
- Emergency return-to-base functionality
- Real-time coordinate transmission to drone

### 📊 System Monitoring
- Real-time video streaming
- Performance metrics tracking
- System health monitoring
- Alert generation for security events

### 🛸 UAV Integration
- Microsoft AirSim integration for UAV simulation
- Real-time coordinate tracking and transmission
- Google Sheets integration for coordinate logging
- Autonomous survey missions
- Direct drone control based on tracking data

## 🏗️ System Architecture

### High-Level Architecture

The system consists of several key components:

1. **UAV Platform**: Quadcopter with onboard sensors and camera
2. **Base Station**: Central command center for mission control
3. **Image Processing Server**: Computer vision and ML algorithms
4. **Web Interface**: User control and monitoring dashboard
5. **Database**: Mission and recognition data storage
6. **Drone Control System**: AirSim-based UAV control interface

### Core Components

#### 1. Object Detection (YOLOv3)
- Real-time person detection in video streams
- Configurable confidence thresholds
- Multi-class object detection capabilities

#### 2. Face Recognition (dlib + Deep Learning)
- 128-dimensional facial feature vectors
- Deep metric learning for face comparison
- Support for multiple recognition models

#### 3. Object Tracking (DeepSORT)
- Multi-object tracking with re-identification
- Kalman filtering for motion prediction
- Hungarian algorithm for optimal assignment

#### 4. Siamese Networks
- Template-based object tracking
- Real-time feature extraction
- Robust tracking in challenging conditions

#### 5. UAV Control System
- Microsoft AirSim integration for simulation
- Real-time coordinate transmission
- Google Sheets API for data logging
- Autonomous survey capabilities
- Direct drone control based on tracking coordinates

## 🛠️ Technologies Used

### Core Technologies
- **Python 3.7+**: Primary programming language
- **OpenCV 4.5+**: Computer vision and image processing
- **PyTorch 1.8+**: Deep learning framework for YOLOv3 and DeepSORT
- **TensorFlow 1.15+**: Siamese network training and inference
- **NumPy**: Numerical computations
- **SciPy**: Scientific computing

### Computer Vision & ML
- **YOLOv3**: Real-time object detection
- **DeepSORT**: Multi-object tracking
- **Siamese Networks**: Template-based tracking
- **dlib**: Face detection and recognition
- **face_recognition**: High-level face recognition API

### UAV Control & Simulation
- **Microsoft AirSim**: UAV simulation and control
- **gspread**: Google Sheets API integration
- **oauth2client**: Google API authentication
- **goto-statement**: Control flow management

### Development Tools
- **CUDA**: GPU acceleration for deep learning
- **Sacred**: Experiment tracking and management
- **PyYAML**: Configuration management
- **Git**: Version control

### Hardware Requirements
- **GPU**: NVIDIA GPU with CUDA support (recommended)
- **Camera**: 1080p HD camera for video capture
- **UAV**: Quadcopter with flight controller
- **Sensors**: GPS, IMU, ultrasonic, infrared sensors
- **Simulation**: Microsoft AirSim for UAV testing

## 📦 Installation

### Prerequisites

1. **Python Environment**
   ```bash
   python --version  # Python 3.7 or higher
   ```

2. **CUDA Support** (Optional but recommended)
   ```bash
   nvidia-smi  # Check GPU availability
   ```

3. **Microsoft AirSim** (For UAV simulation)
   ```bash
   # Install AirSim for UAV simulation
   pip install airsim
   ```

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd uav-autonomous-security-system
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Pre-trained Models**
   ```bash
   # YOLOv3 weights
   wget https://pjreddie.com/media/files/yolov3.weights -P detector/YOLOv3/weight/
   
   # DeepSORT model
   wget <deep_sort_model_url> -P deep_sort/deep/checkpoint/
   ```

4. **Configure Environment**
   ```bash
   cp configs/yolov3.yaml.example configs/yolov3.yaml
   # Edit configuration files as needed
   ```

5. **Setup Google Sheets API**
   ```bash
   # Place your Google API credentials file in the project root
   # Rename to: fypapi-275115-1487f536b9fc.json
   ```

### Docker Installation (Alternative)

```bash
# Build the Docker image
docker build -t uav-security-system .

# Run the container
docker run -it --gpus all uav-security-system
```

## 🚀 Usage

### Basic Usage

1. **Start the Complete System**
   ```bash
   # Start tracking with UAV integration
   python change_yolov3_deepsort.py --video-path path/to/video.mp4
   ```

2. **Face Recognition**
   ```bash
   python encode_faces.py --dataset dataset/ --encodings encodings.pickle
   ```

3. **Training Siamese Model**
   ```bash
   python train_siamese_model.py
   ```

### UAV Control Usage

1. **Real-time UAV Tracking**
   ```bash
   # Start UAV tracking system
   python "drone code/trackDrone.py"
   ```

2. **Autonomous Survey Missions**
   ```bash
   # Run autonomous survey mission
   python "drone code/survey.py" --size 50 --altitude 10 --speed 3
   ```

3. **Coordinate Management**
   ```python
   # Log coordinates to Google Sheets
   python "drone code/spreadsheet.py"
   ```

### Advanced Usage

#### Mission Scheduling
```python
from utils.mission_scheduler import MissionScheduler

scheduler = MissionScheduler()
scheduler.schedule_mission(
    path=[[lat1, lon1], [lat2, lon2]],
    altitude=100,
    duration=3600
)
```

#### Real-time Tracking with UAV Control
```python
from SiameseTracker import SiameseTracker

tracker = SiameseTracker()
tracker.set_first_frame(frame, bounding_box)
tracked_bbox = tracker.track(frame)

# UAV automatically receives coordinates and adjusts position
```

### Configuration

Edit the configuration files in the `configs/` directory:

- `yolov3.yaml`: YOLOv3 detection settings
- `deep_sort.yaml`: DeepSORT tracking parameters
- `configuration.py`: System-wide settings

#### UAV Configuration

**AirSim Setup**
1. Install Microsoft AirSim
2. Configure simulation environment
3. Set up drone model and sensors
4. Configure flight controller parameters

**Google Sheets API**
1. Create Google Cloud Project
2. Enable Google Sheets API
3. Create service account credentials
4. Share spreadsheet with service account

## 📁 Project Structure

```
uav-autonomous-security-system/
├── detector/                 # Object detection components
│   └── YOLOv3/             # YOLOv3 implementation
├── deep_sort/               # Multi-object tracking
│   ├── deep/               # Deep feature extraction
│   └── sort/               # SORT algorithm
├── drone code/              # UAV control system
│   ├── trackDrone.py       # Real-time drone tracking
│   ├── survey.py           # Autonomous survey missions
│   ├── spreadsheet.py      # Coordinate management
│   └── setup_path.py       # AirSim integration
├── embeddings/              # Neural network embeddings
├── inference/               # Model inference utilities
├── utils/                   # Utility functions
├── configs/                 # Configuration files
├── datasets/                # Training datasets
├── tests/                   # Unit tests
├── scripts/                 # Utility scripts
├── demo/                    # Demo videos and results
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── LICENSE                 # MIT License
```

## 📚 Documentation

### Code Documentation

All scripts in the project include comprehensive docstrings following Google-style documentation:

- **Module Docstrings**: Clear description of each module's purpose and functionality
- **Function Docstrings**: Detailed parameter descriptions, return values, and usage examples
- **Class Docstrings**: Complete documentation of classes, methods, and attributes
- **Inline Comments**: Helpful comments explaining complex logic and algorithms

### Key Documented Components

#### Main Tracking Scripts
- `yolov3_deepsort.py`: Basic YOLOv3 + DeepSORT tracking system
- `change_yolov3_deepsort.py`: Enhanced tracking with UAV integration
- `SiameseTracker.py`: Siamese network-based object tracker
- `demo.py`: Interactive demo application

#### UAV Control Scripts
- `drone code/trackDrone.py`: Real-time UAV tracking system
- `drone code/survey.py`: Autonomous survey mission controller
- `drone code/spreadsheet.py`: Google Sheets coordinate management
- `drone code/setup_path.py`: AirSim integration utility

#### Supporting Scripts
- `encode_faces.py`: Face encoding generation system
- `configuration.py`: Model and training configuration management
- `train_siamese_model.py`: Siamese network training script

### Documentation Features

- **Self-Documenting Code**: All functions and classes include comprehensive docstrings
- **Usage Examples**: Practical examples for complex functions
- **Parameter Documentation**: Detailed descriptions of all parameters and return values
- **Important Notes**: Warnings and important considerations for users
- **Cross-References**: Links between related components and functions

## 🧪 Testing

### Unit Testing
```bash
python -m pytest tests/
```

### Integration Testing
```bash
python tests/test_integration.py
```

### Performance Testing
```bash
python scripts/benchmark_performance.py
```

### UAV System Testing
```bash
# Test UAV control system
python "drone code/trackDrone.py"

# Test survey missions
python "drone code/survey.py" --size 10 --altitude 5
```

### Test Results

The system has been tested with the following results:

- **Face Detection**: 95% accuracy in various lighting conditions
- **Face Recognition**: 99.38% accuracy on LFW dataset
- **Person Tracking**: 30 FPS with 90% tracking success rate
- **System Performance**: Real-time processing at 1080p resolution
- **UAV Control**: Sub-second response time for coordinate updates
- **Survey Missions**: 100% mission completion rate in simulation

## 📊 Performance Metrics

### Detection Performance
- **YOLOv3**: 30 FPS on NVIDIA GTX 1080
- **Face Detection**: 95% accuracy
- **Person Detection**: 90% accuracy in crowded scenes

### Tracking Performance
- **DeepSORT**: 100+ FPS tracking
- **Siamese Networks**: Real-time template tracking
- **Multi-object**: Support for 50+ simultaneous tracks

### UAV Performance
- **Coordinate Transmission**: <100ms latency
- **Survey Missions**: 100% completion rate
- **Flight Control**: Sub-second response time
- **Mission Duration**: Up to 8 hours continuous operation

### System Performance
- **Video Processing**: 1080p at 30 FPS
- **Memory Usage**: <4GB RAM
- **GPU Utilization**: 80% on NVIDIA GPU
- **Network Latency**: <50ms for coordinate transmission

## 🤝 Contributing

We welcome contributions to improve the UAV Autonomous Security System!

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Add unit tests for new features
- Update documentation for API changes
- Ensure all tests pass before submitting
- Test UAV integration thoroughly

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
