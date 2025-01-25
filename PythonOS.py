from _collections_abc import Mapping

from datetime import datetime
import time
import os
import math
import copy
import matplotlib.pyplot as mat
import cohere
import mido
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry



co = cohere.Client('OtNd2ISeMuCKurDYOto25OalvrGZpRic57LBx0rR')






cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)
























class Graphing:
    def evaluation(function):
        return (eval(function))

    def transform(word, transform, to):
        wordmap = list(word)
        for i in range(0, len(word)):
            gotword = wordmap[i]
            wordmap.pop(i)
            wordmap.insert(i, str(gotword))
            if wordmap[i] == transform:
                wordmap.pop(i)
                wordmap.insert(i, to)

        return "".join(wordmap)

    def graph(function, domain, ranger):
        resultant = []
        for i in range(-ranger, ranger + 1):
            effectiveP = Graphing.transform(str(i), "-", "n")
            exec("y" + effectiveP + " = []")
        for i in range(-domain, domain + 1):
            newfunction = Graphing.transform(Graphing.transform(function, "^", "**"), "x", "(" + str(i) + ")")
            resultant.append(round(Graphing.evaluation(newfunction)))
            if resultant[i + domain] > ranger:
                for n in range(-ranger, ranger):
                    effectiveN = Graphing.transform(str(n), "-", "n")
                    exec("y" + str(effectiveN) + ".append(' ')")
                exec("y" + str(ranger) + ".append('↟')")
            elif resultant[i + domain] < -ranger:
                for n in range(-ranger + 1, ranger + 1):
                    effectiveN = Graphing.transform(str(n), "-", "n")
                    exec("y" + str(effectiveN) + ".append(' ')")
                exec("yn" + str(ranger) + ".append('↡')")
            else:
                exec("y" + Graphing.transform(str(round(Graphing.evaluation(newfunction))), "-", "n") + ".append('*')")
                for n in range(-ranger, ranger + 1):
                    effectiveI = Graphing.transform(str(n), "-", "n")
                    if round(Graphing.evaluation(newfunction)) != n:
                        exec("y" + str(effectiveI) + ".append(' ')")

        print(resultant)
        for i in range(-ranger, ranger + 1):
            exec("y" + Graphing.transform(str(0 - i), "-", "n") + ".append(str(-i))")
            exec("print('.'.join(y" + Graphing.transform(str(0 - i), "-", "n") + "))")
class Security:
    def passwordFromUser(username):
        index = users.index(username)
        return eval("passwords[" + str(index) + "]")

    def verify(username):
        correct = Security.passwordFromUser(username)
        guessing = True
        while guessing == True:
            guess = input("Please insert your password (Say !cancel to stop): ")
            if guess == "!cancel":
                print("Action disabled")
                time.sleep(1)
                return False
            elif guess == correct:
                print("Verification succesful")
                time.sleep(1)
                return True
            else:
                print("Password Incorrect")
            whitespace(2)

    def indiceFind(username):
        return users.index(username)

    def userToDisplay():
        global display_users
        display_users = []
        for a in range(0, len(users)):
            if users[a][-1] == "®":
                userstars = []
                userstars.append(users[a][0])
                for i in range(0, len(users[a])-2):
                    userstars.append("*")

                display_users.append("".join(userstars))

            else:
                display_users.append(users[a])


def navigation():
    global registered_locations
    global registered_latitude
    global registered_longitude
    chosen_location = input("Please insert the location you want to use: ")
    if chosen_location in registered_locations:
        print("Is this it?")
        whitespace(1)
        print(f'[{chosen_location}]')
        print(f'Laitude: {registered_latitude[registered_locations.index(chosen_location)]} N')
        print(f'Longitude: {registered_longitude[registered_locations.index(chosen_location)]} E')

        whitespace(2)
        locateconfirmation = input("If yes, type in 'Y': ")
        if locateconfirmation == 'Y':
            return [True, chosen_location, registered_longitude[registered_locations.index(chosen_location)], registered_latitude[registered_locations.index(chosen_location)]]
        else:
            print("Oh.. okay!")
            editconfirmation = input("If you want to update the settings, say '1': ")
            if editconfirmation == '1':
                whitespace(1)
                newlatitude = input("Please insert the new LATITUDE in NORTH: ")

                newlongitude = input("Please insert the new LONGITUDE in EAST: ")

                newlongitude, newlatitude = float(newlongitude), float(newlatitude)
                location_indice = registered_locations.index(chosen_location)
                longitude.pop(location_indice)
                longitude.insert(location_indice, newlongitude)
                latitude.insert(location_indice, newlatitude)
                whitespace(1)
                print("Edit complete! This attempt to fetch the location will not be recorded.")
            else:
                return [False]
    else:
        filtered_list = []
        filtered_longitude = []
        filtered_latitude = []


        for i in range(0,len(registered_locations)):
            if chosen_location in registered_locations[i]:
                filtered_list.append(registered_locations[i])
                filtered_latitude.append(registered_latitude[i])
                filtered_longitude.append(registered_longitude[i])

        print("Looks like your chosen location isn't registered...")
        print("Did you mean these?")
        whitespace(1)
        for t in range(0, len(filtered_list)):
            print(f'{filtered_list[t]} | Coordinates: ({filtered_latitude[t]} N, {filtered_longitude[t]} E)')
        whitespace(1)
        newconfirmation = input("If one of these you would want to choose, say 'Y'. Any other response will cause a new location to be registered: ")
        if newconfirmation == 'Y':
            chosen_location = input("Please insert the location you want PythonOS to use: ")
            if chosen_location in registered_locations:

                print("Is this it?")
                whitespace(1)
                print(f'[{chosen_location}]')
                print(f'Laitude: {registered_latitude[registered_locations.index(chosen_location)]} N')
                print(f'Longitude: {registered_longitude[registered_locations.index(chosen_location)]} E')

                whitespace(2)
                locateconfirmation = input("If yes, type in 'Y': ")
                if locateconfirmation == 'Y':
                    return [True, chosen_location, registered_longitude[registered_locations.index(chosen_location)], registered_latitude[registered_locations.index(chosen_location)]]
                else:
                    print("Oh.. okay!")
                    editconfirmation = input("If you want to update the settings, say '1': ")
                    if editconfirmation == '1':
                        whitespace(1)
                        newlatitude = input("Please insert the new LATITUDE in NORTH: ")
                        newlongitude = input("Please insert the new LONGITUDE in EAST: ")

                        newlongitude, newlatitude = int(newlongitude), int(newlatitude)
                        location_indice = registered_locations.index(chosen_location)
                        longitude.pop(location_indice)
                        longitude.insert(location_indice, newlongitude)
                        latitude.insert(location_indice, newlatitude)
                        whitespace(1)
                        print("Edit complete! This attempt to fetch the location will NOT be recorded.")
                    else:
                        return [False]
            else:
                print("Looks like that's also not a registered location...")
        else:
            create_longitude = input(f"Please input the new LONGITUDE in EAST of {chosen_location}: ")
            create_latitude = input(f"Please input the new LATITUDE in NORTH of {chosen_location}: ")
            create_longitude, create_latitude = float(create_longitude), float(create_latitude)
            registered_locations.append(chosen_location)
            registered_longitude.append(create_longitude)
            registered_latitude.append(create_latitude)
            whitespace(1)
            print("Your location has been registered, and this attempt of fetching the location HAS BEEN recorded.")
            return [True, chosen_location, create_longitude, create_latitude]

