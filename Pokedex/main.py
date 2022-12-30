#Bibliotecas/Frameworks usados na construção do programa
#Libraries/Frameworks used in building the program


#1 - In your CMD, type 'pip install PIL', hit enter and wait for the download to finish.
#2 - In your CMD, type 'pip install tkinter', hit enter and wait for the download to finish.
#3 - In your CMD, type 'pip install turtle', hit enter and wait for the download to finish.
#4 - After that, run the file 'main.py' in your ide, and have fun.

from tkinter import HORIZONTAL, ttk
from tkinter import *
from turtle import radians
from PIL import Image, ImageTk
from dadosPoke import *
import random

############# Cores/Colors ###########
#Cores usadas no background do frame da janela, letras, valores, entre outros..
#Colors used in the window frame's background, letters, values, among others.

co0 = "#444466"  # Preta/Black
co1 = "#feffff"  # Branco/White

co2 = "#6f9fbd" # Azul/Blue
c03 = "#008000" # Verde/Green
co4 = "#ef5350" # Vermelha/Red

co5 = "#38576b"  # Valor/Value
co6 = "#403d3d"   # Letra/ Letter


#Criando a janela / window creation
janela = Tk()
janela.title('Pokédex')# Window name
janela.geometry('550x600')# Window Size
janela.iconbitmap('imagens/pokeball.ico') #icon of window
janela.configure(bg=co1) #window background color

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)#Separation Configurations

style = ttk.Style(janela)
style.theme_use("clam")




# Criando a frame onde ficará a imagem do Pokemon com algumas informações
#Size of the tab where the pokemon will be
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)


#Função responsável por fazer a mudança dos dados, verificando 'dadosPoke' e trazendo os valores encontrados
##Function responsible for changing the data, checking 'dataPoke' and bringing the values found
def trocar_pokemon(i):
    global imagem_pokemon, pok_img1

    #Troca as cores de fundo do frame do pokemon baseado no tipo visto na array e seu indice de valor equivalente
    #Switch the background colors of the pokemon frame based on the type seen in the array and its index of equivalent value
    frame_pokemon['bg'] = pokemon[i]['tipo'][3]


    # informações Pokemon - 
    # Nome
    # Geração
    # ID
    # Pokemon information - 
    # Name
    # Generation
    # ID
    pok_nome['text'] = i # name/ nome
    pok_nome['bg'] = pokemon[i]['tipo'][3] #Vai no indice 3 pegando a cor da chave 'tipo'/Go to index 3 by picking the color of the 'type' key
    pok_ger['text'] = pokemon[i]['tipo'][1] #Generation/ geração
    pok_ger['bg'] = pokemon[i]['tipo'][3] #Troca o fundo/Change the background
    pok_ID['text'] = pokemon[i]['tipo'][0] #ID
    pok_ID['bg'] = pokemon[i]['tipo'][3]#Troca o fundo/Change the background
    pok_sts1['text'] = pokemon[i]['status'][0]#mostra/troca os status do pokemon - shows/changes the status of the pokemon
    pok_leveis['text'] = pokemon[i]['leveis'][0]#mostra/troca os leveis baseado nos status do pokemon - shows/changes levels based on the pokemon's status
    imagem_pokemon = pokemon[i]['tipo'][2] # troca a imagem do pokemon / change the pokemon image
    

    # Imagem Pokemon - Propriedades de como ficara na janela
    # Pokemon Image - Properties of how it will look in the window
    imagem_pokemon = Image.open(imagem_pokemon)
    img_pokemon = imagem_pokemon.resize((238,238))
    imagem_pokemon = ImageTk.PhotoImage(img_pokemon)

    pok_img1 = Label(frame_pokemon, image = imagem_pokemon, relief = 'flat', bg = pokemon[i]['tipo'][3], fg=co1)#Troca o fundo
    pok_img1.place(x = 60, y=50)

    #Para não haver conflito do id e geração com a imagem, os dois ficaram na frente da imagem
    #To avoid conflict of the id and generation with the image, both were in front of the image
    pok_ger.lift()
    pok_ID.lift()

# Nomes - Geração / Names - Generation
# - Bulbassauro, Charmander, Squirtle 1 Geração
# - Chikorita, Totodile e Cyndaquil. 2 Geração
# - Treecko, Torchic e Mudkip. 3 Geração

