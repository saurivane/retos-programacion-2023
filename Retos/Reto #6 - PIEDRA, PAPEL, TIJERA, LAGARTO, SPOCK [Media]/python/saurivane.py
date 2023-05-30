"""/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */"""
from enum import Enum


class Jugadas(Enum):
    PIEDRA = "🗿"
    PAPEL = "📃"
    TIJERA = "✂️"
    LAGARTO = "🐊"
    SPOCK = "🖖"


def game_pptls(game : list[tuple[str,str]]):
    player1 = 0
    player2 = 0
    
    for move in game:
        p1_jugada = move[0]
        p2_jugada = move[1]
        
        if p1_jugada != p2_jugada: 
            if (p1_jugada == "🗿" and p2_jugada == "✂️") or (p1_jugada == "📃" and p2_jugada == "🗿") or (p1_jugada == "✂️" and p2_jugada == "📃") or (p1_jugada == "🐊" and p2_jugada == "🖖") or (p1_jugada == "🖖" and p2_jugada == "🗿"):
                player1 += 1
            else:
                player2 += 1


    if player1 == player2:
        print('Tie!')
    elif player1 > player2:
        print('Player 1')
    elif player2 > player1:
        print('Player 2')
        
game_pptls([("📃","🗿"),("✂️","🗿"),("🖖","🗿")])
game_pptls([("🐊","📃"),("🖖","📃"),("✂️","📃")])
game_pptls([("🖖","🐊"),("🖖","🖖"),("🖖","📃"),("🗿","✂️"),("📃","🗿")])