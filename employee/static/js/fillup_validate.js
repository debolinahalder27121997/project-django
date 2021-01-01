function fillup_val()
{
	var contact = document.myform2.phone.value;
	var location = document.myform2.address.value;
    var depart = document.myform2.dept.value;

	if(contact.length !== 10)
        {
            alert("Wrong number");
            return false;
        }
        else if(isNaN(contact))
        {
            alert("INVALID entry");
            return false;
        }
        else if(contact === ''|| contact === null)
        {
            alert("phone number missing");
            return false;
        }
        else if(location == null || location == "")
        {
            alert("Please enter Address");
            return false;
        }
        else if(dept == null || dept == "")
        {
            alert("Please enter Address");
            return false;
        }

}
