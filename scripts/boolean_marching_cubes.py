__author__ = "Shervin Azadi"
__license__ = "MIT"
__version__ = "1.0"
__url__ = "https://github.com/shervinazadi/spatial_computing_workshops"
__summary__ = "Boolean Marching Cubes developed for Spatial COmputing Design Studio Workshops"

import topogenesis as tg
import numpy as np
import pyvista as pv
import os
import copy
import trimesh as tm
import pandas as pd


def create_symmetry_stencils(sym_str):
    #  creating stencils
    so_base = tg.create_stencil("von_neumann", 0, 1)
    sx_base = copy.deepcopy(so_base)
    sx_base.set_index((0, 0, 0), 0)
    sx_base.set_index((1, 0, 0), 1)

    # setting separate direction
    corner_state = dict(
        OO=so_base,
        XP=sx_base,
        XN=np.flip(sx_base, 0),
        YP=np.transpose(sx_base, (1, 0, 2)),
        YN=np.transpose(np.flip(sx_base, 0), (1, 0, 2)),
        ZP=np.transpose(sx_base, (2, 1, 0)),
        ZN=np.transpose(np.flip(sx_base, 0), (2, 1, 0))
    )

    for key, value in corner_state.items():
        value.function = tg.sfunc.sum
        corner_state[key] = value

    # setting paired directions
    corner_state["XX"] = corner_state["XN"] + corner_state["XP"]
    corner_state["YY"] = corner_state["YN"] + corner_state["YP"]
    corner_state["ZZ"] = corner_state["ZN"] + corner_state["ZP"]

    stencils = []

    for i, sym in enumerate(sym_str):
        # init the symmetry stencil with the first item
        sym_stencil = copy.deepcopy(corner_state[sym[0]])
        # iteratively add the rest of the symmetry stencils together
        for key in sym[1:]:
            sym_stencil += corner_state[key]
        # append
        stencils.append(sym_stencil)
        # compute the sum of all stencils
        if i == 0:
            stencil_sum = copy.deepcopy(sym_stencil)
        else:
            stencil_sum += sym_stencil

    # check if there is any neighbours that are not included
    stencil_rest = tg.create_stencil("von_neumann", 1, 1) - stencil_sum

    # print(np.zeros((3,3,3)).sum())
    if (np.array(stencil_rest).sum()):
        stencil_rest.function = tg.sfunc.sum
        stencils.append(stencil_rest)

    # add the sum function to all stencils
    for s in stencils:
        s.function = tg.sfunc.sum

    return stencils


def bi_cube_lattices():
    # create all possible configurations
    l_bis = []
    for i in range(2**8):
        bi = np.array(list(np.binary_repr(i, width=8))
                      ).astype(int).reshape((2, 2, 2))
        l_bi = tg.to_lattice(bi, [0, 0, 0])
        l_bis.append(l_bi)
    return l_bis


def extract_corner_profiles(stencils, l_bis):
    #######################

    # generate corner profiles

    corner_profiles = []
    for l in l_bis:
        # apply the stencils in all corners of all possible configurations
        r_s = [l.apply_stencil(s).flatten() for s in stencils]

        # concatenate corner_profiles into columns
        result = np.c_[tuple(r_s)]

        corner_profiles.append(result)

    return corner_profiles

    ######################


