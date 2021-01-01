function forgot()
	{
		 var email_id = document.myform3.email.value;  
         var atposition=email_id.indexOf("@");  
         var dotposition=email_id.lastIndexOf("."); 
    	 var password = document.myform3.newpass.value;

    	if (atposition<1 || dotposition<atposition+2 || dotposition+2>=email_id.length)
        {  
            alert("Please enter a valid e-mail address \n atpostion:"+atposition+"\n dotposition:"+dotposition);  
            return false;  
        }
    	else if (password.length <8) 
        {
            alert("Password must be at least 8 characters long.");
            return false;
        }
	}