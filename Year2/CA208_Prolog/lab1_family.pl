/* FACTS */

parents(david, george, noreen).
parents(jennifer, george, noreen).
parents(georgejr, george, noreen).
parents(scott, george, noreen).
parents(joanne, george, noreen).

parents(jessica, david, edel).
parents(clara, david, edel).
parents(michael, david, edel).
parents(laura, georgejr, susan).
parents(anna, scott, siobhan).


/* Relationships */

father(X, Y) :- parents(Y, X, _).
male(michael).
male(X) :- father(X, _).

mother(X, Y) :- parents(Y, _, X).
female(joanne).
female(jessica).
female(jennifer).
female(clara).
female(laura).
female(anna).
female(X) :- mother(X, _).

grandfather(X,Y) :- father(X, Z), father(Z, Y).
grandfather(X,Y) :- father(X, Z), mother(Z, Y).

grandmother(X,Y) :- mother(X, Z), mother(Z, Y).
grandmother(X,Y) :- mother(X, Z), father(Z, Y).

brother(X,Y) :- male(X), father(Z, X), father(Z, Y),  X \== Y.
sister(X,Y) :- female(X), father(Z,X), father(Z,Y), X \== Y.


% NEW RELATIONSHIPS
parent(X,Y) :- father(X,Y) ; mother(X,Y).
sibling(X,Y) :- brother(X,Y) ; sister(X,Y).

uncle(X,Y) :- male(X), not(father(X,Y)), brother(X,Z), father(Z,Y).

aunt(X,Y) :- parent(Z,Y), sister(X,Z).
aunt(X,Y) :- female(X), not(mother(X,Y)), uncle(Z,Y), parents(_,Z,X).

cousin(X,Y) :- parent(Z,X), parent(W,Y), sibling(Z,W).
