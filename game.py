from player import Player
from typing import List, Callable
from card import UnoCard
from util import PlayedCards
import random

class Game:
    def __init__(self,player_num:int):
        self.player_num = player_num
        self.playedcards = PlayedCards()

        self.player_list: List[Player] = []
        self.unocard_pack:List[UnoCard] = []
        self.create_unocard_pack()

        self.cur_location:int = None
        self.cur_color:str = None

    #创造牌组
    def create_unocard_pack(self):
        colors = ['red','blue','yellow','green']
        type = ['reverse','skip','draw2']*2
        numbers = [0] + 2*[i for i in range(1,10)]
        for color in colors:
            for number in numbers:
                self.unocard_pack.append(UnoCard("number",color,number))
            for action in type:
                self.unocard_pack.append(UnoCard(action,color,0))
        for _ in range(4):
            self.unocard_pack.append(UnoCard('wild','wild',10))
            self.unocard_pack.append(UnoCard('wild_draw4','wild_draw4',10))
        random.shuffle(self.unocard_pack)
        
    #将玩家加对对局中同时将game赋给玩家
    def add_player(self,player:Player):
        self.player_list.append(player)
        player.game = self
    #发牌！ 每人8张 第一个出牌/主公9张(需要设定模式)
    def deal_cards(self):
        for player in self.player_list:
            player.get_card(8)
    
