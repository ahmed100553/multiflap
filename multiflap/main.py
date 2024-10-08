'''
file main.py
@author Gianmarco Ducci
@copyright Copyright © UCLouvain 2020

multiflap is a Python tool for finding periodic orbits and assess their stability via the Floquet multipliers.

Copyright <2020> <Université catholique de Louvain (UCLouvain), Belgique>

List of the contributors to the development of multiflap, Description and complete License: see LICENSE and NOTICE files.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
import numpy as np
from  ms_package.multiple_shooting import MultipleShooting
from aero_package.bird_model import BirdModel
from aero_package.bird import Shoulder, Elbow, Wrist, Joint
import time
from numpy.linalg import norm
from numpy import inf
from ms_package.lma_solver import Solver
from utilities.save_data import SaveData

sim_name = "bird_flight"
SaveData(sim_name).make_folder()
# generate bird kinematics by calling "bird" module
bird_shoulder = Shoulder(axis_x=Joint(0.2,0.014,-np.pi/2),
                         axis_y=Joint(-np.deg2rad(19),np.deg2rad(20),np.pi/2),
                         axis_z=Joint(0,np.deg2rad(44),np.pi))
bird_elbow = Elbow(axis_x=Joint(0.,np.pi/6,-np.pi/2),
                   axis_y=Joint(np.pi/6,np.pi/6,-np.pi/2))

bird_wrist = Wrist(axis_y=Joint(-np.pi/6,np.pi/6,np.pi/2),
                   axis_z=Joint(0.,0.,0.))

mybird = BirdModel(shoulder=bird_shoulder, elbow=bird_elbow, wrist=bird_wrist)

# set initial guess for multiple-shooting scheme
x0 = [18., 0.5, 0.1, 0.01]

# generate multiple-shooting object
ms_obj = MultipleShooting(x0, M = 2, period=0.25, t_steps=70, model = mybird)

# call the LMA solver
mysol = Solver(ms_obj = ms_obj).lma()
print(mysol[3])

sol_array = mysol[3].space
sol_time = mysol[3].time

# define eigenvalues
# eigenvalues = mysol[3].eigenvalues

# save data
# SaveData(sim_name).save_data('multipliers_LC', eigenvalues)
SaveData(sim_name).save_data('solution_LC', sol_array)
SaveData(sim_name).save_data('time_array_LC', sol_time)