# - Bulbassaurus, Charmander, Squirtle 1 Generation
# - Chikorita, Totodile and Cyndaquil. 2 Generation
# - Treecko, Torchic and Mudkip. 3 Generation 



pok_nome = Label(frame_pokemon, text='', relief = 'flat', anchor= CENTER, font=('Fixedsys 20 bold'), fg=co1)#Property of how it will look in the frame
pok_nome.place(x = 12, y=15)

# Geração --- Generation 
pok_ger = Label(frame_pokemon, text='', relief = 'flat', anchor= CENTER, font=('Fixedsys 10'), bg=co1, fg=co1)#Property of how it will look in the frame
pok_ger.place(x = 12, y=50)

# Número Id ---  Id Number 
pok_ID = Label(frame_pokemon, text='', relief = 'flat', anchor= CENTER, font=('Fixedsys 8'), bg=co1, fg=co1)#Property of how it will look in the frame
pok_ID.place(x = 12, y=75)

# Status 
pok_sts = Label(janela, text='Status', relief = 'flat', anchor= CENTER, font=('Fixedsys 22'), bg=co1, fg=co0)#Property of how it will look in the frame
pok_sts.place(x = 15, y=310)

#Informações Status --- Status Information
pok_sts1 = Label(janela, text='HP: 45\n\nAtaque: 49\n\nDefesa: 49\n\nVelocidade: 45', relief = 'flat', anchor= CENTER, font=('Fixedsys 10'), bg=co1, fg=co6)#Property of how it will look in the frame
pok_sts1.place(x = 15, y=360)

#Leveis 
pok_level = Label(janela, text='Leveis', relief = 'flat', anchor= CENTER, font=('Fixedsys 20'), bg=co1, fg=co6)
pok_level.place(x = 180, y = 310)

# Informações dos Leveis --- Leveis Information 
pok_leveis = Label(janela, text='105 - 152\n\n48 - 111\n\n48 - 111\n\n45 - 106', relief = 'flat', anchor= CENTER, font=('Fixedsys 10'), bg=co1, fg=co6)
pok_leveis.place(x = 180, y = 355)


# Menu Lateral Pokemon / Pokemon Side Menu
# Aqui é onde as imagens são posicionadas, sua propriedades e a função responsável por efetuar a troca das informações.
# Here is where the images are positioned, their properties, and the function responsible for exchanging the information.
imagem_pokemon_1 = Image.open('imagens/icon_01.png')
img_pokemon_1 = imagem_pokemon_1.resize((40,40))
imagem_pokemon_1 = ImageTk.PhotoImage(img_pokemon_1)

b_pok_img1 = Button(janela, command = lambda: trocar_pokemon('Bulbassauro'), image = imagem_pokemon_1, text='Bulbassauro', width=160, relief = 'raised', overrelief=RIDGE,compound = LEFT, anchor=NW, padx = 5, font=('Fixedsys 14'),bg=co1, fg=co0)
b_pok_img1.place(x = 375, y=10)


imagem_pokemon_2 = Image.open('imagens/icon_04.png')
img_pokemon_2 = imagem_pokemon_2.resize((40,40))
imagem_pokemon_2 = ImageTk.PhotoImage(img_pokemon_2)

b_pok_img2 = Button(janela, command = lambda: trocar_pokemon('Charmander'), image = imagem_pokemon_2, text='Charmander', width=160, relief = 'raised', overrelief=RIDGE,compound = LEFT, anchor=NW, padx = 5, font=('Fixedsys 14'),bg=co1, fg=co0)
b_pok_img2.place(x = 375, y=60)


imagem_pokemon_3 = Image.open('imagens/icon_07.png')
img_pokemon_3 = imagem_pokemon_3.resize((40,40))
imagem_pokemon_3 = ImageTk.PhotoImage(img_pokemon_3)

b_pok_img3 = Button(janela, command = lambda: trocar_pokemon('Squirtle'),image = imagem_pokemon_3, text='Squirtle', width=160, relief = 'raised', overrelief=RIDGE,compound = LEFT, anchor=NW, padx = 5, font=('Fixedsys 14'),bg=co1, fg=co0)
b_pok_img3.place(x = 375, y=110)


