$(document).ready(function(){
	//滚动条
	var mySwiper = new Swiper ('.swiper-container', {
		direction: 'horizontal', // 垂直切换选项
		// loop: true, // 循环模式选项
		speed: 1000, // 切换速度
		hashNavigation: true, //设置锚点
		// noSwiping: true,//设置进制滑动
		parallax: true,//设置视差效果
		centeredSlides: true,//块居中
		allowTouchMove: false,//进制鼠标拖动

// 		// 如果需要分页器
// 		pagination: {
// 			el: '.swiper-pagination',
// 			type: 'progressbar',
// 			renderProgressbar: function (progressbarFillClass,index) {
// 				return '<span class="' + progressbarFillClass + '">' + (index) + '</span>';
// 			}
// 		},

		// 如果需要前进后退按钮
		// navigation: {
		// 	nextEl: '.swiper-button-next',
		// 	prevEl: '.swiper-button-prev',
		// },
		
		// 回调函数
		on:{
			progress: function (){//slider切换结束时执行

				var progress = this.progress;
				var $bar = $('.register-progress-bar');
				$bar.stop();
				$("#step1").stop();
				$("#step2").stop();
				$("#step3").stop();
				switch (progress){
					case 0:$bar.animate({"width":"33%",},1000);
					$("#step1").animate({"font-size":"19px","color":"white"},1000);
					$("#step2").animate({"font-size":"16px","color":"#D3D3D3"},1000);
					$("#step3").animate({"font-size":"16px","color":"#D3D3D3"},1000);
						break;
					case 0.5:$bar.animate({"width":"66%",},1000);
					$("#step1").animate({"font-size":"16px","color":"#D3D3D3"},1000);
					$("#step2").animate({"font-size":"19px","color":"white"},1000);
					$("#step3").animate({"font-size":"16px","color":"#D3D3D3"},1000);
						break;
					case 1:$bar.animate({"width":"100%",},1000);
					$("#step1").animate({"font-size":"16px","color":"#D3D3D3"},1000);
					$("#step3").animate({"font-size":"19px","color":"white"},1000);
					$("#step2").animate({"font-size":"16px","color":"#D3D3D3"},1000);
						break;
					default:
						break;
				}
			},
			init: function(){
				swiperAnimateCache(this); //隐藏动画元素 
				swiperAnimate(this); //初始化完成开始动画
			},
// 			slideChangeTransitionEnd: function(){ 
// 				swiperAnimate(this); //每个slide切换结束时也运行当前slide动画
// 				this.slides.eq(this.activeIndex).find('.ani').removeClass('ani'); //动画只展现一次，去除ani类名
// 			}
		},
	});
	
	//input框
	var input_student_id = $("#student_id");
	var input_password = $("#password");
	var input_password_check = $("#password_check");
	var input_name = $('#name');
	var input_VerificationCode = $('#VerificationCode');

	//input输入框-默认聚焦到student_id
	$("#student_id").focus();
	
	//给slider1中的input添加值改变事件
	$('.slider1-input').bind('input propertychange', function()
	{
		$("#slider1-note-errors").fadeOut(500);
		$(this).css("border","none");
	});
	
	//给slider1-submit添加点击事件
	$("#slider1-submit").click(function(){
		event.preventDefault();//去除本身的事件
		
		//判断输入框是否为空
		if (input_student_id.val()==""){
			$("#slider1-note-errors").fadeIn(1000);
			$("#slider1-note-errors h1").text("用户名不能为空！");
			input_student_id.css("border", "1px solid red");
			input_student_id.focus();
			return 0;
		}else if(input_password.val()==""){
			$("#slider1-note-errors").fadeIn(1000);
			$("#slider1-note-errors h1").text("密码不能为空！");
			input_password.css("border", "1px solid red");
			input_password.focus();
			return 0;
		}
		
		//判断两次输入的密码是否一致
		if(input_password.val() !== input_password_check.val()){
			$("#slider1-note-errors").fadeIn(1000);
			$("#slider1-note-errors h1").text("两次输入的密码不一致");
			input_password_check.css("border", "1px solid red");
			input_password_check.focus();
			return 0;
		}
		
		//判断用户名是否已经存在
		$.ajax({
			type:"POST",
			url:"check/",
			data:{
				'student_id':$("#student_id").val(),
				'password':$('#password').val(),
			},
			success: function(result){
				if(result==="true"){
					mySwiper.slideTo(1,1000,false);
				}
				else if(result==="false"){
					$("#slider1-note-errors").fadeIn(1000);
					$("#slider1-note-errors h1").text("用户名已经存在！");
					input_student_id.css("border", "1px solid red");
					input_student_id.focus();
				}
			},
		})
	});

	//给slider2-img添加点击事件
	$('#verificationCode').click(function () {
        // this.src="/Day14_jsp/Code?"+new Date().getTime();
		this.src="verificationCode/?"+new Date().getTime();
	});

	//给slider2中的input添加值改变事件
	$('.slider2-input').bind('input propertychange', function()
	{
		$("#slider2-note-errors").fadeOut(500);
		$(this).css("border","none");
	});

	//给slider2-submit添加点击事件
	$('#slider2-submit').click(function(){
		event.preventDefault();//去除本身的事件

		//判断name输入框是否为空
		if (input_name.val()===""){
			$("#slider2-note-errors").fadeIn(1000);
			$("#slider2-note-errors h1").text("姓名不能为空！");
			input_name.css("border", "1px solid red");
			input_name.focus();
			return 0;
		}

		//判断验证码是否正确
		$.ajax({
			type:"POST",
			url:"verificationCode/check/",
			data:{
				'name':input_name.val(),
				'code':input_VerificationCode.val(),
			},
			success: function(result){
				if(result==="true"){
					mySwiper.slideTo(2,1000,false);
				}
				else if(result==="false"){
					$("#slider2-note-errors").fadeIn(1000);
					$("#slider2-note-errors h1").text("验证码错误");
					input_VerificationCode.css("border", "1px solid red");
					input_VerificationCode.focus();
				}
			},
		})
	});
	//为slide3中的a标签添加鼠标移入移出事件
	$("#slider3-login-a").mouseenter(function(){
		$("#slider3-login").animate({
			backgroundColor:"rgba(255,255,255,0.4)",
			fontSize:"26px",
		},100);
	});
	$("#slider3-login-a").mouseout(function(){
		$("#slider3-login").animate({
			backgroundColor:"rgba(0,0,0,0)",
			fontSize:"25px",
		},100);
	});
});
