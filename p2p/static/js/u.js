var testValue = function() {
        if(!/^(\d+|\d+\.|\d+\.\d{1,2})$/.test($("#Jcarry_amount").val())){
            $("#Jcarry_balance").html("请输入正确的数字格式且仅包含两位小数");
            //修复无输入金额是 显示空白
                var newMoney =foramtmoney($("#Jcarry_totalAmount").val(),2);
                $("#Jcarry_acount_balance").text(newMoney+"元");
                return false;
        }else{
               return true;
        }
    };
jQuery(function() {
    
    $("#Jcarry_amount").keyup(function() {
        setCarryResult()
    });
    $("#Jcarry_amount").blur(function() {
        setCarryResult()
    });
    $("#Jcarry_bank_id").change(function() {
        if ($(this).val() == "other") {
            $("#Jcarry_otherbank").removeClass("hide");
            $('.otherbank-content').show();
            $("#Jcarry_bankSuggestNote").addClass("f_red");
            $("#Jcarry_bankSuggestNote").html("其他银行的提现时间约为3-5个工作日,建议使用推荐的银行进行提现操作。");
        } else {
            $("#Jcarry_otherbank").addClass("hide");
            $('.otherbank-content').hide();
            $("#Jcarry_otherbank").val("");
            $("#Jcarry_bankSuggestNote").removeClass("f_red");
            if ($(this).find("option:selected").attr("day") != undefined)
                $("#Jcarry_bankSuggestNote").html("提现时间约为" + $(this).find("option:selected").attr("day") + "个工作日。");
            else
                $("#Jcarry_bankSuggestNote").html("提现时间约为3个工作日。");
        }
    });

    $("#Jcarry_otherbank").change(function() {
        $("#Jcarry_bankSuggestNote").removeClass("f_red");
        if ($(this).find("option:selected").attr("day") != undefined)
            $("#Jcarry_bankSuggestNote").html("提现时间约为" + $(this).find("option:selected").attr("day") + "个工作日。");
        else
            $("#Jcarry_bankSuggestNote").html("提现时间约为3个工作日。");
    });

    $('.user_button').removeAttr('disabled');   
    $("#Jcarry_From").submit(function() {
        if(!testValue()){
            return false;
        }
        if ($.trim($("#Jcarry_amount").val()) == "" || !$.checkNumber($("#Jcarry_amount").val()) || parseFloat($("#Jcarry_amount").val()) <= 0) {
            $.showErr(LANG.CARRY_MONEY_NOT_TRUE, function() {
                $("#Jcarry_amount").focus();
            });
            return false;
        }
        if (parseFloat($("#Jcarry_acount_balance_res").val()) < 0) {
            $.showErr(LANG.CARRY_MONEY_NOT_ENOUGHT, function() {
                $("#Jcarry_acount_balance_res").focus();
            });
            return false;
        }

        if ($("#Jcarry_region_lv4").val() == "0") {
            $.showErr("请选择开户行所在地", function() {
                $("#Jcarry_region_lv4").focus();
            });
            return false;
        }
        $(this).find(".user_button").css("background" , "#e8ebf2").attr("disabled" , "disabled");
        return true;
    });
    $("#Jcarry_From_2").submit(function() {
        //处理提示语
        var location_url = window.location.href;
        var title_tips = '添加银行卡信息不成功';
        if (location_url) {
            if (location_url.indexOf('editorBank') != '-1') {
                title_tips = '修改银行卡信息不成功';
            }
        }
        //
        if ($("#Jcarry_real_name").val() == "") {
            $.showErr("请输入开户名", function() {
                $("#Jcarry_real_name").focus();
            }, title_tips);
            return false;
        }
        if ($("#Jcarry_bank_id").val() == "") {
            $.showErr(LANG.PLASE_ENTER_CARRY_BANK, function() {
                $("#Jcarry_bank_id").focus();
            }, title_tips);
            return false;
        }
        if ($("#Jcarry_bank_id").val() == "other" && $("#Jcarry_otherbank").val() == "") {
            $.showErr(LANG.PLASE_ENTER_CARRY_BANK, function() {
                $("#Jcarry_bank_id").focus();
            }, title_tips);
            return false;
        }

        if ($("#Jcarry_region_lv4").val() == "0") {
            $.showErr("请选择开户行所在地", function() {
                $("#Jcarry_region_lv4").focus();
            }, title_tips);
            return false;
        }

        if ($("#Jcarry_bankzone").val() == "") {
            $.showErr("请输入开户行网点", function() {
                $("#Jcarry_bankzone").focus();
            }, title_tips);
            return false;
        }

        //长度限制
        if ($("#Jcarry_bankzone").val().length > 30) {
            $.showErr("开户行网点内容长度不能超过30个字符", function() {
                $("#Jcarry_bankzone").focus();
            }, title_tips);
            return false;
        }

        if ($.trim($("#Jcarry_bankcard").val()) == "") {
            $.showErr(LANG.PLASE_ENTER_CARRY_BANK_CODE, function() {
                $("#Jcarry_bankcard").focus();
            }, title_tips);
            return false;
        }
        if ($.trim($("#Jcarry_rebankcard").val()) == "") {
            $.showErr(LANG.PLASE_ENTER_CARRY_CFR_BANK_CODE, function() {
                $("#Jcarry_rebankcard").focus();
            }, title_tips);
            return false;
        }
        if ($.trim($("#Jcarry_bankcard").val()) != $.trim($("#Jcarry_rebankcard").val())) {
            $.showErr(LANG.TWO_ENTER_CARRY_BANK_CODE_ERROR, function() {
                $("#Jcarry_rebankcard").focus();
            }, title_tips);
            return false;
        }
        return true;
    });
});

