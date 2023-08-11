from pyfirmata import Arduino, util
from time import time

contador = 0
board = Arduino('COM3')

it = util.Iterator(board)
it.start()

valD2 = board.get_pin('d:2:o')
valD3 = board.get_pin('d:3:o')
valD6 = board.get_pin('d:6:o')
valD7 = board.get_pin('d:7:o')

estadomuv1 = True   # Quando 1 dedo estiver levantado, o carrinho vai para esqueda
estadomuv2 = True   # Quando 1 dedo estiver levantado, o carrinho vai frente
estadomuv3 = True   # Quando 1 dedo estiver levantado, o carrinho vai para Direita
estadomuv4 = True   # Quando 1 dedo estiver levantado, o carrinho vai trás



while True:
    time.sleep(0.15)

    estadomuv1 = valD2.write ()
    estadomuv2 = valD3.write, valD7.write ()
    estadomuv3 = valD6.write ()
    estadomuv4 = valD2.write, valD6.write ()

    while contador != 0:
        if contador == 1:
            board.digital[2].write(1)
        elif contador == 2:
            board.digital[2].write(1)
            board.digital[6].write(1)
        elif contador == 3:
            board.digital[6].write(1)
        elif contador == 4:
            board.digital[3].write(1)
            board.digital[7].write(1)
        





