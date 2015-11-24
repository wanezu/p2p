//初始化
;(function($) {
    $(function() {
		if( !!window.ActiveXObject && !window.XMLHttpRequest){
			  return;
		}
		var bool=true;
		$appDownload=$('<div class="layAppTop">\
		<div class="app">\
			<a class="app_btn" href="javascript:void(0)"></a>\
			<div class="app_box">\
				<i class="icon_a"></i>\
				<h2>扫码关注微信</h2>\
				<div class="app_tab">\
					<div class="app_tab_con"></div>\
					<ul>\
					<li class="app_ios">\
						<a href="https://itunes.apple.com/cn/app/di-yip2p/id853552412?mt=8" target="_blank" title="下载ios版"></a>\
					</li>\
					<li class="app_android">\
					<a href="http://www.firstp2p.com/down/apk" title="下载安卓版"></a>\
					</li>\
					</ul>\
				</div>\
			</div>\
		</div>\
		<a class="backToTop" href="javascript:void(0)"></a>\
		</div>').appendTo($("body")).hide();
		
			$('.app').hover(function(){
				$('.app_box').stop().show();				
				var $img = $("<img />");
				if(bool){
					bool=false;
					$img.attr("src","/Public/static/meiti/images/common/app_01.png");
					$(".app_tab_con").append($img);
					}				
			},function(){
				$('.app_box').stop().hide();
				})
			
        $backToTopEle = $('.backToTop').click(function() {
            $("html,body").animate({
                    scrollTop: 0
                },
                300);
        });
		
        $(window).bind("scroll resize",
            function() {
                var st = $(document).scrollTop(),
                    winh = $(window).height();
                (st > 0) ? $appDownload.fadeIn() : $appDownload.fadeOut();
                var wid = $(this).width();
                var backW = $('.layAppTop').width();
                if (wid < 1000) {
                    $('.layAppTop').css("right", 0)
                } else {
                    $('.layAppTop').css("right", 20)
                }
            });
    })
	
})(jQuery);
