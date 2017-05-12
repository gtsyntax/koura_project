$(document).ready(function() {

	var $username  = $('input#id_username');
	var $password  = $('input#id_password');
	$('#login-btn').attr("disabled", true);
	$username.keyup(function(){
		if($username.length > 0){
			$password.keyup(function(){
				if($password.length > 0){
					$('#login-btn').attr("disabled", false);
				} 
			})
		}
	})

	var questionList = [];

	// This holds the question data
	function attachQuestion(questionData, prepend){
		var questionUser = questionData.user.username;
		var questionTitle = questionData.title;
		var questionImage = questionData.image;
		var questionCreated = questionData.date_display;
		if (questionImage == null){
			var questionHtml = "<span>" + "Question asked &middot; "+ questionCreated + "</span>" +
							"<h2>" + questionTitle + "?</h2>" + 
							"<small>by " + questionUser + "</small>"+
							"<br><hr>"
		} else {
			var questionHtml = "<span>" + "Question asked &middot; "+ questionCreated + "</span>" +
							"<h2>" + questionTitle + "?</h2>" + 
							'<img src=' + questionImage + ' class="img-responsive" />' +
							"<small>by " + questionUser + "</small>"+
							"<br><hr>"
		}
		if (prepend==true){
			$("#q-box").prepend(questionHtml)
		} else {
			$("#q-box").append(questionHtml)
		}

	}

	// The question data is looped and parsed through this logic
	function parseQuestions(){
		if (questionList == 0) {
			$("#q-box").text("No questions yet")
		} else {
			$.each(questionList, function(key, value){
				var questionKey = key;
				attachQuestion(value)
			})

		}
	}

	// Logic that fetches the question the api.
	function fetchQuestions(){
		$.ajax({
			url: '/api/question/',
			type: 'GET',
			success: function(data){
				questionList = data
				parseQuestions();
			}
		})
	}
	fetchQuestions()

	// Logic for creating question with ajax call
	var $questionForm = $('#question-form');
	$questionForm.bind('submit', function(event){
		event.preventDefault();
		// Value gotten from the input field is stored in the variable this_
		var this_ = $(this)
		var formData = this_.serialize()

		$.ajax({
			url: '/api/question/create/',
			type: 'POST',
			data: formData,
			success: function(data){
				this_.find("input[type=text]").val("")
				attachQuestion(data, true)
			}
		})
	})

});