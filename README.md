# Campaign Photo Frame App

## Design
- **Developed by**: Poran
- **Designed by**: Sairan

## Features
- Select a frame from the gallery.
- Upload your photo.
- Zoom and position your photo.
- Download the final result.
- Share directly (if supported).

## Technical Note: Local Usage
This app is optimized to run locally (by opening `index.html` directly) without a web server. To achieve this, the frame images are encoded as Base64 strings in `frames_data.js`.

### How to Update Frames
If you add or ensure new images in the `images/` folder:
1. Ensure you have Python installed.
2. Run the included script:
   ```bash
   python3 encode_frames.py > frames_data.js
   ```
3. Refresh `index.html`.

This updates the app with your new images while maintaining the "Download" functionality on local files.
