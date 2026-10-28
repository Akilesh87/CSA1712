bird(sparrow).
bird(eagle).
bird(parrot).
bird(crow).
bird(penguin).
bird(ostrich).

cannot_fly(penguin).
cannot_fly(ostrich).

can_fly(X) :- bird(X), \+ cannot_fly(X).

check(X) :- can_fly(X), !, format('~w can fly.~n', [X]).
check(X) :- bird(X), !, format('~w cannot fly.~n', [X]).
check(X) :- format('~w is not a known bird.~n', [X]).