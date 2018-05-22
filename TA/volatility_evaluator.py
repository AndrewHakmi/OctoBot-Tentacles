"""
CryptoBot Package

$package_description: {
    "name": "volatility_evaluator",
    "type": "TA",
    "version": "1.0.0",
    "requirements": []
}
"""

from evaluator.TA.TA_evaluator import VolatilityEvaluator


# average_true_range
class ATRVolatilityEvaluator(VolatilityEvaluator):
    def __init__(self):
        super().__init__()

    def eval_impl(self):
        pass


# mass index
class MassIndexVolatilityEvaluator(VolatilityEvaluator):
    def __init__(self):
        super().__init__()

    def eval_impl(self):
        pass


class ChaikinVolatilityEvaluator(VolatilityEvaluator):
    def __init__(self):
        super().__init__()

    def eval_impl(self):
        pass
