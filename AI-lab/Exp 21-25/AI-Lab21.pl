move(0, _, _, _) :- !.
move(N, Source, Target, Aux) :-
    M is N - 1,
    move(M, Source, Aux, Target),
    format('Move disk ~w from ~w to ~w~n', [N, Source, Target]),
    move(M, Aux, Target, Source).