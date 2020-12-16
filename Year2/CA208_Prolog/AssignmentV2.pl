%Relationships
route(dublin, cork, 200, 'fct').
route(cork, dublin, 200, 'fct').
route(cork, corkAirport, 20, 'fc').
route(corkAirport, cork, 25, 'fc').
route(dublin, dublinAirport, 10, 'fc').
route(dublinAirport, dublin, 20, 'fc').
route(dublinAirport, corkAirport, 225, 'p').
route(corkAirport, dublinAirport, 225, 'p').
route(dublinAirport, londonAirport, 600, 'p').
route(londonAirport, dublinAirport, 600, 'p').
route(corkAirport, londonAirport, 825, 'p').
route(londonAirport, corkAirport, 825, 'p').
route(londonAirport, london, 30, 'ftc').
route(london, londonAirport, 30, 'ftc').


modey(f, 5).
modey(c, 80).
modey(t, 100).
modey(p, 500).
modez(5, f).
modez(80, c).
modez(100, t).
modez(500, p).

l(L) :- findall(M,routenTemp(_,_,_,_,M), L).
source(List) :- findall(Source,route(Source,_,_,_), List).
dest(List) :- findall(Destiny,route(_,Destiny,_,_), List).



%foo(Ftime1) :- routen(S,D),findall(Times,(string_chars(Modes1,ModeList),member(f,ModeList),
%	Times is Dist / 5), Ftime1).


modes([],_,[]).
modes([X|Tail],F,[NewX|NewTail]) :-
	Goal =.. [F,X,NewX], call(Goal),
	modes(Tail,F,NewTail).

max(X,Y,Z) :- X =< Y, !, Z = Y.
max(X,_,X).

myMember(X,[X|_]) :- !.
myMember(X,[_|T]) :- myMember(X,T).

maxList([X],X).
maxList([X,Y|T],M) :-
	maxList([Y|T],M1),
	max(X,M1,M).



deletion(Source, List) :- findall(Places,(source(Sources), member(Places,Sources),
		Places \= Source), List).

add(X,L,L) :- myMember(X,L),!.
add(X,L,[X|L]).






myLast(X,[X]).
myLast(X,[_|T]) :-
	myLast(X,T).

journeyTemp(S,D,M) :-
	source(List),
	routenTemp(S,D,M,List).
routenTemp(S,D,Lst,Sources) :-
	route(S,D,Dist,M),
	string_chars(M,ModeList),
	modes(ModeList,modey,Speeds),
	maxList(Speeds,Fastest),
	modez(Fastest,FastestMode),
	Time is Dist / Fastest,
	append([],[S,D,FastestMode,Time],Lst),
	deletion(S,Sources),!.
routenTemp(S,D,Lst,Sources) :-			% recursive function
	route(S,D1,Dist1,M1),		%checks next route
	deletion(S,Sources),
	routen(D1,D,Lst2),			% recursively does this until it matches
	string_chars(M1,ModeList1),
	modes(ModeList1,modey,Speed1),
	maxList(Speed1,TopSpeed1),	%everything else is calculated similarly to base case
	Time1 is Dist1 / TopSpeed1,
	modez(TopSpeed1,BestMode1),
	append([S,D1,BestMode1,Time1],Lst2,Lst).

