# Swiss-Style Tournament Manager

This project is a Python module that uses the PostgreSQL database to keep track of players and matches in a swiss-style game tournament.

The program is tested by executing tournament_test.py.  If all goes well, the results will look like this:
```
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournamentgit$ python tournament_test.py
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournamentgit$
```

#Follow These Steps To Test The Program
(I'm assuming you already have python2.7 installed)

###Install Virtualbox###
https://www.virtualbox.org/wiki/Downloads

###Install Vagrant###
https://www.vagrantup.com/downloads

Verify that Vagrant is installed and working by typing in the terminal:

    $ vagrant -v   # will print out the Vagrant version number

###Clone the Repository###
Once you are sure that VirtualBox and Vagrant are installed correctly execute the following:

    $ git clone https://github.com/RPMorganomous/tournamentgit.git
    $ cd tournamentgit
    $ cd vagrant

###Verify that these files exist in the newly cloned repository:

    --tournamentgit          #folder containing tournament files
    ----tournament.py        #file that contains the python functions which 
                                unit tests will run on
    ----tournament_test.py   #unit tests for tournament.py
    ----tournament.sql       #postgresql database
    --Vagrantfile            #template that launches the Vagrant environment
    --pg_config.sh           #shell script provisioner called by Vagrantfile
                                that performs configurations

###Launch the Vagrant Box###

    $ vagrant up   #to launch and provision the vagrant environment
    $ vagrant ssh  #to login to your vagrant environment

###Change Directory To The Tournament Directory###

    $ cd /
    $ cd vagrant
    $ cd tournament

###Initialize the database###

    $ psql                       #start PostgreSQL
    vagrant=> \i tournament.sql  #import drops any existing tournament 
                                    database and creates a new database
    vagrant=> \q                 #exit PostgreSQL


###Run the tests###

    $ python tournament_test.py

You should see this result:

    Success!  All tests pass!

###Shutdown Vagrant machine###

    $ vagrant halt


###Destroy the Vagrant machine###

    $ vagrant destroy

###Coming Soon - UPGRADES###
* HTML interface for managing users and tournaments
* Mobile client app for monitoring tournament progress remotly
