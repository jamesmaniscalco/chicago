# convert weights and measures from various units to others.
# Uses floating-point arithmetic.

# rather than converting from one arbitrary unit to another, convert through metric if need be.

#############
#  WEIGHTS  #
#############

def grams_to_kilograms(weight):
    return weight * 0.001
    
def grams_to_ounces(weight):
    return weight * 0.035274
    
def grams_to_pounds(weight):
    return weight * 0.00220462
    

def kilograms_to_grams(weight):
    return weight / 0.001

def ounces_to_grams(weight):
    return weight / 0.035274
    
def pounds_to_ounces(weight):
    return weight / 0.00220462
    
    
#############
#  VOLUMES  #
#############

def milliliters_to_liters(volume):
    return volume * 0.001
    
def milliliters_to_cubic_inches(volume):
    return volume * 0.0610237
    
    
def liters_to_milliliters(volume):
    return volume / 0.001
    
def cubic_inches_to_milliliters(volume):
    return volume / 0.0610237
    
    
