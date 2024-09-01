1. navigate to https://github.com/vibbits/containers-workshop
2. go to folder apptainer
3. adapt the `pbs` script to your local setup
4. at UGent, switch to the `donphan` debug cluster `module swap cluster/donphan`
5. build the apptainer image `sbatch build-from-docker-recipe.pbs`
5. after about 2-5 min, you should have created a file `mutatex.sif`  
