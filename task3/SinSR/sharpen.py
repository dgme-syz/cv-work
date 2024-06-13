import cv2, argparse, os
import numpy as np

def main(args):
    img = cv2.imread(args.image_path)
    kernel = np.array([[0, -1, 0], 
                    [-1, 5, -1], 
                    [0, -1, 0]], np.float32)
    dst = np.zeros_like(img)
    for i in range(3):
        dst[:, :, i] = cv2.filter2D(img[:, :, i], -1, kernel)
    # 如果输出路径是文件夹
    if os.path.isdir(args.output_path):
        filename = os.path.basename(args.image_path)
        output_path = os.path.join(args.output_path, filename)
        cv2.imwrite(output_path, dst)
    else:
        cv2.imwrite(args.output_path, dst)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sharpen an image')
    parser.add_argument('--image_path', help='path to the image')
    parser.add_argument('--output_path', help='path to the output image')
    args = parser.parse_args()
    # 如果输入路径是文件夹
    image_path = args.image_path
    if os.path.isdir(image_path):
        for filename in os.listdir(image_path):
            img_path = os.path.join(image_path, filename)
            args.image_path = img_path
            main(args)
    else:
        main(args)