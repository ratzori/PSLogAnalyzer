#!/usr/bin/python
import sys
import re

# Input handlers

#PokerStars Hand #xxxx...:  Hold'em No Limit ($xx.xx/$xx.xx USD) - YYYY/MM/DD HH:MM:SS TZ
def hand( data ):
    hand_number = data.group(1)
    game_type = data.group(2)
    small_blind = data.group(3)
    big_blind = data.group(4)
    currency = data.group(5)
    year = data.group(6)
    month = data.group(7)
    day = data.group(8)
    hour = data.group(9)
    min = data.group(10)
    sec = data.group(11)
    timezone = data.group(12)

    # Do something
    print ("Hand number", hand_number, "currency:", currency, "small blind:", small_blind, "big blind:", big_blind)

    return

# Seat x: nick ($x.xx in chips)
def table_status( data ):
    seat_number = data.group(1)
    player = data.group(2)
    money = data.group(3)

    # Do something
    print ("Player status", player, "seat:", seat_number, "money:", money)

    return

# nick: posts small blind $xx.xx
def small_blind( data ):
    player = data.group(1)
    blind = data.group(2)

    # Do something
    print("Player", player, " small blind:", blind)

    return

# nick: posts big blind $xx.xx
def big_blind( data ):
    player = data.group(1)
    blind = data.group(2)

    # Do something
    print("Player", player, " big blind:", blind)

    return

# *** HOLE CARDS ***
def hole_cards( data ):

    # Do something
    print("Hole cards")

    return

# Dealt to nick [xx xx]
def dealt( data ):

    player = data.group(1)
    card1 = data.group(2)
    card2 = data.group(3)

    # Do something
    print("Dealt cards", player, card1, card2)

    return

# nick: folds
def folds( data ):

    player = data.group(1)

    # Do something
    print("Folds", player)

    return

# nick: checks
def checks( data ):

    player = data.group(1)

    # Do something
    print("Checks", player)

    return

# *** FLOP CARDS *** [xx yy zz]
def flop_cards( data ):

    card1 = data.group(1)
    card2 = data.group(2)
    card3 = data.group(3)

    # Do something
    print("Flop cards", card1, card2, card3)

    return

# Compile Regex patterns
hand_re = re.compile(r'^PokerStars Hand #([0-9]+): (.+) \(\$([0-9]+\.[0-9]+)\/\$([0-9]+\.[0-9]+) (\w+)\) - ([0-9])+\/([0-9])+\/([0-9])+ ([0-9])+:([0-9])+:([0-9])+([0-9])+ (\w+)')
table_status_re = re.compile(r'^Seat ([0-9]): (\w+) \(\$([0-9]+\.[0-9]+) in chips\)')
small_blind_re = re.compile(r'^(\w+): posts small blind \$([0-9]+\.[0-9]+)')
big_blind_re = re.compile(r'^(\w+): posts big blind \$([0-9]+\.[0-9]+)')
hole_cards_re = re.compile(r'^\*\*\* HOLE CARDS \*\*\*')
dealt_re = re.compile(r'^Dealt to (\w+) \[(\w+) (\w+)\]')
folds_re = re.compile(r'^(\w+): folds')
checks_re = re.compile(r'^(\w+): checks')
flop_cards_re = re.compile(r'^\*\*\* FLOP \*\*\* \[(\w+) (\w+) (\w+)\]')

# Main parser loop
for line in sys.stdin:

    hand_m = hand_re.match(line)

    if ( hand_m ):
        hand( hand_m )
        continue

    table_status_m = table_status_re.match(line)

    if (table_status_m):
        table_status(table_status_m)
        continue

    small_blind_m = small_blind_re.match(line)

    if ( small_blind_m ):
        small_blind( small_blind_m )
        continue

    big_blind_m = big_blind_re.match(line)

    if ( big_blind_m ):
        big_blind( big_blind_m )
        continue

    hole_cards_m = hole_cards_re.match(line)

    if ( hole_cards_m ):
        hole_cards( hole_cards_m )
        continue

    dealt_m = dealt_re.match(line)

    if ( dealt_m ):
        dealt( dealt_m )
        continue

    folds_m = folds_re.match(line)

    if ( folds_m ):
        folds( folds_m )
        continue

    checks_m = checks_re.match(line)

    if ( checks_m ):
        checks( checks_m )
        continue

    flop_cards_m = flop_cards_re.match(line)

    if ( flop_cards_m ):
        flop_cards( flop_cards_m )
        continue

