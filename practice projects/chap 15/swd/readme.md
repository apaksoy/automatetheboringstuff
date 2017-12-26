This readme is all about the xkcd.plist property list file and its contents unless stated otherwise. It was used to run scheduledWebDownloader.py on a regular basis via launchctl (a variant of launchcd) on mac OS.

The xkcd.plist file was initially placed under /Users/Alper/Library/launchagents directory but then it was placed in the same folder with the Python script and that also worked perfectly well. The property list file ran the scheduledWebDownloader.py script every 15 seconds. You can give the property list file any name you like but its extension has to be "plist".

The StandardErrorPath and StandardOutPath keys are very nice to have in the property list file. Otherwise, error messages caused by the script and the messages the script are supposed to print out to the screen during its normal interpretation would be missed out. 

The label key is necessary but it need not have the same name with the .plist file as some on Stack OverFlow claim.

Unfortunately, the absolute path for the Python interpreter has to be provided either in the ProgramArguments key or at the top of the script file as a shebang line. Having the relative path

	#!/usr/bin/env python3

at the top of the script file or just 

	<string>python3</string>

in the .plist file along with the script does not work. 

Absolute path to the script also needs to be provided in the property list file. Making it executable and defining its location as a PATH in the .bash_profile file does not work withut the absolute path even when it has the absolute path to the interpreter at the top of the script file.

The following lines can replace the two lines about the timing and run the script at 5:45 am every day. One needs to use the 24-hour time notation to describe the pm times.

	<key>StartCalendarInterval</key>
	<dict>
 		<key>Hour</key>
		<integer>5</integer>
  		<key>Minute</key>
  		<integer>45</integer>
	</dict>

Use the following terminal commands to load and unload the propertly list file.

	launchctl load xkcd.plist
	launchctl unload xkcd.plist

Also check the specified .err and .out files to see if the program has run nicely. These files are not updated before the property list file is unloaded. For some “errors”, even those files may not show anything. You could understand that there is something amiss by observing that the script is not doing it is supposed to do by things not happening, i.e. files downloaded, as they should.  