function tips(input, msg, top, left) {
    var tip = '<div class="cashdraw_tips" style="top: ' + top + 'px; left:' + left + 'px; display: block;"><div class="cashdraw_tip_header"></div><div class="cashdraw_tip_body_container"><div class="cashdraw_tip_body"><div class="cashdraw_tip_content">' + msg + '</div></div></div></div>';
    $("#imgtips").after(tip);
    input.onmouseout = function() {
        setTimeout(function() {
            $(".cashdraw_tips").remove()
        }, 500);
    }
}

function setCarryResult() {
    if(!testValue()){
        return;
    }
    var carry_amount = 0;
    var total_amount = parseFloat($("#Jcarry_totalAmount").val());
    $("#Jcarry_balance").html("");
    //过滤字符输入
    if ( !! $("#Jcarry_amount").val() && isNaN(parseFloat($("#Jcarry_amount").val()))) {
        $("#Jcarry_balance").html("请输入合法数字");
        return;
    } else if ($('#Jcarry_amount').val().indexOf('-') != -1) { //负数处理  edit caolong 2014-1-24
        $("#Jcarry_balance").html("请输入正整数");
        return;
    }

    if ($.trim($("#Jcarry_amount").val()).length > 0) {

        if ($("#Jcarry_amount").val() == "-") {
            carry_amount = "-0";
        } else {
            carry_amount = parseFloat($("#Jcarry_amount").val());
        }
    }

    if (!(carry_amount > 0)) {
        $("#Jcarry_balance").html(LANG.CARRY_MONEY_NOT_TRUE);
        //return;//注释掉 js最后一位的处理
    }
    //else if ((carry_amount * 100 % 1) > 0) { editor caolong 2014-1-13 
    else if ($('#Jcarry_amount').val().lastIndexOf('.') != '-1') {
        var amount_length = $('#Jcarry_amount').val().substr($('#Jcarry_amount').val().lastIndexOf('.') + 1);
        if (amount_length.length > 2) {
            $("#Jcarry_balance").html(LANG.CARRY_MONEY_DECIMAL);
            return;
        }
    } else if (carry_amount > total_amount) {
        $("#Jcarry_balance").html(LANG.CARRY_MONEY_NOT_ENOUGHT);
        //当提现金额大于账号金额时输出负值
        $("#Jcarry_acount_balance").text(foramtmoney(total_amount - carry_amount, 2) + " 元");
        //$("#Jcarry_acount_balance").text("0.00元");
        return;
    } else if (carry_amount == 0) {
        $("#Jcarry_balance").html(LANG.MIN_CARRY_MONEY);
        return;
    }

    var fee = 0;
    if (carry_amount > 0 && carry_amount < 20000) {
        fee = 0; //免手续费
    }
    if (carry_amount >= 20000 && carry_amount < 50000) {
        fee = 0;
    }
    if (carry_amount >= 50000) {
        fee = 0;
    }

    if (carry_amount + fee > total_amount) {
        $("#Jcarry_balance").html(LANG.CARRY_MONEY_NOT_ENOUGHT);
    }
    //  $("#Jcarry_fee").html(foramtmoney(fee,2)+" 元");
    //  var realAmount = carry_amount+fee;
    //$("#Jcarry_realAmount").val(foramtmoney(realAmount,2)+" 元");
    var acount_balance = total_amount - carry_amount - fee;
    //$("#Jcarry_acount_balance_res").val(foramtmoney(acount_balance,2));
    $("#Jcarry_acount_balance").text(foramtmoney(acount_balance, 2) + " 元");
}

//格式化金钱

function foramtmoney(price, len) {
    len = len > 0 && len <= 20 ? len : 2;
    price = parseFloat((price + "").replace(/[^\d\.-]/g, "")).toFixed(len) + "";
    var l = price.split(".")[0].split("").reverse(),
        r = price.split(".")[1];
    t = "";
    for (i = 0; i < l.length; i++) {
        t += l[i] + ((i + 1) % 3 == 0 && (i + 1) != l.length ? "," : "");
    }
    var re = t.split("").reverse().join("") + "." + r;
    return re.replace("-,", "-");
}
