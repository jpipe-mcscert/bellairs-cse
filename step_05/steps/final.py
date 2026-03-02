######
## Justification deployable
######

from typing import Any, Callable
from jpipe_runner.framework.decorators.jpipe_decorator import jpipe

# jpipe-runner --library steps/final.py --diagram final --format svg final.json


# git checkout -b step_05
# touch modified_file.py
# git add modified_file.py 
# git commit -m "modified file added"  
# git push

# Cleanup
# git checkout main
# git push -d origin step_05
# git branch -D step_05

mock = {
    'accuracy':     0.82,
    'model_file':   'https://huggingface.co/boltuix/bert-emotion',
    'test_dataset': 'tests.csv',
    'counterfacts': 'counterfacts.csv'
}


@jpipe()
def all_conditions_are_met():
    return True

######################
#### Performance #####
######################

## Conclusion c
@jpipe(consume=["a"])
def my_model_is_performant(produce: Callable[[str, Any], None]) -> bool:
    # nothing more to do than reaching this stage
    return True

@jpipe(consume=["model", "d"], produce=["a"])
def accuracy_is_greater_than_80(model: bool, d: bool,
                                produce: Callable[[str, Any], None]) -> bool:
    # load the model; load the tests; measure accuracy
    if model and d and mock['accuracy'] > 0.80:
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

#####################
#### Convergence ####
#####################

## Strategy check_convergence
@jpipe(consume=["logs", "model"])
def assessing_logs_to_measure_convergence(logs: bool, model: bool) -> bool:
    return logs and model

## Evidence e2_conv
@jpipe(produce=["logs"])
def intermediate_logs_are_available(produce: Callable[[str, Any], None]) -> bool:
    produce('logs', True)
    return True

## Evidence e1_conv
@jpipe(produce=["model"])
def trained_model_is_available(produce: Callable[[str, Any], None]) -> bool:
    produce('model', True)
    return True


