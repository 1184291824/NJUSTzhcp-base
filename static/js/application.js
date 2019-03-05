$(document).ready(function(){
	let menu_option = $('.menu-left-option');
	let identity_text = $('#span-identity').text();
	let menu_option_5 = $('#menu-left-option-5');
	let menu_option_6 = $('#menu-left-option-6');


	// 给菜单中的选项方块添加鼠标移入和移出事件
	menu_option.mouseenter(function(){
		$(this).css('background-color','rgba(0,0,0,0.3)');
	});
	menu_option.mouseleave(function(){
		$(this).css('background-color','rgba(0,0,0,0)');
	});
	if(identity_text === 'student'){
		menu_option_5.off();
		menu_option_5.off();
		menu_option_6.off();
		menu_option_6.off();
	}
	if(identity_text === 'captain'){
		menu_option_6.off();
		menu_option_6.off();
	}


	//submitApplication
	let application_input = $('.submit-application-input');
	let submit_application = $('#submit-application');
	let application_name = $('#application-name');
	let score = $('#score');
	let detail = $('#detail');
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



	//myActivity页面
	//给每一行表格添加点击效果，点击之后出现详细信息
	$('.myActivity-base').click(function () {
		$(this).next().fadeToggle('fast');
	});



	//reviewApplication页面
	let reviewApplication_title_1 = $('#reviewApplication-title-1');
	let reviewApplication_title_2 = $('#reviewApplication-title-2');
	let reviewApplication_title = $('.reviewApplication-title');
	let reviewApplication_title_bar = $('.reviewApplication-title-bar');
	let reviewApplication_title_bar_left = reviewApplication_title_bar.position().left;
	//给标题栏添加效果

	reviewApplication_title.bind({
		mouseenter:function () {
			let reviewApplication_title_bar_left = $(this).position().left+$(this).width()/2-32;
			reviewApplication_title_bar.stop().animate({
				left: reviewApplication_title_bar_left+'px'
			}, 'slow')
		},
		mouseleave:function () {
			reviewApplication_title_bar.stop().animate({
				left: reviewApplication_title_bar_left+'px'
			}, 'slow')
		},
		click:function () {
			reviewApplication_title_bar_left = $(this).position().left+$(this).width()/2-32;
			let reviewApplication_tbody_id = 'reviewApplication-tbody-'+this.id.slice(-1);
			$('.reviewApplication-tbody').css('display', 'none');
			$('#'+reviewApplication_tbody_id).css('display', 'table-row-group');
			if ($('#'+reviewApplication_tbody_id).find('td').length === 0){
				$('#'+reviewApplication_tbody_id).html("<tr><td colspan='5'><h1>您还未审批过任何申请！</h1></td></tr>");
			}
		}
	});
});