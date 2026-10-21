guess = "beach"
ans = "teach"
def check_whats_missing(guess,ans):
    common = set(guess) & set(ans)
    print(sorted(list(common)))
    for x in common:
        print(x)


check_whats_missing(guess, ans)