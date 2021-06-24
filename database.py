from sqlite3 import *
def insertscore(player_id,name,score):
    con = connect('rps.db')
    cur = con.cursor()
    cur.execute("insert into scores(player_id,name,high_score) values('{0}','{1}',{2})".format(player_id,name,score))
    con.commit()
    con.close()
def updatescore(player_id,score):
    con = connect('rps.db')
    cur = con.cursor()
    cur.execute("update scores set high_score = {0} where player_id = '{1}'".format(score,player_id))
    con.commit()
    con.close()
def getscore():
    con = connect('rps.db')
    cur = con.cursor()
    cur.execute("select * from scores")
    players = cur.fetchall()
    con.close()
    return players
def searchscore(player_id):
    con = connect('rps.db')
    cur = con.cursor()
    cur.execute("select * from scores where player_id = '{0}'".format(player_id))
    player = cur.fetchone()
    con.close()
    return player







