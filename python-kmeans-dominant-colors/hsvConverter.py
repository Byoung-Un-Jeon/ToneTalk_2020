import cv2

# 이미지파일을 컬러로 읽어온다.
img_color = cv2.imread('images/test4.png')
# 이미지의 높이와 너비를 갖고온다.
height,width = img_color.shape[:2]
# hsv이미지로 변환한다.
img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)

# 범위를 정하여 hsv이미지에서 원하는 색 영역을 바이너리 이미지로 생성한다.
# (가운데와 마지막값은 너무어두워서 검은색에 가까운색과 너무 옅어서 흰색에 가까운색을 제외시키기위해 30으로해야한다.
lower_blue = (0, 48, 80)
upper_blue = (20, 255, 255)
# 앞서 선언한 범위값을 사용하여 바이너리 이미지를 얻는다.(범위내에 있는 픽셀들은 흰색이되고 나머지는 검은색이 된다.)
img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)

# 원본이미지에서 범위값에 해당하는 영상부분을 흭득한다.
img_result = cv2.bitwise_and(img_color, img_color, mask = img_mask)

# 화면에 영상결과들 보여준다.
cv2.imshow('img_color', img_color)
cv2.imshow('img_mask', img_mask)
cv2.imshow('img_result', img_result)

# 키보드입력대기함수 및 자원해제
cv2.waitKey(0)
cv2.destroyAllWindows()