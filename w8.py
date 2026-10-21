from collections import deque
tickets=deque()
def raise_tickets(t):
    tickets.append(t)
    print("Raised:",t)
def serve():
    if tickets:
        print("serving:",tickets.popleft())
    else:
        print("no tickets:")
raise_tickets("t1-login issue")
raise_tickets("t2-payment fail")
raise_tickets("t3-password reset")
serve()
serve()
print("waiting:",list(tickets))
