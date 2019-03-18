mui.ready(function() {
    if ($('#identity').text()!=='captain'){
        $('.a-captain')[0].addEventListener('tap', function () {
            mui.alert('您的身份不是班长', '权限出错', '确定');
        })
    }
    if ($('#identity').text()!=='teacher'){
        $('.a-teacher')[0].addEventListener('tap', function () {
            mui.alert('您的身份不是老师', '权限出错', '确定');
        })
        $('.a-teacher')[1].addEventListener('tap', function () {
            mui.alert('您的身份不是老师', '权限出错', '确定');
        })
    }
    mui('.mui-button-row').on('tap', '#button-logout', function () {
        mui.confirm('退出登录？', '提示', ['确定','取消'],function (button) {
            if (button['index']===0){
                $(location).attr('href', '../logout/');
            }
        });
    });
     /*
     * 隐藏滚动条
     */
     var Fun_App = {
    delscroll: function(){
        plus.webview.currentWebview().setStyle({
            scrollIndicator: 'none',
        });
    },  }
});