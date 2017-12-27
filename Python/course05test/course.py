import cv2

person = cv2.imread("person.jpg",cv2.IMREAD_COLOR)

icon_gray = cv2.cvtColor(person,cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(icon_gray, 190, 255, cv2.THRESH_BINARY_INV)

icon_fg = cv2.bitwise_and(person,person,mask=mask)

cv2.imwrite("result04.png",icon_fg)
