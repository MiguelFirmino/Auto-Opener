from time import sleep
from pyautogui import hotkey, write, press
from pygetwindow import getWindowsWithTitle

user_path = "C:/Users/F248584/"
desktop_path = "C:/Users/Public/Desktop/"

class Program:
  def __init__(self, path, filename, title):
    self.path = path
    self.filename = filename
    self.fullpath = self.path + self.filename
    self.title = title

programs = [
  Program(user_path, "TEXTOS PADRÃO NOTAS.txt", "TEXTOS PADRÃO NOTAS"),
  Program(user_path, "TICKETS TRATADOS v1.4.1.xlsx", "TICKETS TRATADOS"),
  Program(user_path, "TEXTOS PADRÃO v1.1.0.doc", "TEXTOS PADRÃO"),
  Program("", "snippingtool", "Ferramenta de Captura"),
  Program(desktop_path, "MenuAplic.lnk", "Menu Principal"),
  Program(desktop_path, "Nice Cluster2.lnk", "My Profile"),
  Program(desktop_path, "Orhganiza - Google Chrome.exe", "Portal Orhganiza")
]

def open_program(program):
  hotkey("win", "r")
  write(program.fullpath)
  press("enter")
  sleep(0.05)

check_if_closed = lambda x: len(getWindowsWithTitle(x.title)) == 0

for program in programs:
  try:
    if check_if_closed(program):
      print(f"Opening program: {program.filename}")
      open_program(program)
    else:
        print(f"Program: {program.filename} is already open")
  except:
      pass