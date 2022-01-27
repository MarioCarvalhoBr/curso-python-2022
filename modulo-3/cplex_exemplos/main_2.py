# pip install cplex
# Código base: 
# https://gist.github.com/WPettersson/287de1e739d4d7869d555fd28ac587cf
#/usr/bin/env python3

import cplex

# Create an instance of a linear problem to solve
problem = cplex.Cplex()


# We want to find a maximum of our objective function
problem.objective.set_sense(problem.objective.sense.maximize)

# The names of our variables
names = ["x", "y"]

# A função objetiva. Mais precisamente, os coeficientes da função objetivo 
# Observe que estamos lançando para floats.
objective = [3.0, 2.0]

# Limites inferiores. 
# Como todos são zero, simplesmente não podemos passá-los, pois todos os zeros é o padrão.
lower_bounds = [0.0, 0.0]

# Limites superiores. O padrão aqui seria cplex.infinity, ou 1e+20.
upper_bounds = [cplex.infinity, cplex.infinity]

# Adicionou ao problema as variáveis
problem.variables.add(obj = objective,
                      lb = lower_bounds,
                      ub = upper_bounds,
                      names = names)

# Restrições

# As restrições são inseridas em duas partes, como uma parte esquerda e uma parte direita
# papel. Na maioria das vezes, elas serão representadas como matrizes em seu problema. Dentro
# nosso caso, temos "3x + 3y ≤ 300", "6x + 3y  ≤ 480" e "3x + 3y  ≤ 480" que podemos
# escreva como matrizes da seguinte forma:


# Primeiro, nomeamos as restrições
constraint_names = ["c1", "c2", "c3"]

# As restrições reais agora são adicionadas. Cada restrição é na verdade uma lista
# consistindo em dois objetos, cada um dos quais são listas. A primeira lista
# representa cada uma das variáveis na restrição e a segunda lista é a
# coeficiente da respectiva variável. Os dados são inseridos desta forma como o
# matriz de restrições geralmente é esparsa.

# A primeira restrição é inserida referindo-se a cada variável por seu nome
# (que definimos anteriormente). Isso então representa "3x + y - z"

first_constraint = [["x", "y"], [3.0, 3.0]]
# Nesta segunda restrição, nos referimos às variáveis por seus índices. Desde a
# "x" foi a primeira variável que adicionamos, "y" a segunda e "z" a terceira, isso
# então representa 3x + 4y + 4z
second_constraint = [[0, 1], [6.0, 3.0]]

terceira_constraint = [[0, 1], [3.0, 3.0]]
constraints = [ first_constraint, second_constraint, terceira_constraint ]

# Até agora não adicionamos um lado direito, então fazemos isso agora. Observe que o
# a primeira entrada nesta lista corresponde à primeira restrição e assim por diante.
rhs = [300, 480, 480]

# Precisamos entrar nos sentidos das restrições. Ou seja, precisamos dizer ao Cplex
# se cada restrição deve ser tratada como um limite superior (≤, denotado por "L"
# para menor que), um limite inferior (≥, denotado "G" para maior que) ou uma igualdade
# (=, denotado "E" para igualdade)
constraint_senses = [ "L", "L", "L"]

# Observe que podemos definir os sentidos como uma string. Ou seja, também poderíamos usar
# constraint_senses = "LL"
# para passar nossas restrições

# E adicione as restrições
problem.linear_constraints.add(lin_expr = constraints,
                               senses = constraint_senses,
                               rhs = rhs,
                               names = constraint_names)

# Resolva o problema
problem.solve()

# Funcao objetivo
lista_resultados = problem.solution.get_values()

# And print the solutions
x = lista_resultados[0]
y = lista_resultados[1]
print(f"{x}x {y}y")

print("Objective value: ", problem.solution.get_objective_value())
