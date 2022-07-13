def check_log_in(u, p):
    filename = "test.txt"
    user = []
    with open(filename) as f:
        for line in f:
            user.append([str(n) for n in line.strip().split(",")])
    for pair in user:
        username, password = pair[0], pair[1]
        if u == username and p == password:
            return True
