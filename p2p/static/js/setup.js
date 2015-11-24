;
(function($) {
    $(function() {
        (function() {
            // tooltip
            $(document).tooltip({
                track: true
            });
            var msglock = false;

            var popStr = "设置";

            // 短信验证弹出框
            $('#add_submit_btn').click(function() {
                getCode();


            });

            var popuoStr = '<div class="wee-send">\
            <div class="send-input">\
                <div class="error-box">\
                    <div class="error-wrap">\
                        <div class="e-text" style="width: 305px;">请填写6位数字验证码</div>\
                    </div>\
                </div>\
                <p>已向&nbsp;<span class="color_green">' + $(".mobile_num").html() + ' </span>&nbsp;发送验证短信</p>\
                <input type="text" class="ipt-txt w150" id="pop_code" placeholder="短信验证码" maxlength="10" value="">\
                <input type="button" id="action-send-code" class="reg-sprite btn-blue-h34 btn-gray-h34" value="发送">\
            </div>\
            </div>';
            //popup
            function popup() {

                if ($('.weedialog .dialog-content').length <= 0) {
                    $.weeboxs.open(popuoStr, {
                        boxid: null,
                        boxclass: 'ui_send_msg',
                        contentType: 'text',
                        showButton: true,
                        showOk: true,
                        okBtnName: '下一步',
                        showCancel: false,
                        title: popStr + '收货地址',
                        width: 463,
                        height: 125,
                        type: 'wee',
                        onclose: function() {

                        },
                        onok: function() {
                            var code = $(".ui_send_msg #pop_code").val();
                            var data = {
                                "code": code,
                                "sp": 1
                            };
                            var url = '/account/DeliveryPro';
                            $text = $(".ui_send_msg .error-box").find('.e-text'),
                                showError = function() {
                                    $(".ui_send_msg .error-box").css({
                                        'display': 'block',
                                        'visibility': 'visible'
                                    });
                                    $(".ui_send_msg .ipt-txt").addClass("err-shadow");
                                };

                            if (!/^\d{6}$/.test(code)) {
                                showError();
                                $text.html("请填写6位数字验证码");
                                return;
                            }
                            $.ajax({
                                url: url,
                                type: "post",
                                data: data,
                                dataType: "json",
                                beforeSend: function() {
                                    // $text.html("正在提交，请稍候...");
                                },
                                success: function(data) {
                                    // alert(JSON.stringify(data));
                                    if (data.errorCode == 1) {
                                        showError();
                                        $text.html(data.errorMsg);
                                    } else {
                                        $.weeboxs.close();
                                        location.href = "/account/delivery";
                                    }
                                },
                                error: function() {
                                    showError();
                                    $text.html("服务器错误，请重新再试！");
                                }
                            });
                            // $.weeboxs.close();
                        }
                    });
                } else {
                    $('.weedialog .dialog-content').html(popuoStr);
                }


            }

            // 点击“重新发送”按钮获取短信验证码
            $('body').on("click", "#action-send-code", function() {

                getCode();
            });

            function popup_1(str) {
                var word = (!!str ? str : '正在提交,请稍后...');
                var html = '';
                html += '<div class="wee-send">';
                html += '<div class="send-input">';
                html += '<div class="error-box">';
                html += '<div class="error-wrap">';
                html += '<div class="e-text" >' + word + '</div>';
                html += '</div>';
                html += '</div>';
                html += '<p></p>';
                html += '</div>';
                html += '</div>';
                if ($('.weedialog .dialog-content').length <= 0) {
                    $.weeboxs.open(html, {
                        boxid: null,
                        boxclass: 'weebox_send_msg',
                        showTitle: true,
                        contentType: 'text',
                        showButton: false,
                        showOk: true,
                        okBtnName: '完成注册',
                        showCancel: false,
                        title: '提交表单',
                        width: 250,
                        height: 120,
                        type: 'wee'
                    });
                } else {
                    $('.weedialog .dialog-content .e-text').html(word);
                }
            }

            var button = "";
            var errorSpan = "";
            var status = "";
            if ($("#add_submit_btn").text() == "修改") {
                status = 6;
                popStr = "修改";
            } else {
                status = 5;
            }

            function setProperty() {
                button = $(".ui_send_msg #action-send-code");
                bgGray();
                _reset();

            }

            var bgGray = function() {

                button.addClass("btn-gray-h34");
                button.val("正在获取中...");
                button.attr("disabled", "disabled");
            }

            var _set = function(msg) {
                var errorSpan = $(".ui_send_msg .error-box");
                errorSpan.css('visibility', 'visible');
                errorSpan.find('.e-text').html(msg);
                $(".ui_send_msg .ipt-txt").addClass("err-shadow");
            }

            var _reset = function() {
                var errorSpan = $(".ui_send_msg .error-box");
                errorSpan.css('visibility', 'hidden');
                errorSpan.find('.e-text').html('');
            }
            var timer = null;

            function updateTimeLabel(duration) {
                //var button = $(".ui_send_msg #action-send-code");
                var timeRemained = duration;
                //button.val(timeRemained + '秒后重新发送');
                timer = setInterval(function() {
                    button.val(timeRemained + '秒后重新发送');

                    timeRemained -= 1;
                    if (timeRemained == -1) {
                        clearInterval(timer);
                        msglock = false;
                        button.val('重新发送').removeAttr('disabled').removeClass("btn-gray-h34");
                    }
                }, 1000);
            }

            var callback = function(data) {
                //var button = $(".ui_send_msg #action-send-code");

                if (!msglock) {
                    updateTimeLabel(60, 'action-send-code');
                    msglock = true;
                }
                if (data.code != 1) {
                    _set(data.message);
                } else {
                    _reset();
                }


                //button.val('重新发送').removeAttr('disabled').removeClass("btn-gray-h34");
            }

            function getCode() {
                var data = {
                    "is_delivery": status
                };
                var getcodeUrl = '/index/EMCode';

                $.ajax({
                    url: getcodeUrl,
                    type: "post",
                    data: data,
                    dataType: "json",
                    beforeSend: function() {
                        //popup_1();
                    },
                    success: function(result) {
                        // alert(JSON.stringify(result));

                        //$(".dialog-mask").remove();
                        //$(".weebox_send_msg").remove();
                        if ($(".dialog-content").length <= 0) {
                            popup();
                        }

                        setProperty();
                        callback(result);
                    },
                    error: function() {

                    }
                });
            }
        })();



        //设置密保问题JS   
        (function() {


            var msglock = false;
            var button = null;
            function setProperty() {
                button = $(".ui_send_msg #ques-send-code");
                bgGray();
                _reset();

            };

            var bgGray = function() {

                button.addClass("btn-gray-h34");
                button.val("正在获取中...");
                button.attr("disabled", "disabled");
            };

            var _set = function(msg) {
                var errorSpan = $(".ui_send_msg .error-box");
                errorSpan.css('visibility', 'visible');
                errorSpan.find('.e-text').html(msg);
                $(".ui_send_msg .ipt-txt").addClass("err-shadow");
            };

            var _reset = function() {
                var errorSpan = $(".ui_send_msg .error-box");
                errorSpan.css('visibility', 'hidden');
                errorSpan.find('.e-text').html('');
            };

            var timer = null;

            function updateTimeLabel(duration) {
                //var button = $(".ui_send_msg #action-send-code");
                var timeRemained = duration;
                //button.val(timeRemained + '秒后重新发送');
                timer = setInterval(function() {
                    button.val(timeRemained + '秒后重新发送');

                    timeRemained -= 1;
                    if (timeRemained == -1) {
                        clearInterval(timer);
                        msglock = false;
                        button.val('重新发送').removeAttr('disabled').removeClass("btn-gray-h34");
                    }
                }, 1000);
            }

            var callback = function(data) {

                if (!msglock) {
                    updateTimeLabel(60);
                    msglock = true;
                }
                if (data.code != 1) {
                    _set(data.message);
                } else {
                    _reset();
                }
            }


            var id_html = '';
            id_html += '<div class="wee-pwp">';
            id_html += '<p class="pwp-decr font16">为了保证账户安全，设置密保问题前请先进行身份验证</p>';
            id_html += '<a href="javascript:;"  class="common-sprite btn-red-h46 j_valid_phone">验证手机号码</a>';
            id_html += '<a href="/account/ProtectAnswerPwd"  class="common-sprite btn-red-h46 mt20">回答密保问题</a>';
            id_html += '</div>';
            var popuoStr = '<div class="wee-send">\
             <div class="send-input">\
                 <div class="error-box">\
                     <div class="error-wrap">\
                        <div class="e-text" style="width: 305px;">请填写6位数字验证码</div>\
                        </div>\
                    </div>\
                    <p>已向&nbsp;<span class="color_green">' + $(".mobile_num").html() + ' </span>&nbsp;发送验证短信</p>\
                    <input type="text" class="ipt-txt w150" id="pop_code" placeholder="短信验证码" maxlength="10" value="">\
                    <input type="button" id="ques-send-code" class="reg-sprite btn-blue-h34 btn-gray-h34" value="发送">\
              </div>\
              </div>';
            var mibao_box = null,
                valid_box = null,
                getMsgCode = function(type) {
                    var getcodeUrl = '/account/protectionMobileCode',
                        data = {
                            type: type
                        };
                    $.ajax({
                        url: getcodeUrl,
                        data: data,
                        type: "post",
                        dataType: "json",
                        beforeSend: function() {},
                        success: function(result) {
                            showbox();
                            setProperty();
                            callback(result);
                        },
                        error: function() {

                        }
                    });
                },
                showbox = function() {
                    !!mibao_box && mibao_box.close();
                    !!valid_box && valid_box.close();
                    valid_box = $.weeboxs.open(popuoStr, {
                        boxid: null,
                        boxclass: 'ui_send_msg',
                        contentType: 'text',
                        showButton: true,
                        showOk: true,
                        okBtnName: '完成验证',
                        showCancel: false,
                        title: '验证手机号码',
                        width: 463,
                        height: 125,
                        type: 'wee',
                        onclose: function() {

                        },
                        onok: function() {
                            var code = $(".ui_send_msg #pop_code").val();
                            var data = {
                                "code": code,
                                "sp": 1
                            };
                            var url = '/account/DoCheckProtectionMobile';
                            $text = $(".ui_send_msg .error-box").find('.e-text'),
                                showError = function() {
                                    $(".ui_send_msg .error-box").css({
                                        'display': 'block',
                                        'visibility': 'visible'
                                    });
                                    $(".ui_send_msg .ipt-txt").addClass("err-shadow");
                                };

                            if (!/^\d{6}$/.test(code)) {
                                showError();
                                $text.html("请填写6位数字验证码");
                                return;
                            }
                            $.ajax({
                                url: url,
                                type: "post",
                                data: data,
                                dataType: "json",
                                beforeSend: function() {
                                    // $text.html("正在提交，请稍候...");
                                },
                                success: function(data) {
                                    // alert(JSON.stringify(data));
                                    if (data.errorCode === 0) {
                                        $.weeboxs.close();
                                        location.href = data.url;
                                    } else {
                                        showError();
                                        $text.html(data.errorMsg);
                                    }
                                },
                                error: function() {
                                    showError();
                                    $text.html("服务器错误，请重新再试！");
                                }
                            });
                            // $.weeboxs.close();
                        }
                    });

                },
                showwaybox = function() {
                    mibao_box = $.weeboxs.open(id_html, {
                        boxid: null,
                        boxclass: '',
                        contentType: 'text',
                        showButton: true,
                        showOk: false,
                        okBtnName: '',
                        showCancel: false,
                        title: '选择身份验证方式',
                        width: 455,
                        height: 192,
                        type: 'wee'
                    });
                };



            $('#pw_submit_button').click(function() {
                getMsgCode($(this).data("type"));
            });

            // 修改密保弹出框
            $('#pw_submit_button_01').click(function() {
                showwaybox();

            });

            //验证手机号码
            $("body").on("click", ".j_valid_phone", function() {
                getMsgCode(1);
            });

            $('body').on("click", "#ques-send-code", function() {
                getMsgCode(1);
            });

        })();
        // 设置密保短信验证弹出框
    });
})(jQuery);