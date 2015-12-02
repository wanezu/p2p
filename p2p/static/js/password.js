;(function($) {
    $(function() {
    	$("#old_password,#new_password,#re_new_password").each(function() {
            this.value = "";
        });
        var old_pas= $("#old_password");
        var new_pas= $("#new_password");
        var re_pas= $("#re_new_password");
        function getErTip(el){
            if(!(el instanceof jQuery)){
                el=$(el);
            }
            return el.next('.error_tip');
        }
        function old_pas_verify(){
            var inputVal=$(this).val();
            var errorTip=getErTip(this);
            var returnVal=false;
            if(inputVal.length==0){
                errorTip.text('旧密码不能为空');
            }else if(inputVal.length<5 || inputVal.length>25){
                errorTip.text('旧密码长度为5-25位');
            }else{
                returnVal=true;
            }
            return returnVal;
        }
        // function new_pas_verify(){
        //     return pas_strength_mod.blurFn(true);
        // }
        function re_pas_verify(){
            var inputVal=$(this).val();
            var errorTip=getErTip(this);
            var returnVal=false;
            if(inputVal.length==0){
                errorTip.text('密码不能为空');
            }else if(new_pas.val()!=inputVal){
                errorTip.text('确认密码和新密码不一致');
            }else{
                returnVal=true;
            }
            return returnVal;
        }
        old_pas.on({
            'focus':function(){
                getErTip(this).text("");
            },
            'blur':function(){
                old_pas_verify.call(this);
            }
        });
        new_pas.blur(function(){
            var re_pas_val=re_pas.val();
            var inputVal=$(this).val();
            var re_pas_tip=getErTip(re_pas);
            if(pas_strength_mod.blurFn(true)){
                if(!/^\s*$/.test(re_pas_val)){
                    if(inputVal!=re_pas_val){
                        re_pas_tip.text('确认密码和新密码不一致');
                    }else{
                        re_pas_tip.text('');
                    }
                }
            }
        });
        re_pas.on({
            'focus':function(){
                getErTip(this).text("");
            },
            'blur':function(){
                if(!pas_strength_mod.blurFn()){
                    return;
                }
                re_pas_verify.call(this);
            }
        });
        function valid(){
            var returnVal=true;
            if(!old_pas_verify.call(old_pas.get(0))){
                returnVal=false;
            }
            // if(!new_pas_verify()){
            //     returnVal=false;
            // }
            if(!re_pas_verify.call(re_pas.get(0))){
                returnVal=false;
            }
            return returnVal;
        }
        $("#modify").submit(function() {
            if (!valid()) {
                return false;
            } else {
                return true;
            }
        });
    });
})(jQuery);

//密码强度验证
var pas_strength_mod;
(function(){
    $(function(){
        var pasInput=$('#new_password');
        var jQJson={
            input:pasInput,
            strengthWrap:pasInput.nextAll('.pass-item-tip-password')
        }
        pas_strength_mod=new Pas_strength(jQJson);
    })
})();

