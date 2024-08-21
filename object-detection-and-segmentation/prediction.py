from ultralytics import YOLO


MODEL_PATH = 'models/'
DATA_DIR = 'data/'


model = YOLO(MODEL_PATH + "yolov8n.pt")

model.predict(source=DATA_DIR + 'image_1.jpg', save=True, conf=0.5, save_txt=True)

# model.export(format='onnx')
