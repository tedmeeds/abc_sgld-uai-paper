import numpy as np
import pylab as pp
import scipy as sp
import cPickle

def extract_from_pkl( pkl_file, algo_key, save_name ):
  print "loading %s"%(pkl_file)
  r = cPickle.load( open( pkl_file ))
  
  nbr_chains = len(r[algo_key]["results"])
  
  np.savetxt("%s-%s-mean-errors.txt"%(save_name, algo_key), r[algo_key]['mean_errors'])
  for chain_id in range(nbr_chains):
    theta = r[algo_key]["results"][chain_id]["THETA"]
    
    np.save( "%s-%s-theta-chain%d.npy"%(save_name, algo_key,chain_id), theta )
    
    print save_name, algo_key, chain_id, theta.shape
  

results_dir = "../../abc_sgld/code/exponential_problem/images/"
results_dir2 = "../../abc_sgld_blowfly/"

algonames = ["SL-ABC", "SGLD", "SGHMC", "SGNHT"]

SGLD_no_sticky   = "bf-no-sticky-SG-Langevin-results.pkl"
SGLD_sticky   = "bf-sticky-SG-Langevin-results.pkl"

SGNHT_no_sticky  = "bf-no-sticky-SG-Thermostats-results.pkl"
SGNHT_sticky2  = "bf-sticky2-SG-Thermostats-results.pkl"
SGNHT_no_sticky2 = "bf-no-sticky2-SG-Thermostats-results.pkl"
SGNHT_sticky5  = "bf-sticky5-SG-Thermostats-results.pkl"

SLMCMC_no_sticky = "bf-no-sticky-SL-MCMC-results.pkl"
SLMCMC_sticky = "bf-sticky-SL-MCMC-results.pkl"

times = np.loadtxt( results_dir+"exp-SL-MCMC-tvd-times-omega-rate-0p01.txt" )

if __name__ == "__main__":
  
  
  #r = extract_from_pkl( results_dir2 + SLMCMC_no_sticky, "SL-MCMC", "bf-no-sticky" )
  #r = extract_from_pkl( results_dir2 + SLMCMC_sticky, "SL-MCMC", "bf-sticky" )
  #r = extract_from_pkl( results_dir2 + SGNHT_no_sticky, "SG-Thermostats", "bf-no-sticky" )
  #r = extract_from_pkl( results_dir2 + SGNHT_no_sticky2, "SG-Thermostats", "bf-no-sticky2" )
  #r = extract_from_pkl( results_dir2 + SGNHT_sticky2, "SG-Thermostats", "bf-sticky" )
  
  #r = extract_from_pkl( results_dir2 + SGLD_sticky, "SG-Langevin", "bf-sticky" )
  #r = extract_from_pkl( results_dir2 + SGLD_no_sticky, "SG-Langevin", "bf-no-sticky" )
  r = extract_from_pkl( results_dir2 + SGNHT_sticky5, "SG-Thermostats", "bf-sticky5" )