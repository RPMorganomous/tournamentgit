#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        return psycopg2.connect("dbname=tournament")
    except:
        print 'CONNECTION TO DATABASE %s FAILED' % 'tournament'
        return 'error'

def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    if conn != 'error':
        c = conn.cursor()
        c.execute("UPDATE players SET matches = 0, wins = 0;")
        conn.commit()
        conn.close()
    else:
        print 'conn = %s' % conn

def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    if conn != 'error':
        c = conn.cursor()
        c.execute("DELETE FROM players;")
        conn.commit()
        conn.close()
    else:
        print 'conn = %s' % conn

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    if conn != 'error':
        c = conn.cursor()
        c.execute("SELECT * FROM players;")
        row_count = c.rowcount
        conn.close()
        return row_count
    else:
        print 'conn = %s' % conn

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
#    name = raw_input("enter name: ")
    conn = connect()
    if conn != 'error':
        c = conn.cursor()
        c.execute("INSERT INTO players (name, wins, matches) VALUES (%s,0,0)", (name,))
        conn.commit()
        conn.close()
    else:
        print 'conn = %s' % conn

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    if conn != 'error':
        c = conn.cursor()
        c.execute("SELECT * FROM players order by wins desc;")
        standings_query = list(c.fetchall())
        conn.close()
        return standings_query
    else:
        print 'conn = %s' % conn

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    if conn != 'error':
        c = conn.cursor()
        c.execute("UPDATE players SET matches = matches + 1 WHERE id = '%s' ", (loser,))
        c.execute("UPDATE players SET wins = wins + 1, matches = matches + 1 WHERE id = '%s' ", (winner,))
        conn.commit()
        conn.close()
    else:
        print 'conn = %s' % conn

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = connect()
    if conn != 'error':
        c = conn.cursor()
#       c.execute(
#              "CREATE VIEW pairings AS SELECT
#              a.id, a.name, b.id, b.name FROM players as a, players as b
#              WHERE a.wins = b.wins
#              AND a.id < b.id
#              ORDER BY a.wins DESC;")
        i = 0
        pairings_query = []
        l=[]
        for x in range(4):
            c.execute("SELECT id, name FROM players ORDER BY wins Limit 2 OFFSET '%s'", (i,))
            l = c.fetchall()
            pairings_query.append( l[0] + l[1] )
# debug      print 'short querey is: ', pairings_query
            i = i + 2
        conn.close()
        return pairings_query
    else:
        print 'conn = %s' % conn

