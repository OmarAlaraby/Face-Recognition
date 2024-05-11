import os
import json

def generate_json(images_folder, output_file):
    data = []
    for filename in os.listdir(images_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(images_folder, filename)
            data.append({"path": image_path, "type": "Banana"})

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

images_folder = "Images/bananas"
output_file = "Data/bananas.json"

generate_json(images_folder, output_file)
