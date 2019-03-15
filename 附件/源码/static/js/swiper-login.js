$(document).ready(function(){
	//滚动条
	var mySwiper = new Swiper ('.swiper-container-h', {
		direction: 'horizontal', // 水平切换选项
		loop: false, // 循环模式选项
		speed: 1000, // 切换速度
		hashNavigation: true, //设置锚点
		noSwiping: true,//设置进制滑动
		parallax: true,//设置视差效果
		
		//分页效果
		// effect : 'coverflow',
		// slidesPerView: 3,
		centeredSlides: true, //块居中

		// 如果需要分页器
// 		pagination: {
// 			el: '.swiper-pagination',
// 			// type: 'progressbar',
// 			clickable: 'true',
// 		},

		// 如果需要前进后退按钮
		navigation: {
			nextEl: '.swiper-button-next',
			prevEl: '.swiper-button-prev',
		},

		// 如果需要滚动条
		scrollbar: {
			el: '.swiper-scrollbar',
			draggable: 'true',
		},
		
		// mousewheel: true,
	});
	mySwiper.scrollbar.$el.css({
		'height':'15px',
		'background': 'rgba(0,0,0,0.05)',
		});
	mySwiper.scrollbar.$dragEl.css('background','rgba(255,255,255,.5)');
	
	
	
	
	//初始化竖直滑动条
	var swiperV = new Swiper('.swiper-container-v', {
		direction: 'vertical', //垂直滚动
		loop: true, // 循环模式选项
		speed: 1000, // 切换速度
		parallax: true,//设置视差效果
		mousewheel: true,//设置鼠标滚轮可用
	});

	//登录按钮点击事件
	$(".log-button-login").click(function () {
		mySwiper.slideTo(1, 600, false);//切换到第二个slide
	});



	//为slide1中的a标签添加点击事件
	$("#slider1-login-a").click(function(){
		mySwiper.slideTo(1, 600, false);//切换到第二个slide
	});
	
	//为slide1中的a标签添加鼠标移入移出事件
	$("#slider1-login-a").mouseenter(function(){
		$("#slider1-login").animate({
			backgroundColor:"rgba(255,255,255,0.4)",
			fontSize:"26px",
		},100);
	})
	$("#slider1-login-a").mouseout(function(){
		$("#slider1-login").animate({
			backgroundColor:"rgba(0,0,0,0)",
			fontSize:"25px",
		},100);
	})
	
	//为slide2中的登录按钮添加鼠标移入效果
	$("#slider2-login-form input[type='submit']").mouseenter(function(){
		$(this).stop();
		$(this).animate({
			backgroundColor:"rgb(221,180,221)",
		},1000);
	})
	$("#slider2-login-form input[type='submit']").mouseout(function(){
		$(this).stop();
		$(this).animate({
			backgroundColor:"rgb(221,160,221)",
		},1000);
	})
	
	//为slide2中的登录按钮添加点击Ajax判断
	$("#slider2-login-form input[type='submit']").click(function(){
		event.preventDefault();
		$.ajax({
			type:"POST",
			url:"check/",
			data:{
				'student_id':$("#student_id").val(),
				'password':$('#password').val(),
			},
			success: function(result){
				if(result==="true"){
					$(location).attr('href', '/zhcp/index/');
				}else if(result==="passwordWrong"){
					$('#slider2-login-form #password-wrong').show();
				}else if(result==="idDoesNotExist"){
					$('#slider2-login-form #id-DoesNotExist').show();
				}
			},
		});
	});

	//为slide2中的输入框添加值改变效果
	$('#slider2-login-form input').bind('input propertychange', function()
	{
		$('#slider2-login-form #password-wrong').hide();
		$('#slider2-login-form #id-DoesNotExist').hide();
	});
});