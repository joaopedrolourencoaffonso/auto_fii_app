import os

os.system("app_fii.py")

#nome = open("app_fii.py","r")
#teste = nome.read()
#nome.close()
#teste = str(teste)
#exec(teste)





























#import PySimpleGUI as sg

## layout the Window
#layout = [[sg.Text('A custom progress meter')],
#          [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
#          [sg.Cancel()]]

## create the Window
#window = sg.Window('Custom Progress Meter', layout)
## loop that would normally do something useful
#for i in range(1000):
#    # check to see if the cancel button was clicked and exit loop if clicked
#    event, values = window.read(timeout=0)
#    if event == 'Cancel' or event is None:
#        break
#        # update bar with loop value +1 so that bar eventually reaches the maximum
#    window['progbar'].update_bar(i + 1)
## done with loop... need to destroy the window as it's still open
#window.close()
