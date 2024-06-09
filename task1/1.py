import cv2, argparse, os
import numpy as np
from matplotlib import pyplot as plt

radius, t0 = 3, 0.1
window_size = 2 * radius + 1
w_size = (window_size, window_size)
kernel = np.ones((window_size, window_size))

def calc_dark(img):
    # 得到暗通道图像
    merge_img = np.min(img, axis=-1)
    return cv2.erode(merge_img, kernel)

def calc_a(dark, img):
    # 估计全球大气光 a 值
    w, h, _ = img.shape
    idn, tot_pixes = np.argsort(dark.reshape(-1))[::-1], w * h
    
    a, sample = [0., 0., 0.], tot_pixes // 1000
    for i in range(sample):
        x, y = idn[i] // h, idn[i] % h
        for j in range(3):
            a[j] += img[x][y][j]
    for i in range(3):
        a[i] /= sample
    return a
        
def calc_tx(img, a :list):
    # 获得 t(x) 的估计值
    omega = 0.95
    n_img = img.copy()
    for i in range(3):
        n_img[:, :, i] = n_img[:, :, i] / a[i]
    
    return 1 - omega * calc_dark(n_img)
    
def calc_jx(img, tx, a):
    n_img = img.copy()
    tx = np.maximum(tx, t0)
    for i in range(3):
        n_img[:, :, i] = (n_img[:, :, i] - a[i]) / tx + a[i]
    return n_img
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image Dehazing')
    parser.add_argument('-i', type=str, help='Image path')
    parser.add_argument('-o', type=str, default='res.bmp', help='Output path')
    
    args = parser.parse_args()
    path = args.i
    img = cv2.imread(path, 1)
    if img is None:
        print('Image not found')
        exit()

    img = img.astype(np.float32) / 255.0
    dark = calc_dark(img)
    a = calc_a(dark, img)
    tx = calc_tx(img, a)
    # tx = cv2.ximgproc.guidedFilter(img, tx, radius=15, eps=0.001, dDepth=-1)
    ans = calc_jx(img, tx, a)
    
    cv2.imwrite(parser.parse_args().o, ans * 255)
    
    

            
    