def profiles_to_lattices(uniq_corner_arang, stencils):
    stencil_ind = []
    for s in stencils:
        filled_ind = np.array(np.where(np.array(s) == 1)).T
        # relocate to corner
        filled_ind_reloc = filled_ind - 1
        # flip vertically
        filled_ind_flpd = np.flip(filled_ind_reloc, 0).astype(int)

        stencil_ind.append(filled_ind_flpd)
    # print(stencil_ind)

    ######################

    # generate mini-lattices to represent the geometrical equivalent of unique corner arrangments
    base_zero = np.zeros((2, 2, 2), dtype=np.int8)

    corner_neigh_lattices = []
    corner_loc_lattices = []
    # for each unique arangement, create a representation
    for uca in uniq_corner_arang:
        corner_arang = np.copy(base_zero)
        corner_loc = np.copy(base_zero)
        corner_loc[0, 0, 0] = 1

        shift = np.zeros(3)
        # for each list of indices of each stencil
        for i, s_inds in enumerate(stencil_ind):
            # for each index
            for j, s_i in enumerate(s_inds):
                # check if the sum is big enough to mark this index
                if uca[i] > j:
                    # check if the index is positive
                    if s_i.sum() >= 0:
                        # mark as one
                        corner_arang[tuple(s_i)] = 1
                    # if the index is negative
                    else:
                        # mark as one
                        corner_arang[tuple(s_i)] = 1
                        # record the index as a shift
                        shift += s_i

        # roll neighbourhood and locations
        corner_arang = np.roll(corner_arang, tuple(
            shift.astype(int)), (0, 1, 2))
        corner_loc = np.roll(corner_loc, tuple(shift.astype(int)), (0, 1, 2))

        # convert to lattice
        corner_lat = tg.to_lattice(corner_arang, np.zeros(3))
        corner_neigh_lattices.append(corner_lat)

        corner_loc_lat = tg.to_lattice(corner_loc, np.zeros(3))
        corner_loc_lattices.append(corner_loc_lat)

    return (corner_loc_lattices, corner_neigh_lattices)


def to_csv(lattice, filepath: str):
    """This method saves the lattice to a csv file

    Args:
        filepath: path to the csv file
    """
    # volume to panda dataframe
    vol_df = lattice.to_pandas()

    # specifying metadata and transposing it
    metadata = pd.DataFrame({
        'minbound': lattice.minbound,
        'shape': np.array(lattice.shape),
        'unit': lattice.unit,
    })

    with open(filepath, 'w') as df_out:

        metadata.to_csv(df_out, index=False, header=True,
                        float_format='%g', line_terminator='\n')

        df_out.write('\n')

        vol_df.to_csv(df_out, index=False, float_format='%g',
                      line_terminator='\n')


def save_design_templates(corner_loc_lattices, corner_neigh_lattices, templates_path):
    interior_zero = tg.to_lattice(
        np.zeros((2, 2, 2), dtype=np.int8), [0, 0, 0])
    border_pad = np.pad(interior_zero, (1, 1), 'constant', constant_values=(1))
    base_zero = tg.to_lattice(np.zeros((4, 4, 4), dtype=np.int8), [0, 0, 0])
    s = tg.create_stencil("von_neumann", 1, 1)
    s.set_index([0, 0, 0], 0)

    for i, core, neigh in zip(range(len(corner_loc_lattices)), corner_loc_lattices, corner_neigh_lattices):
        # construct saving paths
        core_path = os.path.join(templates_path, 'core_' + f'{i:02}' + '.csv')
        neigh_path = os.path.join(
            templates_path, 'neighs_' + f'{i:02}' + '.csv')
        e_neigh_path = os.path.join(
            templates_path, 'e_neighs_' + f'{i:02}' + '.csv')

        # aggregate neighbours
        neigh = tg.to_lattice(
            np.pad(neigh, (1, 1), 'constant', constant_values=(0)), [0, 0, 0])

        # construct the padded core
        core_pad = tg.to_lattice(
            np.pad(core, (1, 1), 'constant', constant_values=(0)), [0, 0, 0])
        # extract the outer neighbours of the core
        core_3ind = np.array(np.where(core_pad == 1)).flatten()
        pals = base_zero.find_neighbours_masked(s, loc=core_3ind)
        extra_neighs = np.copy(base_zero).flatten()
        # set the extra neighbours as the current state of the core
        extra_neighs[pals] = neigh[tuple(core_3ind)]
        extra_neighs = tg.to_lattice(
            extra_neighs.reshape((4, 4, 4)), [0, 0, 0])
        # remove interior pals
        extra_neighs *= border_pad

        # save to csv
        to_csv(core_pad, core_path)
        to_csv(neigh, neigh_path)
        to_csv(extra_neighs, e_neigh_path)


