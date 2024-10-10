# Game? Pygame module does not work rn
# 

def math_factory(f):
    return {
        "add": lambda x,y: x+y,
        "subtract": lambda x,y: x-y,
        "multiply": lambda x,y: x*y,
        "divide": lambda x,y: x/y if y !=0 else "cannot divide by zero"
    }.get(f, lambda x,y: "invalid operation")

def outcome_factory(production):
    def timer(t):
        if production == 10:
            return("High material, high workers")
        elif production >= 8 and t <= 5:
            return("High material, high workers")
        elif production >= 8 and t > 5:
            return("High material, low workers")
        elif production >=4 and production < 8:
            if t>=5:
                return("Normal material, low workers")
            elif t<5:
                return("Normal material, high workers")
        elif production < 4 and production > 0:
            return("Low material, low workers")
        else:
            return("bruh wut")
    return timer

def time_to_walk_factory(num_people):
    def speed(mph):
        return()

