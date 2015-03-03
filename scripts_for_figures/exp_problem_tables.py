import numpy as np
import pylab as pp
import scipy as sp

results_dir = "../../abc_sgld/code/exponential_problem/images/"
results_dir2 = "../../abc_sgld_exponential/"

algonames = ["SL-ABC", "SGLD", "SGHMC", "SGNHT"]

times = np.loadtxt( results_dir+"exp-SL-MCMC-tvd-times-omega-rate-0p01.txt" )
times = times.astype(int)
sticky_files = []
sticky_files.append( results_dir2+"exp2-SL-MCMC-tvd-omega-rate-0p1.txt" )
sticky_files.append( results_dir2+"exp2-SG-Langevin-tvd-omega-rate-0p1.txt" )
sticky_files.append( results_dir2+"exp2-SG-HMC-tvd-omega-rate-0p1.txt" )
sticky_files.append( results_dir2+"exp2-SG-Thermostats-tvd-omega-rate-0p1.txt" )


non_sticky_files = []
non_sticky_files.append( results_dir+"exp-SL-MCMC-tvd-omega-rate-100p0.txt" )
non_sticky_files.append( results_dir+"exp-SG-Langevin-tvd-omega-rate-100p0.txt" )
non_sticky_files.append( results_dir+"exp-SG-HMC-tvd-omega-rate-100p0.txt" )
non_sticky_files.append( results_dir+"exp-SG-Thermostats-tvd-omega-rate-100p0.txt" )

print times
time_ids = [4,8]

for algo, fn in zip( algonames, sticky_files ):
  tdv = np.loadtxt( fn )
  mn = tdv.mean(0)
  std = tdv.std(0)
  for idx in time_ids:
    print "%s at %08d has %3.4f tdv"%(algo,times[idx],mn[idx])
  #print mn

for algo, fn in zip( algonames, non_sticky_files ):
  tdv = np.loadtxt( fn )
  mn = tdv.mean(0)
  std = tdv.std(0)
  for idx in time_ids:
    print "%s at %08d has %3.4f tdv"%(algo,times[idx],mn[idx])

algonames = ["SL-ABC", "SGLD", "SGHMC", "SGNHT"]
files2use = []
files2use.append( results_dir+"exp-SL-MCMC-tvd-omega-rate-100p0.txt" )
files2use.append( results_dir+"exp-SG-Langevin-tvd-omega-rate-100p0.txt" )
files2use.append( results_dir+"exp-SG-HMC-tvd-omega-rate-100p0.txt" )
files2use.append( results_dir2+"exp3-SG-Thermostats-tvd-omega-rate-100p0.txt" )
files2use_sticky = []
files2use_sticky.append( results_dir2+"exp2-SL-MCMC-tvd-omega-rate-0p1.txt" )
files2use_sticky.append( results_dir2+"exp2-SG-Langevin-tvd-omega-rate-0p1.txt" )
files2use_sticky.append( results_dir2+"exp2-SG-HMC-tvd-omega-rate-0p1.txt" )
files2use_sticky.append( results_dir2+"exp2-SG-Thermostats-tvd-omega-rate-0p1.txt" )
#files2use.append( results_dir2+"exp2-SG-Thermostats-tvd-omega-rate-0p1.txt" )
# table_str = "Algo "
# for idx in time_ids:
#   table_str += "& $%d$ "%(times[idx])
# table_str += "\\\\\n"
#
# for algo, fn in zip( algonames, files2use ):
#   tdv = np.loadtxt( fn )
#   mn = tdv.mean(0)
#   std = tdv.std(0)
#
#   table_str += "%s "%(algo)
#   for idx in time_ids:
#     print "%s at %08d has %3.4f tdv"%(algo,times[idx],mn[idx])
#
#     table_str += "& $%2.3f$ "%(mn[idx])
#   table_str += "\\\\\n"
#
# print table_str

table_str = " & \multicolum{2}{Non-sticky} & \multicolum{2}{Non-sticky} \\\\\n"
table_str += "Algo "
for idx in time_ids:
  table_str += "& $%d$ "%(times[idx])
for idx in time_ids:
  table_str += "& $%d$ "%(times[idx])
table_str += "\\\\\n"
  
for algo, fn, fn2 in zip( algonames, files2use, files2use_sticky ):
  tdv = np.loadtxt( fn )
  mn = tdv.mean(0)
  std = tdv.std(0)
  tdv = np.loadtxt( fn2 )
  mn2 = tdv.mean(0)
  std2 = tdv.std(0)
  
  table_str += "%s "%(algo)
  for idx in time_ids:
    print "%s at %08d has %3.4f tdv"%(algo,times[idx],mn[idx])
    
    table_str += "& $%2.3f$ "%(mn[idx])
  for idx in time_ids:
    print "%s at %08d has %3.4f tdv"%(algo,times[idx],mn2[idx])
    
    table_str += "& $%2.3f$ "%(mn2[idx])
  table_str += "\\\\\n"

print table_str