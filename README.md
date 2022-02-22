# Keeping Track of Job Applications 

This setup provides features to help you keep track of jobs you have applied for while on the job hunt. 
Everything is written in Python, and is used through the terminal (Mac). 

## Introduction 

### Directory Hierarchy 

The idea of this setup is to have one directory where everything will be stored in. 
Throughout this README, we will call this directory `jobapps`, although you can call it whatever. 
Within this directory, there will be two subdirectories starting off: 

  1. `python`: this is where all of the code is written, and also is where every command to add/update jobs will be run from. 
  Every Python file is run as an executable. 
  
  2. `data`: this is where the information about various companies, jobs, etc. will be stored. 
  This is designed to *not* be modified by the user. 
  Within this directory there will be a `00-datasets.json` file. 
  
So starting off, the directory hierarchy will be as follows: 
```
jobapps
    |---- python 
            |----<all relevant files>
    |----data
            |----00.datasets.json
```

More subdirectories will be added as you add more databases (more on that later). 



### Philosophy of Tracking Jobs 

When applying to any job, there are three "levels" that can be used to classify any job: 

  1. The "type" of job. 
  
  2. The company that you are applying for with the job. 
  
  3. The actual job itself. 
  
When I say "type", this originally meant the sector of job that you were applying for. 
For example, one job could be considered `Software Engineering | Google | Software Engineer`, 
so it`s class is "Software Engineering", the company is "Google", and the actual job is "Software Engineer" 
Another example could be `Quantitative Finance | Hudson River Trading | Algorithm Developer`. 

When looking at it this way, it makes sense to separate each "type" of job into completely different datasets. 
So one dataset would keep track of every job pertaining to, say, software engineering, 
while another dataset would keep track of all jobs pertaining to quantitative finance, and so on. 
Practically, however, you could split up these datasets however you so choose. 
For example, you could create a new dataset for all jobs you apply to in the year 2022, regardless of sector. 
Or you could create a new dataset with a new alais (i.e. different contact information). 
Basically, **the organization of the datasets is completely up to the user**, 
and so a more accurate representation of the job heirarchy would be: 

  1. The relevant *dataset*, organized however the user sees fit. 
  
  2. The *company* of the job. 
  
  3. The *job* itself. 
  
This is the approach taken throughout this project. 
Users will be able to add, update, modify, and remove information at all three levels of this hierarchy. 

The user should also be able to be able to store relevant documents or files they created throughout the process for each job. 
Maybe they want to write down any questions they were asked during an interview, or keep important documents sent to them. 
So as more datasets, companies, and jobs are added, 
corresponding directories will also be created that will allow the user to organize their information 

## Initializing Database 

To begin using this system, complete the following steps: 

  1. Clone this repository (we will assume it is called `jobapps`). 
  Make sure that you are in this directory. 
  
  2. Every command used for this setup will be run from the `python` subdirectory, so run the following commands: 
  ```
  cd python
  # chmod 755 *.py # fix this later
  ./init.py 
  ```

At this point, everything is set up exactly as described, ready for use. 

## Understanding Commands (with Example)

First, make sure you are in the `python` directory, as all commands are to be run here. 
All executables that have to do with adding, updating, modifying, or removing some part of the dataset in the heirarchy are of the form 
```
<descriptive character><action>.py [other arguments]
```
The "descriptive characters" are 

  1. **d** for dataset level. 
  
  2. **c** for company level. 
  
  3. **j** for job level. 
  
The possible actions are **add**, **rem**, **up**, and **sel** (although not every level of the heirarchy has all four). 
So for example, running the command `./jadd.py [...]` would add a job (you would have to supply arguments to specify more", 
or the command `crem.py [...]` would remove a specified company from the database. 

The first step is to add a dataset you will be working with. 
Suppose this dataset is all jobs you are applying to in 2022, so you decide to name it `22`. 
Run the following command: 
```
./dadd.py 22 -e <email> -p <phone number> -g <github> -l <linkedin> -t <twitter>
```
A new dataset will be created called `22`, and will store all of your contact information as well. 
A directory `jobapps/22` will be created as well. 

Next, suppose the user applies to a job at Google. It would need to be added to this database. 
Every company must be given an associated nickname that will be used to identify it, such as `GOOG`. 
When adding a company to the dataset, we must supply both the companies`s full name and nickname as follows: 
```
./cadd.py "Google" GOOG
```
Google has been added to the `22` dataset with id `GOOG`, and the directory `jobapps/22/GOOG` will be created. 

Now that Google is in the dataset, we want to add a specific job that we applied for. 
Sticking with the example, suppose we applied to a software engineering job. 
Just like at the company level, each job needs both a full name and an associated nickname; 
we will use "Software Engineer" and "SWE". 
To add this job, run the following command: 
```
./jadd.py GOOG "Software Engineer" SWE
```
In addition to the job being added, the directory `jobapps/22/GOOG/filesSWE` is created. 
This directory can be used to store any relevant documents pertenant to this specific job. 

Suppose that a few days later, we get an email back asking us to complete the assessment, 
a noteworthy point in the application process. 
We can log this update by running the following command: 
```
./jup.py GOOG SWE -m "received invitation to take assessment" 
```

For another full on example, let`s look at the example with Hudson River Trading. 
We want to :

  1. Add the company to the dataset (with company id HRT). 
  
  2. Add the job to the dataset (with job id AD). 
  
  3. Log update, saying we were rejected. 
  
In code: 
```
./cadd.py "Hudson River Trading" HRT 
./jadd.py HRT "Algorithm Developer" AD 
./jup.py HRT AD -m "rejected" -r
```
Notice the `-r` flag in the last command. This is one of several optional flags that can be used to indicate the status of a given job. 

Lastly, if you want quick access to all of the jobs you have applied for, run the following command: 
```
./print.py
```
This will print out relevant information for all jobs applied to in the `22` dataset. 
It prints each company, the jobs applied to for each company, and all logged updates for each job. 
After that, it also prints out the number of jobs applied to, the number of companies applied to, and the name of the current dataset. 

If you want to print out, say, only the names of the companies printed out and omit the rest, 
there is an optional flag to specify the "level" of information printed. Running
```
./print.py -l
```
will print out only the company names. Running 
```
./print.py -ll
```
will print both the company names and jobs for each company, but will omit the logs for each job. 
Using `-lll` will print out all three levels of information (which is the default). 

Additionally, if you want to print out information for only a single company, 
you can supply the company`s id as an optional argument. 
For example, running 
```
./print.py GOOG
```
will print out the full information for all jobs applied for with Google. 
As before, you can also specify the level of information printed out, with either `-l` or `-ll`. 

Using the `-h` flag will give specific information about a given command, 
including any optional arguments and flags. 
