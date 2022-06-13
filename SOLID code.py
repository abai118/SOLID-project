import csv


class DataExtractor():

    def rawData(filename):
        with open(filename, "r") as file:
            csvReader = csv.DictReader(file)
            data = list(csvReader)
        return data


class DataAnalyzer():

    def getResult(CSVfile, maximumCol, minimumCol, nameCol):
        data = DataExtractor.rawData(CSVfile)

        result = ""
        count = float(data[0][maximumCol]) - float(data[0][minimumCol])

        for eachItem in data:
            difference = abs(float(eachItem[maximumCol]) - float(eachItem[minimumCol]))
            if difference <= count:
                count = difference
                result = eachItem[nameCol]
                # print(count, result)
        return(result)


def main():
    weatherCSV = "/home/akhil118/Desktop/git/SOLID-project/weather.csv"
    footballCSV = "/home/akhil118/Desktop/git/SOLID-project/football.csv"

    smallestTemperatureSpread = DataAnalyzer.getResult(weatherCSV, "Max", "Min", "Day")
    nameOfTheTeamWithTheSmallestDifference = DataAnalyzer.getResult(footballCSV, "F", "A", "Team")

    print("The day number with the smallest temperature spread is day", smallestTemperatureSpread)
    print("Name of the team with the smallest difference is ", nameOfTheTeamWithTheSmallestDifference)


main()
