# Programa para pausar de 2 em 2 horas e tocar um video no youtube ou musica no computador
# 1 - escrever código de espera de 2 em 2 horas.
# 2 - escrever codigo para abrir o navegador e tocar algo.
# 3 - colocar esses códigos em algum loop.

import webbrowser
from time import sleep

count = 0
while (count <= 3):
    sleep(20)
    webbrowser.open(url = 'https://www.youtube.com/watch?v=NVoVA6itDmI')
    count += 1
    print('Tocando pela {}ª vez.'.format(count))
