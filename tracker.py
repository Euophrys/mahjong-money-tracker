import PySimpleGUI as sg

sg.theme('DarkAmber')
layout = [  [sg.Text('Earnings:', key='Label', pad=(5,0))],
            [sg.Text('¥0', key='Money', size=(12,1), font=(None, 18), pad=(5,(0,3)))],
            [sg.Text('Rate'), sg.Input('1.0', key='Rate', size=(5,1))],
            [sg.Text('Shuugi (¥)'), sg.Input('500', key='Shuugi', size=(6,1))],
            [sg.Text('End Score'), sg.Input('', key='Score', size=(5,1)), sg.Button('Add')],
            [sg.Button('Tsumo Shuugi', size=(12,1))],
            [sg.Button('Add Shuugi', size=(12,1))],
            [sg.Button('Pay Shuugi', size=(12,1))],
            [sg.Input('', key='Value', size=(8,1)), sg.Button('Add Value')]
]

window = sg.Window('Mahjong Money Tracker', layout, resizable=True)
money = 0

def validate(values, key):
    try:
        value = float(values[key])
        return value
    except:
        sg.popup_cancel('%s is not a number.' % key)
        return None

def update_money():
    absolute_money = abs(money)

    sign = ''
    if money < 0:
        sign = '– '
        window['Label'].update(value='Losses:')
    else:
        window['Label'].update(value='Earnings:')

    if absolute_money >= 1000000000:
        window['Money'].update(value='%s¥%dm' % (sign, absolute_money / 1000000))
    elif absolute_money >= 1000000:
        window['Money'].update(value='%s¥%dk' % (sign, absolute_money / 1000))
    else:
        window['Money'].update(value='%s¥%d' % (sign, absolute_money))

while True:
    event, values = window.read()

    if event is None:
        break

    if event in ('Tsumo Shuugi', 'Add Shuugi', 'Pay Shuugi'):
        shuugi = validate(values, 'Shuugi')
        if shuugi is None: continue

        if event is 'Tsumo Shuugi':
            money += shuugi * 3
        elif event is 'Add Shuugi':
            money += shuugi
        elif event is 'Pay Shuugi':
            money -= shuugi
        
        update_money()

    if event is 'Add':
        rate = validate(values, 'Rate')
        score = validate(values, 'Score')
        if rate is None or score is None: continue

        money += score * 100 * rate
        update_money()
        window['Score'].update(value='')
    
    if event is 'Add Value':
        value = validate(values, 'Value')
        if value is None: continue

        money += value
        update_money()

window.close()