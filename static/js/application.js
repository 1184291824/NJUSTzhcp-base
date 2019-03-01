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
});