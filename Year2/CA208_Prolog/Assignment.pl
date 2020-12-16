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

%modey(Mode,Speed) facts which shows the speed of a Mode of transport
modey(f, 5).
modey(c, 80).
modey(t, 100).
modey(p, 500).

%modez(Speed,Mode) facts which shows the Mode corresponding to it's speed
modez(5, f).
modez(80, c).
modez(100, t).
modez(500, p).


routen(S,D,Lst) :- 		%base case checks if a fact exists for source S and destination D
	route(S,D,Dist,M),			%and returns the route, fastest mode, and time taken in M
	string_chars(M,ModeList),	% converts string to list
	modes(ModeList,modey,Speeds),	%applies modey predicate to each item in ModeList and result stored in the list Speeds
	maxList(Speeds,Fastest),		% finds the fastest speed and stores it in Fastest
	modez(Fastest,FastestMode),		%applies modez to Fastest to get FastestMode
	Time is Dist / Fastest,			% calcutates time
	append([],[S,D,FastestMode,Time],Lst), !.	%store result in the list Lst.

routen(S,D,Lst) :-			% recursive function
	route(S,D1,Dist1,M1),		%checks next route
	routen(D1,D,Lst2),			% recursively does this until it matches
	string_chars(M1,ModeList1),
	modes(ModeList1,modey,Speed1),
	maxList(Speed1,TopSpeed1),	%everything else is calculated similarly to base case
	Time1 is Dist1 / TopSpeed1,
	modez(TopSpeed1,BestMode1),
	append([S,D1,BestMode1,Time1],Lst2,Lst).



modes([],_,[]).		%base case: if list is empty, we have nothing to return
modes([X|Tail],F,[NewX|NewTail]) :-		%else we apply funtor F to each element of the list in first argument
	Goal =.. [F,X,NewX], call(Goal),	% and store it to newlist
	modes(Tail,F,NewTail).				% i.e Goal will become modey(Mode,Speed) on each item and Speed will be stored in the newlist

%more efficient method of getting the max between 2 numbers
max(X,Y,Z) :- X =< Y, !, Z = Y.
max(X,_,X).

%predicate which returns the maximum number in a list
maxList([X],X) :- !.	%if one element in list, that element is the max
maxList([X,Y|T],M) :-	% else we keep searching recursively
	maxList([Y|T],M1),
	max(X,M1,M).

journey(S,D,M) :-		% journey predicate calls the routen predicate
	routen(S,D,M).		% result stored in M

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
deletion(Source, Result) :- 
	findall(Places,(source(List), member(Places,List), Places \= Source),Result).