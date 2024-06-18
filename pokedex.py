import pypokedex
import customtkinter as tk
from tkinter import *
from tkinter import messagebox
import urllib3
from io import BytesIO
import PIL.Image, PIL.ImageTk



tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

tela = tk.CTk()
tela.geometry("600x500")
tela.title("PokeDex")
tela.config(padx=10, pady=10)
tela.iconbitmap(default="pokebolaICO.ico")

pokedexLabel = tk.CTkLabel(tela, text="Pokedex")
pokedexLabel.configure(font=("arial", 20))
pokedexLabel.pack(padx=10, pady=10)

pokemonFoto = tk.CTkLabel(tela, text="")
pokemonFoto.pack()

pokemonInfo = tk.CTkLabel(tela, text="")
pokemonInfo.configure(font=("arial", 20))
pokemonInfo.pack(padx=10, pady=10)

pokemonTipos = tk.CTkLabel(tela, text="")
pokemonTipos.configure(font=("arial", 20))
pokemonTipos.pack(padx=10, pady=10)

def buscarPokemon():
    pokemon = pypokedex.get(name=pokemonIDEntrada.get(1.0, "end-1c"))
    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemonFoto.configure(image=img)
    pokemonFoto.image = img

    pokemonInfo.configure(text=f"{pokemon.dex} - {pokemon.name}")
    pokemonTipos.configure(text=f"{pokemon.types}")

pokemonIDLabel = tk.CTkLabel(tela, text="ID ou Nome")
pokemonIDLabel.configure(font=("arial", 20))
pokemonIDLabel.pack(padx=10, pady=10)

pokemonIDEntrada = tk.CTkTextbox(tela, height=1)
pokemonIDEntrada.configure(font=("arial", 20))
pokemonIDEntrada.pack(padx=10, pady=10)

buscarBotao = tk.CTkButton(tela, text="Buscar", command=buscarPokemon)
buscarBotao.configure(font=("arial", 20))
buscarBotao.pack(padx=10, pady=10)








tela.mainloop()