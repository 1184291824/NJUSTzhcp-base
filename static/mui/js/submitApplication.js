mui.ready(function () {
    mui.init();
    //submitApplication
    let application_name = $('#application-name');
    let score = $('#score');
    let code = $('#verificationCode');
    //点击刷新验证码
    $('#verificationCode-img').click(function () {
        this.src="../verificationCode/?"+new Date().getTime();
    });

    //给submitApplication中的提交按钮添加事件
    mui(document.body).on('tap', '#submit-application', function(e) {
        if(application_name.val() === ''){
            mui.alert('申请名称不能为空', '提示', '确定', function () {
                application_name.focus();
            });
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
                if(result==="true"){
                    mui('.mui-btn').button('loading');
                    mui.alert('提交成功，即将跳回首页', '提示', '确定', function () {
                        $('.mui-input-group').submit();
                    });
                }
                else if(result==="false"){
                    mui.alert('验证码错误', '提示', '确定', );
                    $('#verificationCode-img')[0].src="../verificationCode/?"+new Date().getTime();
                }
            },
        })
    });
});