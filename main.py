import pyautogui as pag
import time

pag.alert('''NÃO MOVA OU UTILIZE O MOUSE E O TECLADO!
O Python irá controlar seu computador.''')
time.sleep(0.5)

pag.PAUSE = 1

# abrir o navegador e selecionar a conta certa na janela do google
pag.press('winleft')
pag.write('chrome')
pag.press('enter')
time.sleep(1)
pag.press('tab')
pag.press('enter')

# entrar no google drive
pag.write('https://drive.google.com/drive/my-drive')
pag.press('enter')
time.sleep(3)

# acessar a pasta desejada
pag.press('down')
time.sleep(0.5)
pag.press('up')
time.sleep(0.5)
pag.press('enter')

# entrar na área de trabalho, atalho ('win + D') e pegar a posição do arquivo com o .position()
pag.hotkey('winleft', 'd')
pag.moveTo(34, 34, 1)

# clicar e arrastar o arquivo com o qual farei o backup
pag.mouseDown()
pag.moveTo(707, 435, 1)

# enquanto arrastar, mudar para a tela do drive
pag.hotkey('alt', 'tab')
time.sleep(1)

# largar o arquivo no drive
pag.mouseUp()
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('tab')
pag.press('enter')

# esperar 5 segundos e fechar o navegador e as pastas
time.sleep(5)

# fechando o navegador
pag.hotkey('alt', 'f4')

# EXIBE UMA MENSAGEM DE ALERTA DE PROCESSO FINALIZADO
pag.alert('''PROCESSO FINALIZADO!
Feche a janela e volte a utilizar o computador normalmente.''')

