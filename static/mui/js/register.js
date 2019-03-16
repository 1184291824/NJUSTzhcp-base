$(document).ready(function () {
   mui.ready(function () {
       //缓存
       var input_student_id = $("#student_id");
       var input_password = $("#password");
       var input_password_check = $("#password_check");
       var input_name = $('#name');
       var input_class_id = $('#class-id');
       var input_VerificationCode = $('#VerificationCode');
       var verificationCode_img = $('#verificationCode');

       document.getElementById('button-register').addEventListener('tap', function () {
           if (input_student_id.val()===""){
               mui.alert('学号不能为空', '注意', '确定', function () {
                   input_student_id.focus();
               });
               return 0;
           }
           if (input_password.val()===""){
               mui.alert('密码不能为空', '注意', '确定', function () {
                   input_password.focus();
               });
               return 0;
           }
           if (input_password_check.val()!==input_password.val()){
               mui.alert('两次输入的密码不一致', '注意', '确定', function () {
                   input_password_check.val("").focus();
               });
               return 0;
           }
           if (input_name.val()===""){
               mui.alert('姓名不能为空', '注意', '确定', function () {
                   input_name.focus();
               });
               return 0;
           }
           if (input_class_id.val()===""){
               mui.alert('班级不能为空', '注意', '确定', function () {
                   input_class_id.focus();
               });
               return 0;
           }

           //判断验证码是否正确
           $.ajax({
               type:"POST",
               url:"mCheck/",
               data:{
                   'student_id': input_student_id.val(),
                   'password': input_password.val(),
                   'name':input_name.val(),
                   'class_id': input_class_id.val(),
                   'code':input_VerificationCode.val(),
               },
               success: function(result){
                   if(result==="true"){
                       mui.alert('注册成功！', '提示', '确定', function () {
                           mui.openWindow({
                               url: '../login/',
                           })
                       })
                   }
                   else if(result==="false"){
                       mui.alert('验证码错误', '提示', '确定', function () {
                           input_VerificationCode.val("").focus();
                           verificationCode_img[0].src="../verificationCode/?"+new Date().getTime();
                       })
                   }
                   else if(result==="StudentExist"){
                       mui.alert('您输入的学号已存在', '提示', '确定', function () {
                           input_student_id.val("").focus();
                           verificationCode_img[0].src="../verificationCode/?"+new Date().getTime();
                       })
                   }
                   else if(result==="ClassesDoesNotExist"){
                       mui.alert('您输入的班级不存在', '提示', '确定', function () {
                           input_class_id.val("").focus();
                           verificationCode_img[0].src="../verificationCode/?"+new Date().getTime();
                       })
                   }
                   },
           })
       })
   })
});