### Projeto Automação de Processos | Backup AutomatizadoDocumentação PYAUTOGUI: https://pyautogui.readthedocs.io/en/latest/##Código que exibe as teclas a serem utilizadas no metodo .press(): pyautogui.KEYBOARD_KEYSCódigo para localizar a posição de um item na tela para utilizar o mouse.Lembrando que a posição muda de acordo com a resolução do munitor utilizado na máquina:pyautogui.position()#O projeto consiste em um código convertido em executável que realiza um processo de backup automatizado, enviando um arquivo da área de trabalho de uma máquina para uma pasta para o drive de uma conta google.Bibliotecas utilizadas:- pip install pyautogui- pip install pyinstallerCriar o código em um ambiente virtual.Com o código finalizado e testado, rodar o seguinte código no terminal:*lembrando que o parâmetro '-w' deverá ser utilizado somente quando o código utilizar alguma janela para interação com o usuário. pyinstaller --onefile -w nome-do-arquivo.pyAo final do processo, alguns arquivos serão gerados na pasta do projeto:- pasta build - excluir- arquivo com extensão '.spec' - excluir- pasta dist - onde se encontra o arquivo '.exe'O arquivo deve estar na mesma pasta de todas as bases de dados ou outros arquivos necessários para a execução do código, pois caminhos não podem ser replicados em máquinas diferentes.