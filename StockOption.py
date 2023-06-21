import math

class StockOption(object):
    def __init__(self, S0, K, r, T, N, params):
        """
        Initialize the stock option base class.
        Defaults to European call unless specified.

        :param S0: initial stock price
        :param K: strike price
        :param r: risk-free interest rate
        :param T: time to maturity
        :param N: number of time steps
        :param pu: probability at up state
        :param pd: probability at down state
        :param div: Dividend yield
        :param is_put: True for a put option,
                False for a call option
        :param is_am: True for an American option,
                False for a European option
        """
        self.S0 = S0
        self.K = K
        self.r = r
        self.T = T
        self.N = max(1, N) # Ensure N have at least 1 time step
        self.STs = None  # Declare the stock prices tree

        self.pu = params.get("pu", 0)  # Probability of up state
        self.pd = params.get("pd", 0)  # Probability of down state


        self.div = params.get("div", 0)  # Dividend yield
        self.sigma = params.get("sigma", 0)  # Volatility
        self.is_call = params.get("is_call", True)  # Call or put
        self.is_european = params.get("is_eu", True)  # Eu or Am
        self.dt = T/float(N)  # Single time step, in years
        self.df = math.exp(-(r-self.div) * self.dt)  # Discount factor