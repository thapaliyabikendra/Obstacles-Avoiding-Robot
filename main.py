import cv2
from darkflow.net.build import TFNet

img = cv2.imread('image.jpg')
print(img.shape)
resized = cv2.resize(img, (256, 256))
print(resized.shape)

options = {"model": "cfg/tiny.cfg", 
           "load": "tiny.weights", 
           "threshold": 0.1}
tfnet = TFNet(options)

original_img = cv2.imread("image.jpg")
#original_img = cv2.resize(original_img, (224, 224))
original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)

results = tfnet.return_predict(original_img)

def boxing(original_img, predictions):
    newImage = np.copy(original_img)

    for result in predictions:
        top_x = result['topleft']['x']
        top_y = result['topleft']['y']

        btm_x = result['bottomright']['x']
        btm_y = result['bottomright']['y']

        confidence = result['confidence']
        label = result['label'] + " " + str(round(confidence, 3))

        if confidence > 0.3:
            newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (255,0,0), 3)
            newImage = cv2.putText(newImage, label, (top_x, top_y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.8, (0, 230, 0), 1, cv2.LINE_AA)
            
    return newImage

import matplotlib.pyplot as plt

_, ax = plt.subplots(figsize=(20, 10))
ax.imshow(boxing(original_img, results))
