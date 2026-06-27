from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="road_damage_yolo/data.yaml",
    epochs=1,
    imgsz=640,
    batch=4,
    workers=2,
    device="cpu"
)