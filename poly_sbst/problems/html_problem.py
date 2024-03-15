
from poly_sbst.common.abstract_executor import AbstractExecutor
from poly_sbst.problems.abstract_problem import AbstractProblem
import numpy as np

class HTMLTestSuiteProblem(AbstractProblem):

    def __init__(self, executor: AbstractExecutor, n_var: int=1, n_obj=1, n_ieq_constr=0, xl=None, xu=None):
        """Initialize the problem.
        """
        super().__init__(executor, n_var, n_obj, n_ieq_constr, xl, xu)
        self.executor = executor
        self._name = "HTMLTestSuiteProblem"
        self.previous_coverage = 0
        self.first_evaluation = True

    def _evaluate(self, x:np.ndarray, out, *args, **kwargs):
        # gettign a test and evaluating the fitness funciton based on its coverage over the number of tests 
        # i is the index of the test in the test suite 
        
        tests = x[0]
        self.executor._full_coverage = [] # reset the coverage evaluation
        self.executor._coverage = set()
        
        eval_metrics = []
        n_t = len(tests)
        for test in tests:
            exceptions, execution_time, coverage = self.executor._execute_input(test)
            n_l = len(coverage)
            eval_metrics.append(n_l/n_t)
            
            
        fitness = max(eval_metrics)
        with open('plt/rndhtml.txt', 'a') as f:
        # with open('plt/tnrnmthtml.txt', 'a') as f:
            f.write(str(fitness) + ' ')

        self.execution_data[self.n_evals] = {"input": test, "output": fitness, "execution_time": execution_time}

        self.n_evals += 1

        out["F"] = -fitness

