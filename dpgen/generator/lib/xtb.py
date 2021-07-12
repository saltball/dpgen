def make_xtb_input(sys_data):
    coordinates = sys_data['coords'][0]
    atom_names = sys_data['atom_names']
    #atom_numbs = sys_data['atom_numbs']
    atom_types = sys_data['atom_types']
    # get atom symbols list
    symbols = [atom_names[atom_type] for atom_type in atom_types]

    titlekeywords = 'DPGEN'

    buff = [str(len(coordinates)),titlekeywords]

    for ii, (symbol, coordinate) in enumerate(zip(symbols, coordinates)):
        buff.append("%s %f %f %f" % (symbol, *coordinate))
    buff.append('\n')
    return '\n'.join(buff)