$(document).ready(function(){
	$('#AddClass button').click(function(){
		$('#AddClass p').addClass('red');
	});

	$('#SlideToggle button').click(function(){
		$('#SlideToggle img').slideToggle("slow", function(){

		});
	});

	$('#Append button').click(function() {
		$('#Append p#first').append("<p>This is a new paragraph</p>");
	})

	$('#Hide button').click(function() {
		$('#Hide p').hide();
	})

	$('#Show button').click(function() {
		$('#Show p').show().css('display', 'inline-block');
	})

	$('#Toggle button').click(function() {
		$('#Toggle p').toggle();
	})

	$('#SlideDown button').click(function() {
		$('#SlideDown p').slideDown("slow", function() {

		}).css('display', 'inline-block');
	})

	$('#SlideUp button').click(function() {
		$('#SlideUp p').slideUp("slow", function() {

		})
	})

	$('#FadeIn button').click(function(){
		$('#FadeIn p').fadeIn("slow").css('display', 'inline-block');
	})

	$('#FadeOut button').click(function(){
		$('#FadeOut p').fadeOut('slow');
	})

	$('#Before button').click(function() {
		$('#Before h2').before($('#Before p').css('width', '100%'));
	})

	$('#After button').click(function() {
		$('#After p').after($('#After h2'));
	})

	$('#html button').click(function() {
		var html_string = $('#html p').html();
		$('#html p').text(html_string);
	})

	$('#val button').click(function() {
		$('#val').append("<p>"+$('#txt_val').val()+"</p>");
	})

	$('#text button').click(function() {
		$('#text h2').text($('#text p').text());
	})
});

console.log('ready!');

