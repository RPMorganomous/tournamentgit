-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- get rid of the existing database
DROP DATABASE IF EXISTS tournament;

-- create the new database
CREATE DATABASE tournament;

-- connect to the new database
\c tournament

-- create the players table
CREATE TABLE players(id serial NOT NULL PRIMARY KEY,
                    name varchar(100),
                    wins int,
                    matches int);

-- create the tournament table
CREATE TABLE tournament(TournamentID int,
                        TournamentName varchar(100),
                        TournamentCity varchar(100),
                        TournamentDate date,
                        TournamentCompetitorsID text);

-- create the results table
CREATE TABLE scores(TournamentID int,
                    PlayerID int,
                    PlayerScore int);

-- create the matches table
CREATE TABLE matches(RoundID int,
                    MatchID int,
                    PlayerOneID int,
                    PlayerOneScore int,
                    PlayerTwoID int,
                    PlayerTwoScore int
                    );


