import pandas as pd
import matplotlib.pyplot as plt

Data = pd.DataFrame({
    "Name": ["Tehran", "Mashhad", "Isfahan", "Karaj", "Shiraz",
             "Tabriz", "Qom", "Ahvaz", "Kermanshah", "Urmia"],
    "longitude": [51.3347, 59.6168, 51.668, 50.9915, 52.5311,
                  46.2919, 50.8746, 48.6842, 47.065, 45.0725],
    "latitude": [35.7219, 36.2605, 32.6546, 35.84, 29.5918,
                 38.0962, 34.6416, 31.3183, 34.3142, 37.5527],
    "population": [8693706, 3001184, 1961260, 1592492, 1565572,
                   1558693, 1201158, 1184788, 946651, 736224]
})

Data.to_csv("data_cities.csv", index=False)

plt.scatter(Data["longitude"], Data["latitude"], marker="p")
plt.xlim(40,65)
plt.ylim(25,40)

plt.title("Map Of Iran")
plt.xlabel("longitude")
plt.ylabel("latitude")
plt.grid()
plt.show()