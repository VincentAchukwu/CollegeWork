% Q1 Book Recommender

book(illiad, homer, drama, 500).
book(c, richie, study, 150).
book(nt_bible, sams, reference, 480).
book(monty_python, cleese, comedy, 300).
book(of_Mice_and_Men, john_steinbeck, fiction, 200).

buildLibrary(Lib) :- findall(book(Title, Author, Genre, Size), book(Title, Author,
Genre, Size), Lib).

is_holiday(book(_, _, G, P)) :- (G \= study ; G \= reference), P < 400.
is_revision(book(_, _, G, P)) :- (G == study ; G == reference), P > 300.
is_literacy(book(_, _, G, _)) :- G == drama.
is_leisure(book(_, _, G, _)) :- (G == comedy ; G == fiction).

holiday(B, [B|_]) :- is_holiday(B).
holiday(B, [_|T]) :- holiday(B,T).

revision(B, [B|_]) :- is_revision(B).
revision(B, [_|T]) :- revision(B, T).

literacy(B, [B|_]) :- is_literacy(B).
literacy(B, [_|T]) :- literacy(B, T).

leisure(B, [B|_]) :- is_leisure(B).
leisure(B, [_|T]) :- leisure(B, T).


% Q2 North-East-South-West

directly_north(a,f).
directly_north(b,g).
directly_north(c,h).
directly_north(d,i).
directly_north(e,j).
directly_north(f,k).
directly_north(g,l).
directly_north(h,m).
directly_north(i,n).
directly_north(j,o).
directly_north(k,p).
directly_north(l,q).
directly_north(m,r).
directly_north(n,s).
directly_north(o,t).

directly_west(a,b).
directly_west(b,c).
directly_west(c,d).
directly_west(d,e).
directly_west(f,g).
directly_west(g,h).
directly_west(h,i).
directly_west(i,j).
directly_west(k,l).
directly_west(l,m).
directly_west(m,n).
directly_west(n,o).
directly_west(p,q).
directly_west(q,r).
directly_west(r,s).
directly_west(s,t).

directly_east(X,Y) :- directly_west(Y,X).
directly_south(X,Y) :- directly_north(Y,X).

north(X,Y) :- directly_north(X,Y).
north(X,Y) :- directly_north(Z,Y), north(X,Z).
east(X,Y) :- directly_east(X,Y).
east(X,Y) :- directly_east(Z,Y), east(X,Z).
south(X,Y) :- north(Y,X).
west(X,Y) :- east(Y,X).

north_west(X,Y) :- north(Z,Y), west(X,Z).
north_east(X,Y) :- north(Z,Y), east(X,Z).
south_east(X,Y) :- south(Z,Y), east(X,Z). % could also say north(Y,X), same applies to sw.
south_west(X,Y) :- south(Z,Y), west(X,Z).
