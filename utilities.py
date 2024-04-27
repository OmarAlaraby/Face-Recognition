import cv2
def resize_image(img, target_width, target_height):
    resized_img = cv2.resize(img, (target_width, target_height))
    return resized_img
