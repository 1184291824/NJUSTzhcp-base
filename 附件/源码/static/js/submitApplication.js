$(document).ready(function () {
    //submitApplication
	let application_input = $('.submit-application-input');
	let submit_application = $('#submit-application');
	let application_name = $('#application-name');
	let score = $('#score');
	let code = $('#verificationCode');

	//对input添加值改变效果
	application_input.bind('input propertychange', function()
	{
		$(".submit-application-error").fadeOut(500);
		$(this).css({
			'border': 'none',
    		'border-left': '1px solid #f8f8f8',
		});
	});

	//点击刷新验证码
	$('#verificationCode-img').click(function () {
		this.src="../verificationCode/?"+new Date().getTime();
	});

	//给submitApplication中的提交按钮添加事件
	submit_application.click(function () {
		event.preventDefault();
		if(application_name.val() === ''){
			$('#submit-application-error1').fadeIn(500);
			application_name.css('border', '1px solid red');
			return false;
		}
		if(score.val() === ''){
			$('#submit-application-error2').fadeIn(500);
			score.css('border', '1px solid red');
			return false;
		}
		//判断验证码是否正确
		$.ajax({
			type:"POST",
			url:"../verificationCode/check/",
			data:{
				'code':code.val(),
			},
			success: function(result){
				console.log(result);
				if(result==="true"){
					$('#submit-application-form>form').submit();
				}
				else if(result==="false"){
					$('#submit-application-error3').fadeIn(500);
					$('#verificationCode-img')[0].src="../verificationCode/?"+new Date().getTime();
				}
			},
		})

	});
});