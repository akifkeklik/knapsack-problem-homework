
# Knapsack Problem - Akif Keklik - 222803008
# Çözüm: Dinamik Programlama ve Greedy (value/weight oranı)

def knapsack_dp(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)
    item_taken = [0] * n

    for i in range(n):
        vi, wi = values[i], weights[i]
        for w in range(capacity, wi - 1, -1):
            if dp[w - wi] + vi > dp[w]:
                dp[w] = dp[w - wi] + vi

    w = capacity
    for i in reversed(range(n)):
        vi, wi = values[i], weights[i]
        if w >= wi and dp[w] == dp[w - wi] + vi:
            item_taken[i] = 1
            w -= wi

    return max(dp), item_taken

def knapsack_greedy_ratio(values, weights, capacity):
    n = len(values)
    items = list(range(n))
    ratio = [values[i] / weights[i] for i in range(n)]
    items.sort(key=lambda i: ratio[i], reverse=True)

    total_value = 0
    total_weight = 0
    selected_items = [0] * n

    for i in items:
        if total_weight + weights[i] <= capacity:
            selected_items[i] = 1
            total_value += values[i]
            total_weight += weights[i]

    return total_value, selected_items

# Örnek kullanım:
if __name__ == "__main__":
    # Küçük örnek veri (ks_40_0)
    values = [90001, 89751, 10002, 89501, 10254]
    weights = [90000, 89750, 10001, 89500, 10252]
    capacity = 100000

    optimal_value, selected = knapsack_dp(values, weights, capacity)
    print("DP - Optimal Value:", optimal_value)
    print("Selected Items (0/1):", selected)

    # Büyük örnek için greedy çalıştırılabilir
    # optimal_value, selected = knapsack_greedy_ratio(values, weights, capacity)
