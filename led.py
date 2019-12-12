from tkinter import *    
import serial

arduino = serial.Serial('COM4', 9600)
message = ''
def ap():
    op = 'ap\n'
    r = op.encode('ascii')
    arduino.write(r)
    message = 'Apagado'
    printMess(message)


def en():
    op = 'en\n'
    r = op.encode('ascii')
    arduino.write(r)
    message = 'Encendido'
    printMess(message)

def printMess(message):
    m.set(message)


root = Tk()
root.geometry("250x80")

m = StringVar()

root.title("LED")
frame = Frame(root)

Button(root, text="Encender", command = en).pack()
Button(root, text="Apagar", command = ap).pack()

Label(root, justify = 'center', textvariable = m).pack()

root.mainloop()
    