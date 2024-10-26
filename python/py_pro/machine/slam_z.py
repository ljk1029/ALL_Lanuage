import cv2
import numpy as np

def draw_matches(img1, kp1, img2, kp2, matches): 
    rows1, cols1 = img1.shape[:2] 
    rows2, cols2 = img2.shape[:2] 
    img_matches = np.zeros((max(rows1, rows2), cols1 + cols2, 3), dtype=np.uint8) 
    img_matches[:rows1, :cols1, :] = img1 
    img_matches[:rows2, cols1:cols1 + cols2, :] = img2 
    for match in matches: 
        img_matches[match[0][1]:match[0][1] + match[1][1], match[0][0]:match[0][0] + match[1][0], :] = (0, 255, 0) 
        return img_matches
    
def feature_matching(img1, img2): 
    sift = cv2.xfeatures2d.SIFT_create() 
    kp1, des1 = sift.detectAndCompute(img1, None) 
    kp2, des2 = sift.detectAndCompute(img2, None) 
    if len(kp1) == 0 or len(kp2) == 0: 
        return None 
    bf = cv2.BFMatcher(cv2.NORM_L2, False) 
    matches = bf.match(des1, des2) 
    return matches

def slam_example(img1_path, img2_path, map_path): # 读取图像和地图 
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE) 
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE) 
    map_img = cv2.imread(map_path, cv2.IMREAD_GRAYSCALE) # 提取特征点 
    kp1 = [] 
    kp2 = [] 
    for i in range(len(map_img)): 
        for j in range(len(map_img[0])): 
            if map_img[i][j] != 0: kp1.append(cv2.KeyPoint(j, i, 10)) 
            kp2.append(cv2.KeyPoint(j, i, 10)) # 匹配特征点 
            matches = feature_matching(img1, img2) # 绘制匹配结果 
            if matches is not None: 
                img_matches = draw_matches(img1, kp1, img2, kp2, matches) 
                cv2.imshow('Matches', img_matches) 
                cv2.waitKey(0)

if __name__ == '__main__': 
    slam_example('img1.jpg', 'img2.jpg', 'map.jpg')