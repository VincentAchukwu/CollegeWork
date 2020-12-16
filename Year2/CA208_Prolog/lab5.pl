class(X,zero) :- !.
class(X,positive) :- X > 0, !.
class(X,negative) :- X < 0, !.

split([],[],[]) :- !.
split([X|T],[X|XP],N) :- X >= 0, split(T,XP,N), !.
split([X|T],P,[X|XN]) :- split(T,P,XN), !.

:- dynamic fib/2.
fib(0,1).
fib(1,1).
fib(X,N) :-
	X1 is X - 1, X2 is X - 2,
	fib(X1,N1), fib(X2,N2),
	N is N1 + N2, asserta(fib(X,N)), !.
