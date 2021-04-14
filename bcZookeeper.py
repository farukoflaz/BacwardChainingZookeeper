"""
CS461 Artificial Intelligence
Homework 5

Group nick: CROSSBREAKER

Abdullah Emir Öztürk (S1)
Ege Kemahlıoğlu (S1)
Koray Barkın Cıngı (S2)
Ömer Faruk Oflaz (S2)
Ömer Faruk Ünal (S2)
"""
import random

#global variable to store rules
rules = {} 
#assigning all rules
rules["Z1"] = [["has hair"] , "is a mammal"]
rules["Z2"] = [["gives milk"] , "is a mammal"]
rules["Z3"] = [["has feathers"] , "is a bird"]
rules["Z4"] = [["flies","lays eggs"] , "is a bird"]
rules["Z5"] = [["is a mammal","eats meat"] , "is a carnivore"]
rules["Z6"] = [["is a mammal","has pointed teeth","has claws","has forward-pointing eyes"] , "is a carnivore"]
rules["Z7"] = [["is a mammal","has hoofs"] , "is an ungulate"]
rules["Z8"] = [["is a mammal","chews cud"] ,"is an ungulate"]
rules["Z9"] = [["is a carnivore","has tawny color","has dark spots"] , "is a cheetah"]
rules["Z10"] = [["is a carnivore","has tawny color","has black stripes"] , "is a tiger"]
rules["Z11"] = [["is an ungulate","has long legs","has a long neck","has tawny color","has dark spots"] ,"is a giraffe"]
rules["Z12"] = [["is an ungulate","has white color","has black stripes"] , "is a zebra"]
rules["Z13"] = [["is a bird","does not fly","has long legs","has a long neck","is black and white"] , "is an ostrich"]
rules["Z14"] = [["is a bird","does not fly","swims","is black and white"] , "is a penguin"]
rules["Z15"] = [["is a bird","is a good flyer"] , "is an albatross"]

#global variable that holds possible animals 
animals = ['is an albatross', 'is a penguin', 'is an ostrich', 'is a zebra', 'is a giraffe', 'is a tiger', 'is a cheetah']

#working_memory = ["has hair", "has forward-pointing eyes", "has claws", "has pointed teeth", "has tawny color", "has dark spots"] #cheetah
#working_memory = ["has hair", "has forward-pointing eyes", "has claws", "has pointed teeth", "has tawny color", "has black stripes"] #tiger
#working_memory = ["has hair","chews cud","has white color","has black stripes"] #zebra
#working_memory = ["flies","lays eggs","is a good flyer"] #albatross
#working_memory = ["has feathers","lays eggs","swims","does not fly","is black and white","has tawny color"] #surprise example splashy
working_memory = list()
wrong_infos = list()


def isConsequent(hypothesis):
    """
    This function returns list of antecedents of argument hypothesis if there is any,
    otherwise it returns empty list
    """
    antecedents = list()
    
    for j in range(15):
        if hypothesis == rules[f"Z{j+1}"][1]: #checks whether there is corresponding rule that has argument as consequent
            antecedents.append((f"Z{j+1}",rules[f"Z{j+1}"][0])) #appends antecedents to list
    
    return antecedents

def isFact(input):
    """
    This funtion returns True if argument input is in the working memory,
    otherwise it returns False
    """
    if input in working_memory:
        return True
    else:
        return False    
 
def backwardChaining(ps):
    """
    This function simulates backward chaining process
    """
    valid = False

    if isFact(ps): #if it is in working memory, then it is done
        return True
    
    if isConsequent(ps) == []: #if this function returns empty list, it means there is no antecedent
        return False           #for this argument so returns False

    else:
        possible_rules = isConsequent(ps) # gets possible antecedents of rules

        for rule in possible_rules:
            
            if (not isFact(rules[rule[0]][1])) and (rules[rule[0]][1] not in wrong_infos):
                print(f"Rule {rule[0]} is fired")
                print(f"Rule {rule[0]}=> anticedents: {rules[rule[0]][0]}, consequent: {rules[rule[0]][1]}")
                input()
            valid = valid or BC_anded(rule[1]) #we make OR operation for independent rules
                                               #if one of them is True, then it is True 
            
            if valid:    #if current argument is True, then it is proven that it is also fact 
                if not isFact(ps):
                    working_memory.append(ps)
                    print("It", ps)
                    print("Current working memory:", working_memory,"\n")
                    input()
                return True
            
    if ps not in wrong_infos:
        wrong_infos.append(ps)                
                
    return False

def BC_anded(ps):
    """
    This funtion do AND operation for process
    it returns False if any of the antecedents is False,
    otherwise it returns True
    """
    valid = True

    for rule in ps:
        valid = valid and backwardChaining(rule)

        if not valid:
            if ps[0] not in wrong_infos:
                wrong_infos.append(ps[0])
            return False

    if not isFact(ps[0]):
        working_memory.append(ps[0])
        print("It", ps[0])
        print("Current working memory:", working_memory,"\n")
        input()
      
    return True       

def main():
    """
    main function
    """
    
    val = "begin"
    print("Please tell me about the creature entering one by one!\nType exit to terminate this process.")
    while val != "exit":
        val = input()
        working_memory.append(val)
    
    print("Initial working memory:", working_memory,"\n")
    print("There would be waits for user input in the remaining part to check the current situation")
    print("Please press the enter to continue execution. \n")
    for i in range(7):
        
        initial_hypo = random.choice(animals)
        animals.remove(initial_hypo)
        
        print("Initial hypothesis: ", initial_hypo)
        input()
        valid = backwardChaining(initial_hypo)

        if valid:
            print("Hypothesis it", initial_hypo, "TRUE")
            break
        else:
            print("Hypothesis", initial_hypo,"FALSE")    
        print("----------------------------------------------------\n")

if __name__ == "__main__":
    main()
