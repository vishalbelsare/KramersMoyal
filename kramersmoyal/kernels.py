import numpy as np


def epanechnikov_1d(n_points):
    """
    Generates the Epanechnikov kernel in 1 dimension

    Parameters
    ----------
    n_points  : integer
        Number ( >= 1) total array size of the kernel. Must be either smaller
        than the total size of the phase space, for bounded compact support
        kernels, or equivalent of the size of the phase space.

    Returns
    -------
    kernel  : array
        The specified kernel.
    """
    kernel = 1 - np.linspace(-1, 1, n_points, endpoint=True) ** 2

    normalisation = 3 / 4

    return kernel * normalisation


def Epanechnikov_2d(n_points, bandwidth = 0, data=False, bounds=False,
                    symmetric=True):
    """
    Generates the symmetric Epanechnikov kernel in 2 dimension

    Parameters
    ----------
    n_points  : integer
        Number ( >= 1) total array size of the whole phase space. The kernel
        will be of a reduced size in this 2D space of size n_points x n_point.
        Suggested values is of order n_points = 1000.

    bandwidth  : float
        Number ( >= 0) indicating the bandwidth of the kernel. If unspecified,
        the optimal bandwidth according to Silverman will be used.
	    Can require the argument  : data

    data  : array (2D)
	   Data where to apply the kernel. Needed to calculate the extrema, if not
       given by argument bounds, or to	calculate the optimal bandwidth.

    bounds  : array
	   Either an array of two entries, mininum and maximum, or an 2D array of
       minimum and maximum in each dimension. If unspecified and argument data
       is passed as argument, extrema will be taken from there.

    symmetric  : boolean
        The Epanechnikov kernel in two dimensional has a symmetric and a
        non-symmetric version.

    Returns
    -------
    kernel  : array (float)
        The specified kernel.
    """

    if bounds == False:
	if data != False:
	    bounds = np.array([[data[:,0].min(),data[:,0].max()],
			       [data[:,1].min(),data[:,1].max()]])
    elif bounds.size == 2:
	bounds = np.array([[bounds[0],bounds[1]],
		           [bounds[0],bounds[1]]])
    elif bounds.size != 4:
	raise ValueError("""Bounds must be either an array of 2 entries, a 2D array
                        of the bounds at each dimension, or not specified, thus
                        extracted from the provided argument data""")

    # 1d linear space for underlying space
    x1  = np.linspace(-1 * bandwidth, 1 * bandwidth, Mn)
    # 2d linear space for Kernel generator
    x1_2D, y1_2D = np.meshgrid(x1, x1, sparse=True)                      # 2d linear space for Kernel generator
    BinsSpace = np.zeros([n + Mn, Dim])                                  # Records x1 and x2 spaces


    x1 = np.linspace(-1*bandwidth, 1, n_points, endpoint=True)
    x1_2D, y1_2D = np.meshgrid(x1, x1, sparse=True)


    if symmetric == True:
	# Epanechnikov kernel:
	#   (8/3*pi)*3/4(1 - (x² + y²), x=-1 to x=1 CHECK!
    	kernel = 1 - (np.power(x1_2D,2) + np.power(y1_2D,2)) / (np.power(bandwidth,2))
    	kernel[kernel < 0.] = 0.	#Remove <0 values

    	normalisation = 2 / (bandwidth * np.pi)

    elif symmetric == False:


    return kernel * normalisation
