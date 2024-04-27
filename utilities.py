def resize_image(img, target_width, target_height):
    width, height = img.size
    aspect_ratio = width / height

    # Calculate the new dimensions while maintaining the aspect ratio
    if aspect_ratio > 1:
        new_width = target_width
        new_height = int(target_width / aspect_ratio)
    else:
        new_width = int(target_height * aspect_ratio)
        new_height = target_height

    # Resize the image
    resized_img = img.resize((new_width, new_height))
    return resized_img
