
from poly_sbst.generators.abstract_generator import AbstractGenerator
from poly_sbst.common.abstract_grammar import AbstractGrammar
from poly_sbst.generators.url_generator import UrlGenerator
import random
import numpy as np



class UrlTestSuiteGenerator(AbstractGenerator):

    def __init__(self):
        super().__init__()
        self._name = "UrlGenerator"
        self.test_gen = UrlGenerator()
        self.max_length = 40
        self.min_length = 2


    def cmp_func(self, x:np.ndarray, y:np.ndarray) -> float:
        return 0.0

    # generates random test for the urltest module  
    def generate_random_test(self, n=1):
        '''define the grammer for the url'''
        
        samples=[]
        
        n = random.randint(self.min_length, self.max_length)
        for i in range(n):
            samples.append(self.test_gen.generate_random_test())

        return np.array(samples)

