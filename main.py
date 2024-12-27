import cv2
from ultralytics import YOLO
import serial

# Configuration du port série
ser = serial.Serial('/dev/ttyACM0', 9600)  # port select exp: ACM0 or ACM1 or tty12 ...

# Chargement du modèle YOLOv8
model = YOLO('path_your_model_location')  # Chemin vers votre modèle YOLOv8

# Initialisation de la capture vidéo
cap = cv2.VideoCapture(0)  # Webcam par défaut

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensionner l'image à une taille plus standard (facultatif)
    frame = cv2.resize(frame, (640, 480))

    # Effectuer la détection avec YOLO
    results = model(frame, device='0')  # Assurez-vous d'utiliser le GPU si nécessaire

    # Processus et affichage des résultats
    for result in results:
        boxes = result.boxes.xyxy
        labels = result.boxes.cls
        scores = result.boxes.conf

        for box, label, score in zip(boxes, labels, scores):
            if score > 0.5:  # Filtrer les résultats en fonction du score de confiance
                x1, y1, x2, y2 = map(int, box)
                class_name = model.names[int(label)]
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'{class_name}: {score:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                # Envoi des commandes série selon le label détecté
                if class_name == 'stop_panel' or class_name == 'red_sign':
                    print("Envoi de 'stop'")
                    ser.write(b'stop')  # Commande pour arrêter le robot
                elif class_name == 'green_sign':
                    print("Envoi de 'avant'")
                    ser.write(b'avant')  # Commande pour avancer le robot

    # Affichage de l'image avec les détections
    cv2.imshow('Live Detection', frame)

    # Quitter avec la touche 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libération des ressources
cap.release()
cv2.destroyAllWindows()
