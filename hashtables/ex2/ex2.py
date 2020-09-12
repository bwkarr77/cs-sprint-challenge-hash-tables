#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    route = []
    for each in tickets:
        source = each.source
        # if source = "NONE", then it's the start of the trip
        cache[source] = each.destination
    # starting/ending location = "NONE" (aka start/stop the trip)
    board = cache["NONE"]

    while board is not "NONE":
        # start with 'NONE', and append each trip afterwards
        route.append(board)
        # set the destination of the current flight to be the key of next flight
        board = cache[board]
        # the LAST flight will have 'NONE' as it's destination
    route.append(board)
    return route
