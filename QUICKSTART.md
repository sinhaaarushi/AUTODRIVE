# 🚀 Quick Start Guide

Get AUTODRIVE up and running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- Git
- 8GB+ RAM
- CUDA-compatible GPU (optional, but recommended)

## Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/autodrive.git
cd autodrive
```

## Step 2: Set Up Environment

### Option A: Using Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv autodrive_env

# Activate virtual environment
# On Windows:
autodrive_env\Scripts\activate
# On macOS/Linux:
source autodrive_env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Option B: Using Conda

```bash
# Create conda environment
conda create -n autodrive python=3.8
conda activate autodrive

# Install dependencies
pip install -r requirements.txt
```

## Step 3: Download Pre-trained Models

You'll need to download the pre-trained models. Create the directories and place the model files:

```bash
# Create model directories
mkdir -p saved_models/regression_model
mkdir -p saved_models/lane_segmentation_model
mkdir -p saved_models/object_detection_model

# Download models (you'll need to provide the actual model files)
# Place them in the respective directories:
# - saved_models/regression_model/model.ckpt
# - saved_models/lane_segmentation_model/best_yolo11_lane_segmentation.pt
# - saved_models/object_detection_model/yolo11s-seg.pt
```

## Step 4: Run the Demo

### Complete Simulation
```bash
python src/inference/run_fsd_inference.py
```

### Lane Detection Only
```bash
python src/inference/run_segmentation_obj_det.py
```

### Steering Prediction Only
```bash
python src/inference/run_steering_angle_prediction.py
```

## Step 5: View Results

The system will open multiple windows showing:
- **Original Frame**: Raw camera input
- **Segmented Frame**: Lane and object detection results
- **Steering Wheel**: Real-time steering angle visualization

Press 'q' to quit the simulation.

## Troubleshooting

### Common Issues

1. **Import Error: No module named 'tensorflow'**
   ```bash
   pip install tensorflow==1.15.0
   ```

2. **CUDA Error**
   - Install CUDA-compatible TensorFlow version
   - Or use CPU-only version: `pip install tensorflow-cpu==1.15.0`

3. **OpenCV Error**
   ```bash
   pip install opencv-python==4.8.1.78
   ```

4. **Model Files Missing**
   - Ensure all model files are in the correct directories
   - Check file permissions

### Performance Tips

- **GPU Acceleration**: Use CUDA-compatible GPU for faster inference
- **Memory**: Close other applications to free up RAM
- **Resolution**: Lower image resolution for better performance

## Next Steps

- Read the [full documentation](README.md)
- Explore the [architecture](docs/ARCHITECTURE.md)
- Train your own models using the training scripts
- Contribute to the project

## Support

- Create an [issue](https://github.com/yourusername/autodrive/issues) for bugs
- Check the [FAQ](docs/FAQ.md) for common questions
- Join our [discussions](https://github.com/yourusername/autodrive/discussions)

---

🎉 **Congratulations! You're now running AUTODRIVE!** 