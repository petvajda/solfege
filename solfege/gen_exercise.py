import random

#############
### NOTES ###
#############
NOTES_NORMAL = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
NOTES_SHARP  = list(map(lambda x: x+'#', NOTES_NORMAL))
NOTES_FLAT   = list(map(lambda x: x+'b', NOTES_NORMAL))
ALL_NOTES    = NOTES_NORMAL + NOTES_SHARP + NOTES_FLAT

######################
### PENTATON MODES ###
######################
PENTATON = [1, 2, 3, 5, 6]

####################
### SCALES MODES ###
####################
MODES = [1, 2, 3, 4, 5, 6, 7]

def check_order(list):
    for i in range(len(list)-1):
        if abs(list[i] - list[i+1]) <= 2:
            return True
    return False

def rand_mode(modes):
    while check_order(modes):    
        a = random.randrange(len(modes)-1)
        modes[a], modes[a+1] = modes[a+1], modes[a]
        # print('{0} {1} {2}'.format(a, a+1, modes))
    return modes

def exercise(modes):
    print(ALL_NOTES[random.randrange(len(ALL_NOTES))], end=' ')
    print(rand_mode(modes))

def gen_exercise():
    exercise(PENTATON)
    exercise(MODES)

if __name__ == '__main__':
    gen_exercise()
