from ultralytics import YOLO
import torch



if __name__ == '__main__':
# 모델 로드 (객체 탐지 or 세그멘테이션 선택)
    model = YOLO("yolov8s.pt")  # 'yolov8s-seg.pt'을 사용하면 세그멘테이션 가능

    # 학습 실행
    model.train(
        data=r"C:\\CD\\PYTHON\\YOLOTEST\\My First Project.v2i.yolov8\\data.yaml",  # 데이터셋 경로
        epochs=10,       # 학습 반복 횟수
        imgsz=640,        # 입력 이미지 크기
        batch=16,         # 배치 크기 (VRAM에 맞게 조절)
        workers=4,        # 데이터 로딩 속도
        device="cuda",    # GPU 사용 ('cpu'로 변경 가능)
        optimizer="AdamW",  # 최적화 알고리즘
        patience=20,      # 성능 개선 없으면 자동 종료
        dropout=0.1       # 과적합 방지
    )