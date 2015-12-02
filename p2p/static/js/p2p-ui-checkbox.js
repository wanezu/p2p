/*
 * p2p-ui-checkbox - jQuery plugin for p2p-ui-checkbox
 * author snowNorth
 * Version:  1.0
 * 兼容性检查 ie7+
 * html结构
    <div class="p2p-ui-checkbox">
    <a href="javascript:void(0)" data-ui="checkbox" [data-val="定义值 默认为1"]></a>
    <span>说明</span>
    <input type="hidden" name="name" >
    </div>
* css
    //css部分
    // .p2p-ui-checkbox .common-sprite{display:inline-block;background-image: url(../images/common/btn_icon.png); background-repeat:no-repeat}
    // .p2p-ui-checkbox .check-normal{background-position:0 -250px;}
    // .p2p-ui-checkbox .check-normal:hover{background-position:-30px -250px; }
    // .p2p-ui-checkbox .check-select{background-position:-59px -250px; }
    // .p2p-ui-checkbox .check-select:hover{background-position:-88px -250px; }
    // .p2p-ui-checkbox .check-disable{background-position:-116px -250px; cursor:text;}
    // .p2p-ui-checkbox .check-normal,.check-select,.check-disable{width: 15px;height: 15px;}
*/

(function($, window, document, undefined) {

    $.fn.p2pUiCheckbox = function(options) {
        //多选组件 
        var defaults = {
            checked: "check-select", //选中样式
            disabled: "check-disable", //disable样式
            val_checked: "1", //选中值
            val_unchecked: "0"//不选中值
        };
        var opts = $.extend(defaults, options);
        this.each(function(i, el) {
            var ele = $(el);
            var checkbox = ele.find('a[data-ui=checkbox]');
            var input = ele.find("input");
            var val_checked = checkbox.attr("data-val") || opts.val_checked;
            var val_unchecked = checkbox.attr("data-val") ? "" : opts.val_unchecked;

            if (!input.length) {
                return;
            }

            input = input.eq(0);
            if (input.val() == val_checked ) {
                checkbox.removeClass(opts.checked);
                checkbox.addClass(opts.checked);
            }

            if (input.attr("disabled")) {
                checkbox.removeClass(opts.disabled);
                checkbox.addClass(opts.disabled);
            }
            ele.click(function(e) {
                if (checkbox.hasClass(opts.disabled)) {
                    return;
                }
                var el = e.srcElement || e.target;
                if (el.tagName !== "A" && el.tagName !== "SPAN") {
                    return;
                } else if (el.tagName === "A" && !el.getAttribute("data-ui")) {
                    return;
                }
                checkbox.toggleClass(opts.checked);
                checkbox.hasClass(opts.checked) ? input.val(val_checked) : input.val(val_unchecked);
                //添加change事件触发
                input.change();
            });
        });
    };

})(jQuery, window, document);
