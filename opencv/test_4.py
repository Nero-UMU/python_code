import cv2

dog = cv2.imread('doge.jpg')
cat = cv2.imread('cat.jpg')

dog = cv2.resize(dog, (800, 800))
cat = cv2.resize(cat, (800, 800))
print(dog.shape)
print(cat.shape)
both = cv2.addWeighted(dog, 1, cat, 1, 0)
cv2.imshow('cat_doge',both)
cv2.waitKey(0)