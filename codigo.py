import  pyautogui
import time

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("opera gx")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.press("tab")
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha senha aqui")


pyautogui.press("enter")

time.sleep(2)

import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)


for linha in tabela.index:
    
    pyautogui.click(x=653, y=294)
 
    codigo = tabela.loc[linha, "codigo"]
   
    pyautogui.write(str(codigo))
 
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

