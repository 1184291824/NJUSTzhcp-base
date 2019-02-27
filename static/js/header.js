$(document).ready(function(){
	//登录和注册按钮效果
	$("#log-button a").mouseenter(function(){
		$(this).stop();
		$(this).animate({
			backgroundColor:"rgba(255,255,255,0.3)",
			fontSize:"21px",
		},500);
	});
	$("#log-button a").mouseout(function(){
		$(this).stop();
		$(this).animate({
			backgroundColor:"rgba(0,0,0,0)",
			fontSize:"20px",
		},500);
	});
});