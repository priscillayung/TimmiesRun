def sendOrderMail():
    template = get_template('Order_Mail.html')
    
    runPerson =
    runTime =
    subject, from_email, to = 'TimmiesRun (Reply to this Emailaddress ONLY!)', 'umanage.mpd@gmail.com', 'alex@myplanetdigital.com'
    
    html_content = render_to_string('Order_Mail.html')
    text_content = strip_tags(html_content) #this strips the html, so people will have the text as well
    
    #Create the email, and attach the HTML version as well.
    
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
