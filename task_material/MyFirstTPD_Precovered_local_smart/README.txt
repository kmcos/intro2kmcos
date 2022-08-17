This example shows how to run a temperature programmed reaction with kmcos and the "tps" feature (time per snapshot).
The directory for the model only included runfile7.py, as that is the only runfile that will be used for this workshop exercise.

If the user would like to learn more after this workshop, there are additional runfile examples inside  https://github.com/kmcos/kmcos/tree/master/examples/MyFirstTPD_Precovered_local_smart

After compiling the model by running the build file, look at runfile 7 which is already in the model's directory.

There are some loading features. Let's ignore that for now.

We see that we set the "steps per snapshot" and the "time per snapshot" between lines 50 and 60. The tps is set at 1.0, which means that anytime a snapshot reaches beyond 1 second of simulation time, the snapshot will end without doing further steps (so the actual steps per snapshot will not be constant). For example, if the sps is set at 100 steps but tps is set at , if 1 second is reached after 43 steps, then the snapshot will end at 43 steps instead of finishing all 100 steps.

In this runfile, for the temperature programmed reaction, we also set the initial temperature, final temperature, and heating rate for the temperature programmed reaction. Near the bottom of the file is a loop that goes across temperatures.

Now, try running this runfile.
After the file is run, open the TOFs file produced by the snapshots module. Make a scatter plot with the x axis as temperature and the Y axis as the TOF_data , and make another for TOF_integ.
Save this plotting file.

Now, open the runfile, change the TPS to 0.1, run again, and make the same plots.