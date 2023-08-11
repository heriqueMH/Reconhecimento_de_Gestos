import cv2
import mediapipe as mp
import serial


#chamar open cv e mediapipe

webcam = cv2.VideoCapture(1)          # selecionar cam
hand = mp.solutions.hands             # pontos na mão
Hand = hand.Hands(max_num_hands = 1)  # número de mãos
mpDraw = mp.solutions.drawing_utils   # desenho das ligações
# conexao = serial.Serial('COM3', 115200)

while True:
    check,img = webcam.read()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = Hand.process(img)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    handsPoints = results.multi_hand_landmarks
    h, w, c = img.shape
    trackPoints = []                                 # Variavel de pontos
    dedos = [8,12,16,20]
    contador = 0

    if handsPoints:
        for points in handsPoints:
            mpDraw.draw_landmarks(img,points,hand.HAND_CONNECTIONS) 
            for id, cord in enumerate(points.landmark):
                x, y = int(cord.x * w), int(cord.y * h)
                # cv2.putText(img,str(id), (x, y + 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0),2)  #exibindo mapeando os depos
                trackPoints.append ((x, y))
            
        if points:
            if trackPoints [4][0] < trackPoints[2][0]:         #Condição para contar dedão
                contador +=1
            for x in dedos:
                if trackPoints[x][1] < trackPoints[x-2][1]:    # Condção para contar os 4 dedos da mão
                    contador +=1 
             
            # if contador != 0:
            #     print(contador)
            #     conexao.write(str(contador).encode())

        cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,0,0),5) # Exibindo número de dedos na tela pelo contador

 

        # print(contador) # exibindo contador no terminal
        ''


    cv2.imshow("Imagem",img)
    # cv2.waitKey(1)
    if cv2.waitKey(5) & 0xFF == 27:
      break