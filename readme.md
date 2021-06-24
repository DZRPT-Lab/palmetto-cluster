# Palmetto Cluster

## Getting Started

To get access to Palmetto, you need to submit a request, which can be done [here](https://www.palmetto.clemson.edu/palmetto/basic/new/).

Once you have access, you will need to submit a request to get access to our lab storage and queue. You can do this by emailing ithelp@clemson.edu. Make sure you also copy Dr. Hubig so she can respond to approve the request. 

## Helpful Links
- [Access Request](https://www.palmetto.clemson.edu/palmetto/basic/new/)
- [Main Palmetto Page/JupyterHub Access](http://www.palmetto.clemson.edu/)
- [Intro Training](https://clemsonciti.github.io/workshop-palmetto/index.html)
- [Documentation](https://www.palmetto.clemson.edu/palmetto/)

## Login 
You will mainly interact with Palmetto via the command line. To login, you can use the following command: 

```
# Login
ssh <your username>@login.palmetto.clemson.edu
```

**NOTE:** This logs you into the login node, so you shouldn't run any intensive jobs on this node or you will impact everyone using the cluster. 


*Helpful Tip:* If the login command is difficult to remember you can add an alias to make it easier to login. On a Mac, you would do this by opening the terminal and editing your `.zshrc` file, which you will find in your user's home directory. Add the following line to the end of the `.zshrc` file: 

```
alias palmetto='ssh <your username>@login.palmetto.clemson.edu'
```

Once this is there you only need to type `palmetto` to login. 

## Storage

Your home directory is allocated 100GB of storage. If you want to use the Dzrpt lab storage (currently its size is 5TB) you will find it in 

```
/zfs/dzrptlab
```

## Modules
Each time you login, you will need to reload modules. For example, if you want to use Anaconda, you need to load it first.

```
# Load Anaconda
module add anaconda3/5.0.1-gcc/8.3.1

# List currently loaded modules
module list

# Show available modules
module avail
```

## Adding Customer Notebook Kernels
There are a few default kernels that can be used for Jupyter notebooks, but you can also create your own custom kernels and make them available to Jupyter. 

```
$ conda create --name myenv python=2.7
$ source activate myenv
$ conda install jupyter
$ python -m ipykernel install --user --name python_custom --display-name "My Python"
```

## Interactive Terminal

If you want to do something interesting or more intensive, you need to move off of the login node and onto a dedicated compute node. Below is a command that will give you access to a node using our dedicated dzrpt lab queue. 

```
qsub -I -q dzrptlab -l select=1:ncpus=5:mem=10gb,walltime=1:00:00

qsub             # Submit a request to scheduler
    -I           # Interactive
    -q           # Queue name
    -l           # Resources requested
    select=1     # One computer node
    ncpus        # Number of cpus
    mem          # Memory required
    interconnect # Type of network connectivity
    walltime     # Want node for 1 hour
```

If you want to use a different queue for some reason, you can see what's available with: 

```
# Check queue limits and available configurations
checkqueuecfg

# How busy each cluster is
whatsfree
```

If you want to see what nodes are available on Palmetto, you can check them with

```
# Show the hardware/nodes
cat /etc/hardware-table
```

## Batch Jobs

Sometimes you don't want to run things interactively, you would rather submit the job and let it run in the background and you can come back when it's finished. To do this, you need to write a batch script and submit it to the queue. There is an example batch script in this repo, `batch_example.pbs`, which runs a simple python file, `palmetto_example.py`.

Pay attention to the first few lines of the batch script, which contain information about how to configure the job and environment.

To run this job, execute the following command: 

```
qsub batch_example.pbs
```


