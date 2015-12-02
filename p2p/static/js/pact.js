; (function ($) {
    $(function () {
         var one_mess = null,
            pact_dialog = $("#pact-dialog"),
            dia_agreement = null,
            past_show = null;

         //一键签署
        var qianshuHtml = "<div id=\"dialog-message\" title=\"确认签署\">" +
            "<div class=\"agreement1\">" +
                "<p>使用一键签署，您需要阅读并同意所有待签署合同<input type=\"hidden\" id=\"hid_id\" value=\"0\"/></p>" +
                "<p class=\"int_chk\">" +
                    "<input type=\"checkbox\" id=\"int_checkbox\" /><label for=\"int_checkbox\">我已阅读并同意</label></p>" +
                "<p class=\"loading\"><a href=\"javascript:void(0)\" id=\"one-qianshu\" class=\"btn-base  past-show\">一键签署</a></p></div></div>";

        //签署完成
        var pactHtml ="<p class=\"ag-top\">签署成功</p>" +
                "<p class=\"ag-center\">" +
                    "<label id=\"lb-btn\">3</label>秒后退出</p>" +
                "<p><a href=\"#\" id=\"past-btn-true\" class=\"btn-base btn-chk  past-show\">确定</a></p>";

        //签署失败
        var errorHtml ="<p class=\"ag-top\">出错了，请稍后重试</p>" +
                "<p class=\"ag-center\">" +
                    "<label id=\"lb-btn\">3</label>秒后退出</p>" +
                "<p><a href=\"#\" id=\"past-btn-true\" class=\"btn-base btn-chk  past-show\">确定</a></p>";
      //签署中
        var pactloding="<a href=\"#\" class=\"btn-base btn-chk  past-show\">一键签署中<img src=\"/static/v1/images/common/loading_d.gif\" width=\"20px\" style=\"vertical-align: middle;margin-left: 3px;\" /></a>";

          //公用下拉菜单
    $(".j-click-qianshu").each(function(i, v) {
        var $t = $(this);
        $t.click(function() {
            $(pact_dialog).empty();
            $(pact_dialog).append(qianshuHtml);
            one_mess = $("#dialog-message");
            Open_dialog(one_mess);
            //隐藏域的值
            $("#hid_id").val($t.data("pos"));
        });
    });

        $("body").on("click", "#one-qianshu", function () {
            var id = $("#hid_id").val();
            if(id){
                if ($(this).hasClass("btn-chk")) {
                    $(".loading").empty();
                    $(".loading").append(pactloding);
                    $.ajax({
                        url:APP_ROOT+"/account/contsignajax/"+id+"?"+$.now(),
                        dataType:"json",
                        success:function(result){
                            dia_agreement = $(".agreement1");
                            $(dia_agreement).empty();
                            if(result.status == 1){
                                $(dia_agreement).append(pactHtml);
                                Countdown(3);
                            } else{
                                $(dia_agreement).append(errorHtml);
                                Countdown(3);
                            }
                        },
                        error:function(ajaxobj){
                        }
                   });
                }
            }
        });
        $("body").on("click", "#past-btn-true", function () {
            $(one_mess).dialog("close");
            location.reload();
        });
        //打开弹出层
        function Open_dialog(id) {
            $(id).dialog({
                //autoOpen: false,
                height: 245,
                width: 483,
                modal: true,
                dialogClass: "pact-tip",
                closeText:"关闭"
            });
            $(id).dialog("open");
        }

       //判断单选框是否选中
        $( "body" ).on( "dialogclose",one_mess, function( event, ui ) {
             $(one_mess).dialog( "destroy" );
        } );
        $("body").on("click", "#int_checkbox", function() {
            past_show = $(".past-show");
            if ($(this).prop("checked") == true) {
                $(past_show).addClass("btn-chk");
            } else {
                $(past_show).removeClass("btn-chk");
            }
        });
   //倒计时
        function Countdown(count) {
            var cdown;
            cdown = setInterval(onCountDown, 1000);
            function onCountDown() {
                count--;
                $("#lb-btn").html(count);
                if (count == 0) {
                    $(one_mess).dialog( "destroy" );
                    clearInterval(cdown);
                   // $(one_mess).dialog("close");
                    $(pact_dialog).empty();
                    location.reload();

                }
            }
        }
    });
})(jQuery);
