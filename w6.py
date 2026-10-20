history=[]
def visit(page):
    history.append(page)
    print("visited:",page)
def back():
    if len(history)>1:
        history.pop()
        print("back to:",history[-1])
    else:
        print("no more history")
visit("google.com")
visit("wikipedia.org")
visit("github.com")
back()
back()
print("current page:",history[-1])