from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2
from openpyxl import Workbook
import colorsys
import numpy as np

# construct the argument parser and parse the arguments
from sklearn.metrics import pairwise_distances_argmin_min

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True, help = "Path to the image")
# ap.add_argument("-c", "--clusters", required = True, type = int, help = "# of clusters")
# args = vars(ap.parse_args())
# load the image and convert it from BGR to RGB so that
# we can dispaly it with matplotlib
# print("file name : "+args["image"])
#image = cv2.imread(args["image"])
# #
write_wb = Workbook()
write_ws = write_wb.active
write_ws.cell(1, 1, "result")
for i in range(10):
    #image = "images/lip_data/test"+ str(i+1) +".png"
    image = cv2.imread("images/lip_data/test"+ str(i+1) +".png")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # show our image
    # plt.figure()
    # plt.axis("off")
    # plt.imshow(image)
    # reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    # cluster the pixel intensities
    #clt = KMeans(n_clusters = args["clusters"])
    clt = KMeans(n_clusters = 2)
    clt.fit(image)
    # build a histogram of clusters and then create a figure
    # representing the number of pixels labeled to each color
    hist = utils.centroid_histogram(clt)
    # closest, _ = pairwise_distances_argmin_min(KMeans.cluster_centers_, X)
    #bar = utils.plot_colors(hist, clt.cluster_centers_)
    data_list = []
    data_list.append("test"+ str(i+1) +".png")
    for a in range(2):
        for b in range(3):
            data_list.append(clt.cluster_centers_[a][b])
    write_ws.append(data_list)

    data_list = []
    write_wb.save("images/data.xlsx")
# show our color bart
# plt.figure()
# plt.axis("off")
# plt.imshow(bar)
# plt.show()