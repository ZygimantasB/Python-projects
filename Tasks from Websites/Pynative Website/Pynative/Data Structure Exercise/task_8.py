from classes import all_task

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}


dat_structure = all_task.DataStructureTask8(
    [47, 64, 69, 37, 76, 83, 95, 97],
    {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
)

print(dat_structure.removing_data())
