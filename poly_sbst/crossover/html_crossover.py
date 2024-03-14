from poly_sbst.crossover.abstract_crossover import AbstractCrossover
import numpy as np
import random


class HTMLTestSuiteCrossover(AbstractCrossover):
    def __init__(self, cross_rate: float = 0.9):
        super().__init__(cross_rate)


    def _do_crossover(self, problem, a, b) -> tuple:
        # crossover the test suite
        # cut both parents in half and combine them
        x=[]
        y=[]
        for i in range(min(len(a), len(b))):
            if random.random() < self.cross_rate:
                string1 = random.choice(a)
                string2 = random.choice(b)
                
                # Calculate half length of strings
                half_len1 = len(string1) // 2
                half_len2 = len(string2) // 2
                
                # Perform crossover by mixing the halves of the strings
                x.append(string1[:half_len1] + string2[half_len2:])
                y.append(string2[:half_len2] + string1[half_len1:])

                return np.array(x), np.array(y)
            else:
                return a,b


        # parent1=a
        # parent2=b
        # parent1half1=parent1[:len(parent1)//2]
        # parent1half2=parent1[len(parent1)//2:]
        # parent2half1 = parent2[:len(parent2)//2]
        # parent2half2 = parent2[len(parent2)//2:]
        # child1 = np.array(list(parent1half1) + list(parent2half2))
        # child2 = np.array(list(parent2half1) + list(parent1half2))
        
        # return child1 , child2
    

