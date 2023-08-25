def water_jug_problem(capacity_jug1, capacity_jug2, target):
    jug1 = 0
    jug2 = 0  
    steps = []  
    
    while jug1 != target and jug2 != target:
        
        if jug1 == 0:
            jug1 = capacity_jug1
            steps.append(f"Fill jug 1")
       
        elif jug1 > 0 and jug2 < capacity_jug2:
            amount_to_pour = min(jug1, capacity_jug2 - jug2)
            jug1 -= amount_to_pour
            jug2 += amount_to_pour
            steps.append(f"Pour {amount_to_pour} from jug 1 to jug 2")
        
        elif jug2 == capacity_jug2:
            jug2 = 0
            steps.append(f"Empty jug 2")
        
        elif jug2 < capacity_jug2 and jug1 > 0:
            amount_to_pour = min(jug1, capacity_jug2 - jug2)
            jug1 -= amount_to_pour
            jug2 += amount_to_pour
            steps.append(f"Pour {amount_to_pour} from jug 1 to jug 2")
    
    return steps

jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

steps_taken = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)
for step in steps_taken:
    print(step)

name = "BAlAGUHAN"
print("192124151, " + name + "!")

name = "WATERJUGPROBLEM"
print("3, " + name + "!")

