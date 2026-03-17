# Assets Directory

This directory contains demo images and GIFs for the AUTODRIVE project.

## Required Images

Please add the following images to showcase your project:

1. **demo.gif** - A short GIF showing the real-time simulation in action
2. **simulation.png** - Screenshot of the main simulation interface
3. **lane_detection.png** - Screenshot showing lane detection results
4. **object_detection.png** - Screenshot showing object detection results
5. **steering.png** - Screenshot showing steering angle prediction

## Image Guidelines

- **Resolution**: Use high-quality images (1920x1080 or higher)
- **Format**: PNG for screenshots, GIF for animations
- **Content**: Show clear examples of the AI models working
- **File Size**: Keep images under 5MB for optimal loading

## How to Capture Demo Images

1. **Run the simulation**: `python src/inference/run_fsd_inference.py`
2. **Take screenshots** of the different windows:
   - Original camera feed
   - Segmented image with lane detection
   - Steering wheel visualization
3. **Record a short video** and convert to GIF for the demo animation

## Example Commands

```bash
# On macOS, use Cmd+Shift+4 to capture screenshots
# On Windows, use Snipping Tool or Win+Shift+S
# On Linux, use gnome-screenshot or similar tools
``` 