# System Diagrams

This document contains the key system diagrams for the UAV-Based Autonomous Security System as described in the project report.

## 1. System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    UAV-Based Security System                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐        │
│  │   UAV       │    │  Base       │    │  Image      │        │
│  │  Platform   │◄──►│  Station    │◄──►│ Processing  │        │
│  │             │    │             │    │  Server     │        │
│  │ ┌─────────┐ │    │ ┌─────────┐ │    │ ┌─────────┐ │        │
│  │ │ Camera  │ │    │ │ Mission │ │    │ │ YOLOv3  │ │        │
│  │ │ Sensors │ │    │ │ Control │ │    │ │ DeepSORT│ │        │
│  │ │ Flight  │ │    │ │ Database│ │    │ │ Siamese │ │        │
│  │ │ Control │ │    │ │ Web UI  │ │    │ │ Networks│ │        │
│  │ └─────────┘ │    │ └─────────┘ │    │ └─────────┘ │        │
│  └─────────────┘    └─────────────┘    └─────────────┘        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 2. Sequence Diagram

```
User          UAV          Base Station    Image Processing
 │             │              │                    │
 │ Start Mission│             │                    │
 │─────────────►│             │                    │
 │              │ Take Off    │                    │
 │              │────────────►│                    │
 │              │             │                    │
 │              │ Start Video │                    │
 │              │────────────►│                    │
 │              │             │ Process Video      │
 │              │             │───────────────────►│
 │              │             │                    │
 │              │             │ Detect Person      │
 │              │             │◄───────────────────│
 │              │             │                    │
 │              │             │ Face Recognition   │
 │              │             │◄───────────────────│
 │              │             │                    │
 │              │ Track Target│                    │
 │              │◄────────────│                    │
 │              │             │                    │
 │              │ Follow Mode │                    │
 │              │────────────►│                    │
 │              │             │                    │
 │              │ Return Base │                    │
 │              │────────────►│                    │
 │              │ Land        │                    │
 │              │────────────►│                    │
```

## 3. Activity Diagram

```
                    Start
                      │
                      ▼
              ┌──────────────┐
              │ Initialize   │
              │ System       │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Load Mission │
              │ Parameters   │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ UAV Takeoff  │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Start Video  │
              │ Capture      │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Detect       │
              │ Persons      │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Face         │
              │ Recognition  │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Track Target │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Follow Mode  │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Return to    │
              │ Base         │
              └──────────────┘
                      │
                      ▼
                    End
```

## 4. Block Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    System Components                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐                    │
│  │   Hardware      │    │    Software     │                    │
│  │   Components    │    │   Components    │                    │
│  │                 │    │                 │                    │
│  │ ┌─────────────┐ │    │ ┌─────────────┐ │                    │
│  │ │   UAV       │ │    │ │  YOLOv3     │ │                    │
│  │ │  Platform   │ │    │ │  Detector   │ │                    │
│  │ └─────────────┘ │    │ └─────────────┘ │                    │
│  │                 │    │                 │                    │
│  │ ┌─────────────┐ │    │ ┌─────────────┐ │                    │
│  │ │   Camera    │ │    │ │  DeepSORT   │ │                    │
│  │ │   System    │ │    │ │  Tracker    │ │                    │
│  │ └─────────────┘ │    │ └─────────────┘ │                    │
│  │                 │    │                 │                    │
│  │ ┌─────────────┐ │    │ ┌─────────────┐ │                    │
│  │ │   Sensors   │ │    │ │  Siamese    │ │                    │
│  │ │   (GPS,     │ │    │ │  Networks   │ │                    │
│  │ │   IMU, etc) │ │    │ └─────────────┘ │                    │
│  │ └─────────────┘ │    │                 │                    │
│  │                 │    │ ┌─────────────┐ │                    │
│  │ ┌─────────────┐ │    │ │  Face       │ │                    │
│  │ │   Flight    │ │    │ │ Recognition │ │                    │
│  │ │ Controller  │ │    │ └─────────────┘ │                    │
│  │ └─────────────┘ │    │                 │                    │
│  └─────────────────┘    └─────────────────┘                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 5. Flow Chart Diagram

```
                    Start
                      │
                      ▼
              ┌──────────────┐
              │ Input Video  │
              │ Stream       │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Preprocess   │
              │ Frame        │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ YOLOv3       │
              │ Detection    │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Extract      │
              │ Bounding     │
              │ Boxes        │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Face         │
              │ Detection    │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Face         │
              │ Recognition  │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ DeepSORT     │
              │ Tracking     │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Update       │
              │ UAV Position │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Display      │
              │ Results      │
              └──────────────┘
                      │
                      ▼
                    Continue
```

## 6. Use Case Diagram

