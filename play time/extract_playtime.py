import os
import re

read_file_name = 'statsx_shell_played_time.txt'
output_file_name = 'output_player_playtime.txt'

script_directory = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(script_directory, read_file_name)
output_file_path = os.path.join(script_directory, output_file_name)


def read_playtime_data(file):
    pdata = {}

    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            if not line.strip():
                break

            if 'LAST_VISIT' in line or 'TODAY_PLAY' in line:
                continue

            print(f"Processing line: {line}")

            match = re.match(r'"([^"]+)#([^"]+)" "([^"]+)" (\d+)', line)
            if match:
                key, pname, played_time, unused = match.groups()

                if key == "PLAYED_TIME":
                    playtime_seconds = int(played_time)
                    pdata[pname] = {'playtime_seconds': playtime_seconds}
                else:
                    print(f"Ignoring line with key: {key}")

    return pdata


def convert_seconds_to_dhm(seconds, decimal_places=2):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)

    d = round(d, decimal_places)
    h = round(h, decimal_places)
    m = round(m, decimal_places)

    return d, h, m


if os.path.exists(output_file_path):
    os.remove(output_file_path)

player_data = read_playtime_data(file_path)

if not os.path.exists(output_file_path):
    open(output_file_path, 'w', encoding='utf-8').close()

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for player_name, data in player_data.items():
        total_playtime = data['playtime_seconds']

        if total_playtime <= 0:
            output_file.write(f"Player: {player_name} didn't play.\n\n")
            continue

        days, hours, minutes = convert_seconds_to_dhm(total_playtime, 0)

        output_file.write(f"Player: {player_name}\n")
        if days > 0:
            output_file.write(f"Playtime: {days} days, {hours} hours, {minutes} minutes\n\n")
        elif hours > 0:
            output_file.write(f"Playtime: {hours} hours, {minutes} minutes\n\n")
        else:
            output_file.write(f"Playtime: {minutes} minutes\n\n")

print("Extraction complete!")
