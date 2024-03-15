


from datetime import datetime
from poly_sbst.common.random_seed import get_random_seed
from poly_sbst.common.abstract_executor import AbstractExecutor
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.algorithms.soo.nonconvex.random_search import RandomSearch
from poly_sbst.sampling.abstract_sampling import AbstractSampling
from poly_sbst.crossover.random_crossover import OnePointCrossover
from poly_sbst.problems.test_suite_problem import TestSuiteProblem
from poly_sbst.generators.test_suite_generator import TestSuiteGenerator
from poly_sbst.mutation.test_suite_mutation import TestSuiteMutation
from pymoo.optimize import minimize
from urllib.parse import urlparse
from html.parser import HTMLParser


from pymoo.operators.selection.rnd import RandomSelection
from poly_sbst.generators.url_suite_generator import UrlTestSuiteGenerator
from poly_sbst.problems.url_problem import UrlTestSuiteProblem
from poly_sbst.crossover.url_crossover import UrlTestSuiteCrossover
from poly_sbst.mutation.url_mutation import UrlTestSuiteMutation
from pymoo.algorithms.soo.nonconvex.random_search import RandomSearch
import numpy as np


def optimize(runs=5):

    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y")

    for run in range(runs):

        seed = get_random_seed()
        pop_size = 20
        num_gen = 5


        # generator = TestSuiteGenerator() 
        generator = UrlTestSuiteGenerator() 


        executor = AbstractExecutor(urlparse) 
        
        problem = UrlTestSuiteProblem(executor) 
        
        method = GA(pop_size=pop_size,
                n_offsprings=int(pop_size/2),
                sampling=AbstractSampling(generator),
                mutation=UrlTestSuiteMutation(generator=generator),
                crossover=UrlTestSuiteCrossover(cross_rate=0.9),
                eliminate_duplicates=False,
                # selection=RandomSelection()
                )
        # method=RandomSearch()
        res = minimize(problem,
                method,
                termination=('n_gen', num_gen),
                seed=seed,
                verbose=True,
                eliminate_duplicates=False,
                save_history=True
                )
        
        # print("Best solution found: %s" % res.X)
        print("Function value: %s" % res.F)
        # print("Execution data:", res.problem.execution_data)


if __name__ == "__main__":
    optimize()
    # print('            TournamentSelection        ')
        