import PySimpleGUI as sg

def get_todos():
    with open("todos.txt", "r") as file_path:
        todos= file_path.readlines()
        return todos

def write_todos(element):
    with open("todos.txt","w") as file_path:

        file_path.writelines(element)

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do",key="todo")
add_button = sg.Button("Add")
to_do_list = sg.Listbox(values=get_todos(),enable_events=True,size=[45,10])

window = sg.Window("To-Do app",layout=[[label],[input_box, add_button],[to_do_list]])




while True:

    event,values = window.read()
    print(event)
    print(values)
    if event=="Add":
        todos = get_todos()
        new_todo = values[0]+"\n"
        todos.append(new_todo)
        write_todos(todos)
        window[1].update(values=todos)

    elif event == 0:
        window["todo"].update(value=values[0][0])


    elif event == sg.WIN_CLOSED:
        break

window.close()
