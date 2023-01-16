from importlib.resources import contents #Importation du module pour les contents
from re import X #Importation automatique
import discord #Importation du module disocrd 
from discord.ext import commands # Importation du module discordt ext où on importe les methodes commandes de ce module
from discord_slash import ButtonStyle, SlashCommand #Importation de discord slash, ou l'on importe les methode de ButtonStyle et de SlashCommand
from discord_slash.utils.manage_components import * #Importation des tout le module des components de discord slash
from questionPy import * #Importation du second fichier .py qui contient les differentes questions
from random import * #Importation du module random 

bot = commands.Bot(command_prefix = "!", description = "Bot qui pose des questions pour vous entrainez en Python") #Creation d'une instance du bot dans une variable bot, qui prend en prefix de commande "!" 
slash = SlashCommand(bot, sync_commands=True) #Creation d'une instance de SlashCommand dans la variable slash, on active les commandes avec le boolean True

@bot.event #On declare un evenement du bot, avec le prefix "@", puis "bot.event"
async def on_ready(): #Creation de la fonction à partir d'une deja presente dans le module, on_ready(), cette fonction permet de faire des actions quand le bot s'active
    print("prêt !") #On print "pret !" dans la console pour signaler que le bot est bien allumé



@bot.command() #Creation d'une commande a partir du bot, avec le prefix "@", puis "bot.command"
async def choix(ctx): #Creation d'une fonction qu'on nomme comme l'on veut, le nom de la fonction sera la commande a taper avec le prefix de notre bot, soit "!", on met en parametre "ctx" pour le contexte que le bot doit avoir

    chooseList = randint(0, 8) #Assigne un nombre aleatoire à la variable chooseList entre 0 et 8

    if chooseList == 0: #Si le nombre de la variable est egal à 0 alors 
        x = question1 #Assigne à la variable x la liste question1
        y = reponse1 #Assigne à la variable y la liste question1
    if chooseList == 1: #Si le nombre de la variable est egal à 1 alors 
        x = question2 #Assigne à la variable x la liste question2
        y = reponse2 #Assigne à la variable y la liste question2
    if chooseList == 2: #Si le nombre de la variable est egal à 2 alors 
        x = question3 #Assigne à la variable x la liste question3
        y = reponse3 #Assigne à la variable y la liste question3
    if chooseList == 3: #Si le nombre de la variable est egal à 3 alors 
        x = question4 #Assigne à la variable x la liste question4   
        y = reponse4 #Assigne à la variable y la liste question4
    if chooseList == 4: #Si le nombre de la variable est egal à 4 alors 
        x = question5 #Assigne à la variable x la liste question5    
        y = reponse5 #Assigne à la variable y la liste question5
    if chooseList == 5: #Si le nombre de la variable est egal à 5 alors 
        x = question6 #Assigne à la variable x la liste question6
        y = reponse6 #Assigne à la variable y la liste question6
    if chooseList == 6: #Si le nombre de la variable est egal à 6 alors 
        x = question7 #Assigne à la variable x la liste question7
        y = reponse7 #Assigne à la variable y la liste question7
    if chooseList == 7: #Si le nombre de la variable est egal à 7 alors 
        x = question8 #Assigne à la variable x la liste question8
        y = reponse8 #Assigne à la variable y la liste question8
    if chooseList == 8: #Si le nombre de la variable est egal à 8 alors 
        x = question9 #Assigne à la variable x la liste question9
        y = reponse9 #Assigne à la variable y la liste question9

    buttons = [ #Creation d'une liste de bouton
        create_button( #Creation d'un bouton 
            style=ButtonStyle.blue, #Attributation de la couleur bleue au bouton
            label=x[1], #Le texte dans le bouton sera ce qui a à l'index 1 de la liste x
            custom_id=y[1] #On attribut l'index 1 de la liste y à un ID du bouton
        ),
        create_button( #Creation d'un bouton
            style=ButtonStyle.green,#Attributation de la couleur verte au bouton
            label=x[2], #Le texte dans le bouton sera ce qui a à l'index 2 de la liste x
            custom_id=y[2] #On attribut l'index 2 de la liste y à un ID du bouton
        ),
        create_button( #Creation d'un bouton
            style=ButtonStyle.red, #Attributation de la couleur rouge au bouton
            label=x[3], #Le texte dans le bouton sera ce qui a à l'index 3 de la liste x
            custom_id=y[3] #On attribut l'index 3 de la liste y à un ID du bouton
        ),
        create_button( #Creation d'un bouton
            style=ButtonStyle.blurple, #Attributation de la couleur bleue violet au bouton
            label=x[4], #Le texte dans le bouton sera ce qui a à l'index 4 de la liste x
            custom_id=y[4] #On attribut l'index 4 de la liste y à un ID du bouton
        )
    ]

    action_row = create_actionrow(*buttons) #Creation d'un Actionrow qui prend comme composants tous les boutons de la liste de boutons
    fait_choix = await ctx.send(x[0], components=[action_row]) #On assigne à la variable "fait_choix" le fait d'envoyer un message, qui prendre le contenue de l'index 0 de la premiere liste et qui enverra notre actionrow, donc nos boutons

    def check(m): #Creation d'une fonction permettant de verifier qui est l'auteur de la commande pour eviter les bots, on met en paramettre m, qui correspond au message
        return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id #Retourne True si : l'auteur du message et le meme qui celui envoyé, et si l'id de l'origine du message et le meme que l'id des messages

    button_ctx = await wait_for_component(bot, components=action_row, check=check) #Assigne à la variable "button_ctx", l'affichage des boutons, avec en parametre : le bot, les composents (ici nos boutons), et la fonction check permettant de verifier l'etat du message
    if button_ctx.custom_id == "1": #Si l'id du boutton cliquer est egal à 1 alors
        await button_ctx.edit_origin(content=x[5]) #Edit du message principal par celui qui à l'index 5 dans la liste de la variable x    
             
    else : #Sinon 
        await button_ctx.edit_origin(content=x[6]) #Edit du message principal par celui qui à l'index 6 dans la liste de la variable x   


bot.run("") #Entre guillement veuiller mettre le token de votre bot pour le connecter à votre serveur

#© TDLegends
