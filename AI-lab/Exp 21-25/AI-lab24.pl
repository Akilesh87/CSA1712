disease(diabetes).
disease(hypertension).
disease(obesity).
disease(anemia).
disease(heart_disease).

diet(diabetes,     'Low sugar, high fiber foods, whole grains, green vegetables. Avoid sweets and white rice.').
diet(hypertension, 'Low salt (DASH diet), fruits, vegetables, low-fat dairy. Avoid pickles and processed food.').
diet(obesity,      'Low calorie, high protein and fiber, plenty of water. Avoid fried food and sugary drinks.').
diet(anemia,       'Iron-rich foods like spinach, beetroot, dates, legumes, with vitamin C. Avoid tea right after meals.').
diet(heart_disease,'Low saturated fat, oats, nuts, fish, fruits and vegetables. Avoid red meat and trans fats.').

suggest :-
    write('Enter disease name (end with a full stop): '),
    read(D),
    suggest_diet(D).

suggest_diet(D) :-
    diet(D, Plan), !,
    format('Suggested diet for ~w: ~w~n', [D, Plan]).
suggest_diet(D) :-
    format('No diet information available for ~w. Please consult a doctor.~n', [D]).