import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the probability using Bayes' theorem
def calculate_posterior_prob(sensitivity, specificity, prevalence):
    prevalence = prevalence / 100
    false_positive_rate = 1 - specificity
    P_positive = (sensitivity * prevalence) + (false_positive_rate * (1 - prevalence))
    P_infected_given_positive = (sensitivity * prevalence) / P_positive
    return P_infected_given_positive * 100

# Parameters
sens = 99 / 100
prevalence_range = np.linspace(0.001, 50, 500)  # from 0.001% to 50%
specificities = [99 / 100, 99.9 / 100, 99.99 / 100, 99.999 / 100]

# Plotting
plt.figure(figsize=(12, 8))

for spec in specificities:
    probabilities = [calculate_posterior_prob(sens, spec, prev) for prev in prevalence_range]
    plt.plot(prevalence_range, probabilities, label=f'Specificity = {spec * 100}%')

plt.xlabel('Infection Prevalence (%)')
plt.ylabel('Probability of Infection Given Positive Test (%)')
plt.title('Probability of Infection Given Positive Test as a Function of Prevalence and Specificity')
plt.legend()
plt.grid(True)
plt.show()