imagem_pokemon_4 = Image.open('imagens/icon_152.png')
img_pokemon_4 = imagem_pokemon_4.resize((40,40))
imagem_pokemon_4 = ImageTk.PhotoImage(img_pokemon_4)

b_pok_img4 = Button(janela, command = lambda: trocar_pokemon('Chikorita'), image = imagem_pokemon_4, text='Chikorita', width=160, relief = 'raised', overrelief=RIDGE,compound = LEFT, anchor=NW, padx = 5, font=('Fixedsys 14'),bg=co1, fg=co0)
b_pok_img4.place(x = 375, y=160)


imagem_pokemon_5 = Image.open('imagens/icon_155.png')
img_pokemon_5 = imagem_pokemon_5.resize((40,40))
imagem_pokemon_5 = ImageTk.PhotoImage(img_pokemon_5)

b_pok_img5 = Button(janela, command = lambda: trocar_pokemon('Cyndaquil'), image = imagem_pokemon_5, text='Cyndaquil', width=160, relief = 'raised', overrelief=RIDGE,compound = LEFT, anchor=NW, padx = 5, font=('Fixedsys 14'),bg=co1, fg=co0)
b_pok_img5.place(x = 375, y=210)


imagem_pokemon_6 = Image.open('imagens/icon_158.png')
img_pokemon_6 = imagem_pokemon_6.resize((40,40))
imagem_pokemon_6 = ImageTk.PhotoImage(img_pokemon_6)

b_pok_img6 = Button(janela, command = lambda: trocar_pokemon('Totodile'), image = imagem_pokemon_6, text='Totodile', width=160, relief = 'raised', overrelief=RIDGE,compound = LEFT, anchor=NW, padx = 5, font=('Fixedsys 14'),bg=co1, fg=co0)
b_pok_img6.place(x = 375, y=260)


imagem_pokemon_7 = Image.open('imagens/icon_252.png')
img_pokemon_7 = imagem_pokemon_7.resize((40,40))
imagem_pokemon_7 = ImageTk.PhotoImage(img_pokemon_7)

b_pok_img7 = Button(janela, command = lambda: trocar_pokemon('Treecko'), image = imagem_pokemon_7, text='Treecko', width=160, relief = 'raised', overrelief=RIDGE,compound = LEFT, anchor=NW, padx = 5, font=('Fixedsys 14'),bg=co1, fg=co0)
b_pok_img7.place(x = 375, y=310)


imagem_pokemon_8 = Image.open('imagens/icon_255.png')
img_pokemon_8 = imagem_pokemon_8.resize((40,40))
imagem_pokemon_8 = ImageTk.PhotoImage(img_pokemon_8)

b_pok_img8 = Button(janela, command = lambda: trocar_pokemon('Torchic'), image = imagem_pokemon_8, text='Torchic', width=160, relief = 'raised', overrelief=RIDGE,compound = LEFT, anchor=NW, padx = 5, font=('Fixedsys 14'),bg=co1, fg=co0)
b_pok_img8.place(x = 375, y=360)


imagem_pokemon_9 = Image.open('imagens/icon_258.png')
img_pokemon_9 = imagem_pokemon_9.resize((40,40))
imagem_pokemon_9 = ImageTk.PhotoImage(img_pokemon_9)

b_pok_img9 = Button(janela, command = lambda: trocar_pokemon('Mudkip'), image = imagem_pokemon_9, text='Mudkip', width=160, relief = 'raised', overrelief=RIDGE,compound = LEFT, anchor=NW, padx = 5, font=('Fixedsys 14'),bg=co1, fg=co0)
b_pok_img9.place(x = 375, y=410)
# End Pokemon side menu

lista_pok = ['Bulbassauro', 'Charmander', 'Squirtle', 'Chikorita', 'Cyndaquil','Totodile','Treecko','Torchic','Mudkip'] # Escolher um Pokemon aleatório para mostrar no frame./ Choose a random Pokemon to show in the frame.
pok_escolhido = random.choice(lista_pok)
trocar_pokemon(pok_escolhido) # Pass the chosen Pokemon to the function responsible for changing/showing its info. This will display the information, based on the Pokemon's name, randomly chosen from the list.
# Passa o Pokemon escolhido para a função responsável por trocar/mostrar as suas informações. Dessa maneira, será mostrado as informações, baseado no nome do Pokemon, aleatoriamente escolhido na lista.

janela.mainloop() # Window Closing