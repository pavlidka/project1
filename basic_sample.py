from appium import webdriver

desired_caps={
	'platformName':'Windows',
	'deviceName':'WindowsPC',
	'app':r'C:\Windows\System32\notepad.exe'
}

driver=webdriver.Remote('http://localhost:4723',desired_caps)
