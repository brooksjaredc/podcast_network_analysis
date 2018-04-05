jQuery(document).ready(function(e) {
	jQuery('.sub-menu-box.preview-mode').each(function(index, element) {
		var channel_content = '';
		var channel_count = 0;
        jQuery(this).find('.channel-content').each(function(index, element) {
			if(channel_count == 0){
				jQuery(this).addClass('active');
			}
            channel_content += jQuery(this)[0].outerHTML;
			jQuery(this).remove();
			channel_count++;
        });
		jQuery(this).append(channel_content);
    });    
	
	jQuery('.dropdown-mega > a').click(function(){return false;});
	
	if(navigator.userAgent.match(/(Android|iPod|iPhone|iPad|IEMobile|Opera Mini)/)){
		jQuery('.sub-menu-box .channel-title > a').bind('touchstart', function(event){
			var __this = jQuery(this);
			var __parents = __this.parents('.sub-menu-box');	
			var parentTouchStart = jQuery(this).parents('.channel-title');
			var target = "#" + parentTouchStart.attr("data-target");
			jQuery(".channel-content", __parents).removeClass("active");
			jQuery(target).addClass("active");
			return false;
		});
	}else{
		jQuery('.sub-menu-box .channel-title').hover(
			function(){
				var __this = jQuery(this);
				var __parents = __this.parents('.sub-menu-box');				
				var target = "#" + jQuery(this).attr("data-target");
				jQuery(".channel-content", __parents).removeClass("active");
				jQuery(target).addClass("active");
			},
			function(){}
		);
	};
});