import mechanize
import cookielib
import webbrowser

br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.open("http://172.50.1.1:8090/httpclient.html")
br.select_form(name='frmHTTPClientLogin')
br["username"] = "Enter your username/ admission number"
br["password"] = "Enter your password"
res = br.submit()
content = res.read()


if content.find("You have successfully logged in") > 0:
	print "You have successfully logged in"
elif content.find("The system could not log you on. Make sure your password is correct") > 0:
	print "The system could not log you on. Make sure your password is correct written in script"
elif content.find("You have reached Maximum Login Limit") > 0:
	print "You have reached Maximum Login Limit"
else:
	print "system error"

# enter any link  
webbrowser.open("https://www.facebook.com/")