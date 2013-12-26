from pyevolve import Util
from pyevolve import GTree
from pyevolve import GSimpleGA
from pyevolve import Consts
import math

rmse_accum = Util.ErrorAccumulator()

def gp_add(a, b): return a+b
def gp_sub(a, b): return a-b
def gp_mul(a, b): return a*b
def gp_sqrt(a):   return math.sqrt(abs(a))

def eval_func(chromosome):
    global rmse_accum
    rmse_accum.reset()
    code_comp = chromosome.getCompiledCode()
    a = 0
    while a <= 2 * math.pi:
        evaluated     = eval(code_comp)
        target        = math.sin(a)
        rmse_accum   += (target, evaluated)
        a += 0.1

    return rmse_accum.getRMSE()

def main_run():
   genome = GTree.GTreeGP()
   genome.setParams(max_depth=4, method="ramped")
   genome.evaluator += eval_func

   ga = GSimpleGA.GSimpleGA(genome)
   ga.setParams(gp_terminals = ['a', '0.5', '0.1', '1', '2', '3', '4', '5', '6'],
                gp_function_prefix = "gp")

   ga.setMinimax(Consts.minimaxType["minimize"])
   ga.setGenerations(50)
   ga.setCrossoverRate(0.5)
   ga.setMutationRate(0.15)
   ga.setPopulationSize(800)

   ga(freq_stats=10)
   best = ga.bestIndividual()
   print best

if __name__ == "__main__":
   main_run()