def construct_tile_meshes_old(subtile_meshes, corner_profiles, uniq_corner_arang, corner_loc_lattices):
    tile_corner_inds = []
    for prof in corner_profiles:
        # find each corner in the list of unique corner arrangements
        corner_ind = np.array(
            [np.where((p == uniq_corner_arang).all(1)) for p in prof]).flatten()
        tile_corner_inds.append(corner_ind)

    tile_corner_inds = np.array(tile_corner_inds)
    # print(tile_corner_inds)

    ###############################

    # find unique locs

    unique_locs = [np.array(np.where(loc == 1)).flatten()
                   for loc in corner_loc_lattices]
    unique_locs = np.array(unique_locs)

    ###############################

    corner_loc = np.array(np.where(np.ones((2, 2, 2)) == 1)).T
    corner_pos = corner_loc - .5
    # print(corner_pos)

    tiles_meshes = []
    # loading meshes
    for tile in tile_corner_inds:
        last_v_count = 0
        vertice_list = []
        face_list = []
        for c_ind, pos, loc in zip(tile, corner_pos, corner_loc):

            # extract current mesh
            corner_mesh = subtile_meshes[c_ind]
            # extract the uniqe profile of this corner
            u_loc = unique_locs[c_ind]
            if type(corner_mesh) == tm.base.Trimesh:
                # if current profile is different than uniqe profile, we need a transformation, -1 will flip over that dimension and 1 will keep it the same
                trans = (u_loc - loc) * 2 + 1
                # append the vertices
                vertice_list.append(corner_mesh.vertices * trans + pos)
                face_list.append(corner_mesh.faces + last_v_count)
                last_v_count += len(corner_mesh.vertices)

        vs = []
        fs = []
        if len(vertice_list):
            vs = np.vstack(vertice_list)
            fs = np.vstack(face_list)

            tile_mesh = tm.Trimesh(vs * 0.5, fs)
            tiles_meshes.append(tile_mesh)
        else:
            empty_tile = tm.creation.icosphere(subdivisions=1, radius=0.1)
            tiles_meshes.append(empty_tile)

    return tiles_meshes


def save_tile_meshes(tiles_meshes, l_bis, tiles_path):
    pow_two = 2 ** np.arange(7, -1, -1)

    for tile_mesh, l in zip(tiles_meshes, l_bis):

        # order correction
        l = np.roll(l, [1, 1, 1], [0, 1, 2])
        c_id = np.sum(l.flatten(order='F') * pow_two)

        # saving mesh
        tile_mesh_path = os.path.join(tiles_path, 't_' + f'{c_id:03}' + '.obj')
        with open(tile_mesh_path, 'w') as file:
            file.write(tm.exchange.obj.export_obj(tile_mesh))


def marching_cube_mesh(cube_lattice, tiles_path):

    # extract cube indices
    cube_ind = np.transpose(np.indices(cube_lattice.shape),
                            (1, 2, 3, 0)).reshape(-1, 3)
    # extract cube positions
    cube_pos = (cube_ind + 0.5) * cube_lattice.unit + cube_lattice.minbound

    # extract cube tid
    cube_tid = cube_lattice.ravel()

    # remove the cube position and tid where tid is 0
    filled_cube_pos = cube_pos[cube_tid > 0]
    filled_cube_tid = cube_tid[cube_tid > 0]

    # load tiles
    tiles = [0]
    for i in range(1, 256):
        tile_path = os.path.join(tiles_path, 't_' + f'{i:03}' + '.obj')
        tile = tm.load(tile_path)
        tile.vertices *= cube_lattice.unit
        tiles.append(tile)

    last_v_count = 0
    vertice_list = []
    face_list = []

    # place tiles
    for i in range(1, filled_cube_tid.size):
        # extract current tile
        tile = tiles[filled_cube_tid[i]]

        # append the vertices
        vertice_list.append(tile.vertices + filled_cube_pos[i])
        face_list.append(tile.faces + last_v_count)
        last_v_count += len(tile.vertices)

    vs = []
    fs = []
    # if len(vertice_list):
    vs = np.vstack(vertice_list)
    fs = np.vstack(face_list)

    tile_mesh = tm.Trimesh(vs, fs)

    return tile_mesh
