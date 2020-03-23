#  Music
#       /      \
#    Rock      Gothic ------
#    /     \        /       \
# Metal    Gothic Rock       \
#   |             |           \
#    \------------------ Gothic Metal
#                 |          /
#                 The 69 Eyes

class Music(object): pass
class Rock(Music): pass
class Gothic(Music): pass
class Metal(Rock): pass
class GothicRock(Rock, Gothic): pass
class GothicMetal(Metal, Gothic): pass
class The69Eyes(GothicRock, GothicMetal): pass

# L[The69Eyes] = [The69Eyes] + merge(L[GothicRock], L[GothicMetal], [GothicRock, GothicMetal])
# L[GothicRock] = [GothicRock] + merge(L[Rock], L[Gothic], [Rock, Gothic])
# L[GothicMetal] = [GothicMetal] + merge(L[Metal], L[Gothic], [Metal, Gothic])
# L[Rock] = [Rock, Music]
# L[Gothic] = [Gothic, Music]
# L[Metal] = [Metal] + [Rock, Music] = [Metal, Rock, Music]

# После подстановок получаем:
# L[GothicRock] = [GothicRock] + merge([Rock, Music], [Gothic, Music], [Rock, Gothic]) = [GothicRock, Rock, Gothic, Music]
# L[GothicMetal] = [GothicMetal] + merge([Metal, Rock, Music], [Gothic, Music], [Metal, Gothic]) = [GothicMetal] + [Metal, Rock, Gothic, Music] = [GothicMetal, Metal, Rock, Gothic, Music]
# L[The69Eyes] = [The69Eyes] + merge([GothicRock, Rock, Gothic, Music], [GothicMetal, Metal, Rock, Gothic, Music], [GothicRock, GothicMetal])
# = [The69Eyes] + [GothicRock, GothicMetal] + merge([Rock, Gothic, Music], [Metal, Rock, Gothic, Music])
# = [The69Eyes] + [GothicRock, GothicMetal, Metal] + merge([Rock, Gothic, Music], [Rock, Gothic, Music])
# = [The69Eyes, GothicRock, GothicMetal, Metal, Rock, Gothic, Music]


#       Food -------
#      /    \       \
#     Meat  Milk  Flour
#     |   \    \    /  
# Rabbit  Pork  Pasty
#       \   |   /
#          Pie

class Food(object): pass
class Meat(Food): pass
class Milk(Food): pass
class Flour(Food): pass
class Rabbit(Meat): pass
class Pork(Meat): pass
class Pasty(Milk, Flour): pass
class Pie(Rabbit, Pork, Pasty): pass

# L[Pie] = [Pie] + merge(L[Rabbit], L[Pork], L[Pasty], [Rabbit, Pork, Pasty])
# L[Rabbit] = [Rabbit] + merge(L[Meat], [Meat])
# L[Pork] = [Pork] + merge(L[Meat], [Meat])
# L[Pasty] = [Pasty] + merge(L[Milk], L[Flour], [Milk, Flour])
# L[Meat] = [Meat] + merge(L[Food], [Food]) = [Meat, Food]
# L[Milk] = [Milk] + merge(L[Food], [Food]) = [Milk, Food]
# L[Flour] = [Flour] + merge(L[Food], [Food]) = [Flour, Food]

# После подстановок получаем:
# L[Rabbit] = [Rabbit, Meat, Food]
# L[Pork] = [Pork, Meat, Food]
# L[Pasty] = [Pasty] + merge([Milk, Food], [Flour, Food], [Milk, Flour]) = [Pasty] + [Milk, Flour, Food] = [Pasty, Milk, Flour, Food]
# L[Pie] = [Pie] + merge([Rabbit, Meat, Food], [Pork, Meat, Food], [Pasty, Milk, Flour, Food], [Rabbit, Pork, Pasty])
# = [Pie] + [Rabbit] + merge([Meat, Food], [Pork, Meat, Food], [Pasty, Milk, Flour, Food], [Pork, Pasty])
# = [Pie] + [Rabbit, Pork] + merge([Meat, Food], [Meat, Food], [Pasty, Milk, Flour, Food], [Pasty])
# = [Pie] + [Rabbit, Pork, Meat] + merge([Food], [Food], [Pasty, Milk, Flour, Food], [Pasty])
# = [Pie] + [Rabbit, Pork, Meat, Pasty] + merge([Food], [Food], [Milk, Flour, Food])
# = [Pie] + [Rabbit, Pork, Meat, Pasty, Milk, Flour, Food]
# = [Pie, Rabbit, Pork, Meat, Pasty, Milk, Flour, Food]
