import numpy as np

"""
Example case adopted from:

    Practical Bifurcation and Stability Analysis, page 325
    Seydel R.
    Eq. (7.15) - Isothermal chemical reaction dynamics


"""

class Torus:
    def __init__(self, lam=1.8):
        self.lam = lam
        self.dimension=3        # specify the dimension of the problem
    def dynamics(self, x0, t):

        """ODE system
        This function will be passed to the numerical integrator

        Inputs:
            x0: initial values
            t: time

        Outputs:
            x_dot: velocity vector
        """
        y1, y2, y3 = x0
        dy1_dt = (self.lam - 3)*y1 - 0.25*y2 +y1*(y3 + 0.2*(1-y3**2))
        dy2_dt = 0.25*y1 + (self.lam - 3)*y2 + y2*(y3 +0.2*(1-y3**2))
        dy3_dt = self.lam*y3 - (y1**2 + y2**2 + y3**2)

        vel_array = np.array([dy1_dt, dy2_dt, dy3_dt], float)
        return vel_array


    def get_stability_matrix(self, x0, t):

        """
        Stability matrix of the ODE system

        Inputs:
            x0: initial condition
        Outputs:
            A: Stability matrix evaluated at x0. (dxd) dimension
            A[i, j] = dv[i]/dx[j]
        """
        #A_matrix = np.array([[30 - 0.5*y1 -y2 -y3, -y1 + 2*0.001*y2, -y1],
        #                    [y2, y1 - 2*0.001*y2 -self.lam, 0.],
        #                   [-y3, 0., 16.5 - y1 - y3]], float)

        return #A_matrix
