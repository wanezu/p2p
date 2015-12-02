//TODO 密码格式和强弱程度
function Pas_strength(jQJson,extraOptS,calBackJson){
    this.input=jQJson['input'];//监听的密码输入框
    this.strengthWrap=jQJson['strengthWrap'];//密码强度浮动层
    this.type=parseInt(jQJson['input'].data('stretype'));//0表示注册密码，1表示修改密码
    this.calBackJson={//回调函数json格式对象
        'keyup':null,
        'focus':null,
        'blur':null
    }
    var defaults = {};
    this.settings=$.extend({},defaults,extraOptS);//额外参数和默认参数合并
    this.calBackJson=$.extend({},defaults,calBackJson);
    this.init();//立即执行init初始化函数
}
Pas_strength.prototype={
    regObj:{//构造器静态属性
        'num':'[0-9]',
        'lowerLetter':'[a-z]',
        'upperLetter':'[A-Z]',
        'letter':'[a-zA-Z]',
        'symbol':'[`~!@#\$%\^&\*\(\)\\-_\+=<>\?:\"{},\.\/;\'\[\\]|\\\\]'
    },
    init:function(){
        this.bindDomEvent();
    },
    getInputVal:function(){//返回input输入框内容
        return this.input.val();
    },
    isRuo:function(pasStr){//判断是否是弱密码,true表示是,false表示不是
        var regStr="";
        var returnVal=false;
        var regObj=this.regObj;
        regStr='(^'+regObj.num+'+$)'+'|(^'+regObj.letter+'+$)'+'|(^'+regObj.symbol+'+$)';
        //console.log(regStr);
        var newReg=new RegExp(regStr);
        if(pasStr.length<6){
            returnVal=true;
        }
        if(newReg.test(pasStr) && pasStr.length<9){
            returnVal=true;
        }
        return returnVal;
    },
    isQi:function(pasStr){//是否是强密码
        var returnVal=false;
        var regObj=this.regObj;
        var regArr=[regObj.num,regObj.lowerLetter,regObj.upperLetter,regObj.symbol];
        var validCount=0;
        for(var i= 0,max=regArr.length;i<max;i++){
            if(new RegExp(regArr[i]+'+').test(pasStr)){
                validCount++;
            }
        }
        if(validCount==4 && pasStr.length>=9 && pasStr.length<=20){
            returnVal=true;
        }
        if(validCount==3 && pasStr.length>=12 && pasStr.length<=20){
            returnVal=true;
        }
        return returnVal;
    },
    tipLevelFn:function(span,text){
        var className='';
        switch (text){
            case '低':{
                className='color-low';
                break;
            }
            case '中':{
                className='color-mid';
                break;
            }
            case '高':{
                className='color-high';
                break;
            }
        }
        span.removeClass('color-low color-mid color-high').addClass(className);
        span[0].innerHTML = text;
    },
    /**
     * 表单提示
     * @param  {String} callType 调用类型
     * @param ｛number} flag true表示成功，false表示失败
     * @param ｛String} textTip 要显示的文案，错误文案提示或成功时密码强度
     */
    tipFn:function(callType,flag,textTip){
        var _this=this;
        var type=this.type;//0表示注册密码，1表示修改密码
        var input=this.input;
        var errorObj=null;//错误提示盒子
        var iconObj=null;//对号提示盒子
        var iconLevelSpan=null;//提示时密码强度对应的span
        var inputPar=input.parent();
        //debugger;
        if(type==0){//如果是注册密码时
            errorObj=inputPar.nextAll('.error-wrap:first');
            iconObj=inputPar.nextAll('.er-icon:first');
        }else if(type==1){//如果是修改密码时
            errorObj=input.nextAll('.error_tip:first');
            iconObj=input.nextAll('.color-gray2:first');
        }else if(type==2){
            errorObj=input.nextAll('.error-inline:first');
            iconObj=input.nextAll('.color-gray2:first');
        }
        var setters={
            'hide':function(){
                //console.log('hide');
                errorObj.add(iconObj).hide();
            },
            'show':function(flag,textTip){
                if(type==0){//如果是注册密码时
                    if(flag){
                        iconObj.html('<i class="form-sprite icon-right"></i><span>密码安全程度：<span></span></span>');
                        iconLevelSpan=iconObj.find('span span');
                        _this.tipLevelFn(iconLevelSpan,textTip);
                        iconObj.show();
                    }else{
                        errorObj.find('.e-text').text(textTip);
                        errorObj.show();
                    }
                }else if(type==1){//如果是修改密码时
                    if(flag){
                        iconLevelSpan=iconObj.find('span');
                        _this.tipLevelFn(iconLevelSpan,textTip);
                        iconObj.show();
                    }else{
                        errorObj.text(textTip);
                        errorObj.show();
                    }
                }else if(type==2){//如果是找回密码时
                    if(flag){
                        iconLevelSpan=iconObj.find('span');
                        _this.tipLevelFn(iconLevelSpan,textTip);
                        iconObj.show();
                    }else{
                        errorObj.text(textTip);
                        errorObj.show();
                    }
                }
            }
        }
        var args = Array.prototype.slice.apply(arguments, [1]);
        setters[callType].apply(this,args);
    },
    bindDomEvent:function(inputPar){
        var pasStr="";
        var input;
        if(typeof inputPar!="undefined"){
            input=this.input=inputPar;
        }else{
            input=this.input;
        }

        var Wrap=this.strengthWrap;
        var _this=this;//局部保留this指针
        //input=$('#input-password');
        //debugger;
        input.on({
            'keyup keydown':function(){
                pasStr=_this.getInputVal();
                _this.pasPanel(pasStr);
                if(_this.calBackJson.keyup!=null){//keyup事件的回调接口
                    _this.calBackJson.keyup(input);
                }
            },
            'focus':function(){
                pasStr=_this.getInputVal();
                Wrap.show();
                _this.tipFn('hide');
                //_this.tipFn('show',1,'高');
                //debugger;
                _this.pasPanel(pasStr);
                if(_this.calBackJson.focus!=null){//focus事件的回调接口
                    _this.calBackJson.focus(input);
                }
            }
        })
    },
    pasPanel:function(pasStr){
        //debugger;
        var volidArr=[];//pasVolid(pasStr)函数返回的错误数组
        var pwdChecklist=this.strengthWrap.find('#pwd-checklist');
        var levelSpans=pwdChecklist.find('.process');//标识安全等级的3个span
        var volidLis=pwdChecklist.find('.pwd-checklist-item');//标识合法性的3个li
        var levelTextSpan=pwdChecklist.find('.ml4');//密码强度文案提示

        //密码强度
        levelSpans.removeClass('middle low high');
        levelTextSpan.removeClass('color-low color-mid color-high');
        //密码合法性
        volidLis.removeClass().addClass('pwd-checklist-item');
        if(pasStr.length==0){//密码为空时立即返回
            volidLis.addClass('pwd-checklist-item-normal');
            this.tipLevelFn(levelTextSpan,'');
            return;
        }
        switch (this.pasLevel(pasStr)){
            case 0:{
                this.tipLevelFn(levelTextSpan,'低');
                levelSpans.filter(':lt(1)').addClass('low');
                break;
            }
            case 1:{
                this.tipLevelFn(levelTextSpan,'中');
                levelSpans.filter(':lt(2)').addClass('middle');
                break;
            }
            case 2:{
                //debugger;
                this.tipLevelFn(levelTextSpan,'高');
                levelSpans.filter(':lt(3)').addClass('high');
                break;
            }
        }


        if (this.pasValid(pasStr) == 0) {
            volidLis.addClass('pwd-checklist-item-success');
        }else{
            volidArr=this.pasValid(pasStr);
            for(var i= 1;i<=3;i++){
                //debugger;
                if($.inArray(i,volidArr)!=-1){
                    volidLis.eq(i-1).addClass('pwd-checklist-item-error');
                }else{
                    volidLis.eq(i-1).addClass('pwd-checklist-item-success');
                }
            }
        }
    },
    pasLevel:function(pasStr){//判断密码强度
        if(this.isRuo(pasStr)){
            return 0;
        }
        if(this.isQi(pasStr)){
            return 2;
        }
        return 1;
    },
    /**
     * 密码是否合法
     * @param ｛string} pasStr
     * @returns {number} 0表示合法，返回数组表示不合法,1,2,3分别表示第一个，第二个，第三个错误
     */
    pasValid:function(pasStr){
        var regStr="";
        var returnArr=[];
        var flag=true;
        var regObj=this.regObj;
        regStr=function(){
            var regArr=[regObj.num,regObj.letter,regObj.symbol];
            var regStr="[^";
            for(var i= 0,max=regArr.length;i<max;i++){
                regStr=regStr+regArr[i].substr(1,regArr[i].length-2);
            }
            regStr=regStr+']';
            //debugger;
            return regStr;
        }();
        if(pasStr.length<6||pasStr.length>20){
            returnArr.push(1);
            flag=false;
        }
        if(new RegExp(regStr).test(pasStr.replace(/\s*/g,''))){
            returnArr.push(2);
            flag=false;
        }
        if(/\s+/.test(pasStr)){
            returnArr.push(3);
            flag=false;
        }
        if(flag){
            this.isValid=true;
            return 0;
        }else{
            this.isValid=false;
            return returnArr;
        }
    },
    pasAjax:function(pasStr,isAsync,callBack){//向后台发ajax验证密码合法性
        //验证密码是否在黑名单
        var type=this.type;
        var dataJson=null;
        if (type ==0 || type ==2) {
            dataJson = {
                //pwd:'123',
                pwd: pasStr,
                mobile: $('#input-mobile').val()
            }
        } else if(type==1){
            dataJson = {
                //pwd:'123',
                pwd: pasStr,
                flag:"1"
            }
        }
        // $.ajax({
        //     type: "post",
        //     data: dataJson,
        //     url: '/index/PasswordCheck',
        //     dataType: "json",
        //     async: isAsync,
        //     success: function (data) {
        //         callBack(data);
        //     }
        // });
    },
    blurFn:function(isTip){//失去焦点时触发的函数
        var pasStr=this.getInputVal();
        var volidResult=this.pasValid(pasStr);
        var returnVal=false;
        var Wrap=this.strengthWrap;
        Wrap.hide();
        var tipJson={
            'flag':false,
            'text':''
        }
        if(volidResult==0){
            this.pasAjax(pasStr,false,function(data){
                // if(data.errorCode == 0){
                    alert(45454);
                    returnVal=true;
                    tipJson.flag=true;
                // }
                tipJson.text=data.errorMsg;
            });
        }else{
            if(pasStr.length==0){
                tipJson.text='密码不能为空';
            }else{
                switch (volidResult[0]){
                    case 1:{
                        tipJson.text='登录密码为6~20位';
                        break;
                    }
                    case 2:{
                        tipJson.text='登录密码不允许包含特殊符号';
                        break;
                    }
                    case 3:{
                        tipJson.text='登录密码不允许包含空格';
                        break;
                    }
                    default :{
                        tipJson.text='登录密码不正确';
                    }
                }
            }
        }
        if(isTip){
            this.tipFn('show',tipJson.flag, tipJson.text);
        }
        return returnVal;
    }
}

