from pyevolve import Util
from pyevolve import GTree
from pyevolve import GSimpleGA
from pyevolve import Consts
from pyevolve import Selectors
import math

rmse_accum = Util.ErrorAccumulator()

def gp_add2(a, b): return a+b
def gp_add3(a, b, c): return a+b+c
# def gp_add4(a, b, c, d): return a+b+c+d
def gp_sub(a, b): return a-b
def gp_mul(a, b): return a*b
def gp_sqrt(a):   return math.sqrt(abs(a))

def eval_func(chromosome):
    global rmse_accum
    rmse_accum.reset()
    code_comp = chromosome.getCompiledCode()
    a = 0
    pi = math.pi
    xs = [math.pi * i / 8.0 for i in xrange(0,9)]
    for a in xs:
        evaluated     = eval(code_comp)
        target        = math.sin(a)
        rmse_accum   += (target, evaluated)

    return rmse_accum.getRMSE()

def main_run():
    genome = GTree.GTreeGP()
    genome.setParams(max_depth=10, method="ramped")
    genome.evaluator += eval_func

    ga = GSimpleGA.GSimpleGA(genome)
    # ga.selector.set(Selectors.GTournamentSelector)
    terminals = ['a', '0.1', '0.5', '1', '2', str(math.pi)] #, '1', '2', str(math.pi)]

    ga.setParams(gp_terminals = terminals,
                 gp_function_prefix = "gp")

    ga.setMinimax(Consts.minimaxType["minimize"])
    ga.setGenerations(500)
    ga.setCrossoverRate(1.0)
    ga.setMutationRate(0.1)
    ga.setPopulationSize(200)

    ga(freq_stats=100)
    best = ga.bestIndividual()
    print best

if __name__ == "__main__":
    main_run()
