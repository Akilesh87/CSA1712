male(john).   male(mike).   male(tom).   male(david).
female(mary). female(susan). female(anna). female(lisa).

parent(john, mike).
parent(mary, mike).
parent(john, susan).
parent(mary, susan).
parent(mike, tom).
parent(anna, tom).
parent(mike, lisa).
parent(anna, lisa).

father(F, C)  :- male(F), parent(F, C).
mother(M, C)  :- female(M), parent(M, C).
son(S, P)     :- male(S), parent(P, S).
daughter(D, P):- female(D), parent(P, D).
grandparent(G, C) :- parent(G, P), parent(P, C).
grandfather(G, C) :- male(G), grandparent(G, C).
grandmother(G, C) :- female(G), grandparent(G, C).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
brother(B, X) :- male(B), sibling(B, X).
sister(S, X)  :- female(S), sibling(S, X).
ancestor(A, D) :- parent(A, D).
ancestor(A, D) :- parent(A, X), ancestor(X, D).