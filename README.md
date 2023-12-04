# Raspberry Box 🍓
Gachon Univ. Embeded system team project



## OPEN and CLOSE the locker AUTOMATICALLY using OpenCV.

When the owner stand infront of the locker, It recognize the owner and open the lockers door automatically. And when owner leave the locker, the lockers door closed automatically.

1. Collect dataset. - faceDataSet.py
    
    Capture and save 100 different pictures of owners frontal face.

   ![image](https://github.com/Ahnnet/raspberryBox/assets/93837441/fa144da2-20d2-4f19-9b5e-6d3affa75ea4)



    
2. Training - training.py
    
    Train with the owners face picture. Create the trained ‘yml’ file.
    
    - recognizer = cv2.face.LBPHFaceRecognizer_create()
    - recognizer.train(faces, np.array(ids))
    - recognizer.write('trainer/trainer.yml')
  
      
      ![image](https://github.com/Ahnnet/raspberryBox/assets/93837441/16ca7ea8-1470-482f-bd7d-d6097b344370)

    
3. Action - recogFinal.py
    
    Recognize the owners face and open and close the lockers door.







![image](https://github.com/Ahnnet/raspberryBox/assets/93837441/98195e88-9746-445f-bb2c-5c5ca85eb94b)