class Weather:
    def getCurrentWeather(lon, lat):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": ["temperature_2m", "relative_humidity_2m", "precipitation", "wind_speed_10m"]
        }
        responses = openmeteo.weather_api(url, params=params)

        # Process first location. Add a for-loop for multiple locations or weather models
        response = responses[0]
        return response
commandlist = ["!cmds | Lists every command", "!help | Gives brief description of commands",
                           "!users | Lists the users registered", "!listplot | Creates a list using the given data"
                , "!logout | Logs out the user", "!exit | Exits the OS entirely",
                           "!graph basic | Graphs a function with the Graphing class",
                           "!graph advanced | Uses matplotlib to plot functions",
                           "!files check | Shows the files in the first path of your user",
                           "!files manage | Manages files and the file explorer, also allows you to execute Q#",
                           "!ai | Allows you to chat with an AI (powered by Cohere)",
                           "!settings view | Allows you to view the settings",
                           "!settings change | Allows you to change the current settings",
                           "!weather | Allows you to view the weather of a region",
                        "!data save | Saves OS data", "!data load | Loads data to OS", "!data reset | Resets most data"]
class QSharp:
    def createCommand(title, description, execute):
        global commands
        global bonus_commands
        global bonus_executions
        global commandlist
        if title not in commands:
            bonus_commands.append(title)
            commands.append(title)
            commandlist.append(f"{title} | {description}")
            bonus_executions.append(execute)
        else:
            print("Command not added (already in command list!)")
    def deleteCommand(title):
        global commands
        global bonus_commands
        global bonus_executions
        global commandlist
        if title in bonus_commands:
            commands.remove(title)
            command_indice = bonus_commands.index(title)
            bonus_commands.remove(title)
            for i in range(0, len(commandlist)):
                if title in commandlist[i]:
                    commandlist.pop(i)
                    break
            bonus_executions.pop(command_indice)
        else:
            print(f"cannot remove command '{title}', as it is not a bonus command")

