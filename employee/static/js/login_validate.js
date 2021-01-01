function loggin()
{
    var u_name = document.myform.name.value;
    var password = document.myform.pass.value;

    if(u_name == null || u_name == "")
    {
        alert("User Name cant be blank");
        return false;
    }
    else if(password == null || password == "")
        {
            alert("Password can't be blank");
            return false;
        }
    else if (password.length <8) 
        {
            alert("Password must be at least 8 characters long.");
            return false;
        }
}