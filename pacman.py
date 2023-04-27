'''
The Packman Problem
'''    

import copy 

""" Helper functions for checking operator's conditions """

_cnt = 0
number_of_fruit = 0 # Ο Μέγιστος αριθμός φρούτων, αρχικοποιήείται πιο κάτω
my_dict = {}        # Ένα hashmap όπου θα χρησιμοποιήσουμε για την ταυτοποίηση των
                    # θέσεων των arrays όπου έχουμε επισκεφτεί.

# Πίνακας με τις συντεταγμένες δισδιάστατου πίνακα όπου
# πάνω:     [-1,0]
# δεξιά:    [0,1]
# κάτω:     [1,0]
# αριστερά: [0,-1]
directions = [
            [-1,0],
            [0,1],
            [1,0],
            [0,-1]
        ]

# Σε κάθε κλήση της συνάρτησης γίνεται έλεγχος για το άμα μπορεί ο Pacman να μετακινηθεί πάνω, δεξιά, κάτω ή αριστερά.
def dfs(matrix, row, col):
    global _cnt
    global number_of_fruit
    pos = f"{row}:{col}" # Δήλωση hashmap για την αναγνώριση των χαρακτήρων που θα χρησιμοποιήσουμε στο πρόγραμμα.
    # Στην περίπτωση όπου έχουμε παρεμβεί τα όρια του Array όπου γίνεται η αναζήτηση ή έχουμε συναντήσει τον χαρακτήρα 'v'
    # που είναι καταχωρημένος στο hashmap ή έχουν φαγωθεί όλα τα φρούτα.
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or (pos in my_dict.keys() and my_dict[pos] == 'v') or _cnt == number_of_fruit:
        return
    for i in range(len(directions)):    # αναζήτηση στον πίνακα 'directions'
        current_dir = directions[i]
        if matrix[row][col] == 'f':
            _cnt += 1                   # για κάθε φρούτο που βρίσκεται μέσα σε κελί η τιμή της _cnt αυξάνεται κατά ένα
        matrix[row][col] = 'p'       # αφαιρείται - φαγώνεται από τον pacman
        my_dict[pos] = 'v'              # και στη συνέχεια ενημερώνεται για τη συγκεκριμένη θέση του κελιού στο λεξικό με τον χαρακτήρα 'v' για "visited"
        print(matrix)
        matrix[row][col] = ''   
        dfs(matrix, row + current_dir[0], col + current_dir[1]) # αναδρομή και έλεγχος για την επόμενη κατεύθυνση στον πίνακα 
        if _cnt == number_of_fruit:
            return 


def can_eat(state):
    for i in range(len(state)):
        if state[i][0]=='p' and state[i][1]=='f':  
            return 1  

def can_move_right(state):
    return not state[len(state)-1][0]=='p' 

def can_move_left(state):
    return not state[0][0]=='p'


""" Operator function: eat, move right, move left """

def eat(state):
    if can_eat(state):
        for i in range(len(state)):
            if (state[i][0]=='p' and state[i][1]=='f') or state[i][0]=='f' or state[i][1]=='f':  
                global _cnt 
                _cnt = _cnt + 1
                state[i][1]=''
                return state                
    else:
        return state

def move_right(state):
    if can_move_right(state):
        for i in range(len(state)):
            if state[i][0]=='p':
                state[i][0]=''
                state[i+1][0]='p'
                return state
    else: 
        return state
         
def move_left(state):
    if can_move_left(state):
        for i in range(len(state)):
            if state[i][0]=='p':
                state[i][0]=''
                state[i-1][0]='p'
                return state
    else:
        return state


initial_state=[['f',''],['p','f'],['',''],['','f']]  
# print(eat(initial_state))
# print(move_left(initial_state))
# print(move_right(initial_state))

# Έλεγχος αριθμού φρούτων μέσα στο πίνακα.
for i in range(0, len(initial_state)):
    for j in range(0, len(initial_state[0])):
        if initial_state[i][j] == 'f':
            number_of_fruit = number_of_fruit + 1

initial_r = 0 
initial_c = 0
# Εύρεση αρχικής θέσης pac-man
for i in range(0, len(initial_state)):
    for j in range(0, len(initial_state[0])):
        if initial_state[i][j] == 'p':
            initial_r = i 
            initial_c = j
            break 

dfs(initial_state, initial_r, initial_c)
print(_cnt)
