<!--

author:   Alexander Botzki
email:    training@vib.de
version:  1.0.0
language: en
narrator: UK English Female

icon:     https://vib.be/sites/vib.sites.vib.be/files/logo_VIB_noTagline.svg

comment:  This document shall provide an entire compendium and course on the
          development of Open-courSes with [LiaScript](https://LiaScript.github.io).
          As the language and the systems grows, also this document will be updated.
          Feel free to fork or copy it, translations are very welcome...

script:   https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.js
          https://felixhao28.github.io/JSCPP/dist/JSCPP.es5.min.js

link:     https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.css
link:     https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css
link:     https://raw.githubusercontent.com/vibbits/material-liascript/master/img/org.css
link:     https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css
link:     https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@300&display=swap
link:     https://fonts.googleapis.com/css2?family=Open+Sans&display=swap
link:     https://raw.githubusercontent.com/vibbits/material-liascript/master/vib-styles.css

@orcid: [@0](@1)<!--class="orcid-logo-for-author-list"-->

@tutor: Neuropixels
@edition: 1st -->

# Protein Structure Analysis and Visualisation

<section>
Hello and welcome to our @tutor workshop! We are very happy to have you here.

This is the @edition edition of this VIB workshop.

> We are using the interactive Open Educational Resource online/offline course infrastructure called LiaScript.
> It is a distributed way of creating and sharing educational content hosted on github.
> To see this document as an interactive LiaScript rendered version, click on the
> following link/badge:
>
> [![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/vibbits/protein-structure-analysis/main/README.md)

### Lesson overview

> <i class="fa fa-bookmark"></i> **Description**  
> This course consist of short tutorials related to current state of art using Neuropixels technology following with our interactive hands-on course about how to visualize electrophysiological data.

> <i class="fa fa-arrow-left"></i> **Prerequisites**  
> To be able to follow this course, learners should have knowledge in:
>
> 1. Being comfortable working with the CLI (command-line interface) in a Linux-based environment.     
>
> <i class="fa fa-arrow-right"></i> **Learning Outcomes:**  
> By the end of the course, learners will be able to:
>
> 1. Understand Nextflow's basic concepts & syntax: channels, processes, modules, workflows, etc.
> 2. Execute local and publicly available pipelines with different executors and environments
> 3. Write and run Nextflow pipelines
> 4.Write and modify config files for storing parameters related to computing hardware as well as pipeline dependent parameters
>
> <i class="fa fa-user"></i> **Target Audience:** Researchers, trainers, training providers
>
> <svg xmlns="http://www.w3.org/2000/svg" height="14" width="16" viewBox="0 0 576 512"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2023 Fonticons, Inc.--><path d="M384 64c0-17.7 14.3-32 32-32H544c17.7 0 32 14.3 32 32s-14.3 32-32 32H448v96c0 17.7-14.3 32-32 32H320v96c0 17.7-14.3 32-32 32H192v96c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32s14.3-32 32-32h96V320c0-17.7 14.3-32 32-32h96V192c0-17.7 14.3-32 32-32h96V64z"/></svg> **Level:** Beginner  
>
> <i class="fa fa-lock"></i> **License:** [Creative Commons Attribution 4.0 International  License](https://creativecommons.org/licenses/by/4.0/)
>
> <i class="fa fa-money-bill"></i> **Funding:** This project has received funding from VIB.
>
> <i class="fa fa-hourglass"></i> **Time estimation**: 7.30 hours
>
> <i class="fa fa-envelope-open-text"></i> **Supporting Materials**:
>
>  1. [Exercises and solutions](https://github.com/vibbits/protein-structure-analysis)
>  2. [Slides]()  
>
> <i class="fa fa-asterisk"></i> **Requirements:** The (technical) installation requirements are described in the [installations](https://vibbits-nextflow-workshop.readthedocs.io/en/latest/installations.html) section.
>
> <i class="fa fa-life-ring"></i> **Acknowledgement**:
>
> * [VIB](https://www.vib.be/)
>
> <i class="fa fa-anchor"></i> **PURL**:  

### Authors

@[orcid(Alexander Botzki)](https://orcid.org/0000-0001-6691-4233)

### Contributors

Joost van Durme
@[orcid(Janick Mathys)](https://orcid.org/0009-0007-1722-2370),

</section>

## General context

Welcome to our {{workshop_name}} workshop! We are very happy to have you here.

This is the {{workshop_edition}} edition of this workshop.

- The fifth session (2nd September 2024) is dedicated to Protein Structure Analysis and Visualisation.

The presentation which goes alongside this material can be found [here](https://liascript.githib.io/course?https://raw.githubusercontent.com/vibbits/protein-structure-analysis/main/psa-presentation.md).

### Schedule

Schedule day 1:

- 9:30 - 11:00 - Introduction and getting to know ChimeraX (I)
- 11:00 - 11:15 - break
- 11:15 - 12:45 - getting to know ChimeraX (II)
- 12:45 - 13:45 - lunch
- 13:45 - 15:15 - Computational mutagenesis tool MutateX
- 15:15 - 15:30 - break
- 15:30 - 17:00 - FoldSeek

## Installations

Please read this page carefully **before** the start of the workshop.

There are two options for following this workshop:

  1. [Download ChimeraX](https://www.rbvi.ucsf.edu/chimerax/download.html)
  2. <>

### Provided infrastructure

We will be using the Gent section of the [Flemish Supercomputing Center](https://www.vscentrum.be/), you should have already recieved instructions for creating an account.
Specifically, we will be using the [Interactive and Debug](https://docs.hpc.ugent.be/Linux/interactive_debug/) cluster. The cluster is already equipped with the latest version of Nextflow, and Apptainer.

To connect to the cluster, there are two options. For the first option, there is no local setup needed, we will use the Web Interface to access the Gent VSC.

#### Option 1: Web Interface

This utilizes the OnDemand infrastructure at the VSC to launch a web-based version of VSCode for us. Using this, we don't need to make any connections to the clutser other than through the browser.

_If you normally use VSCode locally, this setup is completely seperate and won't have your usual extensions etc._

- Navigate to [https://login.hpc.ugent.be/](https://login.hpc.ugent.be/) and login with your credentials.
- Select "Interactive Apps" from the top bar -> "Code Server"
- Fill in the following settings:
  - Cluster: `donphan (interactive/debug)`
  - Time: 8 (hours)
  - Nodes: 1
  - Cores: 8
  - Select Path -> $VSC_DATA (on the left)
  - Click "Launch"!
- Wait for your job to start -> "Connect to VS Code"

This runs fully in your browser and will continue to run even when your laptop is off etc. Your job will automatically end after 8 hours. **Make sure to save your work.**

#### Option 2: Local Installation

We will be using an SSH connection in VSCode which we can create by following these instructions:

- Download Visual Studio Code ([link](https://code.visualstudio.com/download))
- Add the following extensions for a seamless integration of Nextflow and the VM in VScode:
  - In VSCode, navigate to the 'Extensions' tab, search for the SSH remote package and install it:
  - 'Remote - SSH' (ms-vscode-remote.remote-ssh).
- Modify your local `.ssh/config` file to add the configuration for the cluster - If you already connect to the Gent VSC with this machine, you don't need to do this
  - `Ctrl-Shift-P` will bring up the "command palette"
  - Type `ssh config` and select the option to modify the configuration file (select the first file)
  - Add the following code to your config file:
    ```
    Host login-gent
        User vscXXXXX # Replace Xs with your VSC ID
        HostName login.hpc.ugent.be
        IdentityFile ~/.ssh/id_rsa # This should be replaced with the path to your private key ( windows users might look like this: C:\Users\KrisDavie\Documents\VSC\vsc_id_rsa)
    ```
- Start a terminal in VSCode (select Terminal and then New Terminal)
- Connect to the cluster with the following command: `ssh login-gent`
- Optional: Start `screen` or `tmux` and do the following in the new terminal - This will keep your session alive even when you disconnect from the cluster
- Load the modules for connecting to the interactive cluster: `module swap cluster/donphan`
- Start a job using qsub: `qsub -I -l walltime=08:00:00,nodes=1:ppn=8`
- Note the node you are connected to (e.g. `node4006.donphan.os`)
- Add the following code to your config file:
  ```
  Host node4006
      User vscXXXXX # Replace Xs with your VSC ID
      HostName node4006.donphan.os
      ProxyCommand ssh login-gent -W %h:%p
      # On windows you should use
      # ProxyCommand C:\Windows\System32\OpenSSH\ssh.exe login-gent -W %h:%p
  ```
- Finally you can open a this host in VSCode by typing `Ctrl-Shift-P` and selecting `Remote-SSH: Connect to Host...` and selecting the host you just added.
  - If you didn't run qsub in a screen or tmux session, you will need to use an entire new VSCode window to connect to the host, otherwise when VSCode refreshes, the original connection will be lost and the job will end.

#### Option 3: Custom Installation

You are free to connect to the cluster however you want, but the above 2 methods are the only ones we will support in the session.

### Common Setup

- Install the Nextflow VSCcode Package - This will give you syntax highlighting and linting for Nextflow
- Open a new terminal within VSCode: Terminal -> New Terminal
- Create a new folder for the workshop
- Clone this repository into the folder: `git clone git@github.com:VIBbits/nextflow-workshop.git`
- Load the nextflow module: `module load Nextflow/23.10.0`

## Citing this lesson

Please cite as:

  1. ...

## References

Here are some great tips for learning and to get inspired for other protein structure analysis tasks:

-  [Tutorial by ChimeraX](https://www.rbvi.ucsf.edu/chimerax/tutorials.html)
-  []

--------------------------------------------

*About ELIXIR Training Platform*

The ELIXIR Training Platform was established to develop a training community that spans all ELIXIR member states (see the list of Training Coordinators). It aims to strengthen national training programmes, grow bioinformatics training capacity and competence across Europe, and empower researchers to use ELIXIR's services and tools.

One service offered by the Training Platform is TeSS, the training registry for the ELIXIR community. Together with ELIXIR France and ELIXIR Slovenia, VIB as lead node for ELIXIR Belgium is engaged in consolidating quality and impact of the TeSS training resources (2022-23) (https://elixir-europe.org/internal-projects/commissioned-services/2022-trp3).

The Training eSupport System was developed to help trainees, trainers and their institutions to have a one-stop shop where they can share and find information about training and events, including training material. This way we can create a catalogue that can be shared within the community. How it works is what we are going to find out in this course.

*About VIB and VIB Technologies*

VIB is an entrepreneurial non-profit research institute, with a clear focus on groundbreaking strategic basic research in life sciences and operates in close partnership with the five universities in Flanders – Ghent University, KU Leuven, University of Antwerp, Vrije Universiteit Brussel and Hasselt University.

As part of the VIB Technologies, the 12 VIB Core Facilities, provide support in a wide array of research fields and housing specialized scientific equipment for each discipline. Science and technology go hand in hand. New technologies advance science and often accelerate breakthroughs in scientific research. VIB has a visionary approach to science and technology, founded on its ability to identify and foster new innovations in life sciences.

The goal of VIB Technology Training is to up-skill life scientists to excel in the domains of VIB Technologies, Bioinformatics & AI, Software Development, and Research Data Management.

--------------------------------------------

*Editorial team for this course*

Authors: @[orcid(Alexander Botzki)](https://orcid.org/0000-0001-6691-4233), @[orcid(Bruna Piereck)](https://orcid.org/0000-0001-5958-0669)

Technical Editors: Alexander Botzki

License: [![CC BY](img/picture003.jpg)](http://creativecommons.org/licenses/by/4.0/)
