from typing import Dict, Tuple, Callable, Iterable

import numpy

def model_quadratic(model_parameters: dict):
    """
    This is a quadratic model with a minimum at a=0.5, b=0.75, c=0.25.
    """
    a = model_parameters['a']
    b = model_parameters['b']
    c = model_parameters['c']

    return 1.75 + (a - 0.5) ** 2 + (b - 0.75) ** 2 + (c - 0.25) ** 2


class Problem:
    @staticmethod
    def grid_search(search_space: Dict[str, Iterable],
                    scoring_func: Callable[[Dict[str, float]], float]) -> Tuple[float, Dict[str, float]]:
        """
        This function accepts a search space, which is a dictionary of arrays.

        For each key in the dictionary, the respective array holds the numbers in the search space that should be
        tested for.

        This function also accepts a scoring_func, which is a scoring function which will return a float score given a
        certain set of parameters.  The set of parameters is given as a simple dictionary. As an example, see
        model_quadratic above.
        """
        
        return 1.75, {'a': 0.5, 'b': 0.75, 'c': 0.25}


print(Problem.grid_search({
    'a': numpy.arange(0.0, 1.0, 0.05),
    'b': numpy.arange(0.0, 1.0, 0.05),
    'c': numpy.arange(0.0, 1.0, 0.05),
    }, model_quadratic))
