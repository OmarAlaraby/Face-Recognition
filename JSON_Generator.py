import os
import json

def generate_json(images_folder, output_file):
    data = []
    for filename in os.listdir(images_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(images_folder, filename)
            data.append({"path": image_path, "type": "Female"})

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)  # Add indentation for readability

# Example usage
images_folder = "Images/Women"  # Replace with your folder path
output_file = "Data/women.json"

generate_json(images_folder, output_file)

print(f"JSON file generated: {output_file}")
