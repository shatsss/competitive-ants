from mains.heuristic.runner import heuristic_runner
from players.HeuristicFunctions.FCC.FccRAhead import FccRAhead

# runs FccRAhead algorithm
if __name__ == "__main__":
    heuristic_runner(FccRAhead(id=2), "FCC")
