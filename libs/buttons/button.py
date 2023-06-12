import PyQt5.QtWidgets

class Action:
    def __init__(self):
        self.name = name
        self.action = action
    def delete_last():
        
        





def delete_last():
    print("Deleted")

def clear_all():
    print("Cleared all")

def init_buttons_old(window,**kwargs):
    deleteLastButton = QtWidgets.QPushButton(window)
    deleteLastButton.setText("Delete Last")
    deleteLastButton.move(50,50)
    deleteLastButton.clicked.connect(delete_last)

    clearAllButton = QtWidgets.QPushButton(window)
    clearAllButton.setText("Clear All")
    clearAllButton.move(100,100)
    clearAllButton.clicked.connect(clear_all)


def make_clear_all(window):
    clearAllButton = QtWidgets.QPushButton(window)
    clearAllButton.setText("Clear All")
    clearAllButton.move(100,100)
    clearAllButton.click.connect(clear_all)
def make_delete_last(window,name):

def init_buttons(window,names):
    buttons = []
    for i in name:
        if name == 'clearAllButton':
            make_clear_all(i)
            buttons.append(i)
        if name == 'deleteLastButton':
            make_delete_all(i)
            buttons.append(i)
        else:
            pass
    return buttons