```
                    UAV Security System
                           │
                           ▼
    ┌─────────────────────────────────────────────────┐
    │                                                 │
    │  ┌─────────────┐    ┌─────────────┐           │
    │  │   Security  │    │   System    │           │
    │  │   Guard     │    │  Operator   │           │
    │  └─────────────┘    └─────────────┘           │
    │         │                   │                  │
    │         │                   │                  │
    │         ▼                   ▼                  │
    │  ┌─────────────┐    ┌─────────────┐           │
    │  │   Face      │    │   Mission   │           │
    │  │ Recognition │    │ Scheduling  │           │
    │  └─────────────┘    └─────────────┘           │
    │         │                   │                  │
    │         │                   │                  │
    │         ▼                   ▼                  │
    │  ┌─────────────┐    ┌─────────────┐           │
    │  │   Follow    │    │ Autonomous  │           │
    │  │   Person    │    │   Mission   │           │
    │  └─────────────┘    └─────────────┘           │
    │                                                 │
    └─────────────────────────────────────────────────┘
```

## 7. Data Flow Diagram

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Video     │───►│  Preprocess │───►│  YOLOv3     │
│   Input     │    │   Frame     │    │ Detection   │
└─────────────┘    └─────────────┘    └─────────────┘
                                              │
                                              ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Results   │◄───│  Post-      │◄───│  DeepSORT   │
│   Display   │    │  process    │    │ Tracking    │
└─────────────┘    └─────────────┘    └─────────────┘
                                              │
                                              ▼
                                   ┌─────────────┐
                                   │  Face       │
                                   │ Recognition │
                                   └─────────────┘
                                              │
                                              ▼
                                   ┌─────────────┐
                                   │  UAV        │
                                   │ Control     │
                                   └─────────────┘
```

## 8. Component Interaction Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    Component Interactions                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐        │
│  │   Video     │    │  Detection  │    │  Tracking   │        │
│  │  Capture    │───►│  Module     │───►│  Module     │        │
│  │             │    │             │    │             │        │
│  └─────────────┘    └─────────────┘    └─────────────┘        │
│         │                   │                   │              │
│         │                   │                   │              │
│         ▼                   ▼                   ▼              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐        │
│  │   Frame     │    │  Bounding   │    │  Trajectory │        │
│  │  Buffer     │    │  Boxes      │    │  Prediction │        │
│  └─────────────┘    └─────────────┘    └─────────────┘        │
│         │                   │                   │              │
│         │                   │                   │              │
│         ▼                   ▼                   ▼              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐        │
│  │   Face      │    │  Recognition│    │  UAV        │        │
│  │  Detection  │    │  Results    │    │  Commands   │        │
│  └─────────────┘    └─────────────┘    └─────────────┘        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 9. System State Diagram

```
                    Idle
                      │
                      ▼
              ┌──────────────┐
              │ Initialize   │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Mission      │
              │ Planning     │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ UAV          │
              │ Takeoff      │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Surveillance │
              │ Mode         │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Target       │
              │ Detection    │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Tracking     │
              │ Mode         │
              └──────────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Return to    │
              │ Base         │
              └──────────────┘
                      │
                      ▼
                    Idle
```

## 10. Performance Metrics Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    Performance Metrics                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Detection Performance:                                        │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ YOLOv3: 30 FPS on NVIDIA GTX 1080                    │   │
│  │ Face Detection: 95% accuracy                          │   │
│  │ Person Detection: 90% accuracy in crowded scenes      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Tracking Performance:                                         │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ DeepSORT: 100+ FPS tracking                           │   │
│  │ Siamese Networks: Real-time template tracking         │   │
│  │ Multi-object: Support for 50+ simultaneous tracks    │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  System Performance:                                           │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Video Processing: 1080p at 30 FPS                     │   │
│  │ Memory Usage: <4GB RAM                                 │   │
│  │ GPU Utilization: 80% on NVIDIA GPU                     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Notes

These diagrams represent the key architectural and operational aspects of the UAV-Based Autonomous Security System as described in the project report. The actual implementation may vary based on specific requirements and hardware configurations.

### Key Features Represented:

1. **Modular Architecture**: Clear separation between hardware and software components
2. **Real-time Processing**: Efficient pipeline for video processing and analysis
3. **Multi-stage Detection**: Person detection → Face detection → Face recognition → Tracking
4. **Autonomous Control**: UAV can operate independently with mission planning
5. **Scalable Design**: Components can be upgraded or replaced independently

### System Integration Points:

- **Video Input**: Camera feeds from UAV to processing server
- **Detection Output**: Bounding boxes from YOLOv3 to DeepSORT
- **Tracking Data**: Trajectory information to UAV control system
- **Mission Control**: Commands from base station to UAV platform
- **Results Display**: Processed video with annotations and tracking data 