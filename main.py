from nicegui import ui
from nicegui import ui
print(dir(ui))

def details(row):
    print(row.id)
    print(row)

    # NOW ADD STYLE COLOR RED IN YOUR SELECTED LABEL
    row.style("color:red")
    # PRINT TEXT
    print(row.default_slot.children[0].children.text)

    # NOW UPDATE YOUR SELECTED LABEL TO NEW UPDATE TEXT
    row.default_slot.children[0].children.text = name.value

    # NOW UPDATE
    row.update()

def youremove(row):
    # FOR REMOVE YOUR SELECTED USE FUNCTION REMOVE
    my_tasks.remove(myrow)
    my_tasks.update()

def addnow():
    # NOW APPEND TO my_tasks
    with my_tasks:
        with ui.row() as myrow:
            ui.label(name.value)
            ui.button("update", on_click=lambda:details(myrow))
            ui.button("remove",on_click=lambda:youremove(myrow)).props('flat')
            

name = ui.input(label="Your name")
ui.button("Add", on_click=addnow)
my_tasks = ui.column()

ui.run()
