def calc_height_diff(n):
    if n==None:
        return 0
    return calc_height(n.left) - calc_height(n.right)
