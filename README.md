# Rogue-like игра "Tombs of the Ancient Kings" #
## Игра создана при помощи: ##
- [Python 2.7.2](http://python.org/)
- [libtcod](https://bitbucket.org/jice/libtcod)
- [Данного руководства](http://roguebasin.roguelikedevelopment.org/index.php/Complete_Roguelike_Tutorial,_using_python%2Blibtcod)

## Откуда есть пошла рогалик-игра (Материалы по рогаликам) ##
+ [Статья](http://ru.wikipedia.org/wiki/Roguelike) на википедии.
+ [Roguebasin](http://roguebasin.roguelikedevelopment.org/index.php/Main_Page)
+ [Отечественный форум рогаликолюбов](http://rlgclub.ru/wiki/%D0%A1%D1%82%D0%B0%D1%82%D1%8C%D0%B8)

## Значение некоторых символов в игре: ##
<pre>
@ - Главный герой (Вы)
! - Какое-либо зелье
# - Какой-либо свиток (а так же стены)
D, T, o, g - Монстры
Подробнее, о значении символа в игре можно узнать наведя на него мышью.
</pre>

## Управление: ##
<pre>
y   k   u
  \ | /
  
h - @ - l Перемещение (Традиционный Vi стиль)
  
  / | \
b   j   n

i - Открыть инвентарь
g - Взять какую-либо вещь под игроком
d - Выкинуть вещь из инвентаря
Esc - Выход в меню
Изменить клавиши можно в файле ./Config/game.py
</pre>

