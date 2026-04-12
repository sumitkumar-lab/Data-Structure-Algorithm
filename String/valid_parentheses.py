def ValidParen(v: str) -> bool:
    pass



def make_counter(start=0):
    count = start           # 'count' is captured in the closure

    def increment(step=1):
        nonlocal count      # needed to modify enclosing variable
        count += step
        return count
