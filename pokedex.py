import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import pypokedex
import urllib3
from io import BytesIO
from pypokedex import Move

preta = "#444466"
branco = "#feffff"
azul = "#6f9fbd"
vermelho = "#ef5350"

tela = ctk.CTk()
tela.geometry("800x700")
tela.resizable(height=False, width=False)
tela.iconbitmap(default="pokebolaICO.ico")
tela.configure(bg=branco)

style = ttk.Style(tela)
style.theme_use("clam")

framePokemon = Frame(tela, width=800, height=700, relief='flat', bg=branco)
framePokemon.grid(row=0, column=0)

#====== NOMES DOS POKEMON ======
pokeNome = Label(framePokemon, text="", relief='flat', anchor=CENTER, font=('Fixedsys 40'), bg=branco, fg=preta)
pokeNome.place(x=250, y=15)

#====== TIPO ======
pokeTipo = Label(framePokemon, text="", relief='flat', anchor=CENTER, font=('Ivy 15 bold'), bg=branco, fg=preta)
pokeTipo.place(x=250, y=70)

#====== ID ======
pokeID = Label(framePokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 15 bold'), bg=branco, fg=preta)
pokeID.place(x=250, y=100)

#====== FOTO DO POKEMON ======
pokeFotoLabel = Label(framePokemon, relief='flat', bg=branco, fg=preta)
pokeFotoLabel.place(x=310, y=70)

pokeTipo.lift()

#====== STATUS ======
pokeStatus = Label(framePokemon, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20 bold'), bg=branco, fg=preta)
pokeStatus.place(x=250, y=330)

#====== HP ======
pokeHP = Label(framePokemon, text='', relief='flat', anchor=CENTER, font=('Verdana 15'), bg=branco, fg=preta)
pokeHP.place(x=250, y=365)

#====== ATAQUE ======
pokeAtaque = Label(framePokemon, text='Ataque: ', relief='flat', anchor=CENTER, font=('Verdana 15'), bg=branco, fg=preta)
pokeAtaque.place(x=250, y=395)

#======= DEFESA ======
pokeDefesa = Label(framePokemon, text='Defesa: ', relief='flat', anchor=CENTER, font=('Verdana 15'), bg=branco, fg=preta)
pokeDefesa.place(x=250, y=425)

#====== VELOCIDADE ======
pokeVelocidade = Label(framePokemon, text='Velocidade: ', relief='flat', anchor=CENTER, font=('Verdana 15'), bg=branco, fg=preta)
pokeVelocidade.place(x=250, y=455)

#====== HABILIDADES ======
tituloHB = Label(framePokemon, text='Habilidade', relief='flat', anchor=CENTER, font=('Verdana 20 bold'), bg=branco, fg=preta)
tituloHB.place(x=450, y=330)

pokeHB1 = Label(framePokemon, text='', relief='flat', anchor=CENTER, font=('Verdana 15'), bg=branco, fg=preta)
pokeHB1.place(x=450, y=365)

pokeHB2 = Label(framePokemon, text='', relief='flat', anchor=CENTER, font=('Verdana 15'), bg=branco, fg=preta)
pokeHB2.place(x=450, y=395)

def buscarPokemon():
        pokemon = pypokedex.get(name=pokemonIDEntrada.get(1.0, "end-1c"))
        http = urllib3.PoolManager()
        response = http.request('GET', pokemon.sprites.front.get('default'))
        image = Image.open(BytesIO(response.data))

        image = image.resize((280, 280))
        img = ImageTk.PhotoImage(image)
        pokeFotoLabel.configure(image=img)
        pokeFotoLabel.image = img

        pokeNome.configure(text=f"{pokemon.name.capitalize()}")
        pokeID.configure(text=f"#{pokemon.dex}")
        pokeTipo.configure(text=f"{pokemon.types[0].capitalize()}")
        pokeHP.configure(text=f"HP: {pokemon.base_stats.hp}")
        pokeAtaque.configure(text=f"Ataque: {pokemon.base_stats.attack}")
        pokeDefesa.configure(text=f"Defesa: {pokemon.base_stats.defense}")
        pokeVelocidade.configure(text=f"Velocidade: {pokemon.base_stats.speed}")
        
        if len(pokemon.moves) > 0:
            pokeHB1.configure(text=f"{pokemon.abilities[0].name.capitalize()}")
        else:
            pokeHB1.configure(text="")
        
        if len(pokemon.moves) > 1:
            pokeHB2.configure(text=f"{pokemon.abilities[1].name.capitalize()}")
        else:
            pokeHB2.configure(text="")
            

#====== ABA DE BUSCA ======
pokemonIDLabel = Label(tela, text="ID ou Nome", font=("Verdana 20 bold"), bg=branco, fg=preta)
pokemonIDLabel.place(x=330, y=500)

pokemonIDEntrada = ctk.CTkTextbox(tela, height=1)
pokemonIDEntrada.configure(font=("verdana", 20))
pokemonIDEntrada.place(x=350, y=550)

buscarBotao = ctk.CTkButton(tela, text="Buscar", command=buscarPokemon)
buscarBotao.configure(font=("arial", 20))
buscarBotao.place(x= 350, y=600)

tela.mainloop()
