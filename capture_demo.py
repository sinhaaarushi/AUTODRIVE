#!/usr/bin/env python3
"""
Demo Capture Script for AUTODRIVE
This script helps capture demo images and screenshots for the project documentation.
"""

import cv2
import os
import time
import numpy as np
from datetime import datetime

def create_demo_image():
    """Create a sample demo image for documentation purposes."""
    
    # Create a sample image (640x480)
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    
    # Add some road-like elements
    # Road (gray)
    cv2.rectangle(img, (0, 240), (640, 480), (128, 128, 128), -1)
    
    # Lane markings (white)
    cv2.line(img, (320, 240), (320, 480), (255, 255, 255), 5)
    cv2.line(img, (160, 240), (160, 480), (255, 255, 255), 3)
    cv2.line(img, (480, 240), (480, 480), (255, 255, 255), 3)
    
    # Sky (blue)
    cv2.rectangle(img, (0, 0), (640, 240), (135, 206, 235), -1)
    
    # Add some objects (cars, trees)
    # Car 1
    cv2.rectangle(img, (100, 300), (200, 350), (0, 0, 255), -1)
    cv2.rectangle(img, (100, 350), (200, 380), (0, 0, 255), -1)
    
    # Car 2
    cv2.rectangle(img, (400, 320), (500, 370), (255, 0, 0), -1)
    cv2.rectangle(img, (400, 370), (500, 400), (255, 0, 0), -1)
    
    # Trees
    cv2.circle(img, (50, 150), 30, (34, 139, 34), -1)
    cv2.circle(img, (590, 150), 30, (34, 139, 34), -1)
    
    return img

def create_steering_wheel():
    """Create a steering wheel image."""
    
    # Create a circular steering wheel
    img = np.zeros((300, 300, 3), dtype=np.uint8)
    center = (150, 150)
    radius = 100
    
    # Outer circle
    cv2.circle(img, center, radius, (255, 255, 255), 3)
    
    # Inner circle
    cv2.circle(img, center, radius-20, (255, 255, 255), 2)
    
    # Spokes
    for i in range(3):
        angle = i * 120
        x1 = center[0] + int((radius-40) * np.cos(np.radians(angle)))
        y1 = center[1] + int((radius-40) * np.sin(np.radians(angle)))
        x2 = center[0] + int((radius-10) * np.cos(np.radians(angle)))
        y2 = center[1] + int((radius-10) * np.sin(np.radians(angle)))
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
    
    return img

def create_segmented_image(original_img):
    """Create a segmented version of the original image."""
    
    segmented = original_img.copy()
    
    # Add lane segmentation (light green)
    cv2.rectangle(segmented, (0, 240), (640, 480), (144, 238, 144), -1)
    
    # Add object detection boxes
    # Car 1 with label
    cv2.rectangle(segmented, (100, 300), (200, 380), (0, 0, 255), 2)
    cv2.putText(segmented, "Car: 0.95", (100, 295), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    
    # Car 2 with label
    cv2.rectangle(segmented, (400, 320), (500, 400), (255, 0, 0), 2)
    cv2.putText(segmented, "Car: 0.87", (400, 315), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    
    return segmented

def capture_demo_images():
    """Capture and save demo images for the project."""
    
    # Create assets directory if it doesn't exist
    os.makedirs("assets", exist_ok=True)
    
    print("🎬 Creating demo images for AUTODRIVE...")
    
    # Create demo images
    original_img = create_demo_image()
    segmented_img = create_segmented_image(original_img)
    steering_wheel = create_steering_wheel()
    
    # Save images
    cv2.imwrite("assets/simulation.png", original_img)
    cv2.imwrite("assets/lane_detection.png", segmented_img)
    cv2.imwrite("assets/object_detection.png", segmented_img)
    cv2.imwrite("assets/steering.png", steering_wheel)
    
    print("✅ Demo images created successfully!")
    print("📁 Images saved in assets/ directory:")
    print("   - simulation.png")
    print("   - lane_detection.png")
    print("   - object_detection.png")
    print("   - steering.png")
    
    # Display images
    print("\n🖼️  Displaying demo images (press any key to close)...")
    
    cv2.imshow("Original Simulation", original_img)
    cv2.imshow("Lane Detection", segmented_img)
    cv2.imshow("Object Detection", segmented_img)
    cv2.imshow("Steering Wheel", steering_wheel)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def create_demo_video():
    """Create a simple demo video."""
    
    print("🎥 Creating demo video...")
    
    # Video parameters
    fps = 30
    duration = 5  # seconds
    width, height = 640, 480
    
    # Create video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('assets/demo.mp4', fourcc, fps, (width, height))
    
    # Create frames
    for i in range(fps * duration):
        # Create frame with slight variations
        img = create_demo_image()
        
        # Add some movement (simple animation)
        offset = int(10 * np.sin(i * 0.1))
        cv2.circle(img, (320 + offset, 150), 20, (255, 255, 0), -1)  # Moving object
        
        # Add frame number
        cv2.putText(img, f"Frame: {i}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        out.write(img)
    
    out.release()
    print("✅ Demo video created: assets/demo.mp4")

if __name__ == "__main__":
    print("🚗 AUTODRIVE Demo Capture Tool")
    print("=" * 40)
    
    # Capture demo images
    capture_demo_images()
    
    # Create demo video
    create_demo_video()
    
    print("\n🎉 All demo content created successfully!")
    print("📝 You can now use these images in your README.md file.")
    print("💡 Remember to replace these with actual screenshots from your running system.") 