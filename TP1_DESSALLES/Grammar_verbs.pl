/*---------------------------------------------------------------*/
/* Telecom Paristech - J-L. Dessalles 2018                       */
/* Symbolic Natural Language Processing                 */
/*            http://teaching.dessalles.fr/SNLP                   */
/*---------------------------------------------------------------*/

vaf(Argument) --> v(Argument).

v(none) --> [sleeps].
v(transitive | intransitive) --> [gives].
v(_) --> [eats].

