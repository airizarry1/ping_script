# Welcome to the Ping Script

This is a script that leverages the [os library](https://docs.python.org/3/library/os.html) to ping a network device to verify if the device is up or down. Use this script to learn the basics of python.

## Download the Code

To get started: Download the code and cd the `ping_script` directory

```bash
git clone https://github.com/labeveryday/ping_script.git
cd ping_script
```

## Python Virtual Environment

When executing python code or installing python applications you should get into the practice of creating and managing python virtual environments.
This will allow you to run different versions of a python library while avoiding version conflicts. My preferred tool for python virtual environments is `venv`
There are tools out there. Remember to find what works best for you.

**On Linux or Mac**

```python
python3 -m venv venv
source venv/bin/activate
```

**On Windows**

```cmd
python3 -m venv venv
.\venv\Scripts\activate.bat
```

## Example: Script in action

Before executing your script you must update your device ip address list in the `ip_file.txt` file. This will be the list of ip addresses that will be used in the script.

```bash
(venv) duan@ubuntu ping_script$ cat ip_file.txt 
192.168.23.142
192.168.23.143
192.168.23.144
192.168.23.145
192.168.23.146
192.168.23.147
8.8.8.8
```

Now that you have everything installed and updated you can execute the script

```bash
(venv) duan@ubuntu ping_script$ python tool.py
Down 192.168.23.1 Ping Unsuccessful
Down 192.168.23.2 Ping Unsuccessful
Up 192.168.23.142 Ping successful
Up 192.168.23.143 Ping successful
Up 192.168.23.144 Ping successful

```

>NOTE: To modify the subnets and the range


### About me

Introverted Network Automation Engineer that is changing lives as a Developer Advocate for Cisco DevNet. Pythons scripts are delicious. Especially at 2am on a Saturday night.

My hangouts:

- [LinkedIn](https://www.linkedin.com/in/duanlightfoot/)

- [Twitter](https://twitter.com/labeveryday)