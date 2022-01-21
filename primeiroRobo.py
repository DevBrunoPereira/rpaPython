from tkinter import Button
import pyautogui
import pyautogui as robo

opcao = pyautogui.confirm('Clique no botão desejado:', buttons = ['Excel','Word','Notepad'])

if opcao == 'Excel':
    robo.hotkey('win','r')
    robo.sleep(2)
    robo.typewrite('Excel')
    robo.sleep(2)
    robo.press('Enter')
    robo.sleep(4)
    robo.click(x=600, y=241)
    robo.sleep(3)
    robo.typewrite('Escolho abrir o Excel')
elif opcao == 'Word':
    robo.hotkey('win','r')
    robo.sleep(2)
    robo.typewrite('winword')
    robo.sleep(2)
    robo.press('Enter')
    robo.sleep(6)
    robo.click(x=447, y=334)
    robo.sleep(5)
    robo.typewrite('Escolhi abrir o word')
elif opcao == 'Notepad':
    robo.hotkey('win','r')
    robo.sleep(2)
    robo.typewrite('Notepad')
    robo.sleep(2)
    robo.press('Enter')
    robo.sleep(4)
    robo.typewrite('Escolho abrir o notepad')