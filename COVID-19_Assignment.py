import pandas as pd
from matplotlib import pyplot as plt

#Data Loading

df = pd.read_csv('owid-covid-data.csv')

#Check columns: df.columns
print("Columns: ")
print(df.columns)

#Preview rows: df.head()
print("Preview of Rows: ")
print(df.head())

#Identify missing values: df.isnull().sum()
print("\n Number of null values: \n",df.isnull().sum())

# --Data Cleaning

#Countries of Interest South Africa

south_africa = df[df['location'] == 'South Africa']
botswana = df[df['location'] == 'Botswana']

df.dropna(inplace=True) #edit original data to remove null values

#Convert date

df['date'] = pd.to_datetime(df['date'], errors='coerce')

# --Exploratory Data Analysis

#Total cases for south africa

plt.plot(south_africa['date'], south_africa['total_cases'], label='Total Cases', color='blue')

plt.title('Total COVID-19 Cases Over Time in South Africa')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.tight_layout()
plt.show()

#Total Deaths for south africa

plt.plot(south_africa['date'], south_africa['total_deaths'], label='Total Deaths', color='red')

plt.title('Total COVID-19 Deaths Over Time in South Africa')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.tight_layout()
plt.show()

#Compare daily new cases between countries.

plt.plot(south_africa['date'], south_africa['new_cases'], label='South Africa', color='red')
plt.plot(botswana['date'], botswana['new_cases'], label='Botswana', color='blue')

plt.title('New COVID-19 Cases Between Botswana And South Africa Over Time')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.tight_layout()
plt.show()

#Calculate the death rate

total_deaths = south_africa['total_deaths'].iloc[-1]
total_cases = south_africa['total_cases'].iloc[-1]

death_rate = float(total_deaths) / float(total_cases)

print(f"\n The death rate of South Africa due to COVID-19 is: {death_rate * 100:.2f}%")

#Bar charts (top countries by total cases)

latest_data = df.sort_values('date').groupby('location').last().reset_index()

# Sort by total_cases
top_countries = latest_data.sort_values('total_cases', ascending=False).head(5)  # Show top 5

# Plot
plt.barh(top_countries['location'], top_countries['total_cases'], color='blue')
plt.xlabel('Total Cases')
plt.title('Top 5 Countries by Total COVID-19 Cases')
plt.gca().invert_yaxis()  # Highest at top
plt.tight_layout()
plt.show()

# --Visualizing Vaccination Progress

# Plot cumulative vaccinations over time
plt.plot(south_africa['date'], south_africa['total_vaccinations'], color='blue', label='Total Vaccinations')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.title('Cumulative COVID-19 Vaccinations in South Africa Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()

#Compare % vaccinated population.

# Calculate vaccination percentage
south_africa.loc[:, 'vaccination_percentage'] = (
    south_africa['people_vaccinated'] / south_africa['population']
) * 100

# Plot vaccination percentage over time
plt.plot(south_africa['date'], south_africa['vaccination_percentage'], color='blue', label='Vaccination Percentage')
plt.xlabel('Date')
plt.ylabel('Vaccination Percentage (%)')
plt.title('Vaccination Percentage Over Time in South Africa')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()
