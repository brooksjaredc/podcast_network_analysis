;(function($){
	
	var woocommerce_quantity_buttons = function(){
		var $ = jQuery;
		$( 'div.quantity:not(.buttons_added), td.quantity:not(.buttons_added)' ).addClass( 'buttons_added' ).append( '<input type="button" value="+" id="add1" class="plus" />' ).prepend( '<input type="button" value="-" id="minus1" class="minus" />' );
		$('.buttons_added #minus1').click(function(e) {
			var value = parseInt(jQuery(this).next().val()) - 1;
			if(value>0){
				jQuery(this).next().val(value);
			}
		});
		$('.buttons_added #add1').click(function(e) {
			var value = parseInt(jQuery(this).prev().val()) + 1;
			jQuery(this).prev().val(value);
		});
	}
		
	$(document).ready(function() {
		woocommerce_quantity_buttons();
		
		$(document.body).on('updated_cart_totals', function(){
			woocommerce_quantity_buttons();
		});
		
		$(window).on('scroll', function(){
			scrollFunc();
		});
		
		$.each($('.no-bottom'),function(){
			if($(this).parent().hasClass('main-top-sidebar-wrap')){
				$(this).parent().addClass('no-bottom');
			}
		});
		
		$('#showfullcontentnow').on('click', function(){
			$(this).hide();
			$('.cactus-sidebar-control.sb-right.post-live-comment .main-content-col .body-content').addClass('showfull');			
		});
		
		//ToolTip enable
		function showTollTips(){
			if($('.action-like').length > 0) {
				$('.action-like').find('.jlk').attr({'data-toggle':'tooltip', 'data-placement':'top', 'data-original-title':$('.action-like').parents('.like-button').attr('data-like')});
			};
			if($('.action-unlike').length > 0) {
				$('.action-unlike').find('.jlk').attr({'data-toggle':'tooltip', 'data-placement':'top', 'data-original-title':$('.action-like').parents('.like-button').attr('data-unlike')});
			};
			$('[data-toggle="tooltip"]').tooltip();//.tooltip('show'); for dev
		};
		showTollTips();
		
		/*Focus scroll video submit*/
		$('.submit-video[data-target="#submitModal"]').on('click', function(){
			$('#submitModal input[name="your-email"]').focus();
			$(window).resize();
			setTimeout(function(){$('#submitModal input[name="your-email"]').focus();$(window).resize();},550);
		});
		/*Focus scroll video submit*/
		
		//Open search main menu
		$('.navbar-default .open-search-main-menu').on('click', function(){
			$this = $(this);
			if($this.hasClass('close-sb')) {
				$this.parents('.navbar-default').find('.search-main-menu').removeClass('active');
				setTimeout(function(){$this.parents('.navbar-default').find('.search-main-menu').find('input[type="text"]').blur();},300);	
				$this.removeClass('close-sb');
				
			}else{
				$this.parents('.navbar-default').find('.search-main-menu').addClass('active');
				setTimeout(function(){$this.parents('.navbar-default').find('.search-main-menu').find('input[type="text"]').focus();},300);	
				$this.addClass('close-sb');
				console.log('open')
			};
		});
		//Open search main menu
		
		/*Fix menu hover in mobile*/
		var $menuMobileTouch = $('.navbar-nav:not(.open-menu-mobile-top):not(.search-drop-down):not(.open-menu-mobile) li>a');
		$menuMobileTouch.on('touchstart', function(e){
			var $this = $(this);
			if($this.parent('li').find('ul').length > 0 && !$this.hasClass('no-go-to-touch')){
				$menuMobileTouch.removeClass('no-go-to-touch');
				$this.addClass('no-go-to-touch');
				return false;
			};
		});
		/*Fix menu hover in mobile*/
		
		//Headline
		var cactusMyHeadline = [];
		$('.cactus-headline').each(function(index, element) {
			cactusMyHeadline[index] = $(this).find('.cactus-swiper-container').swiper({
				direction:'vertical',
				loop: true,
				slidesPerView:1,
				autoplay:5000,
                grabCursor: true
			});
			$('.button-next', $(this)).on('click', function(){cactusMyHeadline[index].slideNext()});
			$('.button-prev', $(this)).on('click', function(){cactusMyHeadline[index].slidePrev()});
            
            $(this).find('.cactus-swiper-container').mouseover(function(){cactusMyHeadline[index].stopAutoplay()}).mouseout(function(){cactusMyHeadline[index].startAutoplay()});
		});			
		//Headline
		
		//Open Top menu mobile
		$('#top-nav .navbar-nav.open-menu-mobile-top>li>a').on('click', function(){
			if($(this).parents('li').hasClass('active')){
				$(this).parents('li').removeClass('active');			
			}else{	
				$(this).parents('li').addClass('active');							
			};
		});	
		
		$('.open-menu-mobile-top > li > ul.dropdown-menu').on('click', function(event){
			if(event.pageX < $(this).offset().left) {
				if($(this).parents('li').hasClass('active')){
					$(this).parents('li').removeClass('active');			
				}else{	
					$(this).parents('li').addClass('active');							
				};
			};
		});	
		//Open Top menu mobile
		
		//Open Main menu mobile	
		$(".open-menu-mobile-rps>a").on('click', function(){
			$('body').addClass('open-mobile-menu-ct');			
			return;
		});
		//Open Main menu mobile
		
		/*Close Main menu mobile*/
		$("#off-canvas .close-canvas-menu, .canvas-ovelay").on('click', function(){
			$('body').removeClass('open-mobile-menu-ct');
			return;
		});
		/*Close Main menu mobile*/
		
		/*Sticky Menu*/
		if($('input[name="sticky_navigation"]').length > 0) {
			if($('input[name="sticky_navigation"]').val()=='on') {
				$('#main-menu').css({'min-height':$('#main-menu > .navbar-default:not(.cactus-sticky-menu)').height()});
				var st = $(window).scrollTop();
				if(($('#main-menu').offset().top + $('#main-menu').height()) < st) {
					$('#main-menu .navbar.navbar-default')
					.addClass('cactus-sticky-menu')
					.css({'top':((window.innerWidth>600)?$('#wpadminbar').height():0)+'px', 'transform':'translateY(-100%)', '-ms-transform':'translateY(-100%)', '-webkit-transform':'translateY(-100%)', 'transition':'none', '-webkit-transition':'none', 'margin-top':'-100%'});							
				};
				$(window).on('scroll', function(){	
					if($('#main-menu .navbar.navbar-default:not(.no-open-sticky)').length>0) {								
						st = $(window).scrollTop();
						if(__cactus_check_updown<0){ //down						
							if(($('#main-menu').offset().top + $('#main-menu').height()) < st) {
								if($('#main-menu .navbar.navbar-default').hasClass('fix-down-scroll')) {
									$('#main-menu .navbar.navbar-default')
									.addClass('cactus-sticky-menu')
									.css({'top':((window.innerWidth>600)?$('#wpadminbar').height():0)+'px', 'transform':'translateY(0)', '-ms-transform':'translateY(0)', '-webkit-transform':'translateY(0)', 'transition':'none', '-webkit-transition':'none', 'margin-top':'0'});
								}else{
									$('#main-menu .navbar.navbar-default')
									.addClass('cactus-sticky-menu')
									.css({'top':((window.innerWidth>600)?$('#wpadminbar').height():0)+'px', 'transform':'translateY(-100%)', '-ms-transform':'translateY(-100%)', '-webkit-transform':'translateY(-100%)', 'transition':'none', '-webkit-transition':'none', 'margin-top':'-100%'});	
								};
							};
						}else{
							if(($('#main-menu').offset().top) >= st && $('#main-menu .navbar.navbar-default').hasClass('cactus-sticky-menu')) {
								$('#main-menu .navbar.navbar-default')
								.removeClass('cactus-sticky-menu')
								.removeAttr('style');
							}else{
								$('#main-menu .navbar.navbar-default').css({'transform':'translateY(0)', '-ms-transform':'translateY(0)', '-webkit-transform':'translateY(0)', 'transition':'none', '-webkit-transition':'none', 'margin-top':'0'});
							};
						};
					};
				});
			};
		};
		/*Sticky Menu*/
		var pow=Math.pow, floor=Math.floor, abs=Math.abs, log=Math.log;

		function round(n, precision) {
			var prec = Math.pow(10, precision);
			return Math.round(n*prec)/prec;
		}
		
		function get_formatted_string_number(n) {
			var base = floor(log(abs(n))/log(1000));
			var suffix = 'kmb'[base-1];
			return suffix ? round(n/pow(1000,base),2)+suffix : ''+n;
		}
		/*Like action*/		
		function setClickLike(obj){
			var $this = obj;
			var $valOldLike = $this.parents('.watch-action').find('[class*=lc-]span.lc').text().replace('+','');
			var $valOldunLike = $this.parents('.watch-action').find('[class*=unlc-]span.unlc').text().replace('-','');
			setTimeout(function(){
				var interValLike = setInterval(function(){
					
					var $valLike = $this.parents('.watch-action').find('[class*=lc-]span.lc').text().replace('+','');
					var $valunLike = $this.parents('.watch-action').find('[class*=unlc-]span.unlc').text().replace('-','');
					
					if($valOldLike==$valLike && $valOldunLike==$valunLike) {clearInterval(interValLike); return;}
					
					$('.like-dislike .like').html('<i class="fa fa-thumbs-up"></i>&nbsp; '+get_formatted_string_number(parseInt($valLike)));
					$('.like-dislike .dislike').html('<i class="fa fa-thumbs-down"></i>&nbsp; '+get_formatted_string_number(parseInt($valunLike)));
                    
                    // for mobile display
                    $('.lc', $this).text(get_formatted_string_number(parseInt($valLike)));
                    $('.unlc', $this).text(get_formatted_string_number(parseInt($valunLike)));
					
					if(!$this.parents('.watch-action').find('.status').hasClass('loading-img')) {
						if($this.attr('data-task')=='like'){
							$('<style>[data-post_id="'+$this.attr('data-post_id')+'"][data-task="like"]:before {color:#222222 !important;} [data-post_id="'+$this.attr('data-post_id')+'"][data-task="unlike"]:before {color:rgba(153,153,153,1.0) !important;}</style>').appendTo('head');
							$('[data-post_id="'+$this.attr('data-post_id')+'"][data-task="like"]').addClass('change-icon');
							$('[data-post_id="'+$this.attr('data-post_id')+'"][data-task="unlike"]').removeClass('change-icon');
						}else{
							$('<style>[data-post_id="'+$this.attr('data-post_id')+'"][data-task="unlike"]:before {color:#222222 !important;} [data-post_id="'+$this.attr('data-post_id')+'"][data-task="like"]:before {color:rgba(153,153,153,1.0) !important;</style>').appendTo('head');
							$('[data-post_id="'+$this.attr('data-post_id')+'"][data-task="unlike"]').addClass('change-icon');
							$('[data-post_id="'+$this.attr('data-post_id')+'"][data-task="like"]').removeClass('change-icon');
						};
						
						var $percentBar = parseInt($valLike)/(parseInt($valLike)+parseInt($valunLike)) * 100;
						if($percentBar==0) {$percentBar=50;}
						$('.cactus-like-bar > span').css('width',$percentBar+'%');												
						clearInterval(interValLike);
						return false;
					};
				},50);				
			},500);
		};
		
		$('.share-tool-block.like-button:not(.like-dislike-on-mobile) .action-like > .jlk, .share-tool-block.like-button:not(.like-dislike-on-mobile) .action-unlike > .jlk').on('click', function(){		
			setClickLike($(this));
		});
		/*Like action*/
		
		/*Open slider carousel*/
		function openCarouselListing(index) {
			var element = $('article.cactus-single-content');
			if(index!=null && typeof(index)!='undefined') {element = $('article.cactus-single-content').eq(index)};
			element.each(function(index, element) {
				var $this = $(this);
				$('.open-carousel-listing', $this).off('click');				
                $('.open-carousel-listing', $this).on('click', function(){	
							
					if($('.cactus-transition-open', $this).hasClass('active')) {
						$('.cactus-transition-open', $this).removeClass('active');
						$('.open-carousel-listing', $this).removeClass('active');
					}else{
						$('.cactus-transition-open', $this).addClass('active');
						$('.open-carousel-listing', $this).addClass('active');
					};
				});
            });
			
		};	
		openCarouselListing(0);
		/*Open slider carousel*/
		
		/*Open sharing single*/
		function openShareSingle(index){
			var element = $('article.cactus-single-content');
			if(index!=null && typeof(index)!='undefined') {element = $('article.cactus-single-content').eq(index)};
			
			element.each(function(index, element) {
				var $this = $(this);
				$('.open-cactus-share', $this).off('click');
				
				$('.open-cactus-share', $this).on('click', function(){
					if($(this).hasClass('active')) {
						$(this).removeClass('active');
						$(this).parents('.cactus-share-and-like').find('.social-listing.list-inline').removeClass('active');
					}else{
						$(this).addClass('active');
						$(this).parents('.cactus-share-and-like').find('.social-listing.list-inline').addClass('active');
					};
				});	
			});
			
		};
		openShareSingle(0);
		/*Open sharing single*/
		
		/*Function create Carousel*/
		function __cactusCreateCarousel(elements, index, sliderArray, perview, paginationName){
			var $this = elements;
						
			$this.find('.pagination').attr('data-target', paginationName+'-'+index);
			
			function checkWidthSlide(){
				var defaultWidth = $this.find('.swiper-slide:first-child > .cactus-post-item').outerWidth();			
				$this.find('.swiper-slide').width(defaultWidth);				
			};
			
			checkWidthSlide();
			
			function fixHeightSlider(trabs){
				var topHeight = [];						
				if($this.find('.swiper-slide').find('.cactus-post-item').length > 0) {
					for(var iz=0; iz<$this.find('.swiper-slide').length;iz++){							
						topHeight[iz] = $this.find('.swiper-slide').eq(iz).height();								
					};
					topHeight.sort(function(a, b){return b-a});
				};
				if(perview==1 && $this.find('.post-style-gallery-content').length > 0) {					
					topHeight[0] = $this.find('.swiper-slide.swiper-slide-active').find('.img-content').height();
				};	
				if(perview==1 && $this.find('.testimonials').length > 0) {					
					topHeight[0] = $this.find('.swiper-slide.swiper-slide-active').find('.cactus-testimonials-wrap').height();
				};
				if(trabs==0){								
					$this.find('.swiper-wrapper').height(topHeight[0]);
				}else{
					$this.find('.swiper-wrapper').animate({height:topHeight[0]},500);
				};
				
				if(paginationName=='gall-light-box'){
					$('#cactus-lightbox-caption-content-'+index).css({'padding-top':(window.innerHeight - topHeight[0]) / 2});	
					var intContentWidth	= $('.post-style-gallery-content', $this).width();
					var intImgWidth		= $('.swiper-slide-visible.swiper-slide-active .img-content img', $this).width();
					var fixPositionArrow=10;
					if(intContentWidth >= intImgWidth) {					
						fixPositionArrow = (($('.post-style-gallery-content', $this).width() - $('.swiper-slide.swiper-slide-active .img-content img', $this).width() )/2 + 10);
					};
					$('.post-style-gallery > span', '#cactus-lightbox-caption-content-'+index).css({'right':fixPositionArrow+'px'});
				};
			};
			
			function createSlider(){
				
				sliderArray = $('.cactus-swiper-container', $this).swiper({
					slidesPerView: perview,
					loop:false,
					calculateHeight:true,
					loopedSlides:($this.width() >= 768)?3:2,
					speed:paginationName=='gall-light-box'?600:500,
					grabCursor:true,
					paginationClickable: true,
					pagination: '.pagination[data-target="'+paginationName+'-'+index+'"]',					
					roundLengths:true,
					onInit:function(){						
						fixHeightSlider(0);
						if(paginationName=='testimonials'){				
							$('.pre-carousel, .next-carousel', $this).css({'margin-top':$('.swiper-slide.swiper-slide-active .cactus-testimonials', $this).outerHeight()+'px'});
						};
					}, 
					onSlideChangeStart:function(){						
						fixHeightSlider(1);	
						if(paginationName=='gall-light-box'){
							$('#cactus-lightbox-caption-content-'+index+' .caption-number').text((sliderArray.activeIndex+1)+'/'+$('.swiper-slide:not(.swiper-slide-duplicate)', '#cactus-lightbox-caption-content-'+index).length);
						};	
						if(paginationName=='testimonials'){				
							$('.pre-carousel, .next-carousel', $this).css({'margin-top':$('.swiper-slide.swiper-slide-active .cactus-testimonials', $this).outerHeight()+'px'});
						};				
					},							
					// progress:paginationName=='gall-light-box'?true:false,
					// onProgressChange: function(swiper){
					// 	if(paginationName=='gall-light-box') {
					// 		for (var i = 0; i < swiper.slides.length; i++){
					// 			var slide = swiper.slides[i];
					// 			var progress = slide.progress;
					// 			var translate = progress*swiper.width;  
					// 			var opacity = 1 - Math.min(Math.abs(progress),1);
					// 			slide.style.opacity = opacity;
					// 			swiper.setTransform(slide,'translate3d('+translate+'px,0,0)');
					// 		};
					// 	};
					// },
					// onTouchStart:function(swiper){
					// 	if(paginationName=='gall-light-box') {
					// 		for (var i = 0; i < swiper.slides.length; i++){
					// 			swiper.setTransition(swiper.slides[i], 0);
					// 		};
					// 	};
					// },
					// onSetWrapperTransition: function(swiper, speed) {
					// 	if(paginationName=='gall-light-box') {
					// 		for (var i = 0; i < swiper.slides.length; i++){
					// 			swiper.setTransition(swiper.slides[i], speed);
					// 		};
					// 	};
					// },	
				});
				
				if(paginationName=='testimonials') {
					var checkAutoPlay = 0;
					sliderArray.paramsautoplayDisableOnInteraction=false;
					var intAutoPlayTest = $this.attr('data-autoplay');
					if(intAutoPlayTest!='' && intAutoPlayTest!=null && typeof(intAutoPlayTest)!='undefined' && intAutoPlayTest=='1') {
						function isNumber(n) {return !isNaN(parseFloat(n)) && isFinite(n);};
						var intAutoPlaySpeed = $this.attr('data-speed');
						if(!isNumber(intAutoPlaySpeed)) {intAutoPlaySpeed=5000;}
						sliderArray.params.autoplay=intAutoPlaySpeed;
						sliderArray.startAutoplay();
						
						$this.on({
							mouseenter: function(){
								checkAutoPlay=1;
								sliderArray.stopAutoplay();							
							}, 
							mouseleave: function(){		
								checkAutoPlay=0;					
								if(sliderArray.activeIndex == sliderArray.slides.length-1){
									sliderArray.stopAutoplay();
									setTimeout(function(){sliderArray.swipeTo(0, 1000); sliderArray.startAutoplay();},intAutoPlaySpeed);
								}else{
									sliderArray.startAutoplay();
								};
							}
						});
						
						sliderArray.params.onSlideChangeEnd = function(){
							if(checkAutoPlay == 0){
								if(sliderArray.activeIndex == sliderArray.slides.length-1){
									sliderArray.stopAutoplay();
									setTimeout(function(){sliderArray.swipeTo(0, 1000); sliderArray.startAutoplay();},intAutoPlaySpeed);
								};
							};							
							$this.on({
								mouseenter: function(){
									sliderArray.stopAutoplay();								
								},
								mouseleave: function(){
									if(sliderArray.activeIndex == sliderArray.slides.length-1){
										sliderArray.stopAutoplay();
										setTimeout(function(){sliderArray.swipeTo(0, 1000); sliderArray.startAutoplay();},intAutoPlaySpeed);
									};								
								}
							});							
						};		
					};
				};
				
				$this.find('.next-carousel').on('click', function(){
					if(paginationName=='testimonials') {sliderArray.stopAutoplay();};					
					if(sliderArray.activeIndex==(sliderArray.slides.length-1) 
					|| ((sliderArray.activeIndex+2)==(sliderArray.slides.length-1) && $('.swiper-slide.swiper-slide-visible', $this).length==3) 
					|| ((sliderArray.activeIndex+1)==(sliderArray.slides.length-1) && $('.swiper-slide.swiper-slide-visible', $this).length==2)){
						sliderArray.slideTo(0);						
					}else{
						sliderArray.slideNext();
					};	
				});			
				$this.find('.pre-carousel').on('click', function(){
					if(paginationName=='testimonials') {sliderArray.stopAutoplay();};
					if(sliderArray.activeIndex==0){							
						sliderArray.slideTo(sliderArray.slides.length-1);					
					}else{
						sliderArray.slidePrev();
					};	
				});
				
				$this.find('.btn-next').on('click', function(){					
					if(sliderArray.activeIndex==(sliderArray.slides.length-1)){
						sliderArray.slideTo(0);						
					}else{
						sliderArray.slideNext();
					};	
				});			
				$this.find('.btn-prev').on('click', function(){
					if(sliderArray.activeIndex==0){							
						sliderArray.slideTo(sliderArray.slides.length-1);					
					}else{
						sliderArray.slidePrev();
					};	
				});
				
				if(paginationName=='gall-light-box') {						
					$cactusSwiperGalleryLightBoxPost[index]=sliderArray;
				};
				
				function resizeWidthSlide(){
					var dpr = window.devicePixelRatio;
					if(typeof dpr =='undefined') { dpr = 1;};
					dpr = 1;
					var width = window.innerWidth * dpr;
					
					// sliderArray.appendSlide('<div class="swiper-slide"><div class="cactus-post-item hentry"></div></div>');
									
					if	(width >= 768){
						$this.find('.swiper-slide').width($this.find('.cactus-swiper-container').width()/3);
						sliderArray.params.loopedSlides=3;
					}else if(width >= 480){
						$this.find('.swiper-slide').width($this.find('.cactus-swiper-container').width()/2);
						sliderArray.params.loopedSlides=2;
					}else{
						$this.find('.swiper-slide').width($this.find('.cactus-swiper-container').width());
						sliderArray.params.loopedSlides=1;
					};
					
					if(perview==1 && $this.find('.post-style-gallery-content').length > 0) {
						sliderArray.params.loopedSlides=1;
					};
					
					// sliderArray.removeLastSlide();	
					fixHeightSlider(0);
					
					if(sliderArray.activeIndex > 0) {
						sliderArray.slideTo(0, 500);
					};
					
					if($this.find('.swiper-slide.swiper-slide-visible').length == sliderArray.slides.length && paginationName=='rela') {
						$this.find('.next-carousel').hide();
						$this.find('.pre-carousel').hide();
					}else{
						$this.find('.next-carousel').show();
						$this.find('.pre-carousel').show();
					};
					
					if($this.find('.swiper-slide').length < 2 && paginationName=='gall-light-box') {
						$this.find('.btn-prev').hide();
						$this.find('.btn-next').hide();
					}else{
						$this.find('.btn-prev').show();
						$this.find('.btn-next').show();
					};
									
					sliderArray.update();
					sliderArray.onResize();
				};
						
				resizeWidthSlide();
				setTimeout(function(){
					resizeWidthSlide();
				},368);	
				
				var _df_width = $(window).width();
				$(window).on('resize', function(){
					if($(window).width()!=_df_width){	
						if(paginationName=='gall-light-box') {						
							// for(var k=0; k < sliderArray.slides.length; k++){
							// 	sliderArray.setTransition(sliderArray.slides[k], 0);
							// };	
							$('.swiper-wrapper', $this).stop(true,true).css('transition-duration','0s');
							sliderArray.update();
							sliderArray.onResize();
						};
						resizeWidthSlide();		
						setTimeout(function(){
							resizeWidthSlide();
						},368);	
						
						_df_width = $(window).width();
					};
				});
				
			};	
			
			createSlider();
		};	
		/*Function create Carousel*/
		
		/*carousel related post*/
		var $cactusSwiperRelatedPost = [];
		$('.cactus-related-posts').each(function(index, element) {
			__cactusCreateCarousel($(this), index, $cactusSwiperRelatedPost[index], 'auto', 'rela');			
		});
		/*carousel related post*/
		
		/*carousel listing*/
		var $cactusSwiperCarouselPost = [];
		$('.cactus-listing-carousel').each(function(index, element) {
			__cactusCreateCarousel($(this), index, $cactusSwiperCarouselPost[index], 'auto', 'carPos');			
		});	
		/*carousel listing*/
		
		/*carousel listing*/
		var $cactusSwiperGalleryPost = [];
		$('.post-style-gallery').each(function(index, element) {
			__cactusCreateCarousel($(this), index, $cactusSwiperGalleryPost[index], 1, 'gall');			
		});	
		/*carousel listing*/
		
		/*Prev + next video*/
		function setOffsetButtonVideo(){
			var dpr = window.devicePixelRatio;
			if(typeof dpr =='undefined') { dpr = 1;};
			dpr = 1;
			var ct_width = window.innerWidth * dpr;
			$('.cactus-change-video').removeAttr('style').removeClass('active');
			if(ct_width>=1600) {
				var width = $(window).width();
				
				$('.cactus-change-video').each(function(index, element) {
										
					if($(this).hasClass('cactus-new')) {
						$(this).css({'margin-right':(width - (width - $(this).offset().left) + ($(this).outerWidth(true)-$(this).outerWidth()) )+'px'});
					};
					
					if($(this).hasClass('cactus-old')) {
						$(this).css({'margin-left':(width - $(this).outerWidth() - $(this).offset().left + ($(this).outerWidth(true)-$(this).outerWidth()) )+'px'});
					};	
									
					$(this).addClass('active');
				});
			}else{
				$(this).removeAttr('style');
			};
		};
		setTimeout(setOffsetButtonVideo,368);		
		/*Prev + next video*/
		
		var scrollBarIndex=[];
		$('.video-listing-content').each(function(index, element) {
			var $this=$(this);
			scrollBarIndex[index] = $this;
			scrollBarIndex[index].mCustomScrollbar({
				theme:"light-2",
				onInit: function(){
				},			
			});	
			
			for(var iz=0; iz<=$this.find('.cactus-widget-posts-item').length; iz++) {
				if($this.find('.cactus-widget-posts-item').eq(iz).hasClass('active')){
					scrollBarIndex[index].mCustomScrollbar("scrollTo", ($this.find('.cactus-widget-posts-item').eq(iz).outerHeight(true)*(iz))+'px');
					$('.total-video span', $this.parents('.cactus-video-list-content')).text( (iz+1)+'/'+$this.find('.cactus-widget-posts-item').length );
				};
			};		
			$this.parents('.cactus-video-list-content').find('.user-header').on('click', function(){				
				if($this.parents('.cactus-video-list-content').find('.fix-open-responsive').hasClass('active')) {
					$this.parents('.cactus-video-list-content').find('.fix-open-responsive').removeClass('active');
					$(this).removeClass('active');
				}else{
					$this.parents('.cactus-video-list-content').find('.fix-open-responsive').addClass('active');
					$(this).addClass('active');
				};				
			});				
			
		});
		/*Playlist scroll*/
		
		/*light box*/
		var $cactusSwiperGalleryLightBoxPost = [];	
		function setLightBoxGroup(index){
			var element = $('article.cactus-single-content');
			if(index!=null && typeof(index)!='undefined') {element = $('article.cactus-single-content').eq(index);};
			var defaultIndex = index;
			
			element.each(function(index) {	
						
				if($('.body-content > .wp-caption', element).length > 0 && $('#cactus-lightbox-caption-content-'+defaultIndex).length==0) {
					$(
					'<div id="cactus-lightbox-caption-content-'+defaultIndex+'">'+
					
						'<div class="modal-container">'+
						'</div>'+
						
						'<div class="post-style-gallery">'+
							'<span><i class="fa fa-times"></i></span>'+
							'<!--<a class="pre-carousel" href="javascript:;"><i class="fa fa-angle-left"></i></a>'+
							'<a class="next-carousel" href="javascript:;"><i class="fa fa-angle-right"></i></a>-->'+
							'<div class="btn-prev"><i class="fa fa-chevron-left"></i></div>'+
							'<div class="btn-next"><i class="fa fa-chevron-right"></i></div>'+
							'<div class="pagination"></div>'+
							'<div class="post-style-gallery-content">'+
								'<div class="cactus-swiper-container">'+
									'<div class="swiper-wrapper">'+
									'</div>'+
								'</div>'+


							'</div>'+		
						'</div>'+
						
					'</div>'
					).appendTo('body');
					
					$('#cactus-lightbox-caption-content-'+defaultIndex+' > .post-style-gallery > span, #cactus-lightbox-caption-content-'+defaultIndex+' > .modal-container').on('click', function(){
						$('#cactus-lightbox-caption-content-'+defaultIndex).removeClass('active');
					});
				};				
				$('.body-content > .wp-caption', element).each(function(index) {					
					var $this = $(this);
					
					// get full image URL
					var href = $this.find('img').attr('src');
					if($this.find('a').length > 0 && $this.find('a').attr('href') != ''){
						href = $this.find('a').attr('href');
						if(!href.endsWith('.jpg') && href.endsWith('.png') && href.endsWith('.jpeg') && href.endsWith('.gif')){
							href = $this.find('img').attr('src');
						}
					}
					
					$(
						'<div class="swiper-slide">'+
							'<div class="img-content">'+						
								'<span><img src="' + href + '">'+
								'<div class="thumb-gradient"></div><div class="caption-text">'+$this.find('.wp-caption-text').text()+'</div><div class="caption-number"></div></span>'+
							'</div>'+
						'</div>'
					).appendTo('#cactus-lightbox-caption-content-'+defaultIndex+' .swiper-wrapper');
					$this.on('click', function(){
						$('#cactus-lightbox-caption-content-'+defaultIndex).addClass('active');
						return false;
					});
				});
				
							
				if($('.body-content > .wp-caption', element).length > 0 && $('#cactus-lightbox-caption-content-'+defaultIndex).length>0) {		
						
					__cactusCreateCarousel($('#cactus-lightbox-caption-content-'+defaultIndex+' > .post-style-gallery'), defaultIndex, $cactusSwiperGalleryLightBoxPost[defaultIndex], 1, 'gall-light-box');
					$('.body-content > .wp-caption', element).each(function(index, element) {
						var $this=$(this);						
						$this.on('click', function(){
							
							$('#cactus-lightbox-caption-content-'+defaultIndex).addClass('active');
							$cactusSwiperGalleryLightBoxPost[defaultIndex].slideTo(1,0);
							$cactusSwiperGalleryLightBoxPost[defaultIndex].slideTo(index,0);
							$('#cactus-lightbox-caption-content-'+defaultIndex+' .caption-number').text(($cactusSwiperGalleryLightBoxPost[defaultIndex].activeIndex+1)+'/'+$('.swiper-slide:not(.swiper-slide-duplicate)', '#cactus-lightbox-caption-content-'+defaultIndex).length);
							return false;
						});
					});
				};		
				
			});
		};
		setLightBoxGroup(0);		
		/*light box*/
		
		/*Sidebar fixed*/
		function _fixedSidebar(index, checkScroll) {
			var element = $('.cactus-sidebar-control');
			if(index!=null && typeof(index)!='undefined') {element = $('.cactus-sidebar-control').eq(index)};
			element.each(function(index, element) {
				var $this_item = $(this);
				var defaultOffsetTop = $this_item.find('.main-content-col').offset().top;	 	//top			
				var defaultOffsetBottom = $this_item.offset().top + $this_item.outerHeight();	//bottom	
							
				var myFixed = $this_item.find('.sidebar-content-fixed-scroll.fixed-now');
				if(myFixed.length > 0 && window.innerWidth>991) {
					var defaultOffsetleft = myFixed.offset().left;
					var intWidth = myFixed.width();
					var intHeight = myFixed.outerHeight();
					
					var heightForAbsolute = $this_item.find('.main-content-col').outerHeight();
					if($this_item.find('.main-sidebar-col').outerHeight() > $this_item.find('.main-content-col').outerHeight()) {
						heightForAbsolute = $this_item.find('.main-sidebar-col').outerHeight();
					};
					
					var plusdefaultElements = (20+$('#wpadminbar').height());
					
					myFixed.removeAttr('style').removeClass('check-ab-stop');
					$this_item.find('.main-sidebar-col').removeAttr('style');
					
					function scrollUpdate(scrollTopValue, updownreturn, first_load){											
						defaultOffsetTop = $this_item.find('.main-content-col').offset().top;	 	//top
						defaultOffsetBottom = $this_item.offset().top + $this_item.outerHeight();	//bottom	
						defaultOffsetleft = myFixed.offset().left;
						intWidth = myFixed.width();
						intHeight = myFixed.outerHeight();
						
						function setHeightFixed(){
							heightForAbsolute = $this_item.find('.main-content-col').height();
							if($this_item.find('.main-sidebar-col').outerHeight() > $this_item.find('.main-content-col').outerHeight()) {
								heightForAbsolute = $this_item.find('.main-sidebar-col').height();
							};
						};
						
						setHeightFixed();
						
						if(intHeight > heightForAbsolute) {
							myFixed.removeAttr('style');
							setHeightFixed();	
						};
									
						$this_item.find('.main-sidebar-col').height(heightForAbsolute);
						plusdefaultElements = (20+$('#wpadminbar').height());
												
						var st = scrollTopValue;
						if(st >= (defaultOffsetTop-plusdefaultElements) && st <= (defaultOffsetBottom-myFixed.outerHeight())) {
							
							if(first_load==0){
								if(!myFixed.hasClass('check-fixed-stop-up')) {
									myFixed	
									.addClass('check-fixed-stop-up')
									.removeClass('check-fixed-stop')
									.css({'width':intWidth+'px', 'top':(plusdefaultElements+$('.cactus-sticky-menu').outerHeight())+'px', 'left':defaultOffsetleft+'px', 'position':'fixed',});									
								};
							};
							
							if (updownreturn < 0){
								//down
								if(myFixed.hasClass('check-ab-stop')) {
									myFixed.removeClass('check-ab-stop');
								};
								if(!myFixed.hasClass('check-fixed-stop')) {
									var stickyUpMenuHeight = 0;
									if($('.cactus-sticky-menu').hasClass('fix-down-scroll')) {stickyUpMenuHeight=$('.cactus-sticky-menu').outerHeight()};
									myFixed
									.addClass('check-fixed-stop')
									.removeClass('check-fixed-stop-up')
									.css({'width':intWidth+'px', 'top':(plusdefaultElements+stickyUpMenuHeight)+'px', 'left':defaultOffsetleft+'px', 'position':'fixed',});									
								};
								
							} else {
								//up
								if(myFixed.hasClass('check-ab-stop')) {
									myFixed.removeClass('check-ab-stop');
								};
								if(!myFixed.hasClass('check-fixed-stop-up')) {
									myFixed	
									.addClass('check-fixed-stop-up')
									.removeClass('check-fixed-stop')
									.css({'width':intWidth+'px', 'top':(plusdefaultElements+$('.cactus-sticky-menu').outerHeight())+'px', 'left':defaultOffsetleft+'px', 'position':'fixed',});									
								};
								
							};
						}else{
							if(st >= (defaultOffsetBottom-myFixed.outerHeight()-plusdefaultElements)){
								if(!myFixed.hasClass('check-ab-stop')){
									myFixed.removeAttr('style');
									if(heightForAbsolute == myFixed.outerHeight()){
										myFixed.css({'width':intWidth+'px', 'position':'absolute', 'top':(heightForAbsolute-myFixed.outerHeight())+'px'}).addClass('check-ab-stop');										
									}else{
										myFixed.css({'width':intWidth+'px', 'position':'absolute', 'top':(heightForAbsolute-myFixed.outerHeight()+40)+'px'}).addClass('check-ab-stop');										
									};
								};
							}else{
								if(myFixed.attr('style')!='' && myFixed.attr('style')!=null && defaultOffsetTop >=st){									
									myFixed.removeAttr('style').removeClass('check-ab-stop check-fixed-stop check-fixed-stop-up')//.removeClass('').removeClass('');									
								};
							};
						};
					};
					scrollUpdate($(window).scrollTop(), -1, 0);
					
					if(checkScroll!=1) {
						$(window).on('scroll', function(){
							if(window.innerWidth>991){							
								scrollUpdate($(this).scrollTop(), __cactus_check_updown, 1);
							}else{							
								if(myFixed.attr('style')!='' && myFixed.attr('style')!=null){
									myFixed.removeAttr('style').removeClass('check-ab-stop');
									myFixed.parents('.main-sidebar-col').removeAttr('style');
								};
							};
						});
					};
					
					var checkTimeoutClear = null;
					$('.easy-tab .tabs > li > a').off('click').on('click', function(){
						var $this = $(this);
						
						if(checkTimeoutClear!=null) {clearTimeout(checkTimeoutClear);};
						
						checkTimeoutClear = setTimeout(function(){	
							_fixedSidebar(index, 1);
							if(myFixed.hasClass('check-ab-stop')){
								$('#main-menu .navbar.navbar-default').addClass('no-open-sticky');
								$(window).scrollTop($this.offset().top-100);
								setTimeout(function(){
									$('#main-menu .navbar.navbar-default').removeClass('no-open-sticky');
								},200);
							};
						},100);
					});
				}else{
					//if(myFixed.attr('style')!='' && myFixed.attr('style')!=null){
						myFixed.removeAttr('style').removeClass('check-ab-stop');
						myFixed.parents('.main-sidebar-col').removeAttr('style');
					//};
				};
			});
		};
		
		_fixedSidebar();
		$(window).load(function(){
			_fixedSidebar(0, 1);
		});
		/*Sidebar fixed*/
		
		/*share fixed*/
		function _fixedShareBox(index) {
			var element = $('article.cactus-single-content');
			if(index!=null && typeof(index)!='undefined') {element = $('article.cactus-single-content').eq(index)};
			element.each(function(index, element) {
				var $this_item = $(this);
				var $this = $('.cactus-share-and-like.fix-left', $this_item);
				if($this.length > 0) {
				
					$this.removeAttr('style');
					if(window.innerWidth>=768) {
						var intTop = $this.offset().top;
						var intLeft = $this.offset().left;
						var intWidth = $this.width();
						var intHeight = $this.outerHeight();	
						
						if(intHeight >= $('.body-content.style-5', $this_item).height()) { return false;};
						
						var parentOffset = $('.body-content.style-5', $this_item).offset().top + $('.body-content.style-5', $this_item).height() - intHeight;	
						var parentPaddingTop = 	$('.body-content.style-5', $this_item).height() - intHeight - 50;
						if(intTop <= $(window).scrollTop() && parentOffset >= $(window).scrollTop()) {
							$this.css({'width':intWidth+'px', 'top':'0', 'left':intLeft+'px', 'position':'fixed', 'margin-top':'20px'});								
						}else{
							$this.removeAttr('style');
							if(parentOffset <= $(window).scrollTop()) {
								$this.css({'margin-top':(parentPaddingTop+20)+'px', 'position':'absolute'});
							};				
						};				
						
						$('.open-cactus-share', $this_item).on('click', function(){
							if($(this).hasClass('active')) {								
								setTimeout(function(){
									intTop = $this.offset().top;
									intLeft = $this.offset().left;
									intWidth = $this.width();
									intHeight = $this.outerHeight();							
									parentOffset = $('.body-content.style-5', $this_item).offset().top + $('.body-content.style-5', $this_item).height() - intHeight;	
									parentPaddingTop = 	$('.body-content.style-5').height() - intHeight - 50;
									
									if(intTop <= $(window).scrollTop() && parentOffset >= $(window).scrollTop()) {
										$this.removeAttr('style');
										$this.css({'width':intWidth+'px', 'top':'0', 'left':intLeft+'px', 'position':'fixed', 'margin-top':'20px'});	
									}else{
										if(parentOffset <= $(window).scrollTop()) {
											$this.removeAttr('style');
											$this.css({'margin-top':(parentPaddingTop+20)+'px', 'position':'absolute'});
										};		
									};
								},368);
								
							};
						});
					}else{
						$this.removeAttr('style');
					};
				
				};
            });			
		};	
		function fixedSharebox(){
			_fixedShareBox(0);
		};
		fixedSharebox();
		$(window).load(function(){
			_fixedShareBox();
		});
		$(window).on('scroll', function(){	
			_fixedShareBox();
		});		
		/*share fixed*/
		
		var __df_width = $(window).width();
		$(window).on('resize', function(){	
			if($(window).width()!=__df_width){
				_fixedSidebar();				
				_fixedShareBox();
				$('#main-menu').css({'min-height':$('#main-menu > .navbar-default:not(.cactus-sticky-menu)').height()});
				setTimeout(setOffsetButtonVideo,368);
				__df_width = $(window).width();
			};
		});
		
		/*Testimonials*/
		var $cactusSwiperTestimonialsShortCode = [];
		$('.create-testimonials').each(function(index, element) {
			if($(this).find('.swiper-slide').length > 1) {
				$('.pre-carousel', $(this)).show();
				$('.next-carousel', $(this)).show();
				__cactusCreateCarousel($(this), index, $cactusSwiperTestimonialsShortCode[index], 1, 'testimonials');
				
			};
		});
		/*Testimonials*/
		
		/*Create smart list post*/
		function createSmartListPost(index) {
			function isNumber(n) {return !isNaN(parseFloat(n)) && isFinite(n);};
			function replaceAll(find, replace, str) {return str.replace(new RegExp(find, 'g'), replace);}
			var element = $('article.cactus-single-content');
			if(index!=null && typeof(index)!='undefined') {element = $('article.cactus-single-content').eq(index)};
			element.each(function(index, element) {
				var $this = $(this);
				var PrimaryContent = $this.find('.content-first-content');
				var SubContent = $this.find('.content-smart-hidden');
				var hashPostDataPage=window.location.hash;
				var totalPages = SubContent.find('.page-break-item').length;
				var buttonPrevSmart = $this.find('.prev-smart-post');
				var buttonNextSmart = $this.find('.next-smart-post');
				var defaultPage = PrimaryContent.attr('data-index');
				var pointContent = $this.find('.post-static-page');
				var titleContent = $('.title-page-post', $this).find('span:not(.post-static-page)');
				
				function setDisableButton(){
					if((defaultPage)==1) {
						buttonPrevSmart.addClass('disable-btn');
					}else{
						buttonPrevSmart.removeClass('disable-btn');
					};			
					if((defaultPage)==totalPages) {
						buttonNextSmart.addClass('disable-btn');
					}else{
						buttonNextSmart.removeClass('disable-btn');
					};
				};
				var cactusOldUrlClickSmart = $this.attr('data-url');
				buttonPrevSmart.on('click', function(){
					if(isNumber(defaultPage)) {
						defaultPage = parseFloat(defaultPage);
						PrimaryContent.find('.thumb-opacity').addClass('active');						
						setTimeout(function(){
							var strBodyContent = replaceAll('<!--hidden-page--><!--','',SubContent.find('.page-break-item').eq(defaultPage-1).html());
							strBodyContent = replaceAll('--><!--hidden-page-->','',strBodyContent);							
							PrimaryContent.append('<div id="smp-loading-'+defaultPage+'" style="display:none;">'+strBodyContent+'</div>');
							$('#smp-loading-'+defaultPage)
							.imagesLoaded()
							.always( function( instance ) {
								PrimaryContent.html(strBodyContent +'<div class="thumb-opacity"><div class="circle"></div><div class="circle1"></div></div>');							
								PrimaryContent.find('.thumb-opacity').removeClass('active');								
								$('figure.wp-caption', PrimaryContent).addClass('active');
							});							
						},500);	
						PrimaryContent.attr('data-index', (defaultPage-1));								
						defaultPage =  parseFloat(PrimaryContent.attr('data-index'));
						pointContent.text(defaultPage);
						titleContent.text(SubContent.find('.page-break-item').eq(defaultPage-1).attr('data-title'));
						setDisableButton();
						
						if(defaultPage > 1) {
							window.location.hash = 'smartpost-page-'+defaultPage;
						}else{
							window.location.hash = 'smartpost-page-1';					
						};
						$this.attr('data-url', cactusOldUrlClickSmart + window.location.hash);
					};
					return false;
				});
				
				buttonNextSmart.on('click', function(){
					if(isNumber(defaultPage)) {
						defaultPage = parseFloat(defaultPage);
						PrimaryContent.find('.thumb-opacity').addClass('active');
						setTimeout(function(){
							var strBodyContent = replaceAll('<!--hidden-page--><!--','',SubContent.find('.page-break-item').eq(defaultPage-1).html());
							strBodyContent = replaceAll('--><!--hidden-page-->','',strBodyContent);							
							PrimaryContent.append('<div id="smp-loading-'+defaultPage+'" style="display:none;">'+strBodyContent+'</div>');
							$('#smp-loading-'+defaultPage)
							.imagesLoaded()
							.always( function( instance ) {
								PrimaryContent.html(strBodyContent +'<div class="thumb-opacity active"><div class="circle"></div><div class="circle1"></div></div>');						
								PrimaryContent.find('.thumb-opacity').removeClass('active');
								$('figure.wp-caption', PrimaryContent).addClass('active');
							});
						},500);	
						PrimaryContent.attr('data-index',(defaultPage+1));											
						defaultPage =  parseFloat(PrimaryContent.attr('data-index'));
						pointContent.text(defaultPage);
						titleContent.text(SubContent.find('.page-break-item').eq(defaultPage-1).attr('data-title'));
						setDisableButton();
						
						if(defaultPage > 1) {
							window.location.hash = 'smartpost-page-'+defaultPage;
							
						}else{
							window.location.hash = 'smartpost-page-1';	
						};
						$this.attr('data-url', cactusOldUrlClickSmart + window.location.hash);
					};
					return false;
				});	
				
				setDisableButton();
				
				if(hashPostDataPage!='' && hashPostDataPage!=null && typeof(hashPostDataPage)!='undefined' && hashPostDataPage.toString().split("-").length == 3){
					var	newPageHash=hashPostDataPage.toString().split('-')[2];
					if(isNumber(newPageHash) && hashPostDataPage.toString().split('-')[0]=='#smartpost' && hashPostDataPage.toString().split('-')[1]=='page' && $this.index()==0) {
						if((parseFloat(newPageHash)) <= totalPages) {
							defaultPage = (parseFloat(newPageHash) - 1);
							PrimaryContent.attr('data-index',(defaultPage));
							buttonNextSmart.trigger('click');	
						}else{
							newPageHash=1;
							window.location.hash = 'smartpost-page-1';
						}
					}else{
						newPageHash=1;
						window.location.hash = 'smartpost-page-1';
					};
				};			
            });
			
		};	
		createSmartListPost(0);
		/*Create smart list post*/
		
		/*load next post ajax*/			
			$.fn.visible = function(partial) {
				var $t            	= $(this),
				$w            		= $(window),
				viewTop       		= $w.scrollTop(),
				viewBottom    		= viewTop + $w.height(),
				_top          		= $t.offset().top,
				_bottom       		= _top + $t.height(),
				compareTop    		= partial === true ? _bottom : _top,
				compareBottom 		= partial === true ? _top : _bottom;		
				return ((compareBottom <= viewBottom) && (compareTop >= viewTop));
			};
			
			var _ajax_loading = false;
			var _ajax_no_more_post = false;
			var win = $(window);
			var indexNextPost = 0;
			
			win.on('scroll', function(){
			  /* Auto Load Next Post in single post when scrolling */
			  if($('#scroll_next_marker').length > 0){
					if(!_ajax_no_more_post && !_ajax_loading){						
						var doc = document.documentElement;
						var top_offset = (window.pageYOffset || doc.scrollTop)  - (doc.clientTop || 0);						
						if($('#scroll_next_marker').visible(true)){
							_ajax_loading = true;
							$('.loader').removeClass('hidden');
							var data_count = $('#single-post .cactus-single-content:last-child').attr('data-count');
							var data_enable_fb_comment = $('#single-post .cactus-single-content:first-child').attr('data-enable-fb-comment')
							
							data = 	{
										action 		: 'scroll_next_post',
										timestamp 	: $('#single-post .cactus-single-content:last-child').attr('data-timestamp'),
										id 			: $('#single-post .cactus-single-content:first-child').attr('data-id'),
										data_count 	: data_count,
										data_enable_fb_comment: data_enable_fb_comment,
										is_auto_load_next_post: 1
									};
							if(data_count <= 5)
							{
								$.ajax({
									  type: 'POST',
									  url: cactus.ajaxurl,
									  cache: false,
									  data: data,
									  success: function(html, textStatus, XMLHttpRequest){
											if(html != ''){
												var new_html = $(html);
												$('#single-post').append(new_html);
												if(data_enable_fb_comment == 1)
												{
													FB.XFBML.parse(new_html[0]);
												}
																								
												indexNextPost++;											
												
												var elementsCompleteLoad = $('article.cactus-single-content').eq(indexNextPost);
												
												/*carousel related post*/	
												if($('.cactus-related-posts', elementsCompleteLoad).length > 0)	 {									
													__cactusCreateCarousel($('.cactus-related-posts', elementsCompleteLoad), (indexNextPost), $cactusSwiperRelatedPost[(indexNextPost)], 'auto', 'rela');
												};
												/*carousel related post*/
												
												/*carousel listing*/
												if($('.cactus-listing-carousel', elementsCompleteLoad).length > 0) {
													__cactusCreateCarousel($('.cactus-listing-carousel', elementsCompleteLoad), (indexNextPost), $cactusSwiperCarouselPost[(indexNextPost)], 'auto', 'carPos');
												};
												/*carousel listing*/
												
												/*carousel listing*/
												if($('.post-style-gallery', elementsCompleteLoad).length > 0) {
													__cactusCreateCarousel($('.post-style-gallery', elementsCompleteLoad), (indexNextPost), $cactusSwiperGalleryPost[(indexNextPost)], 1, 'gall');
												};
												/*carousel listing*/												
												
												createSmartListPost(indexNextPost);									
												
												setLightBoxGroup(indexNextPost);
												
												openCarouselListing(indexNextPost);	
												openShareSingle(indexNextPost);
												showTollTips();											
												
												_fixedShareBox(indexNextPost);															
												$(window).on('scroll', function(){	
													 _fixedShareBox(indexNextPost);	
												});
												
												var ___df_width = $(window).width();
												$(window).on('resize', function(){
													if($(window).width()!=___df_width){	
													 	_fixedShareBox(indexNextPost);
														___df_width = $(window).width();	
													};
												});
												
												if($('.cactus-single-content').eq($('.cactus-single-content').length-1).offset().top <= $(window).scrollTop()){
													if(document.URL != $('.cactus-single-content').eq($('.cactus-single-content').length-1).attr('data-url')) {
														window.history.replaceState(null, null, $('.cactus-single-content').eq($('.cactus-single-content').length-1).attr('data-url'));
													};
												};
												
												_fixedSidebar();
												
											} else {
												_ajax_no_more_post = true;	
												_fixedSidebar();											
											};
											_ajax_loading = false;
											$('.loader').addClass('hidden');
											_fixedSidebar();
									  },
									  error: function(MLHttpRequest, textStatus, errorThrown){
										_ajax_loading = false;
										$('.loader').addClass('hidden');
										_fixedSidebar();
									  },
								});
							}
							else
							{$('.loader').addClass('hidden');}
							_fixedSidebar();
						};
					};
				};
			});
		
			/* Change browser URL if meet new article after ajaxed */
			if($('.single-post-content .cactus-single-content').eq(0).length > 0) {
				var cactusOldUrl = $('.cactus-single-content').eq(0).attr('data-url');
				$('.single-post-content .cactus-single-content').eq(0).attr('data-url', cactusOldUrl);
			};
			
			if(typeof(cactus)!='undefined'  && $('.cactus-single-content').length > 0 && $('.single-post-content').length > 0) {
				if(typeof(cactus.scroll_effect_change_url) !== 'undefined'){					
					win.on('scroll', $.debounce( 50, function(){
						var allPosts = $('.cactus-single-content');
						if(allPosts.find('.heading-post').length > 0) {
							allPosts.each(function(){
								var el = $(this);
								if (el.visible(true) && (el.find('.heading-post').offset().top - 200) <= $(window).scrollTop()) {								
									url = el.attr('data-url');
									if(document.URL != url) {
										window.history.replaceState(null, null, url);
									};
								};
							});
							if(allPosts.eq(0).offset().top >=$(window).scrollTop()){
								if(document.URL != allPosts.eq(0).attr('data-url')) {
									window.history.replaceState(null, null, allPosts.eq(0).attr('data-url'));
								};
							};
						};
					}));
				};
			};
		/*load next post ajax*/
		
		/*Suggestion open*/
		function CalculatorOffsetSuggestion() {
			var $elementsCheckSuggestion = $('.single-post-content .cactus-single-content').eq(0).find('.body-content');
			var $elementsSuggestion = $('.cactus-post-suggestion');
			if($elementsCheckSuggestion.length > 0 && $elementsSuggestion.length > 0) {
				
				var intHeightOpenSuggestion = $elementsCheckSuggestion.offset().top + $elementsCheckSuggestion.height();
				$('.suggestion-header > span').on('click', function(){
					if($elementsSuggestion.hasClass('cactus-close')) {
						$elementsSuggestion.removeClass('cactus-close');
					}else{
						$elementsSuggestion.addClass('cactus-close');
					};
					
				});
				$(window).on('scroll', function(){
					intHeightOpenSuggestion = $elementsCheckSuggestion.offset().top + $elementsCheckSuggestion.height();
					if($(window).scrollTop() >= (intHeightOpenSuggestion - window.innerHeight )) {
						if(!$elementsSuggestion.hasClass('active') && !$elementsSuggestion.hasClass('cactus-close') ) {
							$elementsSuggestion.addClass('active');
						};
					}else{
						$elementsSuggestion.removeClass('active');
					};
				});
			};
		};
		CalculatorOffsetSuggestion();			
		/*Suggestion open*/
		
		/*Smart list post scroll*/
		function gotoSmartListPost(){
			if($('.single-post-content .cactus-single-content').eq(0).find('.post-static-page[data-scroll-page="1"]').length > 0) {
				var hashPostDataPage = window.location.hash;				
				if(hashPostDataPage!='' && hashPostDataPage!=null && typeof(hashPostDataPage)!='undefined' && hashPostDataPage.toString().split("-").length == 3){
					var	newPageHash=hashPostDataPage.toString().split('-')[2];
					if(hashPostDataPage.toString().split('-')[0]=='#smartpost' && hashPostDataPage.toString().split('-')[1]=='page') {
						$('html, body').animate({scrollTop:$('.single-post-content .cactus-single-content').eq(0).find('.heading-post').offset().top - (20 + $('#wpadminbar').height())},500);

					};
				};
			};
			if($('.single-post-content .cactus-single-content').eq(0).find('.body-content[data-scroll-page-viewall="1"]').length > 0) {
				$('html, body').animate({scrollTop:$('.single-post-content .cactus-single-content').eq(0).find('.heading-post').offset().top - (20 + $('#wpadminbar').height())},500);
			};
		};
		$(window).load(function(){
			gotoSmartListPost();			
		});			
		/*Smart list post scroll*/
		
		/*go to top*/
		$('.go-to-top').on('click', function(){
			$('html, body').animate({scrollTop:0},500);
		});
		$(window).on('scroll', function(){
			if($(window).scrollTop() >= (window.innerHeight * 0.75)) {
				if(!$('.go-to-top').hasClass('active')) {
					$('.go-to-top').addClass('active');
				};
			}else{
				$('.go-to-top').removeClass('active');
			};
		});
		/*go to top*/
		
		var $__figure_caption = $('.body-content figure.wp-caption');
		if($__figure_caption.length>0){
			$__figure_caption.each(function(index, element) {
                var $this = $(this);
				
				$this.imagesLoaded()
				.always( function( instance ) {				
					$this.addClass('active');
				});
            });
		};
		
	});
	/*Hide popup share video*/
	$('.popup_share_overlay').on('click', function(){
		$('body').removeClass('popup-share-active');
	});
	/*End Hide popup share video*/
	
}(jQuery));

