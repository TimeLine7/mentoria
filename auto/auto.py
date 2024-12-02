import pyautogui
import time
import subprocess
import pyperclip
import pygetwindow as gw
import csv


def abrir_bloco_notas():
    print("Abrindo o Bloco de notas...")
    subprocess.Popen(["notepad.exe"])
    time.sleep(5)
    print("Trazendo o Bloco de notas para o foco")

    janela = None
    
    for win in gw.getWindowsWithTitle("Sem título"):
        if "Sem títuilo" in win.title:
            janela = win
            break
    
    if janela:
        janela.activate()
        time.sleep(3)
    else:
        print("Erro: Não foi possivel localizar o Bloco.")
        
def Colar_texto(texto):
    pyperclip.copy(texto)
    pyautogui.hotkey("ctrl", "v")
    
    
def escrever_no_bloco(arquivo_csv):
    print("Lendo Csv")
    with open(arquivo_csv, mode='r', encoding='utf-8') as file:
        leitor_csv = csv.reader(file)
        for linha in leitor_csv:
            texto = ', '.join(linha)
            Colar_texto(texto)
            pyautogui.press("enter")
            time.sleep(1)

if __name__ == "__main__":
    abrir_bloco_notas()
    escrever_no_bloco('dados.csv')
    print("Auto concluido.")