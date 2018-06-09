from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import os
import csv

_FILENAME='./partecipanti.csv'
with open(_FILENAME, "r") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    tot_iscritti = (len(list(csv.reader(open(_FILENAME))))-1)
    print('Totale iscritti : ' + str(tot_iscritti))

    next(readCSV) # salta intestazione csv
    for row in readCSV:
        nominativo = row[0]
        id_utente = row[1]
        conferma = row[4]
        data_iscrizione = row[6]
        
        file_attestato = 'attestato_'+nominativo.replace(" ", "_").title()+'.jpg'
        img = Image.open('template_attestato.jpg')
        W, H = img.size # dimensioni immagine template
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Roboto-Black.ttf", 120)
        w,h = font.getsize(nominativo)
        draw.text(((W-w)/2, 980),nominativo,(0,0,0),font=font)
        img.save(file_attestato)
        print(file_attestato)


