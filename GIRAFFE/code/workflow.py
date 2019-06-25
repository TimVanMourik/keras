#This is a Nipype generator. Warning, here be dragons.
#!/usr/bin/env python

import sys
import nipype
import nipype.pipeline as pe











#Create a workflow to connect all those nodes
analysisflow = nipype.Workflow('MyWorkflow')
analysisflow.connect(conv2_d, "", conv2_d_1, "")
analysisflow.connect(conv2_d_1, "", max_pooling2_d, "")
analysisflow.connect(max_pooling2_d, "", dropout, "")
analysisflow.connect(dropout, "", flatten, "")
analysisflow.connect(flatten, "", dense, "")
analysisflow.connect(dense, "", dropout_1, "")
analysisflow.connect(dropout_1, "", dense_1, "")

#Run the workflow
plugin = 'MultiProc' #adjust your desired plugin here
plugin_args = {'n_procs': 1} #adjust to your number of cores
analysisflow.write_graph(graph2use='flat', format='png', simple_form=False)
analysisflow.run(plugin=plugin, plugin_args=plugin_args)
