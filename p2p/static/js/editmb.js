//初始化
(function($) {
    $(function() {

        // 表单验证
        $('#password-form').validator({
            rules: {
                validN: [/^\d{6}$/, '请填写6位数字验证码']
            },
            fields: {
                code: "验证码: required;validN;"
            }
        });
        //控制获取验证码
        var msglock = false;
        var button = $("#bt");
        var errorSpan = $("#code-err");
        function setProperty() {
            bgGray();
            _reset();
        };
        var bgGray = function() {
            button.addClass("btn-send-gray");
            button.val("正在获取中...");
            button.attr("disabled", "disabled");
        };
        var _set = function(msg) {
            html = '<span class="msg-wrap n-error" role="alert"><span class="n-icon"></span><span class="n-msg">' + msg + '</span></span>';
            errorSpan.css('display', 'block');
            errorSpan.find('.n-msg').html(html);
            $('#validNum').addClass("n-invalid");
        };
        var _reset = function() {
            errorSpan.css('display', 'none');
            errorSpan.find('.n-msg').html('');
            $('#validNum').removeClass("n-invalid");
        };
        var timer = null;
        function updateTimeLabel(duration) {
            var timeRemained = duration;
            timer = setInterval(function() {
                button.val('重新发送(' + timeRemained + ')');
                timeRemained -= 1;
                if (timeRemained == -1) {
                    clearInterval(timer);
                    msglock = false;
                    button.val('重新发送').removeAttr('disabled').removeClass("btn-send-gray");
                }
            }, 1000);
        }
        var callback = function(data) {
            if (!msglock) {
                updateTimeLabel(180);
                msglock = true;
            }
            if (data.code != 1) {
                _set(data.message);
            } else {
                _reset();
            }
        }

        // 获取并验证手机验证码
        var getMsgCode = function() {
            var getcodeUrl = '/user/EMCode',
                data = {
                    "is_edit": 1
                };
            $.ajax({
                url: getcodeUrl,
                data: data,
                type: "post",
                dataType: "json",
                beforeSend: function() {},
                success: function(result) {
                    setProperty();
                    callback(result);
                },
                error: function() {

                }
            });
        }
        $("#bt").bind('click', function() {
            getMsgCode();
        });
    });
})(jQuery);