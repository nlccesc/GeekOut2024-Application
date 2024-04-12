def heuristic(node, goal, speed=50)
       return travel_time(abs(goal - node), speed)
