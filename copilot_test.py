import subprocess

# Function to get system uptime

def get_system_uptime():
    try:
        # Execute the uptime command
        uptime_output = subprocess.check_output(['uptime']).decode('utf-8')
        return uptime_output.strip()
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    uptime = get_system_uptime()
    print("System Uptime:", uptime)