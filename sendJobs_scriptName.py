# import modules
import numpy
import subprocess
import time

# load matlab module
loadMatlabString = 'module load math/MATLAB/2018b'
subprocess.call(loadMatlabString,shell=True)

# script input parameters
myJob = 'jobName'
myScript = 'scriptName'

# simulation parameters
chiS = 6 # system bond dimension

# range of environment bond dimension
environmentBondDim = range(20,55,5)

# loop over environment bond dimensions and start jobs
for chiE in environmentBondDim:

	# make data file for job submission
	myOutput = 'folderForLogFiles/nameForLogFile' + '.out'
	data = {'myJob': myJob, 'myOutput': myOutput, 'script' : scriptName, 'varA' : chiS, 'varB' : chiE}

	# open template and submit batch
	template = open("sbatchTemplate_scriptName", "rt").read()
	with open("sbatchLauncher", "wt") as output:
		output.write(template.format(**data))

	# send batch jobs to queue
	subprocess.call("sbatch sbatchLauncher",shell=True)

# delete temporary files
subprocess.call("rm sbatchLauncher",shell=True)