var name_post='';
var message='';
function start(){
	$(".login").css("display", "none");
	$(".chat_div").css("display", "");
	name_post = $('#name_account').val();
	
}






function addComment(text, name, pos){

	var last_element = $('.block_msg:last');
	var html = '<div class="block_msg '+(pos=='left'?'left_msg':'right_msg')+'"><p>'+text+'</p><small>'+name+'</small></div>'
   	if (last_element == undefined){
   		$('#chat_list_in').html(html);
   	}
   	else {last_element.after(html);}
    $('#chat_list_in').slimScroll({ scrollBy: '450px' });


    }

 
    

$(document).ready(function (){
	
	$('#chat_list_in').slimScroll({
height: '317px'
});

	$('#post_button').click(function(){
		message = $('#post_msg').val();
 			addComment(message, name_post);
			})
})

function backToStart(){
	$(".login").css("display", "");
	$(".chat_div").css("display", "none");


}