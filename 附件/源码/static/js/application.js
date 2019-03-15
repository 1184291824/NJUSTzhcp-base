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


	//myActivity页面
	//给每一行表格添加点击效果，点击之后出现详细信息
	$('.myActivity-base').click(function () {
		$(this).next().fadeToggle('fast');
	});


});

//reviewApplicationDetail
$(document).ready(function () {
	let reviewApplication_input = $('#reviewApplication-input');
	reviewApplication_input.click(function () {
		$.ajax({
			url: '../submit/',
			type: 'POST',
			data: {
				'pk': $('#application-pk').text(),
				'status': $('#reviewApplication-review').attr('value'),
			},
			success: function (result) {
				reviewApplication_input.css('background-color','green');
			}
		})
	});
});


//UISwitch部分
$(document).ready(function(){
	let switch_num = false;
	$("#switchBase").click(function(){
		if(switch_num === false){
			$("#switchThumb").animate({left:"21px"},"fast");
			$("#switchBase").css({
				"background-color":"#00ff00",
				"border-color":"#00ff00"});
			switch_num = true;
			$('#reviewApplication-review').attr('value','True');
			$('#reviewApplication-review').text('允许申请');
		}
		else{
			$("#switchThumb").animate({left:"0"},"fast");
			$("#switchBase").css({
				"background-color":"rgba(0,0,0,0)",
				"border-color":"darkgray"});
			switch_num = false;
			$('#reviewApplication-review').attr('value','False');
			$('#reviewApplication-review').text('拒绝申请');
		}
	});
});
