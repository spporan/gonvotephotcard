import base64
import os
import json

base_path = 'images'
frames = [
    # Order matters
    {'name': 'জুলাই সনদে হ্যাঁ বলুন', 'filename': 'Gono-bot-8.PNG'},
    {'name': 'দেশের স্বার্থ রক্ষায় "হ্যাঁ" দিন', 'filename': 'Gono-bot-1.PNG'},
    {'name': 'দেশ সংস্কারে হ্যাঁ দিন', 'filename': 'Gono-bot-2.PNG'},
    {'name': 'দেশের মালিকানা বুঝে নিতে হ্যাঁ বলুন', 'filename': 'Gono-bot-3.PNG'},
    {'name': 'জুলাই সনদে হ্যাঁ বলুন', 'filename': 'Gono-bot-4.PNG'},
    {'name': 'দেশের স্বার্থ রক্ষায় "হ্যাঁ" দিন', 'filename': 'Gono-bot-5.PNG'},
    {'name': 'দেশ সংস্কারে হ্যাঁ দিন', 'filename': 'Gono-bot-6.PNG'},
    {'name': 'দেশের মালিকানা বুঝে নিতে হ্যাঁ বলুন', 'filename': 'Gono-bot-7.PNG'}
]

# Check for frame 9
if os.path.exists(os.path.join(base_path, 'Gono-bot-9.PNG')):
    frames.append({'name': 'জুলাই সনদে হ্যাঁ বলুন', 'filename': 'Gono-bot-9.PNG'})

output_frames = []

for frame in frames:
    path = os.path.join(base_path, frame['filename'])
    try:
        with open(path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            output_frames.append({
                "name": frame['name'],
                "url": f"data:image/png;base64,{encoded_string}"
            })
    except FileNotFoundError:
        print(f"Error: Could not find {path}")

# Write to JS file
with open('frames_data.js', 'w') as outfile:
    json_data = json.dumps(output_frames)
    outfile.write(f"window.predefinedFrames = {json_data};")

print(f"Successfully created frames_data.js with {len(output_frames)} frames.")