/*check ie*/
function getInternetExplorerVersion(){
	var rv = -1;
	if (navigator.appName == 'Microsoft Internet Explorer'){
		var ua = navigator.userAgent;
		var re  = new RegExp("MSIE ([0-9]{1,}[\.0-9]{0,})");
		if (re.exec(ua) != null){
			rv = parseFloat( RegExp.$1 );
		};
	}else if (navigator.appName == 'Netscape'){
		var ua = navigator.userAgent;
		var re  = new RegExp("Trident/.*rv:([0-9]{1,}[\.0-9]{0,})");
		if (re.exec(ua) != null){
			rv = parseFloat( RegExp.$1 );
		};
	};
	return rv;
};

/* Set a cookie */
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
};

/* Read a cookie */
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
    };
    return "";
};

/* Check retina screens */
function isRetinaDisplay() {
	if (window.matchMedia) {
		var mq = window.matchMedia("only screen and (min--moz-device-pixel-ratio: 1.3), only screen and (-o-min-device-pixel-ratio: 2.6/2), only screen and (-webkit-min-device-pixel-ratio: 1.3), only screen  and (min-device-pixel-ratio: 1.3), only screen and (min-resolution: 1.3dppx)");
		if (mq && mq.matches || (window.devicePixelRatio > 1)) {
			return true;
		}else {
			return false;
		};
	};
};

var _is_retina = false;
( function() {
	// do something	
	var retina = getCookie("cactus-retina");
    if (retina != "") {
		if(retina = '1'){
		    _is_retina = true;
		};
    }else {
		if(isRetinaDisplay()){
			_is_retina = true;			
			setCookie("cactus-retina", "1", 300);
		} else {
			_is_retina = false;			
			setCookie("cactus-retina", "0", 300);
		};
	};
})();

var __cactus_check_updown = 0;
function scrollFunc(e) {
    if ( typeof scrollFunc.x == 'undefined' ) {
        scrollFunc.x=window.pageXOffset;
        scrollFunc.y=window.pageYOffset;
    }
    var diffX=scrollFunc.x-window.pageXOffset;
    var diffY=scrollFunc.y-window.pageYOffset;

    if( diffX<0 ) {
        // Scroll right
    } else if( diffX>0 ) {
        // Scroll left
    } else if( diffY<0 ) {
		// Scroll down
		__cactus_check_updown=-1;
		//return -1;
    } else if( diffY>0 ) {
		// Scroll up
		__cactus_check_updown=1;
    } else {
        // First scroll event
    }
    scrollFunc.x=window.pageXOffset;
    scrollFunc.y=window.pageYOffset;
}