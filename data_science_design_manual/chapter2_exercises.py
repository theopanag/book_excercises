#### Exercise 2.1 ####

probs_dict = {'peanut_butter': 0.8,
              'jelly': 0.89,
              'both': 0.78}

# We need to calculate P(jelly | peanut_butter)
# We know that P(A|B) * P(B) = P(A intersection B)
# {if A and B are independent -> P(A|B) = P(A)

print(f"Answer to exercise 2.1 is {probs_dict['both'] / probs_dict['peanut_butter']}")


#### Exercise 2.2 ####

pr_A = 0.3
pr_B = 0.7
print("\nAnswer to exercise 2.2")
print("For question (a), no we cannot since we don't know if they're independent")

print(f"For question (b): \nP(A and B) = {pr_A*pr_B}")
print(f"P(A or B) = {pr_A + pr_B}")
print(f"P(A|B) = {pr_A * pr_B / pr_B}")
