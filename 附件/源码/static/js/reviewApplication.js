$(document).ready(function () {
    //reviewApplication页面
	let reviewApplication_title = $('.reviewApplication-title');
	let reviewApplication_title_bar = $('.reviewApplication-title-bar');
	let reviewApplication_title_bar_left = reviewApplication_title_bar.position().left;
	// let reviewApplication_title_bar_left = reviewApplication_title.position().left+reviewApplication_title.width()/2-32;
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
				$('#'+reviewApplication_tbody_id).html("<tr><td colspan='100'><h1>无内容</h1></td></tr>");
			}
		}
	});
});