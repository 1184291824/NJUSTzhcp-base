mui.ready(function () {
	mui('.login-from').on('tap', '#button-login', function(){
		// console.log('tap!');
		event.preventDefault();
		$.ajax({
			type:"POST",
			url:"check/",
			data:{
				'student_id':$("#student_id").val(),
				'password':$('#password').val(),
			},
			success: function(result){
				// console.log('success!');
				if(result==="true"){
					$(location).attr('href', '/zhcp/index/');
				}else if(result==="passwordWrong"){
					mui.alert('用户名或密码错误！', '错误', '确认', function () {
						$('#password').val("").focus();
						// $('#password').focus();
					})
				}else if(result==="idDoesNotExist"){
					mui.alert('用户名不存在！', '错误', '确认', function () {
						$('#student_id').val("").focus();
					})
				}
			},
		});
	});
});