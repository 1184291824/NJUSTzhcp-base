$(document).ready(function(){
	let menu_option = $('.menu-option');
	let identity_text = $('#identity').text();
	let menu_option_5 = $('#menu-option-5');
	let menu_option_6 = $('#menu-option-6');
	let main = $('.main');

	// 给main添加移入效果
	main.slideDown(1000);

	// 给菜单中的选项方块添加鼠标移入和移出事件
	menu_option.mouseenter(function(){
		$(this).css('background-color','rgba(255,255,255,0.2)');
	});
	menu_option.mouseleave(function(){
		$(this).css('background-color','rgba(0,0,0,0.3)');
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
});