import csv


def rawData(filename):
    with open(filename, "r") as file:
        csvReader = csv.DictReader(file)
        data = list(csvReader)
    return data


def result(CSVfile, max, min, name):
    data = rawData(CSVfile)
    # print(data)

    result = ""
    count = float(data[0][max]) - float(data[0][min])

    for eachItem in data:
        difference = abs(float(eachItem[max]) - float(eachItem[min]))
        if difference <= count:
            count = difference
            result = eachItem[name]
            # print(count, result)
    return(result)


def main():
    weatherCSV = "/home/akhil118/Desktop/git/SOLID-project/weather.csv"
    footballCSV = "/home/akhil118/Desktop/git/SOLID-project/football.csv"

    smallestTemperatureSpread = result(weatherCSV, "Max", "Min", "Day")
    nameOfTheTeamWithTheSmallestDifference = result(footballCSV, "F", "A", "Team")

    print("The day number with the smallest temperature spread is day", smallestTemperatureSpread)
    print("Name of the team with the smallest difference is ", nameOfTheTeamWithTheSmallestDifference)


main()
