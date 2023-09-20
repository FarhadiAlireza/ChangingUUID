import json
import subprocess

def get_xray_uuid():
    result = subprocess.check_output(['./xray', 'uuid'], cwd='/usr/local/bin', text=True)
    return result.strip()

with open('/usr/local/etc/xray/config.json') as json_file:
    config_data = json.load(json_file)

inbounds = config_data['inbounds']

for i in range(1, len(inbounds)):
    protocol = inbounds[i]['protocol']
    clients = inbounds[i]['settings']['clients']
    for j in range(len(clients)):
        if protocol == 'trojan':
            clients[j]["password"] = get_xray_uuid()
        else:
            clients[j]["id"] = get_xray_uuid()

with open('/usr/local/etc/xray/config.json', 'w') as json_file:
    json.dump(config_data, json_file, indent=2)

print("UUIDs updated successfully.")
