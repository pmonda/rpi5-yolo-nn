from tiny_yolo import *


if __name__ == "__main__":
    from PIL import Image
    from utils import *

    model = TinyYoloNet()
    model.float()
    model.load_weights("C:/Pranesh/Purdue/Spring 2025/ML Research/rpi5-nn/rpi5-yolo-nn/model_weights/yolov2-tiny-voc.weights")
    model.eval()
    # print(m)
    
    # use_cuda = 1
    # if use_cuda:
    #     model.cuda()

    img = Image.open('pmh2mmc4.png').convert('RGB')
    sized = img.resize((416, 416))

    boxes = do_detect(model, sized, 0.5, 0.5, use_cuda=False)

    class_names = load_class_names('voc.names')
    plot_boxes(img, boxes, 'predict1.jpg', class_names)  