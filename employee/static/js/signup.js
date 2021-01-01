function signnup()
	{
		 var u_name = document.myform2.uname.value;
		 var f_name = document.myform2.fname.value;
		 var l_name = document.myform2.lname.value;
		 var email_id = document.myform2.email.value;  
         var atposition=email_id.indexOf("@");  
         var dotposition=email_id.lastIndexOf("."); 
    	 var password = document.myform2.pass.value;

    	if(u_name == null || u_name == "")
    	{
        	alert("User Name cant be blank");
        	return false;
    	}
    	else if(f_name == null || f_name == "")
    	{
        	alert("First Name cant be blank");
        	return false;
    	}
    	else if(l_name == null || l_name == "")
    	{
        	alert("Last Name cant be blank");
        	return false;
    	}
    	else if (atposition<1 || dotposition<atposition+2 || dotposition+2>=email_id.length)
        {  
            alert("Please enter a valid e-mail address \n atpostion:"+atposition+"\n dotposition:"+dotposition);  
            return false;  
        }
    	else if(password == null || password == "")
        {
            alert("Password can't be blank");
            return false;
        }
        else if (password.length < 8) 
        {
            alert("Password must be at least 8 characters long.");
            return false;
        }
	}