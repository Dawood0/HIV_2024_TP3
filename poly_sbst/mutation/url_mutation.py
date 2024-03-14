
from poly_sbst.mutation.abstract_mutation import AbstractMutation
from poly_sbst.generators.url_suite_generator import UrlTestSuiteGenerator 
import random



class UrlTestSuiteMutation(AbstractMutation):
    
    def __init__(self, mut_rate: float = 0.1, generator= UrlTestSuiteGenerator):
        super().__init__(generator)
        self.mut_rate = mut_rate
        self.generator = generator
        self.mutators = [self._delete_random_character, self._insert_random_symbol,self._replace_random_character]

    def _do_mutation(self, x):
        x=list(x)
        # mutate the test 
        
        for i in range(len(x)):
            mutator = random.choice(self.mutators)
            if random.random() <= self.mut_rate:
                x[i] = mutator(x[i])
        return x
        

    def _delete_random_character(self, s):
        """Returns s with a random character deleted"""
        try:
            url=s.split('.')
            bodyofurl=url[1]
            if len(bodyofurl) > 3:
                pos = random.randint(0, len(bodyofurl) - 1)
                url[1]=bodyofurl[:pos] + bodyofurl[pos + 1 :]
                return '.'.join(url)
            else:
                return s
        except:
            return s

    def _insert_random_symbol(self, s):
        """Returns s with a random symbol inserted"""
        try:
            url=s.split('.')
            bodyofurl=url[1]
            pos = random.randint(3, len(bodyofurl))
            random_character = chr(random.randrange(32, 127))
            url[1]=bodyofurl[:pos] + random_character + bodyofurl[pos+1:]
            return '.'.join(url)
        except:
            return s
        
    def _replace_random_character(self, s):
        """Returns s with a random character replaced"""
        try:
            if s == "":
                return ""
            pos = random.randint(0, len(s) - 1)
            random_character = chr(random.randrange(32, 127))
            return s[:pos] + random_character + s[pos + 1 :]
        except:
            return s
