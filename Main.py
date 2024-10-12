import xml.dom.minidom, os, time, rich, getpass

user = getpass.getuser()

rich.print(f'[bold red]Xml beautifier for Stormworks[/bold red]\n\nMade by Vova_4104\n')
rich.print(f'Manual how to enter file name.\nYou can enter only name: [bold red]vehicle_name[/bold red]\nOr name and extension: [bold red]vehicle_name.xml[/bold red]\n')

time.sleep(0.5)

def rewrite(path = ''):
    try:
        print(f'Path: {path}')
        file = open(path, 'r')
        file_content = file.read()
        file.close()
        if file_content.endswith('<! --BEAUTIFIED-->'):
            print('Already beatufied!')
        else:
            temp_formated = xml.dom.minidom.parseString(file_content)
            formated = f'{temp_formated.toprettyxml()}\n\n<! --BEAUTIFIED-->'
            file = open(path, 'w')
            file.write(formated)
            file.close()
            print('Successfully beautified .xml file!')
    except FileNotFoundError:
        print('No file found')  
    

file = f'C:\\Users\\{user}\\AppData\\Roaming\\Stormworks\\data\\vehicles\\'
name = input('Enter xml file name : ')
if name.endswith('.xml'):
    rewrite(f'{file}{name}')
else:
    rewrite(f'{file}{name}.xml')

time.sleep(2.5)