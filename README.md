# 임베디드

Gachon Univ. Embeded system team project

# Raspberry Box 🍓

OPEN and CLOSE the locker AUTOMATICALLY using OpenCV.

When the owner stand infront of the locker, It recognize the owner and open the lockers door automatically. And when owner leave the locker, the lockers door closed automatically.

1. Collect dataset. - faceDataSet.py
    
    Capture and save 100 different pictures of owners frontal face.
    
2. Training - training.py
    
    Train with the owners face picture. Create the trained ‘yml’ file.
    
    - recognizer = cv2.face.LBPHFaceRecognizer_create()
    - recognizer.train(faces, np.array(ids))
    - recognizer.write('trainer/trainer.yml')
    
3. Action - recogFinal.py
    
    Recognize the owners face and open and close the lockers door.