class Cypher:
    def qwerty(str, count):
        for f in range(0, count):
            alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
            keyboard = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
            string_map = []
            for char in str:
                if char in alphabet:
                    char_index = alphabet.index(char)
                    string_map.append(keyboard[char_index])
                else:
                    string_map.append(char)
            return "".join(string_map)
    def ceaser(str, movement, count):
        for f in range(0, count):
            alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

            string_map = []
            for char in str:
                if char in alphabet:
                    char_index = alphabet.index(char)
                    string_map.append(alphabet[(char_index + movement) % len(alphabet)])
                else:
                    string_map.append(char)
            return "".join(string_map)
    def flip(str):
        alphabet = list(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        reverse_alphabet = alphabet[::-1]

        string_map = []
        for char in str:
            if char in alphabet:
                char_index = alphabet.index(char)
                string_map.append(reverse_alphabet[char_index])
            else:
                string_map.append(char)
        return "".join(string_map)
    def reverseQwerty(str, count):
        for f in range(0, count):
            alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
            keyboard = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
            string_map = []
            for char in str:
                if char in keyboard:
                    char_index = keyboard.index(char)
                    string_map.append(alphabet[char_index])
                else:
                    string_map.append(char)
            return "".join(string_map)


    def encrypt(str):

        a = Cypher.qwerty(str, 2)

        b = Cypher.ceaser(a, 2, 1)

        c = Cypher.flip(b)

        d = Cypher.ceaser(c, (-1), 1)

        return d

    def decrypt(str):


        a = Cypher.ceaser(str, 1, 1)

        b = Cypher.flip(a)

        c = Cypher.ceaser(b, -2, 1)

        d = Cypher.reverseQwerty(c, 2)
        return d









print("Hong Kong" in "Hong Kong, Ting Kau")





print(Cypher.decrypt(Cypher.encrypt("hello! 123, abc's, [edit]")))
print("IF YOU STILL SEE THIS MESSAGE, FIX THE CODE.")

current_time = datetime.now()
formatted_time = int(current_time.strftime("%H"))
exact_time = int(current_time.strftime("%M"))
greeting = ""
if formatted_time < 12:
    greeting = "Morning"
if formatted_time >= 12 and formatted_time < 18:
    greeting = "Afternoon"
else:
    greeting = "Evening"




users = ["Administrator"]
passwords = ["1234"]
files = [[["Downloads"], [[["easy", "flipe", "File 1"], "Folder 2"], "Folder 1"], ["cool", "flipe", "File 2"]]]
display_location = ["0"]
longitude = [0]
latitude = [0]
display_users = ["Administrator"]
visibility = [True]
registered_locations = []
registered_longitude = []
registered_latitude = []
commands = ["!cmds", "!help", "!users", "!listplot", "!logout", "!exit", "!graph basic", "!graph advanced", "!files check", "!files manage", "!ai", "!settings view", "!settings change", "!weather", "!settings reset", "!QCode", "!run", "!data save", "!data load"]
bonus_commands = []
bonus_executions = []
stop = 0
ultastop = 0


user = "Administrator"


def listPlot(a, title):
    print("[||{{{{=============| " + title + "".join(list("]||{{{{=============| ")[::-1]))
    print("[========================]")
    for i in range(0, len(a)-1):
        print("| " + a[i])
        print("-----------------------")
    print("| " + a[-1])
    print("[========================]")

def whitespace(count):
    for i in range(0, count):
        print(" ")

def clear(intensity):
    whitespace(intensity * 25000)






clear(10)



while ultastop != 1:
    print(Cypher.qwerty("a", 2))
    listPlot(display_users, "List of users registered")
    whitespace(3)
    login = input("Good " + greeting + "! Please enter your username here to login/register: ")
    if login + "®" in users:
        login = login + "®"



    if not login in users:
        creation = True
        while creation == True:
            newpass = input("Since this is a new account, please give a password to your user (Say '!cancel' to cancel creation): ")
            if newpass != "!cancel":
                if len(newpass) >= 4:
                    users.append(login)
                    display_users.append(login)
                    files.append([["Downloads"], ["Folder 1"]])
                    passwords.append(newpass)
                    display_location.append("0")
                    longitude.append(0)
                    latitude.append(0)
                    visibility.append(True)
                    user = login
                    creation = False
                else:
                    print("Password not long enough, must be 4 characters long AT LEAST.")
            else:
                print("User creation cancelled")
                creation = False
    else:
        testpass = input("Please insert your password (the password for Administrator is 1234 | Say '!cancel' to cancel login.): ")
        if testpass == passwords[users.index(login)]:
            print("Password succesful")
            user = login
        elif testpass == '!cancel':
            print("Password cancelled")
        else:
            print("That is incorrect, please try again.")
            while testpass != passwords[users.index(login)]:
                testpass = input("Please insert your password (the password for Administrator is 1234 | Say '!cancel' to cancel login.): ")
                if testpass != passwords[user.index(login)]:
                    print("That is incorrect, please try again.")
                    time.sleep(0.2)
                    clear(1)
                elif testpass == "!cancel":
                    break

            print("Password succesful")
            user = login

    time.sleep(2)




    clear(4)

    print(user[-1] == "®")

    if user[-1] == "®":
        usermap = list(user)
        usermap.pop(-1)
        usereading = "".join(usermap)
        print("Welcome to PythonOS, " + usereading + "!")

    else:
        print("Welcome to PythonOS, " + user + "!")
    print("You can now run !cmds to get commands.")
    stop = 0
    while stop != 1:
        try:
            command = input(">_ ")

            if command == "!users":
                print("Here is a list of users registered: ")
                whitespace(1)
                listPlot(display_users, "Registered Users")
            if command == "!listplot":
                stoplisting = 0
                plist = []
                list_title = input("Add a title for your list (Input space if not wanted): ")
                while stoplisting != 1:

                    new_element = input("Add an element (say 'Stop' to finish): ")
                    if new_element != "Stop":
                        plist.append(new_element)
                    else:
                        stoplisting = 1
                listPlot(plist, list_title)
            if command == "!cmds":
                listPlot(commandlist, "Commands")
            if command == "!logout":
                print("Thank you for using PythonOS. See you later " + user + "!")
                time.sleep(2)
                clear(4)
                stop = 1
            if command == "!exit":
                print("Thank you for using PythonOS. We hope you enjoyed your time, all " + str(
                    len(users)) + " of yall. See you later!")
                time.sleep(2)

                stop = 1
                ultastop = 1
            if command == "!graph basic":
                function = input("Please input the function you want to graph (say Syntax for function formatting): ")
                if function == "Syntax":
                    print(
                        "Check the python math module. Most trigonometric functions have 'math.' behind them. Absolute values use abs(x). For other stuff, you should generally just check the math module.")
                    print(" Bonus tips: Remember to ALWAYS use the symbol '*' when multiplying, even with variables.")


                else:
                    try:
                        Graphing.graph(function, int(input("Please select a domain for the function: ")),
                                       int(input("Now select a range: ")))
                    except Exception as e:
                        print("YOU GOT AN ERROR!! " + str(e))

            if command == "!graph advanced":
                function = input("Please input the function (say Syntax for function formatting) : ")
                if function == "Syntax":
                    print(
                        "Check the python math module. Most trigonometric functions have 'math.' behind them. Absolute values use abs(x). For other stuff, you should generally just check the math module.")
                    print(" Bonus tips: Remember to ALWAYS use the symbol '*' when multiplying, even with variables.")
                else:
                    domain = input("Please input a domain: ")
                    precision = input(
                        "Please input a precision (like 1 or 0.5 | Precision is the x-axis plotting difference, or dx): ")
                    domain, precision = float(domain), float(precision)
                    x_plot = []
                    y_plot = []
                    try:
                        for p in range(math.floor(-domain / precision), math.floor((domain / precision) + float(1))):
                            x_plot.append(float(p) * precision)
                            y_plot.append(Graphing.evaluation(
                                Graphing.transform(
                                    Graphing.transform(function, "x", "(" + str(float(p) * precision) + ")"),
                                    "^", "**")))
                        mat.plot(x_plot, y_plot)
                        mat.show()
                    except Exception as e:
                        print("ERROR!!!!!!! " + str(e))

            if command == "!weather":
                current_location = input("Would you like to view the weather of your logged location (Yes/No)? ")
                if "Y" in current_location:
                    wsi = Security.indiceFind(user)
                    current = Weather.getCurrentWeather(longitude[wsi], latitude[wsi]).Current()
                    current_temperature_2m = current.Variables(0).Value()
                    relative_humidity_2m = current.Variables(1).Value()
                    precipitation = current.Variables(2).Value()
                    wind = current.Variables(3).Value()
                    print("https://open-meteo.com  |  Weather data by Open-Meteo.com")

                    print(f"<[ Welcome to {display_location[wsi]}! ]>")
                    whitespace(1)
                    temperature_description = ""
                    humidity_description = ""
                    precipitation_description = ""
                    wind_description = ""
                    if current_temperature_2m < -30:
                        temperature_description = "Take shelter immediately!"
                    elif current_temperature_2m < -10:
                        temperature_description = "Chance of frostbite so be careful!"
                    elif current_temperature_2m < 0:
                        temperature_description = "It's freezing cold!"
                    elif current_temperature_2m < 6:
                        temperature_description = "Better wear a few jackets!"
                    elif current_temperature_2m < 15:
                        temperature_description = "A bit chilly, eh?"
                    elif current_temperature_2m < 21:
                        temperature_description = "Best for a quick jog!"
                    elif current_temperature_2m < 27:
                        temperatue_description = "It's gettin' a bit warm over here!"
                    elif current_temperature_2m < 34:
                        temperature_description = "Make sure to hydrate, you don't wanna look like Jimmy over there..."
                    elif current_temperature_2m < 37:
                        temperature_description = "You need cooling ASAP!"
                    else:
                        temperature_description = "TAKE SHELTER, NOW!"

                    if relative_humidity_2m < 20:
                        humidity_description = "Be careful with sparks! You're in dry territory, my friend."
                    elif relative_humidity_2m < 40:
                        humidity_description = "It's a bit dry, maybe look out for scratches."
                    elif relative_humidity_2m < 60:
                        humidity_description = "Drink a bit more water, it's starting to get dry."
                    elif relative_humidity_2m < 80:
                        humidity_description = "Not too dry, not too moist."
                    else:
                        humidity_description = "You might want to take off that sweater.."

                    if precipitation < 0.5:
                        precipitation_description = "No rain today!"
                    elif precipitation < 2.5:
                        precipitation_description = "A slight drizzle, a raincoat should do the trick."
                    elif precipitation < 7.6:
                        precipitation_description = "The rain is starting to ramp up, get your umbrellas!"
                    elif precipitation < 15:
                        precipitation_description = "There's a rainstorm forming..."
                    else:
                        precipitation_description = "BRO FIND SHELTER"

                    if wind < 12:
                        wind_description = "Not much wind today!"
                    elif wind < 30:
                        wind_description = "Quite swindy over here!"
                    elif wind < 51:
                        wind_description = "The wind's starting to ramp up.. Consider checking for hurricanes or monsoons."
                    elif wind < 87:
                        wind_description = "GALE WIND! GALE WIND ALERT! TAKE SHELTER!"
                    elif wind < 117:
                        wind_description = "STORM WIND! STORM WIND ALERT! TAKE SHELTER!"
                    else:
                        wind_description = "HURRICANE LEVEL WINS ARE INBOUND, FIND SHELTER NOW!"

                    print("Here's today's report:")
                    whitespace(1)

                    print(f"The temperature is {str(round(current_temperature_2m))}C. {temperature_description}")
                    print(f"The relative humidity is {str(round(relative_humidity_2m))}%. {humidity_description}")
                    print(f"The rainfall is {str(round(precipitation))}mm. {precipitation_description}")
                    print(f"The wind is {str(round(wind))}km/h. {wind_description}")
                else:
                    fetch_attempt = navigation()
                    if fetch_attempt[0]:
                        current = Weather.getCurrentWeather(fetch_attempt[2], fetch_attempt[3]).Current()
                        current_temperature_2m = current.Variables(0).Value()
                        relative_humidity_2m = current.Variables(1).Value()
                        precipitation = current.Variables(2).Value()
                        wind = current.Variables(3).Value()
                        print("https://open-meteo.com  |  Weather data by Open-Meteo.com")

                        print(f"<[ Welcome to {fetch_attempt[1]}! ]>")
                        whitespace(1)
                        temperature_description = ""
                        humidity_description = ""
                        precipitation_description = ""
                        wind_description = ""
                        if current_temperature_2m < -30:
                            temperature_description = "Take shelter immediately!"
                        elif current_temperature_2m < -10:
                            temperature_description = "Chance of frostbite so be careful!"
                        elif current_temperature_2m < 0:
                            temperature_description = "It's freezing cold!"
                        elif current_temperature_2m < 6:
                            temperature_description = "Better wear a few jackets!"
                        elif current_temperature_2m < 15:
                            temperature_description = "A bit chilly, eh?"
                        elif current_temperature_2m < 21:
                            temperature_description = "Best for a quick jog!"
                        elif current_temperature_2m < 27:
                            temperatue_description = "It's gettin' a bit warm over here!"
                        elif current_temperature_2m < 34:
                            temperature_description = "Make sure to hydrate, you don't wanna look like Jimmy over there..."
                        elif current_temperature_2m < 37:
                            temperature_description = "You need cooling ASAP!"
                        else:
                            temperature_description = "TAKE SHELTER, NOW!"

                        if relative_humidity_2m < 20:
                            humidity_description = "Be careful with sparks! You're in dry territory, my friend."
                        elif relative_humidity_2m < 40:
                            humidity_description = "It's a bit dry, maybe look out for scratches."
                        elif relative_humidity_2m < 60:
                            humidity_description = "Drink a bit more water, it's starting to get dry."
                        elif relative_humidity_2m < 80:
                            humidity_description = "Not too dry, not too moist."
                        else:
                            humidity_description = "You might want to take off that sweater.."

                        if precipitation < 0.5:
                            precipitation_description = "No rain today!"
                        elif precipitation < 2.5:
                            precipitation_description = "A slight drizzle, a raincoat should do the trick."
                        elif precipitation < 7.6:
                            precipitation_description = "The rain is starting to ramp up, get your umbrellas!"
                        elif precipitation < 15:
                            precipitation_description = "There's a rainstorm forming..."
                        else:
                            precipitation_description = "BRO FIND SHELTER"

                        if wind < 12:
                            wind_description = "Not much wind today!"
                        elif wind < 30:
                            wind_description = "Quite swindy over here!"
                        elif wind < 51:
                            wind_description = "The wind's starting to ramp up.. Consider checking for hurricanes or monsoons."
                        elif wind < 87:
                            wind_description = "GALE WIND! GALE WIND ALERT! TAKE SHELTER!"
                        elif wind < 117:
                            wind_description = "STORM WIND! STORM WIND ALERT! TAKE SHELTER!"
                        else:
                            wind_description = "HURRICANE LEVEL WINS ARE INBOUND, FIND SHELTER NOW!"

                        print("Here's today's report:")
                        whitespace(1)

                        print(f"The temperature is {str(round(current_temperature_2m))}C. {temperature_description}")
                        print(f"The relative humidity is {str(round(relative_humidity_2m))}%. {humidity_description}")
                        print(f"The rainfall is {str(round(precipitation))}mm. {precipitation_description}")
                        print(f"The wind is {str(round(wind))}km/h. {wind_description}")



            if command == "!setup":
                print("Tutorial Guy: Welcome to PythonOS!")
                time.sleep(2.5)
                print("Tutorial Guy: I'm gonna show you around!")
                time.sleep(2.5)
                print("Tutorial Guy: First off, let me introduce you to THE COMMAND SYSTEM! Here, try saying '!cmds'.")
                time.sleep(3.5)
                setup_challenge_one = 0
                while setup_challenge_one != '!cmds':
                    setup_challenge_one = input(">_ ")
                    if setup_challenge_one != '!cmds':
                        print("Tutorial Guy: Not quite, try again!")
                listPlot(commandlist, "Commands")
                time.sleep(2.5)
                print(
                    "Tutorial Guy: See? You just ran a COMMAND! Commands do certain stuff, this command shows you all the commands here!")
                time.sleep(2.5)
                print("Tutorial Guy: I think you're starting to get the hang of this!")
                time.sleep(2.5)
                print(
                    "Tutorial Guy: Now, let me introduce you to the FILE EXPLORER! It's not an operating system without some files!")
                time.sleep(2.5)
                print("Tutorial Guy: Try saying '!files check'!")
                time.sleep(3.5)
                setup_challenge_two = 0
                while setup_challenge_two != '!files check':
                    setup_challenge_two = input(">_ ")
                    if setup_challenge_two != '!files check':
                        print("Tutorial Guy: Not quite, try again!")

                print("Here are your files: ")
                whitespace(1)
                user_index = users.index(user)
                file_names = []
                for i in range(0, len(files[user_index])):
                    if len(files[user_index][i]) >= 2:
                        if files[user_index][i][-2] == "flipe":
                            file_names.append(files[user_index][i][-1] + " (File | Index " + str(i + 1) + ")")
                        else:
                            file_names.append(files[user_index][i][-1] + " (Folder | Index " + str(i + 1) + ")")
                    else:

                        file_names.append(files[user_index][i][-1] + " (File | Index " + str(i + 1) + ")")

                print("   <{}><{}><{}>   ".join(file_names))
                print("Tutorial Guy: Look at that! Those are your files!")
                time.sleep(2.5)
                print(
                    "Tutorial Guy: You know, you could actually see even more if you try '!files manage', but that's for YOU to check out!")
                time.sleep(2.5)
                print("Tutorial Guy: In the mean time, try checking your settings! Say '!settings view'.")
                time.sleep(3.5)
                setup_challenge_three = 0
                while setup_challenge_three != '!settings view':
                    setup_challenge_three = input(">_ ")
                    if setup_challenge_three != '!settings view':
                        print("Tutorial Guy: Not quite, try again!")

                stars = []
                for s in range(0, len(passwords[users.index(user)]) - 1):
                    stars.append("*")
                stars = "".join(stars)
                if user[-1] == "®":

                    userwordmap = list(user)
                    userwordmap.pop(-1)
                    newuserword = "".join(userwordmap)
                    listPlot(
                        ["Username / " + str(newuserword), "Password / " + (passwords[users.index(user)])[0] + stars,
                         "Location / " + display_location[users.index(user)],
                         "Visibility / " + str(visibility[users.index(user)])], "Settings")
                else:
                    listPlot(["Username / " + str(user), "Password / " + (passwords[users.index(user)])[0] + stars,
                              "Location / " + display_location[users.index(user)],
                              "Visibility / " + str(visibility[users.index(user)])], "Settings")

                print("Tutorial Guy: Now, THOSE are your SETTINGS!")
                time.sleep(2.5)
                print("Tutorial Guy: But don't you think something's off?")
                time.sleep(2.5)
                print("Tutorial Guy: Why does the 'location' say '0'?")
                time.sleep(2.5)
                print("Tutorial Guy: Let's go ahead and change that!")
                time.sleep(2.5)
                print("Tutorial Guy: Try saying '!settings change' to change your settings!")
                time.sleep(3.5)
                setup_challenge_final = 0
                while setup_challenge_final != '!settings change':
                    setup_challenge_final = input(">_ ")
                    if setup_challenge_final != '!settings change':
                        print("Tutorial Guy: Not quite, try again!")
                stars = []
                for s in range(0, len(passwords[users.index(user)]) - 1):
                    stars.append("*")
                stars = "".join(stars)
                if user[-1] == "®":

                    userwordmap = list(user)
                    userwordmap.pop(-1)
                    newuserword = "".join(userwordmap)
                    listPlot(
                        ["Username / " + str(newuserword), "Password / " + (passwords[users.index(user)])[0] + stars,
                         "Location / " + display_location[users.index(user)],
                         "Visibility / " + str(visibility[users.index(user)])], "Settings")
                else:
                    listPlot(["Username / " + str(user), "Password / " + (passwords[users.index(user)])[0] + stars,
                              "Location / " + display_location[users.index(user)],
                              "Visibility / " + str(visibility[users.index(user)])], "Settings")
                whitespace(1)
                print("Tutorial Guy: Look at that! Now, we're trying to change Location, so let's say 'Location'!")
                change_selection = input("Please select a setting to change: ")
                setup_complete = False
                while change_selection != 'Location' or setup_complete == False:
                    change_selection = input("Please select a setting to change: ")
                    if change_selection == "Username":
                        print("Not Quite!")
                    elif change_selection == "Password":
                        print("Not Quite!")
                    elif change_selection == "Location":
                        if Security.verify(user):
                            navigation_verification = navigation()
                            if navigation_verification[0]:
                                location_user_indice = Security.indiceFind(user)
                                display_location.pop(location_user_indice)
                                longitude.pop(location_user_indice)
                                latitude.pop(location_user_indice)
                                display_location.insert(location_user_indice, navigation_verification[1])
                                longitude.insert(location_user_indice, navigation_verification[2])
                                latitude.insert(location_user_indice, navigation_verification[3])
                                setup_complete = True
                    elif change_selection == "Visibility":
                        print("Not Quite!")
                    else:
                        print("Not Quite!")
                print(
                    "Tutorial Guy: Alright, I think you're ready to explore the great wonders of PythonOS! Hope you enjoy your stay, :D")

            for g in range(0, len(bonus_commands)):
                if command == bonus_commands[g]:
                    exec(bonus_executions[g])


            if command == "!settings view":

                stars = []
                for s in range(0, len(passwords[users.index(user)]) - 1):
                    stars.append("*")
                stars = "".join(stars)
                if user[-1] == "®":

                    userwordmap = list(user)
                    userwordmap.pop(-1)
                    newuserword = "".join(userwordmap)
                    listPlot(
                        ["Username / " + str(newuserword), "Password / " + (passwords[users.index(user)])[0] + stars,
                         "Location / " + display_location[users.index(user)],
                         "Visibility / " + str(visibility[users.index(user)])], "Settings")
                else:
                    listPlot(["Username / " + str(user), "Password / " + (passwords[users.index(user)])[0] + stars,
                              "Location / " + display_location[users.index(user)],
                              "Visibility / " + str(visibility[users.index(user)])], "Settings")

            if command == "!settings change":
                stars = []
                for s in range(0, len(passwords[users.index(user)]) - 1):
                    stars.append("*")
                stars = "".join(stars)
                if user[-1] == "®":

                    userwordmap = list(user)
                    userwordmap.pop(-1)
                    newuserword = "".join(userwordmap)
                    listPlot(
                        ["Username / " + str(newuserword), "Password / " + (passwords[users.index(user)])[0] + stars,
                         "Location / " + display_location[users.index(user)],
                         "Visibility / " + str(visibility[users.index(user)])], "Settings")
                else:
                    listPlot(["Username / " + str(user), "Password / " + (passwords[users.index(user)])[0] + stars,
                              "Location / " + display_location[users.index(user)],
                              "Visibility / " + str(visibility[users.index(user)])], "Settings")
                whitespace(1)
                change_selection = input("Please select a setting to change: ")
                if change_selection == "Username":
                    if user == "Administrator":
                        print("Sorry, but you cannot change the Username of Administrator..")
                    else:
                        if Security.verify(user) == True:
                            coolnewusername = input("Please insert your NEW username: ")
                            if coolnewusername in users:
                                print("Sorry, but somebody else is already using this name..")
                            else:
                                cooluserindex = Security.indiceFind(user)
                                users.remove(user)
                                user = coolnewusername
                                users.insert(cooluserindex, user)
                                Security.userToDisplay()
                                whitespace(1)
                                print("Username Changed.")
                elif change_selection == "Password":
                    if user == "Administrator":
                        print("Sorry, but you cannot change the Password of Administrator..")
                    else:
                        if Security.verify(user) == True:
                            coolnewpass = input("Please insert your NEW password: ")
                            if len(coolnewpass) < 4:
                                print("Sorry, but your password must have at least 4 characters.")
                            else:
                                newindice = Security.indiceFind(user)
                                passwords.pop(newindice)
                                passwords.insert(newindice, coolnewpass)
                                whitespace(1)
                                print("Password Changed.")
                elif change_selection == "Location":
                    if Security.verify(user):
                        navigation_verification = navigation()
                        if navigation_verification[0]:
                            location_user_indice = Security.indiceFind(user)
                            display_location.pop(location_user_indice)
                            longitude.pop(location_user_indice)
                            latitude.pop(location_user_indice)
                            display_location.insert(location_user_indice, navigation_verification[1])
                            longitude.insert(location_user_indice, navigation_verification[2])
                            latitude.insert(location_user_indice, navigation_verification[3])
                elif change_selection == "Visibility":
                    if user == "Administrator":
                        print("Sorry, but you cannot change the Visibility of Administator.")
                    else:
                        if Security.verify(user):
                            newboolean = input("Please insert the new Visiblity (Y/N): ")
                            visibility_user_indice = Security.indiceFind(user)
                            if newboolean == "Y":
                                if visibility[visibility_user_indice] == True:
                                    print("Umm... Your visibility is already set to True!")
                                else:
                                    visibility.pop(visibility_user_indice)
                                    visibility.insert(visibility_user_indice, True)
                                    users.pop(visibility_user_indice)
                                    visibility_user_map = list(user)
                                    visibility_user_map.pop(-1)
                                    effectiveUser = "".join(visibility_user_map)
                                    user = effectiveUser
                                    users.insert(visibility_user_indice, effectiveUser)
                        elif newboolean == "N":
                            if visibility[visibility_user_indice] == False:
                                print("Umm... Your visibility is already set to False!")
                            else:
                                visibility.pop(visibility_user_indice)
                                visibility.insert(visibility_user_indice, False)
                                users.pop(visibility_user_indice)
                                visibility_user_map = list(user)
                                visibility_user_map.append("®")
                                effectiveUser = "".join(visibility_user_map)
                                user = effectiveUser
                                users.insert(visibility_user_indice, effectiveUser)
                        else:
                            print("wha?")
                        Security.userToDisplay()
                else:
                    print("what.")
            if command == "!settings reset":
                if Security.verify(user):
                    if visibility[visibility_user_indice] == True:
                        print("Visibility has not been changed (Already default)")
                    else:
                        visibility.pop(visibility_user_indice)
                        visibility.insert(visibility_user_indice, True)
                        users.pop(visibility_user_indice)
                        visibility_user_map = list(user)
                        visibility_user_map.pop(-1)
                        effectiveUser = "".join(visibility_user_map)
                        user = effectiveUser
                        users.insert(visibility_user_indice, effectiveUser)

                    location_user_indice = Security.indiceFind(user)
                    display_location.pop(location_user_indice)
                    longitude.pop(location_user_indice)
                    latitude.pop(location_user_indice)
                    display_location.insert(location_user_indice, "NaN")
                    longitude.insert(location_user_indice, 0)
                    latitude.insert(location_user_indice, 0)

            if command == "!QCode":
                print("Welcome to Q#! It's Python but with integrations to the OS, allowing you to create applications")
                whitespace(1)
                print("Coding Space: (Use the symbol '~' to indent)")
                print("'Finish' to stop coding | 'Edit' to edit a line of your code.")
                coding = True
                line = 1
                return_code = []
                type_code = []
                while coding == True:
                    codeLine = input(f"Line {line} | >_ ")
                    originalLine = codeLine
                    if codeLine == "Finish":
                        coding = False
                    elif codeLine == "Edit":
                        edit_line = input("# Which line do you want to edit? ")
                        edit_to = input("# What do you want it to be now? ")
                        return_code.pop(int(edit_line)-1)
                        type_code.pop(int(edit_line)-1)
                        return_code.insert(int(edit_line)-1, edit_to)
                        type_code.insert(int(edit_line)-1, edit_to)
                        clear(1)
                        for i in range(0, len(return_code)):
                            print(
                                "Welcome to Q#! It's Python but with integrations to the OS, allowing you to create applications")
                            whitespace(1)
                            print("Coding Space: (Use the symbol '~' to indent)")
                            print("# 'Finish' to stop coding | 'Edit' to edit a line of your code.")
                            print(f"Line {i+1} | >_ {return_code[i]}")

                    else:
                        codeLine = Graphing.transform(codeLine, "~", "    ")
                        return_code.append(codeLine)
                        type_code.append(originalLine)
                        line += 1

                whitespace(2)
                print("Now analyzing security...")
                concerning = False
                if "passwords" in "\n".join(return_code) or "passwords" in "\n".join(return_code) or "users" in "\n".join(return_code) or "files" in "\n".join(return_code) or "locations" in "\n".join(return_code) or "display_location" in "\n".join(return_code) or "longitude" in "\n".join(return_code) or "latitude" in "\n".join(return_code) or "registered_locations" in "\n".join(return_code) or "registered_longitude" in "\n".join(return_code) or "registered_latitude" in "\n".join(return_code):
                    concerning = True
                response = co.generate(
                    model='command-r-plus',  # Choose the model (e.g., 'xlarge', 'medium', etc.)
                    prompt=f"User: Check if the following code is trying to use the Class 'Cypher' or 'Security', use encryption/decryption techniques, or fetch/change data in the lists: 'passwords', 'users', 'files', 'locations', 'display_location', 'longitude', 'latitude', 'display_users', 'registered_locations', 'registered_longitude', or 'registered_latitude'. If it does, respond with ONLY 'Y', if not, respond with ONLY 'N'. Here is the code: {'\n'.join(return_code)}. Code concerning: {concerning}. AI Assistant: ",
                    max_tokens=10
                )
                print(response.generations[0].text)
                if "Y" in response.generations[0].text or concerning == True:
                    print("Your code has been blocked, since it has security concerns.")
                else:
                    print("Your code has been deemed safe!")
                    whitespace(1)
                    print("Output:")
                    exec("\n".join(return_code))
                    whitespace(1)
                    print(f"Q# File Format: {"@".join(type_code)}")






            if command == "!files check":
                print("Here are your files: ")
                whitespace(1)
                user_index = users.index(user)
                file_names = []
                for i in range(0, len(files[user_index])):
                    if len(files[user_index][i]) >= 2:
                        if files[user_index][i][-2] == "flipe":
                            file_names.append(files[user_index][i][-1] + " (File | Index " + str(i + 1) + ")")
                        else:
                            file_names.append(files[user_index][i][-1] + " (Folder | Index " + str(i + 1) + ")")
                    else:

                        file_names.append(files[user_index][i][-1] + " (File | Index " + str(i + 1) + ")")

                print("   <{}><{}><{}>   ".join(file_names))

            if command == "!ai":
                print("Powered by Cohere")
                whitespace(2)
                print("Say 'Continue' to continue Cohere's response. | Say 'Finish' to stop the chat.")
                whitespace(3)
                chat = True
                logs = []
                while chat == True:
                    userinput = input("User: ")
                    if userinput != "Continue":
                        logs.append("User: " + userinput)
                    if userinput == "Finish":
                        chat = False

                    response = co.generate(
                        model='command-r-plus',  # Choose the model (e.g., 'xlarge', 'medium', etc.)
                        prompt="   |   ".join(logs) + " | AI Assistant: ",
                        max_tokens=50
                    )
                    print("AI Assistant: " + Graphing.transform(response.generations[0].text, "@", "\n"))
                    logs.append("AI Assistant: " + Graphing.transform(response.generations[0].text, "@", "\n"))

            if command == "!midi":
                selected_file = input("Please input the computer path to the MIDI file: ")
                if not os.path.isfile(selected_file):
                    print("Yo that ain't a file!")

                else:
                    with open(selected_file, 'r') as file:
                        content = file.read()
                        print("aight here you go:")
                        print(str(content))

            if command == "!data save":
                print("Here is the data:")
                whitespace(1)
                print("Users: " + Cypher.encrypt(str(users)))
                print("Passwords: " + Cypher.encrypt(str(passwords)))
                print("Files: " + Cypher.encrypt(str(files))
                      )
                print("Registered Locations: " + Cypher.encrypt(str(registered_locations)))
                print("Registered LONGITUDE (E): " + Cypher.encrypt(str(registered_longitude)))
                print("Registered LATITUDE (N): " + Cypher.encrypt(str(registered_latitude)))
            if command == "!data load":
                if Security.verify(user):
                    print(
                        "Check your encryptions to load everything up. Say 'Skip' if you don't want to load a specific part of data.")
                    whitespace(1)
                    selection1 = input("Load Users: ")
                    if selection1 == 'Skip':
                        print("Users not loaded.")
                    else:
                        users = eval(Cypher.decrypt(selection1))

                    selection2 = input("Load Passwords: ")
                    if selection2 == 'Skip':
                        print("Passwords not loaded.")
                    else:
                        print(passwords)
                        passwords = eval(Cypher.decrypt(selection2))
                        print(passwords)
                        print(passwords[Security.indiceFind(user)])

                    selection3 = input("Load Files: ")
                    if selection3 == 'Skip':
                        print("Files not loaded.")
                    else:
                        files = eval(Cypher.decrypt(selection3))

                    selection4 = input("Load Registered Locations: ")
                    if selection4 == 'Skip':
                        print("Locations not loaded.")
                    else:
                        registered_locations = eval(Cypher.decrypt(selection4))
                    selection5 = input("Load Registered Longitude: ")
                    if selection5 == 'Skip':
                        print("Longitude not loaded.")
                    else:
                        registered_longitude = eval(Cypher.decrypt(selection5))
                    selection6 = input("Load Registered Latitude: ")
                    if selection6 == 'Skip':
                        print("Latitude not loaded.")
                    else:
                        registered_latitude = eval(Cypher.decrypt(selection6))


            if command == "!data reset":
                if Security.verify(user):
                    users = ["Administrator"]
                    passwords = ["1234"]
                    files = [[["Downloads"]]]
                    registered_locations = ["0"]
                    registered_longitude = [0]
                    registered_latitude = [0]
                    whitespace(1)
                    print("Process finished.")

            if command == "!files manage":
                print("step")
                execute_path = [str(users.index(user))]
                print("step")
                openstop = False
                print("step")
                user_index = users.index(user)
                print("step")
                open_path = copy.deepcopy(files[user_index])
                print("step")
                print(
                    "Please select a folder/file to open (Select an index | Say 'Reset' to reset path | Say 'Stop' to stop the process): ")
                print("Additionally, say 'Add' to add files, 'Remove' to remove files, or 'Execute' to run Q# files")
                print("Here are your files: ")
                whitespace(1)
                user_index = users.index(user)
                file_names = []
                for i in range(0, len(open_path)):
                    if len(open_path[i]) >= 2:
                        if open_path[i][-2] == "flipe":
                            file_names.append(open_path[i][-1] + " (File | Index " + str(i + 1) + ")")
                        else:
                            file_names.append(open_path[i][-1] + " (Folder | Index " + str(i + 1) + ")")
                    else:

                        file_names.append(open_path[i][-1] + " (Folder | Index " + str(i + 1) + ")")

                print("   <{}><{}><{}>   ".join(file_names))
                while openstop == False:
                    verycooluserindice = Security.indiceFind(user)

                    whitespace(1)
                    opening = input(">: ")
                    try:
                        if opening == "Reset":
                            execute_path = [str(users.index(user))]

                            open_path = copy.deepcopy(files[user_index])
                            file_names = []
                            for i in range(0, len(open_path)):
                                if len(open_path[i]) >= 2:
                                    if open_path[i][-2] == "flipe":
                                        file_names.append(open_path[i][-1] + " (File | Index " + str(i + 1) + ")")
                                    else:
                                        file_names.append(open_path[i][-1] + " (Folder | Index " + str(i + 1) + ")")
                                else:

                                    file_names.append(open_path[i][-1] + " (Folder | Index " + str(i + 1) + ")")
                            whitespace(2)

                            print("   <{}><{}><{}>   ".join(file_names))
                        elif opening == "Stop":
                            openstop = True
                        elif opening == "Add":
                            add_location = input(
                                "Please input the folder you want to add your file to (Use Main PC for base menu): ")
                            if add_location == "Main PC":
                                ff = input("File or Folder?")
                                if ff == "File":

                                    files[verycooluserindice].append(
                                        [Graphing.transform(Graphing.transform(input("Please select what you want in your file (@ for new line, ~ for indent): "), "@", "\n"), "~", "    "), "flipe",
                                         input("Please select a name for your file: ")])
                                if ff == "Folder":
                                    files[verycooluserindice].append([input("Please select a name for your folder: ")])
                            else:

                                add_path = copy.deepcopy(files[verycooluserindice])
                                print(
                                    "Please select a folder to open (Select an index | Say 'Finish' to lock in the folder | Say 'Cancel' to cancel manual adding): ")

                                print("Here are your files: ")
                                whitespace(1)
                                user_index = users.index(user)
                                file_names = []
                                for i in range(0, len(add_path)):
                                    if len(add_path[i]) >= 2:
                                        if add_path[i][-2] == "flipe":
                                            file_names.append(
                                                add_path[i][-1] + " (File | Index " + str(
                                                    i + 1) + ")")
                                        else:
                                            file_names.append(
                                                add_path[i][-1] + " (Folder | Index " + str(
                                                    i + 1) + ")")
                                    else:

                                        file_names.append(
                                            add_path[i][-1] + " (Folder | Index " + str(
                                                i + 1) + ")")
                                manual_add_stop = False
                                real_add_path = [str(verycooluserindice)]
                                steps = 0
                                print("   <{}><{}><{}>   ".join(file_names))
                                while manual_add_stop == False:
                                    add_opening = input(">+ ")

                                    steps += 1

                                    if add_opening != "Finish":
                                        real_add_path.append(str(int(add_opening) - 1))
                                        add_path = copy.deepcopy(
                                            add_path[int(int(add_opening) - 1)])
                                        add_path.pop(-1)
                                        tempfold = False
                                        if len(add_path) >= 2:
                                            if add_path[-1] == "flipe":
                                                add_path.pop(-1)
                                                tempfold = True

                                        file_names = []
                                        if len(add_path) == 1:
                                            if tempfold == True:
                                                print(
                                                    "It's a text file! It reads... SIKE! You're in ADD mode, you ain't ADDING a file to a file!")
                                                print(
                                                    "Your file path has now been reset to the Main PC path.")
                                                whitespace(1)
                                                add_path = copy.deepcopy(
                                                    files[verycooluserindice])
                                            else:
                                                for i in range(0, len(add_path)):
                                                    if len(add_path[i]) >= 2:
                                                        if add_path[i][-2] == "flipe":
                                                            file_names.append(add_path[i][
                                                                                  -1] + " (File | Index " + str(
                                                                i + 1) + ")")
                                                        else:
                                                            file_names.append(add_path[i][
                                                                                  -1] + " (Folder | Index " + str(
                                                                i + 1) + ")")
                                                    else:

                                                        file_names.append(add_path[i][
                                                                              -1] + " (Folder | Index " + str(
                                                            i + 1) + ")")
                                        else:
                                            for i in range(0, len(add_path)):
                                                if len(add_path[i]) >= 2:
                                                    if add_path[i][-2] == "flipe":
                                                        file_names.append(add_path[i][
                                                                              -1] + " (File | Index " + str(
                                                            i + 1) + ")")
                                                    else:
                                                        file_names.append(add_path[i][
                                                                              -1] + " (Folder | Index " + str(
                                                            i + 1) + ")")
                                                else:

                                                    file_names.append(add_path[i][
                                                                          -1] + " (Folder | Index " + str(
                                                        i + 1) + ")")

                                        print("   <{}><{}><{}>   ".join(file_names))

                                        if len(add_path) == 0:
                                            print(
                                                "There's... nothing in this folder/file....")
                                    elif add_opening == "Finish" and steps >= 2:
                                        ff = input("File or Folder?")
                                        if ff == "File":

                                            manual_add_location = eval("files[" + "][".join(
                                                real_add_path) + "][-1]")
                                            exec("files[" + "][".join(
                                                real_add_path) + "].pop(-1)")
                                            exec("files[" + "][".join(
                                                real_add_path) + "].append([Graphing.transform(Graphing.transform(input('Please select what you want in your file (@ for new line, ~ for indent): '),'@', '\n'), '~', '    '),'flipe',input('Please select a name for your file: ')])")
                                            exec("files[" + "][".join(
                                                real_add_path) + "].append(manual_add_location)")
                                        manual_add_stop = True
                                        add_opening = "Cancel"
                                        opening = "Reset"

                                        if ff == "Folder":
                                            manual_add_location = eval("files[" + "][".join(
                                                real_add_path) + "][-1]")
                                            exec("files[" + "][".join(
                                                real_add_path) + "].pop(-1)")
                                            exec("files[" + "][".join(
                                                real_add_path) + "].append([input('Please select a name for your folder: ')])")

                                            exec("files[" + "][".join(
                                                real_add_path) + "].append(manual_add_location)")
                                        manual_add_stop = True
                                        add_opening = "Cancel"
                                        opening = "Reset"
                                    elif add_opening == "Cancel":
                                        print("ok")
                                        manual_add_stop = True
                                        add_opening = "Cancel"
                                        opening = "Reset"

                        elif opening == "Remove":
                            remove_location = input(
                                "Please input the folder/file you want to remove: ")

                            remove_path = copy.deepcopy(files[verycooluserindice])
                            print(
                                "Please select a folder to open (Select an index | Say 'Finish' to lock in the folder | Say 'Cancel' to cancel action): ")

                            print("Here are your files: ")
                            whitespace(1)
                            user_index = users.index(user)
                            file_names = []
                            for i in range(0, len(remove_path)):
                                if len(remove_path[i]) >= 2:
                                    if remove_path[i][-2] == "flipe":
                                        file_names.append(
                                            remove_path[i][
                                                -1] + " (File | Index " + str(
                                                i + 1) + ")")
                                    else:
                                        file_names.append(
                                            remove_path[i][
                                                -1] + " (Folder | Index " + str(
                                                i + 1) + ")")
                                else:

                                    file_names.append(
                                        remove_path[i][-1] + " (Folder | Index " + str(
                                            i + 1) + ")")
                            manual_remove_stop = False
                            real_remove_path = [str(verycooluserindice)]
                            steps = 0
                            print("   <{}><{}><{}>   ".join(file_names))
                            while manual_remove_stop == False:
                                remove_opening = input(">+ ")

                                steps += 1

                                if remove_opening != "Finish" and remove_opening != "Cancel":
                                    real_remove_path.append(str(int(remove_opening) - 1))
                                    print(real_remove_path)
                                    remove_path = copy.deepcopy(
                                        remove_path[int(int(remove_opening) - 1)])
                                    remove_path.pop(-1)
                                    tempfold = False
                                    if len(remove_path) >= 2:
                                        if remove_path[-1] == "flipe":
                                            remove_path.pop(-1)
                                            tempfold = True

                                    file_names = []
                                    if len(remove_path) == 1:
                                        if tempfold == True:
                                            print(
                                                "It's a text file!")


                                        else:
                                            for i in range(0, len(remove_path)):
                                                if len(remove_path[i]) >= 2:
                                                    if remove_path[i][-2] == "flipe":
                                                        file_names.append(
                                                            remove_path[i][
                                                                -1] + " (File | Index " + str(
                                                                i + 1) + ")")
                                                    else:
                                                        file_names.append(
                                                            remove_path[i][
                                                                -1] + " (Folder | Index " + str(
                                                                i + 1) + ")")
                                                else:

                                                    file_names.append(remove_path[i][
                                                                          -1] + " (Folder | Index " + str(
                                                        i + 1) + ")")
                                    else:
                                        for i in range(0, len(remove_path)):
                                            if len(remove_path[i]) >= 2:
                                                if remove_path[i][-2] == "flipe":
                                                    file_names.append(remove_path[i][
                                                                          -1] + " (File | Index " + str(
                                                        i + 1) + ")")
                                                else:
                                                    file_names.append(remove_path[i][
                                                                          -1] + " (Folder | Index " + str(
                                                        i + 1) + ")")
                                            else:

                                                file_names.append(remove_path[i][
                                                                      -1] + " (Folder | Index " + str(
                                                    i + 1) + ")")

                                    print("   <{}><{}><{}>   ".join(file_names))

                                    if len(remove_path) == 0:
                                        print(
                                            "There's... nothing in this folder/file....")
                                elif remove_opening == "Finish" and steps >= 2:
                                    original_remove_path = copy.deepcopy(real_remove_path)
                                    (real_remove_path).pop(-1)


                                    real_armove_path = copy.deepcopy(real_remove_path)

                                    print(real_armove_path)
                                    print(
                                        "Debugging for Developers: \>  files[" + "][".join(
                                            real_armove_path) + "].pop(" + str(
                                            real_remove_path[-1]) + ")")
                                    exec("files[" + "][".join(
                                        real_armove_path) + "].pop(" + str(
                                        real_remove_path[-1]) + ")")
                                    remove_opening = "Cancel"
                                    opening = "Reset"
                                    manual_remove_stop = True
                                elif remove_opening == "Finish" and steps < 2:
                                    print(
                                        "Uhh... you can't remove files from the Main PC path using manual removing....")
                                elif remove_opening == "Cancel":
                                    print("ok")
                                    remove_opening = "Cancel"
                                    opening = "Reset"
                                    manual_remove_stop = True









                        elif opening == "Execute":
                            print(execute_path)


                            if eval("len(files[" + "][".join(execute_path) + "])") == 3:

                                if eval("files[" + "][".join(execute_path) + "][-2]") == "flipe":

                                    whitespace(2)
                                    print("Now analyzing security...")
                                    concerning = False
                                    if "passwords" in eval("files[" + "][".join(execute_path) + "][0]") or "users" in eval("files[" + "][".join(execute_path) + "][0]") or "files" in eval("files[" + "][".join(execute_path) + "][0]") or "locations" in eval("files[" + "][".join(execute_path) + "][0]") or "display_location" in eval("files[" + "][".join(execute_path) + "][0]") or "longitude" in eval("files[" + "][".join(execute_path) + "][0]") or "latitude" in eval("files[" + "][".join(execute_path) + "][0]") or "registered_locations" in eval("files[" + "][".join(execute_path) + "][0]") or "registered_longitude" in eval("files[" + "][".join(execute_path) + "][0]") or "registered_latitude" in eval("files[" + "][".join(execute_path) + "][0]"):
                                        concerning = True

                                    response = co.generate(
                                        model='command-r-plus',  # Choose the model (e.g., 'xlarge', 'medium', etc.)
                                        prompt=f"User: Check if the following code is trying to use the Class 'Cypher' or 'Security', use encryption/decryption techniques, or fetch/change data in the lists: 'passwords', 'users', 'files', 'locations', 'display_location', 'longitude', 'latitude', 'display_users', 'registered_locations', 'registered_longitude', or 'registered_latitude'. If it does, respond with ONLY 'Y', if not, respond with ONLY 'N'. Here is the code: {eval("files[" + "][".join(execute_path) + "][0]")}. Code concerning: {concerning}. AI Assistant: ",
                                        max_tokens=10
                                    )
                                    print(response.generations[0].text)

                                    if "Y" in response.generations[0].text or concerning == True:
                                        print("Your code has been blocked, since it has security concerns.")
                                    else:
                                        print("Your code has been deemed safe!")
                                        whitespace(1)
                                        print("Output:")

                                        exec(eval("files[" + "][".join(execute_path) + "][0]"))



                                else:

                                    print("This ain't a file..")

                            else:

                                print("This ain't a file..")





                        else:
                            execute_path.append(str(int(opening) - 1))
                            open_path = copy.deepcopy(open_path[int(int(opening) - 1)])
                            open_path.pop(-1)
                            tempfold = False
                            if len(open_path) >= 2:
                                if open_path[-1] == "flipe":
                                    open_path.pop(-1)
                                    tempfold = True

                            file_names = []
                            if len(open_path) == 1:
                                if tempfold == True:
                                    print("It's a text file! It reads...")
                                    whitespace(1)
                                    print(open_path[0])
                                else:
                                    for i in range(0, len(open_path)):
                                        if len(open_path[i]) >= 2:
                                            if open_path[i][-2] == "flipe":
                                                file_names.append(
                                                    open_path[i][-1] + " (File | Index " + str(i + 1) + ")")
                                            else:
                                                file_names.append(
                                                    open_path[i][-1] + " (Folder | Index " + str(i + 1) + ")")
                                        else:

                                            file_names.append(open_path[i][-1] + " (Folder | Index " + str(i + 1) + ")")
                            else:
                                for i in range(0, len(open_path)):
                                    if len(open_path[i]) >= 2:
                                        if open_path[i][-2] == "flipe":
                                            file_names.append(open_path[i][-1] + " (File | Index " + str(i + 1) + ")")
                                        else:
                                            file_names.append(open_path[i][-1] + " (Folder | Index " + str(i + 1) + ")")
                                    else:

                                        file_names.append(open_path[i][-1] + " (Folder | Index " + str(i + 1) + ")")

                            print("   <{}><{}><{}>   ".join(file_names))

                            if len(open_path) == 0:
                                print("There's... nothing in this folder/file....")
                        whitespace(2)
                    except Exception as error:
                        print("AN ERROR OCCURED!! " + str(error))
                        print("Guide to errors: ")
                        listPlot(["list index out of range | Try resetting",
                                  "invalid literal | Try entering correct syntax and resetting"], "Errors")
                        whitespace(1)
                        print(f"Debugging for developers: {files[verycooluserindice]}")

            whitespace(2)
        except Exception as e:
            print("It looks like there's an error! " + str(e))



