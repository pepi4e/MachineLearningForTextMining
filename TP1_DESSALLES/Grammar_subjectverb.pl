/*---------------------------------------------------------------*/
/* Telecom Paristech - J-L. Dessalles 2018                       */
/* Symbolic Natural Language Processing                 */
/*            http://teaching.dessalles.fr/SNLP                   */
/*---------------------------------------------------------------*/


% --- Productions rules

np(Number) --> det(Number), n(Number), v(Number).

sv(Number) --> det(Number), n(Number), v(Number).

% -- Lexicon

det(singular) --> [a].
det(plural) --> [many].
det(_) --> [the].        % '_' matches anything 

n(singular) --> [dog].
n(plural) --> [dogs].

v(singular) --> [loves].
v(plural) --> [love].
