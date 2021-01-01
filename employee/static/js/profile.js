$(function(){
    $('[data-toggle="tooltip"]').tooltip();
    $(".side-nav .collapse").on("hide.bs.collapse", function() {                   
        $(this).prev().find(".fa").eq(1).removeClass("fa-angle-right").addClass("fa-angle-down");
    });
    $('.side-nav .collapse').on("show.bs.collapse", function() {                        
        $(this).prev().find(".fa").eq(1).removeClass("fa-angle-down").addClass("fa-angle-right");        
    });
}) 


function proffile()
{
	var contact = document.myform.phone.value;
	var location = document.myform.address.value;
	var depart = document.myform.dept.value;

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
        else if(depart == null || depart == "")
        {
        	alert("Please enter your Department");
        	return false;
        }
}
