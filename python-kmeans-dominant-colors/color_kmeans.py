from sklearn.cluster import KMeans
import utils
import cv2
from openpyxl import Workbook

import matplotlib.pyplot as plt
import colorsys
import numpy as np

#엑셀로 보내기 위해서 엑셀 환경 만들어준다.
write_wb = Workbook()
write_ws = write_wb.active
#1,1 칸에는 result를 입력해준다.
write_ws.cell(1, 1, "result")
#괄호 안에 들어가는게 범위 655개 다하면 시간이 걸리니 테스트할때는 10개만.
for i in range(20):
    #openCV를 이용해 이미지를 읽어온다.
    image = cv2.imread("images/lip_data/test"+ str(i+1) +".png")
    #기본적으로 BGR값으로 읽어오기 때문에 RGB값으로 변환시켜준다.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    #기본적으로 이미지에 색이 두가지만 있다고 가정한다. -> 클러스터링 2개만한다면 입술색과 피부색 데이터를 가져올 수 있다.
    clt = KMeans(n_clusters = 2)
    clt.fit(image)
    hist = utils.centroid_histogram(clt)
    data_list = []
    data_list.append("test"+ str(i+1) +".png")
    #히스토그램 bar로 나타난 이미지에서 rgb값을 추출한다.
    #첫번째 반복이 두번인 이유는 클러스터링으로 두가지색을 했기 때문이다.
    #두번째 반복이 세번인 이유는 RGB세가지 값을 추출하기 때문이다.
    for a in range(2):
        for b in range(3):
            data_list.append(clt.cluster_centers_[a][b])
    #추출되어진 RGB값을 엑셀에 저장한다.
    write_ws.append(data_list)
    data_list = []
    write_wb.save("images/data.xlsx")