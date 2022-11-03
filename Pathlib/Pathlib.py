from pathlib import Path
from time import sleep

# Pega o caminho do arquivo dentro do projeto atual
_path = Path()
print(f'1 - o caminho do arquivo no projeto é {_path}')
sleep(2)

# Pega o caminho completo do arquivo no sistema operacional
_path2 = Path(__file__)
print(f'2 - o caminho completo é {_path2}')
sleep(2)

# Pega o caminho do projeto
project_path = _path2.absolute()
print(f'3 - o caminho do projeto é {project_path}')

sleep(2)
#Pega a pasta pai do arquivo atual
parent_folder = _path2.parent
parent_parent_folder = _path2.parent.parent

sleep(2)
print(f'4 - O caminho do pai do arquivo é {parent_folder}')
sleep(2)
print(f'5 - O caminho do pai do arquivo é {parent_parent_folder}')

# É Possível criar pastas entre pastas

#new_folder = parent_folder / 'folder_test'
#new_folder.mkdir()


