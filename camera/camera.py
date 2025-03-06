import sys
import cv2
from ultralytics import YOLO
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer

class CameraViewer(QWidget):
    def __init__(self):
        super().__init__()
        # 모델 파일 경로 (raw string 사용)
        self.model_paths = [
            r"C:\CD\PYTHON\YOLOTEST\camera\epk10.pt",
            r"C:\CD\PYTHON\YOLOTEST\camera\epk50.pt",
            r"C:\CD\PYTHON\YOLOTEST\camera\epk100.pt"
        ]
        
        self.init_ui()
        
        # 웹캠 초기화
        self.cap = cv2.VideoCapture(0)
        
        # YOLOv8 모델 로드
        self.models = []
        for model_path in self.model_paths:
            try:
                model = YOLO(model_path)
                self.models.append(model)
                print(f"모델 로드 성공: {model_path}")
            except Exception as e:
                print(f"모델 {model_path} 로드 실패: {e}")
        if not self.models:
            raise FileNotFoundError("모든 모델 파일을 찾을 수 없습니다.")
        self.model_index = 0
        print("현재 모델:", self.model_paths[self.model_index])
        
        # 타이머 설정 (약 30 fps)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def init_ui(self):
        self.setWindowTitle('실시간 객체 탐지 웹캠 뷰어 (YOLOv8)')
        
        # 콤보박스 생성 및 모델 목록 추가 (파일명만 표시)
        self.combo_box = QComboBox(self)
        for path in self.model_paths:
            # 경로 구분자에 따라 파일명 추출
            self.combo_box.addItem(path.split("\\")[-1])
        self.combo_box.currentIndexChanged.connect(self.change_model)
        
        # 영상 표시 라벨 생성
        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(self.video_label)
        self.setLayout(layout)
        self.resize(800, 600)

    def change_model(self, index):
        self.model_index = index
        print("모델 전환 -> 현재 모델:", self.model_paths[self.model_index])

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # 현재 선택한 모델로 객체 탐지 수행
            current_model = self.models[self.model_index]
            results = current_model(frame)
            # results는 리스트 형태이며, 첫 번째 결과에 탐지 결과가 그려진 이미지가 포함됨
            detected_frame = results[0].plot()
            
            # OpenCV(BGR) -> PyQt(RGB) 변환
            frame_rgb = cv2.cvtColor(detected_frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame_rgb.shape
            bytes_per_line = 3 * w
            qt_image = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)
            self.video_label.setPixmap(pixmap.scaled(self.video_label.size(), Qt.KeepAspectRatio))

    def closeEvent(self, event):
        self.cap.release()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = CameraViewer()
    viewer.show()
    sys.exit(app.exec_())
