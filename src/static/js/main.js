$(document).ready(function() {
	$('.feed').addClass('bold');
	$('.trending').addClass('bold');

	$.ajax({
		url: '/api/question/',
		type: 'GET',
		success: function(data){
			$.each(data, function(key, value){
				var questionKey = key;
				var questionUser = value.user.username;
				var questionTitle = value.title;
				var questionCreated = value.date_display;
				$(".q-box").append(
					"<span>" + "Question asked &middot; "+ questionCreated + "</span>" +
					"<h2>" + questionTitle + "?</h2>" +
					"<small>by " + questionUser + "</small>" +
					"<br><hr>"
				)
			});
		}
	});



});