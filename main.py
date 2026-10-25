import cv2
import numpy as np

def apply_color_filter(image,filter_type):
    filtered_image  = image.copy()
    if filter_type == 'red tint':
     filtered_image[:, :, 1] = 0
     filtered_image[:, :, 0] = 0 
    elif filter_type == 'blue tint':
       filtered_image[:, :, 1] = 0
       filtered_image[:, :, 2] = 0 
    elif filter_type == 'green tint':
       filtered_image[:, :, 0] = 0
       filtered_image[:, :, 2] = 0 
    elif filter_type == 'increase red':
       filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2],50)
    elif filter_type == 'decrease blue':
       filtered_image[:, :, 0] = cv2.add(filtered_image[:, :, 0],50)
    return filtered_image

image_path = 'example.jpg'
image =cv2.imread(image_path)

if image is None:
   print("image is not found")
else:
   filter_type = 'original'

   print("press the following keys to apply filters")
   print("r-Red tint")
   print("b-Blue tint") 
   print("g-Green tint")
   print("i-increase red intensity")
   print("d-decrease blue intensity")
   print("q-quit")

   while True:
      filtered_image = apply_color_filter(image,filter_type)
      cv2.imshow("filtered image",filtered_image)
      key = cv2.waitKey(0) & 0xff

      if key == ord('r'):
         filter_type = 'Red tint'
      elif key == ord('b'):
         filter_type = 'Blue tint'
      elif key == ord('g'):
         filter_type = 'Green tint'
      elif key == ord('i'):
         filter_type = 'increase red intensity'
      elif  key == ord('d'):
         filter_type = 'decrease blue intensity'
      elif key == ord('q'):
         filter_type = 'quit'
      else:
         print("invalid key! please use either 'r','b','g','i','d'or'q'")
cv2.destroyAllWindows()            