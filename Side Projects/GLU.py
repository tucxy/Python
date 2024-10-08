import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Characteristic": [
        "Also employed outside of UMN",
        "Drawing on personal savings",
        "Receive support from family or partner",
        "Visa/residency status prevents from taking on extra work",
        "Only employed at UMN",
        "Other form of supplemental income"
    ],
    "Count": [347, 670, 664, 302, 564, 102],
    "Percentage": [18, 34, 35, 15, 30, 5.4]
}

df = pd.DataFrame(data)

# Pie chart without labels, legend on the side
plt.figure(figsize=(8, 8))
colors = plt.get_cmap('tab20').colors

plt.pie(df['Count'], colors=colors[:len(df)], startangle=90, autopct='%1.1f%%')
plt.title('Income Supplemented Sources')
plt.axis('equal')

# Add legend
plt.legend(df['Characteristic'], loc="center left", bbox_to_anchor=(0.5, 0.5))

# Show the chart
plt.show()
