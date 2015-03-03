import numpy as np
import pylab as pp
import scipy as sp
from scipy import stats as spstats
from abc_sgld.code.blowfly_problem.blowfly_wrapper import *

def view_theta_hist( problem, theta_range, samples, algoname, burnin ):
  figsize = (10,12)
  alpha=0.75
  pp.rc('text', usetex=True)
  pp.rc('font', family='times')
  f = pp.figure( figsize=figsize )
  sp=pp.subplot(1,1,1)
      
  #theta0=theta_range[0]
  #thetaN=theta_range[-1]
  theta_names = [r'\text{log} $P$', r'\text{log} ${\delta}$', r'\text{log} ${N_0}$', r'\text{log} ${\sigma_d}$', r'\text{log} ${\sigma_p}$', r'$\tau$']
  #pp.hist( samples, problem.p.nbins_coarse, range=problem.p.range,normed = True, alpha = alpha )
  for i in range(6):
    sp=pp.subplot(3,2,i+1)
    pp.hist( samples[burnin:,i], 20, normed=True, alpha=0.75)
    #pp.plot( samples[-howmany:,i], 'ko')
    pp.xlabel( theta_names[i], rotation='horizontal')
    # set_tick_fonsize( sp, 16 )
    # set_title_fonsize( sp, 32 )
    # set_label_fonsize( sp, 24 )
  
  #pp.ylim(theta0,thetaN)
  #pp.xlabel( "theta")
  #pp.ylabel( "x")
  
  #pp.xlabel( r'time' )
  #pp.ylabel( r'${\bm \theta}$', rotation='horizontal' )
  
  pp.legend( [algoname], loc=0,fancybox=True,prop={'size':32} )
  
def view_theta_hist_short( problem, theta_range, samples, algoname, burnin, ids, color, note = "" ):
  figsize = (10,4)
  alpha=0.75
  pp.rc('text', usetex=True)
  pp.rc('font', family='times')
  f = pp.figure( figsize=figsize )
  sp=pp.subplot(1,1,1)
      
  #theta0=theta_range[0]
  #thetaN=theta_range[-1]
  theta_names = [r'\text{log} $P$', r'\text{log} ${\delta}$', r'\text{log} ${N_0}$', r'\text{log} ${\sigma_d}$', r'\text{log} ${\sigma_p}$', r'$\tau$']
  #pp.hist( samples, problem.p.nbins_coarse, range=problem.p.range,normed = True, alpha = alpha )
  for i in range(len(ids)):
    idx = ids[i]
    rg = theta_range[i]
    sp=pp.subplot(1,len(ids),i+1)
    
    bins = np.linspace( rg[0], rg[1], 30 )
    pp.hist( samples[burnin:,idx], bins, normed=True, alpha=0.75,color=c)
    #pp.plot( samples[-howmany:,i], 'ko')
    pp.xlabel( theta_names[idx], rotation='horizontal')
    
    if i == 0:
      pp.ylabel( r'$p( {\bm \theta} | {\bf y} )$  '+note , rotation='vertical' )
    pp.xlim( rg[0],rg[1])
    set_tick_fonsize( sp, 16 )
    set_title_fonsize( sp, 32 )
    set_label_fonsize( sp, 32 )
  
  #pp.ylim(theta0,thetaN)
  #pp.xlabel( "theta")
  #pp.ylabel( "x")
  
  #pp.xlabel( r'time' )
  #pp.ylabel( r'${\bm \theta}$', rotation='horizontal' )
  
  pp.legend( [algoname], loc=0,fancybox=True,prop={'size':32} )
      
def view_theta_timeseries( problem, theta_range, samples, algoname, howmany = 1000 ):
  figsize = (16,6)
  alpha=0.75
  pp.rc('text', usetex=True)
  pp.rc('font', family='times')
  f = pp.figure( figsize=figsize )
  sp=pp.subplot(1,1,1)
      
  #theta0=theta_range[0]
  #thetaN=theta_range[-1]
  theta_names = [r'\text{log} $P$', r'\text{log} ${\delta}$', r'\text{log} ${N_0}$', r'\text{log} ${\sigma_d}$', r'\text{log} ${\sigma_p}$', r'$\tau$']
  #pp.hist( samples, problem.p.nbins_coarse, range=problem.p.range,normed = True, alpha = alpha )
  for i in range(6):
    sp=pp.subplot(3,2,i+1)
    pp.plot( samples[-howmany:,i], 'k-', lw=2, alpha=0.5)
    pp.plot( samples[-howmany:,i], 'ko')
    pp.ylabel( theta_names[i], rotation='vertical')
    # set_tick_fonsize( sp, 16 )
    # set_title_fonsize( sp, 32 )
    # set_label_fonsize( sp, 24 )
  
  #pp.ylim(theta0,thetaN)
  #pp.xlabel( "theta")
  #pp.ylabel( "x")
  
  #pp.xlabel( r'time' )
  pp.ylabel( r'$p( {\bm \theta} | {\bf y}$', rotation='horizontal' )
  
  pp.legend( [algoname], loc=0,fancybox=True,prop={'size':32} )
  
    
  #pp.title( r"Simulation with Common Random Numbers", fontsize=22) 
  set_tick_fonsize( sp, 16 )
  set_title_fonsize( sp, 32 )
  set_label_fonsize( sp, 32 )

names = ["SL-MCMC", "SG-Langevin", "SG-Thermo"]
sticky_files = []
#sticky_files.append( "bf-sticky-SL-MCMC-theta-chain0.npy" )
#sticky_files.append( "bf-sticky-SG-Langevin-theta-chain0.npy" )
sticky_files.append( "bf-sticky5-SG-Thermostats-theta-chain0.npy" )

non_sticky_files = []
#non_sticky_files.append( "bf-no-sticky-SL-MCMC-theta-chain0.npy" )
#non_sticky_files.append( "bf-no-sticky-SG-Langevin-theta-chain0.npy" )
#non_sticky_files.append( "bf-no-sticky-SG-Thermostats-theta-chain0.npy" )

if __name__ == "__main__":
  pp.close('all')
  burnin=10000
  theta_range = [[-3,7],[-3,3],[4,9]]
  
  problem = generate_blowfly( bf_problem )
  colors = ["b","g","r"]
  # for f,algoname,c in zip( non_sticky_files, names,colors ):
  #   theta = np.load( f )
  #   view_theta_hist_short( problem, theta_range, theta, algoname, burnin, ids = [0,1,2], color = c )
  #   pp.savefig("../images/blowfly/non-sticky-theta-hist-%s.pdf"%(algoname),bbox_inches='tight')
  for f,algoname,c in zip( sticky_files, names,colors ):
    theta = np.load( f )
    view_theta_hist_short( problem, theta_range, theta, algoname, burnin, ids = [0,1,2], color = c, note=r"persistent {\bm \omega}" )
    pp.savefig("../images/blowfly/sticky-theta-hist-%s.pdf"%(algoname),bbox_inches='tight')
  pp.show()