import PySimpleGUI as sg

layout = [
    [sg.Input(key="-Input-"),
     sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key='-units-'),
     sg.Button('Convert', key='-button-')
     ],
    [sg.Text('Output', key='-output-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-button-':
        input_value = values['-Input-']
        if input_value.isnumeric():
            match values['-units-']:
                case 'km to mile':
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f'{input_value} km is {output} miles.'
                case 'kg to pound':
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f'{input_value} kg is {output} pounds.'
                case 'sec to min':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} seconds is {output} minutes.'
            window['-output-'].update(output_string)

window.close()