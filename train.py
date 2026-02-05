import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO
 
if __name__ == '__main__':
#     修改为自己的配置文件地址
    model = YOLO('./ultralytics/cfg/models/26/yolo26-ParNetAttention.yaml')
#     修改为自己的数据集地址
    model.train(data='./ultralytics/cfg/datasets/coco8.yaml',
                cache=False,
                imgsz=640,
                epochs=10,
                single_cls=False,  # 是否是单类别检测
                batch=8,
                close_mosaic=10,
                workers=0,
                optimizer='MuSGD',  
                # optimizer='SGD',
                amp=False,
                project='runs/train',
                name='yolo26-ParNetAttention',
                )
    
 
