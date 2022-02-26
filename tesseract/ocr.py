import pytesseract

class image_to_string:

  def img_to_string(self, image):
    return pytesseract.image_to_string(image)
