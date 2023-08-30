% Facts: animal and their diets
eats(tiger, meat).
eats(lion, meat).
eats(cat, meat).
eats(deer, plants).

% Rule: An animal is a carnivore if it eats meat.
carnivore(X) :-
    eats(X, meat).

% Rule: An animal is not a carnivore if it doesn't eat meat.
not_carnivore(X) :-
    \+ carnivore(X).
