#!/usr/bin/python
import sys
import re

# Input handlers

#PokerStars Hand #xxxx...:  Hold'em No Limit ($xx.xx/$xx.xx USD) - YYYY/MM/DD HH:MM:SS ET
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

# Compile Regex patterns
hand_re = re.compile(r'^PokerStars Hand #([0-9]+): (.+) \(\$([0-9]+\.[0-9]+)\/\$([0-9]+\.[0-9]+) (\w+)\) - ([0-9])+\/([0-9])+\/([0-9])+ ([0-9])+:([0-9])+:([0-9])+([0-9])+ (\w+)')
table_status_re = re.compile(r'^Seat ([0-9]): (\w+) \(\$([0-9]+\.[0-9]+) in chips\)')
small_blind_re = re.compile(r'^(\w+): posts small blind \$([0-9]+\.[0-9]+)')
big_blind_re = re.compile(r'^(\w+): posts big blind \$([0-9]+\.[0-9]+)')

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

