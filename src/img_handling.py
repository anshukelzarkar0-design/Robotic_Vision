import cv2
def read_image(path):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Image not found at path: {path}")
    return img
def save_image(path, img):
    cv2.imwrite(path, img)
img = read_image(r"assets\Screenshot 2025-08-10 143614.png")
print(img)
cv2.imshow('Prallhad', img)
cv2.waitKey(0)
cv2.destroyAllWindows()