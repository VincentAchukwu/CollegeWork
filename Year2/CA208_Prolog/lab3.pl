myElem(X,[X|_]) :- !.
myElem(X,[_|T]) :- 
	myElem(X,T).

myHead(X,[X|_]).

myLast(X,[X]).
myLast(X,[_|T]) :-
	myLast(X,T).

myTail(X,[_|X]).

myAppend([],L,L).
myAppend([X|T1],L,[X|T2]) :-
	myAppend(T1,L,T2).

myReverse([],[]).
myReverse([X|T1],R) :-
	myReverse(T1,R1), myAppend(R1,[X],R).

myDelete(X,[X|Y],Y).
myDelete(X,[H1|T1],[H1|T2]) :-
	myDelete(X,T1,T2).
