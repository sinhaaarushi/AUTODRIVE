# AUTODRIVE Architecture Documentation

## System Overview

AUTODRIVE is a multi-model AI system designed for autonomous driving simulation. The architecture consists of three main AI models working in parallel to process real-time camera feeds and provide comprehensive driving assistance.

## High-Level Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Camera Input  │    │   Image Pre-    │    │   Multi-Model   │
│   (Real-time)   │───▶│   processing    │───▶│   AI Pipeline   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
                       ┌─────────────────────────────────────────┐
                       │                                         │
                       ▼                                         ▼
              ┌─────────────────┐                    ┌─────────────────┐
              │   Steering      │                    │   Visualization │
              │   Prediction    │                    │   & Feedback    │
              │   (CNN)         │                    │   (Real-time)   │
              └─────────────────┘                    └─────────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   Lane          │
              │   Detection     │
              │   (YOLO)        │
              └─────────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   Object        │
              │   Detection     │
              │   (YOLO)        │
              └─────────────────┘
```

## Model Architecture Details

### 1. Steering Angle Prediction Model

**Architecture**: Custom Convolutional Neural Network (CNN)

```
Input: 66x200x3 RGB Image
    │
    ▼
┌─────────────────┐
│ Conv2D (5x5, 24)│ → ReLU → MaxPool
└─────────────────┘
    │
    ▼
┌─────────────────┐
│ Conv2D (5x5, 36)│ → ReLU → MaxPool
└─────────────────┘
    │
    ▼
┌─────────────────┐
│ Conv2D (5x5, 48)│ → ReLU → MaxPool
└─────────────────┘
    │
    ▼
┌─────────────────┐
│ Conv2D (3x3, 64)│ → ReLU
└─────────────────┘
    │
    ▼
┌─────────────────┐
│ Conv2D (3x3, 64)│ → ReLU
└─────────────────┘
    │
    ▼
┌─────────────────┐
│ Flatten         │
└─────────────────┘
    │
    ▼
┌─────────────────┐
│ Dense (1164)    │ → ReLU → Dropout(0.8)
└─────────────────┘
    │
    ▼
┌─────────────────┐
│ Dense (100)     │ → ReLU → Dropout(0.8)
└─────────────────┘
    │
    ▼
┌─────────────────┐
│ Dense (50)      │ → ReLU → Dropout(0.8)
└─────────────────┘
    │
    ▼
┌─────────────────┐
│ Dense (10)      │ → ReLU → Dropout(0.8)
└─────────────────┘
    │
    ▼
┌─────────────────┐
│ Dense (1)       │ → atan(x) * 2
└─────────────────┘
    │
    ▼
Output: Steering Angle (degrees)
```

**Key Features**:
- 5 convolutional layers with increasing filter sizes
- Dropout regularization (0.8) for overfitting prevention
- L2 regularization for weight decay
- Adam optimizer with learning rate 1e-4
- Mean squared error loss function

### 2. Lane Detection Model

**Architecture**: YOLO11 (You Only Look Once)

```
Input: Full Resolution Image
    │
    ▼
┌─────────────────┐
│ YOLO11 Backbone │ → Feature Extraction
└─────────────────┘
    │
    ▼
┌─────────────────┐
│ Segmentation    │ → Lane Boundary Detection
│ Head           │
└─────────────────┘
    │
    ▼
Output: Lane Segmentation Masks
```

**Key Features**:
- Real-time lane boundary detection
- Confidence threshold: 0.5
- Output: Binary masks for lane regions
- Color coding: Light green for detected lanes

### 3. Object Detection Model

**Architecture**: YOLO11s (Small variant)

```
Input: Full Resolution Image
    │
    ▼
┌─────────────────┐
│ YOLO11s Backbone│ → Feature Extraction
└─────────────────┘
    │
    ▼
┌─────────────────┐
│ Detection Head  │ → Bounding Box + Class Prediction
└─────────────────┘
    │
    ▼
Output: Bounding Boxes + Class Labels
```

**Key Features**:
- Multi-class object detection
- Confidence threshold: 0.5
- Classes: vehicles, pedestrians, traffic signs, etc.
- Output: Bounding boxes with confidence scores

## Data Flow

### 1. Input Processing
- **Source**: Real-time camera feed or pre-recorded video
- **Preprocessing**: 
  - Resize to 200x66 for steering prediction
  - Normalize pixel values to [0,1]
  - Maintain original resolution for detection models

### 2. Multi-Threaded Inference
```python
with concurrent.futures.ThreadPoolExecutor() as executor:
    future_steering = executor.submit(steering_model.predict, image)
    future_lane = executor.submit(lane_model.predict, image)
    future_object = executor.submit(object_model.predict, image)
```

### 3. Output Integration
- **Steering Angle**: Real-time prediction with smoothing
- **Lane Detection**: Overlay on original image
- **Object Detection**: Bounding boxes with labels
- **Visualization**: Combined display with multiple windows

## Performance Characteristics

### Computational Requirements
- **CPU**: Multi-core processor (4+ cores recommended)
- **GPU**: CUDA-compatible GPU for faster inference
- **RAM**: 8GB+ for smooth operation
- **Storage**: 10GB+ for models and dataset

### Real-time Performance
- **Frame Rate**: 30 FPS target
- **Latency**: <100ms end-to-end processing
- **Accuracy**: 87% confidence threshold
- **Concurrent Models**: 3 AI models running simultaneously

## Training Pipeline

### Data Preparation
- **Dataset**: 45,000+ driving images
- **Labels**: Steering angles, lane boundaries, object annotations
- **Augmentation**: Random cropping, rotation, brightness adjustment

### Training Process
1. **Data Loading**: Batch processing with data augmentation
2. **Model Training**: Custom training loop with TensorBoard logging
3. **Validation**: Real-time validation on test set
4. **Checkpointing**: Model saving at regular intervals

### Hyperparameters
- **Batch Size**: 100
- **Learning Rate**: 1e-4
- **Epochs**: 30
- **Optimizer**: Adam
- **Loss Function**: Mean Squared Error

## Deployment Architecture

### Local Development
- **Environment**: Python 3.8+ with virtual environment
- **Dependencies**: requirements.txt
- **Setup**: python setup.py install

### Production Considerations
- **Model Optimization**: TensorRT for GPU acceleration
- **Scalability**: Docker containerization
- **Monitoring**: TensorBoard for training, custom metrics for inference
- **Error Handling**: Graceful degradation and fallback mechanisms

## Security and Safety

### Model Safety
- **Input Validation**: Image format and size validation
- **Output Sanitization**: Steering angle bounds checking
- **Confidence Filtering**: Low-confidence predictions are filtered out

### System Safety
- **Graceful Degradation**: System continues with reduced functionality
- **Error Recovery**: Automatic model reloading on failure
- **Logging**: Comprehensive logging for debugging and monitoring

## Future Enhancements

### Planned Improvements
1. **Model Optimization**: Quantization and pruning for edge deployment
2. **Additional Sensors**: Integration with LiDAR and radar data
3. **Advanced Features**: Traffic sign recognition, pedestrian prediction
4. **Cloud Integration**: Remote model updates and data collection

### Scalability
1. **Distributed Training**: Multi-GPU training support
2. **Model Serving**: REST API for remote inference
3. **Data Pipeline**: Automated data collection and labeling
4. **A/B Testing**: Model comparison and evaluation framework 