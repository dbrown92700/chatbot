# Waittime is time in seconds between runs
# Duration is time in minutes that the test continues to run
# If duration is commented out, test runs indefinitely

wait_time = 60
duration = 60

# IOS device and credentials
# ssh_targets is a set of IP Addresses or DNS resolve-able hostnames
# Assumes that credentials are the same on all devices
# and runs the same command on all systems
# If ssh_targets is an empty set [] or commented out, the test is skipped

# ssh_targets = ['192.168.1.81', '192.168.1.83']
ssh_user = 'username'
ssh_password = 'password'
command = 'show running'

# URLS to pull
# If urls is an empty set [] or commented out this test is skipped

urls=[
	'https://twitter.com',
	'https://www.linkedin.com',
	'https://www.office.com',
	'https://www.microsoft.com/en-us/microsoft-365',
	'https://www.cisco.com',
	'https://www.google.com',
	'https://docs.google.com/spreadsheets/d/1rG2vCzmlmfsAEp2RU6XTVTLXx8J0ekPbCIpgzbdeJFQ/edit?usp=sharing',
	'https://play.google.com',
	'https://photos.google.com',
	'https://www.dropbox.com/s/zlg3hw01yyvorcg/Adirondack%20Chair%20Plans%20-%20Popular%20Mechanics.pdf?dl=0',
	'https://console.aws.amazon.com',
	'https://signup.cloud.oracle.com/',
	'https://signin.webex.com',
	'https://web.webex.com/sign-in'
]
