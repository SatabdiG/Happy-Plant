var nodemailer=require('nodemailer');
var transporter=nodemailer.createTransport(
{
	service:'gmail',
	auth:{
		user:'happy.plantv2.0@gmail.com',
		pass:'happyplant2'
	}
	

}

);

transporter.sendMail({
	from:'happy.plantv2.0@gmail.com',
	to:'satabdi.ganguly89@gmail.com',
	subject:'Hello',
	text:'hello world'


}, function(error, respnse){
	if(error)
{
	console.log(error);

}else{

	console.log("Message sent: " + response.message);
}


});
