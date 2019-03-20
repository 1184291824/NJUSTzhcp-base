mui.init();
(function($) {
    $('.mui-scroll-wrapper').scroll({
        indicators: true, //是否显示滚动条
        deceleration: 0.0004, //阻尼系数,系数越小滑动越灵敏
    });
})(mui);
mui('.mui-slider-right').on('tap', '.mui-btn', function() {
    let pk = $(this).parent().parent('.mui-table-view-cell').attr('id');
    if ($(this).attr('class') === 'mui-btn mui-btn-success') {
        mui.confirm('请问您确定通过这个申请吗', '提示', ['确定', '我手滑了'], function(choice) {
            if (choice['index'] === 0) {
                $.ajax({
                    url: 'submit/',
                    type: 'POST',
                    data: {
                        'pk': pk,
                        'status': 'True',
                    },
                    success: function () {
                        mui.alert('提交成功', '提示', '确定', function () {
                            location.reload();
                        });
                    },
                })
            }
        });
    } else if ($(this).attr('class') === 'mui-btn mui-btn-danger') {
        mui.confirm('请问您确定拒绝这个申请吗', '提示', ['确定', '我手滑了'], function(choice) {
            if (choice['index'] === 0) {
                $.ajax({
                    url: 'submit/',
                    type: 'POST',
                    data: {
                        'pk': pk,
                        'status': 'False',
                    },
                    success: function () {
                        mui.alert('提交成功', '提示', '确定', function () {
                            location.reload();
                        });
                    },
                })
            }
        });
    }
    else if ($(this).attr('class') === 'mui-btn mui-btn-warning') {
        mui.openWindow('detail/?pk='+pk)
    }
});