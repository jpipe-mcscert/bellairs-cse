######
## Justification deployable
######

from typing import Any, Callable
from jpipe_runner.framework.decorators.jpipe_decorator import jpipe

# jpipe-runner --library steps/deployable.py --diagram deployable --format svg deployable.json

mock = {
    'accuracy':     0.82,
    'model_file':   'https://huggingface.co/boltuix/bert-emotion',
    'test_dataset': 'tests.csv',
    'counterfacts': 'counterfacts.csv'
}

#################
#### Shared #####
#################

## Evidence e1
@jpipe(produce=["model"])
def model_is_available(produce: Callable[[str, Any], None]) -> bool:
    # Check that the model file exists and can be loaded
    if 'model_file' in mock:
        produce('model', True)
        return True
    return False

######################
#### Performance #####
######################

## Conclusion c
@jpipe(consume=["a"])
def my_model_is_performant(produce: Callable[[str, Any], None]) -> bool:
    # nothing more to do than reaching this stage
    return True

## Strategy s
@jpipe(consume=["model", "d"], produce=["a"])
def accuracy_is_greater_than_85(model: bool, d: bool,
                                produce: Callable[[str, Any], None]) -> bool:
    # load the model; load the tests; measure accuracy
    if model and d and mock['accuracy'] > 0.85:
        produce("a", mock['accuracy'])
        return True
    return False

@jpipe(produce=["d"])
def test_dataset_is_available(produce: Callable[[str, Any], None]) -> bool:
    # Check that the dataset exists on the disk
    if 'test_dataset' in mock:
        produce('d', True)
        return True
    return False

###################
#### Fairness #####
###################

@jpipe(consume=["x"])
def my_model_is_fair(produce: Callable[[str, Any], None]) -> bool:
    # nothing more to do than reaching this stage
    return True
   
@jpipe(consume=["counterfactual", "model"], produce=["x"])
def assess_counterfactual_fairness(counterfactual: str, model: str,
                                   produce: Callable[[str, Any], None]) -> bool:
    produce('x', True)
    return counterfactual and model


@jpipe(produce=["counterfactual"])
def counterfactual_dataset_is_available(produce: Callable[[str, Any], None]) -> bool:
    if mock['counterfacts']:
        produce("counterfactual", True)
        return True
    return False







