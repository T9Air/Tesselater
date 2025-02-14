import numpy as np
import pyvista as pv
from main import Nozzle_Size
from mesh_loader import get_mesh

mesh = get_mesh()


p=pv.Plotter()
Microstepping=1/16
# Filter cells based on area
# Compute cell sizes
sizes = mesh.compute_cell_sizes()

# Access cell areas
areas = sizes['Area']
#Here we make a quick calculus to see the little areas that are more prone to have errors,depending on your micro-stepping and nozzle size
Minimal_area =Nozzle_Size*Microstepping
filtered_cells = np.where(areas < Minimal_area)


# Extract the cells with thin area
thin_cells = mesh.extract_cells(filtered_cells)

# Add the thin cells to the plotter
p.add_mesh(mesh, color='blue',opacity=0.3)
p.add_mesh(thin_cells, color='red')


p.show()



































