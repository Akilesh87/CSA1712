pos(door).
pos(window).
pos(middle).

% grasp banana: monkey on box, box in the middle
move(state(middle, onbox, middle, hasnot), grasp,
     state(middle, onbox, middle, has)).

% climb on box: monkey and box at same place
move(state(P, onfloor, P, H), climb,
     state(P, onbox, P, H)).

% push box from P1 to P2
move(state(P1, onfloor, P1, H), push(P1, P2),
     state(P2, onfloor, P2, H)) :- pos(P2), P1 \= P2.

% walk from P1 to P2
move(state(P1, onfloor, B, H), walk(P1, P2),
     state(P2, onfloor, B, H)) :- pos(P2), P1 \= P2.

% goal: monkey has banana
plan(state(_, _, _, has), []).
plan(S1, [Action|Rest]) :-
    move(S1, Action, S2),
    plan(S2, Rest).

% iterative deepening so the shortest plan is found
solve(Plan) :-
    length(Plan, _),
    plan(state(door, onfloor, window, hasnot), Plan), !.