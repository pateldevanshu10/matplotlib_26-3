import matplotlib.pyplot as plt

labels = ["Approved", "Rejected"]
counts = [450, 50]
colors = ["blue", "red"]
 
plt.figure(figsize=(6,6))
plt.pie(counts, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)
plt.title("Visa Approval vs. Rejection Rate")
plt.show()

 