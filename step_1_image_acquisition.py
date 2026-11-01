"""Step 1 — Copy into the Unibotics Follow Line code editor."""
import HAL
import WebGUI

while True:
    image = HAL.getImage()
    WebGUI.showImage(image)
