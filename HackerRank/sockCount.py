def sockMerchant(n, ar):
    # Pair the socks together
    store = {}
    for sock in ar:
        store[sock] = store.get(sock, 0) + 1

    # Filter out nonpairs
    pairs = 0
    for sock_type in store.keys():
        sock_count = store[sock_type]
        if sock_count % 2 >= 0:
            pairs += sock_count // 2

    return pairs


print(sockMerchant(
    9,
    [10, 20, 20, 10, 10, 30, 50, 10, 20],
))
