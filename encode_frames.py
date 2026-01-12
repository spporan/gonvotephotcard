import base64
import os
import json

base_path = 'images'
frames = [
    {'name': 'জুলাই সনদে হ্যাঁ বলুন', 'filename': 'Gono-bot-8.PNG'},
    {'name': 'দেশের স্বার্থ রক্ষায় "হ্যাঁ" দিন', 'filename': 'Gono-bot-1.PNG'},
    {'name': 'দেশ সংস্কারে হ্যাঁ দিন', 'filename': 'Gono-bot-2.PNG'},
    {'name': 'দেশের মালিকানা বুঝে নিতে হ্যাঁ বলুন', 'filename': 'Gono-bot-3.PNG'},
    {'name': 'জুলাই সনদে হ্যাঁ বলুন', 'filename': 'Gono-bot-4.PNG'},
    {'name': 'দেশের স্বার্থ রক্ষায় "হ্যাঁ" দিন', 'filename': 'Gono-bot-5.PNG'},
    {'name': 'দেশ সংস্কারে হ্যাঁ দিন', 'filename': 'Gono-bot-6.PNG'},
    {'name': 'দেশের মালিকানা বুঝে নিতে হ্যাঁ বলুন', 'filename': 'Gono-bot-7.PNG'}
]

# Add the 9th frame if it exists (user had 9 in step 103)
if os.path.exists(os.path.join(base_path, 'Gono-bot-9.PNG')):
    frames.append({'name': 'জুলাই সনদে হ্যাঁ বলুন', 'filename': 'Gono-bot-9.PNG'})

print("const predefinedFrames = [")

for i, frame in enumerate(frames):
    path = os.path.join(base_path, frame['filename'])
    try:
        with open(path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            prefix = "data:image/png;base64,"
            # Use a slightly optimized format slightly to print
            print(f"    {{")
            print(f"        name: '{frame['name']}',")
            print(f"        url: '{prefix}{encoded_string}'")
            print(f"    }}{',' if i < len(frames)-1 else ''}")
    except FileNotFoundError:
        print(f"    // Error: Could not find {path}")

print("];")
