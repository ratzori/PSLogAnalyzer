#!/usr/bin/python
import sys
import re

# Input handlers

#PokerStars Hand #xxxx...:  Hold'em No Limit ((symbol)xx.xx(symbol)/(symbol)xx.xx(symbol) CURRENCY) - YYYY/MM/DD HH:MM:SS TZ
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

# Table 'xxxx' x-max Seat #x is the button
def table( data ):
    table_name = data.group(1)
    max_seat = data.group(2)
    button_seat = data.group(3)

    # Do something
    print ("Table", table_name, "seat count:", max_seat, "seat:", button_seat,"is the button")

    return

# Seat x: nick ((symbol)xx.xx(symbol) in chips)
def table_status( data ):
    seat_number = data.group(1)
    player = data.group(2)
    money = data.group(3)

    # Do something
    print ("Player status", player, "seat:", seat_number, "money:", money)

    return

# nick: posts small blind (symbol)xx.xx(symbol)
def small_blind( data ):
    player = data.group(1)
    blind = data.group(2)

    # Do something
    print("Player", player, " small blind:", blind)

    return

# nick: posts big blind (symbol)xx.xx(symbol)
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

# nick: calls (symbol)xx.xx(symbol)
def calls( data ):

    player = data.group(1)
    call = data.group(2)

    # Do something
    print("Calls", player, call)

    return

# nick: bets (symbol)xx.xx(symbol)
def bets( data ):

    player = data.group(1)
    call = data.group(2)

    # Do something
    print("Bets", player, call)

    return

# *** FLOP CARDS *** [xx yy zz]
def flop_cards( data ):

    card1 = data.group(1)
    card2 = data.group(2)
    card3 = data.group(3)

    # Do something
    print("Flop cards", card1, card2, card3)

    return

# nick collected ((symbol)xx.xx(symbol) from the pot
def collected( data ):

    player = data.group(1)
    sum = data.group(2)

    # Do something
    print("Collected", player, sum)

    return

# Uncalled bet
def uncalled_bet( data ):

    bet = data.group(1)
    player = data.group(2)

    # Do something
    print("Uncalled bet returned", player, bet)

    return

# nick collected (symbol)xx.xx(symbol) from pot
def collected( data ):

    player = data.group(1)
    sum = data.group(2)

    # Do something
    print("Collected", player, sum)

    return

# nick: doesn't show hand
def doesnt_show_hand( data ):

    player = data.group(1)

    # Do something
    print("Doesn't show hand", player)

    return

# *** SUMMARY ***
def summary( data ):

    # Do something
    print("Summary")

    return

# Seat x: nick (xxxx) folded before Flop (xxxx)
def summary_folded_before_flop( data ):

    seat_number = data.group(1)
    player = data.group(2)
    extra_info1 = data.group(3)
    extra_info2 = data.group(4)

    # Do something
    print("Summary - folded before flop", seat_number, player)

    return

# Seat x: nick collected (symbol)xx.xx(symbol)
def summary_collected( data ):

    seat_number = data.group(1)
    player = data.group(2)
    extra_info1 = data.group(3)
    sum = data.group(4)

    # Do something
    print("Summary - collected", seat_number, player, sum, extra_info1)

    return

# Compile Regex patterns
hand_re = re.compile(r"^PokerStars Hand #([0-9]+): (.+) \(.*([0-9]+\.[0-9]+).*\/.*([0-9]+\.[0-9]+).* (\w+)\) - ([0-9])+\/([0-9])+\/([0-9])+ ([0-9])+:([0-9])+:([0-9])+([0-9])+ (\w+)")
table_re = re.compile(r"^Table '(.+)' ([0-9])-max Seat #([0-9]) is the button")
table_status_re = re.compile(r"^Seat ([0-9]): (\w+) \(.*([0-9]+\.[0-9]+).* in chips\)")
small_blind_re = re.compile(r"^(\w+): posts small blind .*([0-9]+\.[0-9]+).*")
big_blind_re = re.compile(r"^(\w+): posts big blind .*([0-9]+\.[0-9]+).*")
hole_cards_re = re.compile(r"^\*\*\* HOLE CARDS \*\*\*")
dealt_re = re.compile(r"^Dealt to (\w+) \[(\w+) (\w+)\]")
folds_re = re.compile(r"^(\w+): folds")
checks_re = re.compile(r"^(\w+): checks")
raises_re = re.compile(r"^(\w+): raises .*([0-9]+\.[0-9]+).* to .*([0-9]+\.[0-9]+).*")
calls_re = re.compile(r"^(\w+): calls .*([0-9]+\.[0-9]+).*")
bets_re = re.compile(r"^(\w+): bets .*([0-9]+\.[0-9]+).*")
flop_cards_re = re.compile(r"^\*\*\* FLOP \*\*\* \[(\w+) (\w+) (\w+)\]")
collected_re = re.compile(r"^(\w+) collected .*([0-9]+\.[0-9]+).* from pot")
uncalled_bet_re = re.compile(r"^Uncalled bet \(.*([0-9]+\.[0-9]+).*\) returned to (\w+)")
doesnt_show_hand_re = re.compile(r"^(\w+): doesn't show hand")
summary_folded_before_flop_re = re.compile(r"^Seat ([0-9]): (\w+)(\(?.*\)?) folded before Flop(\(?.*\)?)")
summary_collected_re = re.compile(r"^Seat ([0-9]): (\w+)(\(?.*\)?) collected \(.*([0-9]+\.[0-9]+).*\)")
summary_re = re.compile(r"^\*\*\* SUMMARY \*\*\*")

# Main parser loop
for line in sys.stdin:

    hand_m = hand_re.match(line)

    if ( hand_m ):
        hand( hand_m )
        continue

    table_m = table_re.match(line)

    if ( table_m ):
        table( table_m )
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

    calls_m = calls_re.match(line)

    if ( calls_m ):
        calls( calls_m )
        continue

    bets_m = bets_re.match(line)

    if ( bets_m ):
        bets( bets_m )
        continue

    flop_cards_m = flop_cards_re.match(line)

    if ( flop_cards_m ):
        flop_cards( flop_cards_m )
        continue

    collected_m = collected_re.match(line)

    if ( collected_m ):
        collected( collected_m )
        continue

    uncalled_bet_m = uncalled_bet_re.match(line)

    if ( uncalled_bet_m ):
        uncalled_bet( uncalled_bet_m )
        continue

    doesnt_show_hand_m = doesnt_show_hand_re.match(line)

    if ( doesnt_show_hand_m ):
        doesnt_show_hand( doesnt_show_hand_m )
        continue

    summary_m = summary_re.match(line)

    if ( summary_m ):
        summary( summary_m )
        continue

    summary_folded_before_flop_m = summary_folded_before_flop_re.match(line)

    if ( summary_folded_before_flop_m ):
        summary_folded_before_flop( summary_folded_before_flop_m )
        continue

    summary_collected_m = summary_collected_re.match(line)

    if ( summary_collected_m ):
        summary_collected( summary_collected_m )
        continue
