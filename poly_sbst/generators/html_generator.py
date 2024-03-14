
from poly_sbst.generators.abstract_generator import AbstractGenerator
from poly_sbst.common.abstract_grammar import AbstractGrammar
import random
import numpy as np
from poly_sbst.generators.create_html import generate_html

class HTMLGenerator(AbstractGenerator):

    """RandomGenerator is a generator that generates random strings."""

    def __init__(self) -> None:
        super().__init__()
        self._name = "HTMLGenerator"
        self.min_length = 2
        self.max_length = 40

    @property
    def name(self) -> int:
        return self._name

    def cmp_func(self, x:np.ndarray, y:np.ndarray) -> float:
        return 0.0


    def generate_random_test(self) -> str:
        return self.generate_random_string(
            random.randint(self.min_length, self.max_length)
        )
    
    def generate_random_string(self, length) -> str:
        """Generate a random html of specified length."""
        
        return  generate_html()
        
