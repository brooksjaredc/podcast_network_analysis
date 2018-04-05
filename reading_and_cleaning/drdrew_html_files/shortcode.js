/*shortcode posts classic slider*/
;(function($){
	$(document).ready(function() {
		function isNumber(n) {return !isNaN(parseFloat(n)) && isFinite(n);};
		/*Function create Carousel*/
		function __cactusCreateCarousel(elements, index, sliderArray, perview, position){			
			var $this = elements;
			var container = '';
			if(position=='1') {
				container='.cactus-silder-sync-content';
			}else{
				container='.cactus-silder-sync-listing';
			};

			function checkWidthSlide(){
				var defaultWidth = $this.find(container).find('.swiper-slide > .sync-img-content').outerWidth();			
				$this.find(container).find('.swiper-slide').width(defaultWidth);	
				// console.log(defaultWidth);		
			};
			
			checkWidthSlide();

			function setHeightSlider() {
				var intHeight = $this.find('.cactus-silder-sync-content').find('.swiper-slide:first-child > .sync-img-content').outerHeight();
				$('.cactus-swiper-container, .swiper-wrapper, .swiper-slide',  $this.find('.cactus-silder-sync-content')).height(intHeight);
				// console.log(intHeight);
				// console.log($('.swiper-slide.swiper-slide-active sync-img-content'));
			};
			setHeightSlider();
			var strDirection = $this.attr('data-layout');
			var intAutoPlay = $this.attr('data-autoplay');
			
			function createSlider(){
				
				sliderArray = $(container, $this).swiper({
					slidesPerView: perview,
					loop: false,
					calculateHeight:true,
					speed:500,
					simulateTouch:false,
					direction: strDirection=='vertical'?'vertical':'horizontal',
					roundLengths:true,
					autoplayDisableOnInteraction:false,
					autoHeight:true,
					updateTranslate:true,
				});
				
				if(position=='1') {
					$cactusSwiperSyncPost[index]=sliderArray;
					$this.find('.next-carousel').on('click', function(){
						sliderArray.stopAutoplay();	
						if(sliderArray.activeIndex==(sliderArray.slides.length-1)){
							sliderArray.slideTo(0);						
						}else{
							sliderArray.slideNext();
						};						
					});			
					$this.find('.pre-carousel').on('click', function(){
						sliderArray.stopAutoplay();	
						if(sliderArray.activeIndex==0){							
							sliderArray.slideTo(sliderArray.slides.length-1);					
						}else{
							sliderArray.slidePrev();
						};						
					});					
					var checkAutoPlay = 0;
					if(intAutoPlay!='' && intAutoPlay!=null && typeof(intAutoPlay)!='undefined' && isNumber(intAutoPlay) && intAutoPlay=='1') {
						sliderArray.params.autoplay=5000;
						sliderArray.startAutoplay();
						
						var funcSetTimeOut = null;
						
						$this.on({
							mouseenter: function(){
								if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
								checkAutoPlay = 1;
								sliderArray.stopAutoplay();						
							}, 
							mouseleave: function(){	
								checkAutoPlay = 0;	
								if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};					
								if(sliderArray.activeIndex == sliderArray.slides.length-1){
									sliderArray.stopAutoplay();
									funcSetTimeOut = setTimeout(function(){sliderArray.slideTo(0, 1000); sliderArray.startAutoplay();},5000);
								}else{
									sliderArray.startAutoplay();
								};
							}
						});
						
						sliderArray.params.onSlideChangeEnd = function(){							
							if(checkAutoPlay == 0){
								if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
								if(sliderArray.activeIndex == sliderArray.slides.length-1){
									sliderArray.stopAutoplay();
									funcSetTimeOut = setTimeout(function(){if(checkAutoPlay==0){sliderArray.slideTo(0, 1000); sliderArray.startAutoplay();}},5000);
								};
							};	
							$this.on({
								mouseenter: function(){								
									if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
									sliderArray.stopAutoplay();
								},
								mouseleave: function(){
									if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
									if(sliderArray.activeIndex == sliderArray.slides.length-1){
										sliderArray.stopAutoplay();
										funcSetTimeOut = setTimeout(function(){sliderArray.slideTo(0, 1000); sliderArray.startAutoplay();},5000);
									};
								}
							});							
						};							
					};
				}else{
					$cactusSwiperSyncListing[index]=sliderArray;
				};

				function resizeWidthSlide(){
					var dpr = window.devicePixelRatio;
					if(typeof dpr =='undefined') { dpr = 1;};
					dpr = 1;
					var width = window.innerWidth * dpr;
										
					// sliderArray.appendSlide('<div class="swiper-slide"><div class="sync-img-content"></div></div>');
					
					if(position!='1') {
						if	(width >= 768){
							sliderArray.params.slidesPerView=perview;
						}else if(width >= 480){
							sliderArray.params.slidesPerView=perview;
						}else{
							sliderArray.params.slidesPerView=3;
						};
					}else{
						//
					};
					
					// sliderArray.removeLastSlide();
									
					sliderArray.update();
					sliderArray.onResize();
				};						
				
				resizeWidthSlide();
				setTimeout(resizeWidthSlide,500);
				
				var _df_width = $(window).width();
				$(window).on('resize', function(){
					if($(window).width()!=_df_width){
						$('.swiper-wrapper, .swiper-slide',$this.find(container)).removeAttr('style');
						$('.swiper-wrapper',$this.find('.cactus-silder-sync-content')).removeAttr('style');
						resizeWidthSlide();
						setHeightSlider();	
						sliderArray.update(true);
						sliderArray.slideTo(0);
						_df_width = $(window).width();
					};									
				});
				
			};	
			createSlider();
		};	
		/*Function create Carousel*/
		
		var $cactusSwiperSyncPost = [];
		var $cactusSwiperSyncListing = [];
		var $cactusSwiperSyncPostStart = [];
		var $cactusSwiperSyncListingStart = [];
		$('.cactus-slider-sync').each(function(index, element) {
			var $this=$(this);
			var intAutoPlayFc = $this.attr('data-autoplay');
			
			__cactusCreateCarousel($this, index, $cactusSwiperSyncPost[index], 1, '1');
			

			if($this.attr('data-layout')!='vertical') {
				__cactusCreateCarousel($this, index, $cactusSwiperSyncListing[index], 5, '2');			
				function addRemoveActive(index){
					$('.cactus-silder-sync-listing .swiper-slide', $this).removeClass('active');
					$('.cactus-silder-sync-listing .swiper-slide', $this).eq(index).addClass('active');
				};	
				
				addRemoveActive(0);

				$cactusSwiperSyncPostStart[index]=0;
				$cactusSwiperSyncListingStart[index]=0;
				
				$cactusSwiperSyncPost[index].params.onSlideChangeStart = function(){
					if($cactusSwiperSyncListingStart[index]==1) {
						$cactusSwiperSyncListingStart[index]=0;
					}else{
						$cactusSwiperSyncPostStart[index]=1;			
						$cactusSwiperSyncListing[index].slideTo($cactusSwiperSyncPost[index].activeIndex);
						addRemoveActive($cactusSwiperSyncPost[index].activeIndex);
					};
				};
				
				$cactusSwiperSyncListing[index].params.onSlideChangeStart = function(){
					if($cactusSwiperSyncPostStart[index]==1) {
						$cactusSwiperSyncPostStart[index]=0;
					}else{
						$cactusSwiperSyncListingStart[index]=1;				
						$cactusSwiperSyncPost[index].slideTo( $cactusSwiperSyncListing[index].activeIndex, 500, false);
						addRemoveActive($cactusSwiperSyncListing[index].activeIndex);
					};
				};			
				// console.log($cactusSwiperSyncListing[index]);
				// $cactusSwiperSyncListing[index].params.onClick = function(){
				// 	$cactusSwiperSyncPost[index].stopAutoplay();
				// 	addRemoveActive($cactusSwiperSyncListing[index].clickedIndex);
				// 	$cactusSwiperSyncPost[index].slideTo($cactusSwiperSyncListing[index].clickedIndex);
	
				// 	if($('.cactus-silder-sync-listing .swiper-slide', $this).eq($cactusSwiperSyncListing[index].clickedIndex).offset().left <= $this.offset().left) {
				// 		$cactusSwiperSyncListing[index].slideTo( $cactusSwiperSyncListing[index].clickedIndex-1, 500, false);	
				// 	}else{
				// 		$cactusSwiperSyncListing[index].slideTo( $cactusSwiperSyncListing[index].clickedIndex, 500, false);	
				// 	};
				// 	$cactusSwiperSyncPostStart[index]=0;
				// 	$cactusSwiperSyncListingStart[index]=0;
				// };
				var intSlidesLength = index;
				$this.find('.vertical-align .swiper-slide').each(function(index, element) {
                    $(this).find('.thumb-overlay').on('click', function(){
                    	// console.log("aaaab");
						$cactusSwiperSyncPost[intSlidesLength].stopAutoplay();
						$cactusSwiperSyncPost[intSlidesLength].slideTo( index, 500, false);
						$cactusSwiperSyncListing[intSlidesLength].slideTo( index, 500, false);
						$this.find('.swiper-slide').removeClass('active');
						$(this).parents('.swiper-slide').addClass('active');						
						return false;
					});
                });				
			}else{
				var intSlidesLength = index;
				$this.find('.vertical-align .swiper-slide').each(function(index, element) {
                    $(this).on('click', function(){
                    	// console.log("aaaab");
						$cactusSwiperSyncPost[intSlidesLength].stopAutoplay();
						$cactusSwiperSyncPost[intSlidesLength].slideTo( index, 500, false);
						$this.find('.swiper-slide').removeClass('active');
						$(this).addClass('active');						
						return false;
					});
                });
				
				$cactusSwiperSyncPost[index].params.onSlideChangeStart = function(){						
					$this.find('.vertical-align .swiper-slide').removeClass('active');	
					$this.find('.vertical-align .swiper-slide').eq($cactusSwiperSyncPost[index].activeIndex).addClass('active');	
				};
				
				var _df_width = $(window).width();				
				$(window).on('resize', function(){
					if($(window).width()!=_df_width){
						$this.find('.vertical-align .swiper-slide').removeClass('active');	
						$this.find('.vertical-align .swiper-slide').eq(0).addClass('active');
						_df_width = $(window).width();
					};								
				});
				
				/*Fix ie9*/
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
				function msieversion(){
					var ua = window.navigator.userAgent;
					var msie = ua.indexOf ( "MSIE " );				
					if ( msie > 0 ){
						return parseInt (ua.substring (msie+5, ua.indexOf (".", msie )));
					}else{
						return 0;
					};
				};
				if(getInternetExplorerVersion()!=0 && getInternetExplorerVersion()!=-1) {
					function fixHeightIE9() {
						if(window.innerWidth>767){
							setTimeout(function(){
								$this.find('.cactus-silder-sync-listing').height($this.height());
								$this.find('.vertical-align .swiper-slide').height($this.height()/6);
							},368);	
						}else{
							setTimeout(function(){
								$this.find('.cactus-silder-sync-listing').removeAttr('style');
								$this.find('.vertical-align .swiper-slide').removeAttr('style');
							},368);	
						};
					};					
					fixHeightIE9();
					var __df_width = $(window).width();
					$(window).on('resize', function(){
						if($(window).width()!=__df_width){
							fixHeightIE9();
							__df_width = $(window).width();
						};						
					});
				};
				/*Fix ie9*/
			};					
		});	
        
        $('.newstube_playlist.shortcode').each(function(){
            var index = $('.cactus-widget-posts-item.active', this).index($('.cactus-widget-posts-item', this)) + 1;
            $('.total-video span', this).text(index + '/' + $(this).find('.cactus-widget-posts-item').length );
        });
	});
}(jQuery));

/*end shortcode posts classic slider*/

/*===================================================================================================================================================================================================*/

/*shortcode posts thumb slider*/
;(function($){
	$(document).ready(function() {
		function isNumber(n) {return !isNaN(parseFloat(n)) && isFinite(n);};
		
		/*Function create Carousel*/
		function setVideoSlides(){
			$('[data-type="bg-video"]').each(function(index, element) {
                var $this = $(this);
				var strVideoSource = $this.attr('data-video-source');
				if(strVideoSource!='' && strVideoSource!=null && typeof(strVideoSource)!='undefined') {

					var videoString = '<video width="auto" height="100%" id="video-banner-'+index+'" preload="auto" loop>'+
										  '<source src="'+strVideoSource+'" type="video/mp4">'+
									  '</video>';
					$(videoString).prependTo( $this );
				}
            });
		};
		
		setVideoSlides();
		
		function __cactusCreateCarousel(elements, index, sliderArray, perview, position){
			var $this = elements;
			$this.attr('id', 'cactus-thumb-slider-'+index);
			var intAutoPlay = $this.attr('data-autoplay');
			var container = '';
			if(position=='1') {
				container='.cactus-thumb-slider-container';
			}else{
				container='.cactus-thumb-slider-listing';
			};
			
			function checkHeightSlide(){
				if(position=='1') {					
					$('#cactus-thumb-slider-style-'+index).remove();			
					$this.find(container).find('.swiper-slide').height($this.height());	
					$('<style type="text/css" id="cactus-thumb-slider-style-'+index+'">#cactus-thumb-slider-'+index+' '+container+' .swiper-slide{ height:'+$this.height()+'px}</style>').appendTo('head');	
				};
			};			
			checkHeightSlide();
			
			function createSlider(){
				
				sliderArray = $(container, $this).swiper({
					slidesPerView: perview,
					loop: false,
					calculateHeight:true,
					speed:200,
					simulateTouch:false,
					progress:position=='1'?true:false,
					effect: position=='1'?'fade':'slide',
					// slideToClickedSlide:true,
					// onClick: function(swiper,event){
				 //        swiper.slideNext();
				 //    },
					// onProgressChange: function(swiper){
					// 	if(position=='1') {
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
					// 	if(position=='1') {
					// 		for (var i = 0; i < swiper.slides.length; i++){
					// 			swiper.setTransition(swiper.slides[i], 0);
					// 		};
					// 	};
					// },
					// onSetWrapperTransition: function(swiper, speed) {
					// 	if(position=='1') {
					// 		for (var i = 0; i < swiper.slides.length; i++){
					// 			swiper.setTransition(swiper.slides[i], speed);
					// 		};
					// 	};
					// },
					
					autoplayDisableOnInteraction:false,
				});					
				if(position=='1') {
					$cactusSwiperSyncPost[index]=sliderArray;
					$this.find('.next-carousel').on('click', function(){						
						if(sliderArray.activeIndex==(sliderArray.slides.length-1)){
							sliderArray.slideTo(0);						
						}else{
							sliderArray.slideNext();
						};						
					});			
					$this.find('.pre-carousel').on('click', function(){
						if(sliderArray.activeIndex==0){							
							sliderArray.slideTo(sliderArray.slides.length-1);					
						}else{
							sliderArray.slidePrev();
						};						
					});
					var checkAutoPlay = 0;
					
					if(intAutoPlay!='' && intAutoPlay!=null && typeof(intAutoPlay)!='undefined' && isNumber(intAutoPlay) && intAutoPlay=='1') {
						sliderArray.params.autoplay=5000;
						sliderArray.startAutoplay();
						
						var funcSetTimeOut = null;
																		
						$this.on({
							mouseenter: function(){
								if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
								checkAutoPlay = 1;							
								sliderArray.stopAutoplay();							
							}, 
							mouseleave: function(){	
								checkAutoPlay = 0;
								if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};						
								if(sliderArray.activeIndex == sliderArray.slides.length-1){
									sliderArray.stopAutoplay();
									funcSetTimeOut = setTimeout(function(){sliderArray.slideTo(0, 1000); sliderArray.startAutoplay();},5000);
								}else{
									sliderArray.startAutoplay();
								};
							}
						});
						
						sliderArray.params.onSlideChangeEnd = function(){
							if(checkAutoPlay == 0){
								if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
								if(sliderArray.activeIndex == sliderArray.slides.length-1){
									sliderArray.stopAutoplay();
									funcSetTimeOut = setTimeout(function(){if(checkAutoPlay==0){sliderArray.slideTo(0, 1000); sliderArray.startAutoplay();}},5000);
								};
							};	
							$this.on({
								mouseenter: function(){								
									if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
									sliderArray.stopAutoplay();
								},
								mouseleave: function(){
									if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
									if(sliderArray.activeIndex == sliderArray.slides.length-1){
										sliderArray.stopAutoplay();
										funcSetTimeOut = setTimeout(function(){sliderArray.slideTo(0, 1000); sliderArray.startAutoplay();},5000);
									};
								}
							});							
						};					
					};
				}else{
					$cactusSwiperSyncListing[index]=sliderArray;
				};
				
				function resizeWidthSlide(){
					checkHeightSlide();	
					var dpr = window.devicePixelRatio;
					if(typeof dpr =='undefined') { dpr = 1;};
					dpr = 1;
					var width = window.innerWidth * dpr;
					
					if(position!='1') {
						var newWidthItem = Math.round($(container, $this).outerWidth() / 5 * 2);
						sliderArray.appendSlide('<div class="sync-img-content"></div>');
						if	(width >= 1200){
							sliderArray.params.slidesPerView=perview;
						}else if(width >= 992){							
							newWidthItem = Math.round($(container, $this).outerWidth() / 10.5 * 3);
							$(container+' .swiper-slide', $this).width(newWidthItem);
							sliderArray.params.slidesPerView='auto';
						}else if(width >= 768){
							newWidthItem = Math.round($(container, $this).outerWidth() / 5 * 2);
							$(container+' .swiper-slide', $this).width(newWidthItem);
							sliderArray.params.slidesPerView='auto';	
						}else if(width >= 580){
							newWidthItem = Math.round($(container, $this).outerWidth() / 5 * 2);
							$(container+' .swiper-slide', $this).width(newWidthItem);
							sliderArray.params.slidesPerView='auto';		
						}else{
							newWidthItem = Math.round($(container, $this).outerWidth() / 3 * 2);
							$(container+' .swiper-slide', $this).width(newWidthItem);
							sliderArray.params.slidesPerView='auto';
						};
						// sliderArray.removeLastSlide();
					}else{					
						// for(var k=0; k < sliderArray.slides.length; k++){
						// 	sliderArray.setTransition(sliderArray.slides[k], 0);
						// };	
						// $(container+' > .swiper-wrapper', $this).stop(true,true).css('transition-duration','0s');
					};
					sliderArray.update();
					sliderArray.onResize();;
					
					if(sliderArray.activeIndex>0) {
						sliderArray.slideTo(0);	
					};
				};
						
				resizeWidthSlide();
				setTimeout(function(){
					resizeWidthSlide();
					if(position!='1') {
						$(container+' .swiper-slide', $this).addClass('show-now');	
					};
				},368);	
				
				var _df_width = $(window).width();
				$(window).on('resize', function(){	
					if($(window).width()!=_df_width){					
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
		
		var $cactusSwiperSyncPost = [];
		var $cactusSwiperSyncListing = [];
		var $cactusSwiperSyncPostStart = [];
		var $cactusSwiperSyncListingStart = [];
		$('.cactus-thumb-slider').each(function(index, element) {
			var $this=$(this);
			var topIndex = index;	
			$this.find('.cactus-thumb-slider-listing .thumb-item').each(function(index, element) {
				var itemId = 'set-color-'+topIndex+'-'+index;
                $(this).attr('id', itemId);
				var attrColorStyle = $(this).attr('data-tag-color');
				if(attrColorStyle!='' && attrColorStyle!=null && typeof(attrColorStyle)!='undefined') {
					$(topIndex+' .bottom-absolute').css({});
					$(
					'<style>#'+itemId+' .bottom-absolute {background-color:'+attrColorStyle+';}#'+itemId+'.thumb-item:hover, .swiper-slide.active #'+itemId+'.thumb-item {background-color:'+attrColorStyle+';}#'+itemId+'.thumb-item:hover *:not(.cactus-note-cat), .swiper-slide.active #'+itemId+'.thumb-item *:not(.cactus-note-cat) {color:#FFFFFF;}#'+itemId+'.thumb-item .cactus-note-cat {background-color:'+attrColorStyle+'; color:#FFFFFF; transition:all 0.2s; -webkit-transition:all 0.2s;}#'+itemId+'.thumb-item:hover .cactus-note-cat, .swiper-slide.active #'+itemId+'.thumb-item .cactus-note-cat {background-color:#FFFFFF; color:'+attrColorStyle+'}</style>'
					).appendTo('head');
				};
            });
			
			__cactusCreateCarousel($this, index, $cactusSwiperSyncListing[index], 4, '2');		
			__cactusCreateCarousel($this, index, $cactusSwiperSyncPost[index], 1, '1');
						
			function addRemoveActive(index){
				$('.cactus-thumb-slider-listing .swiper-slide', $this).removeClass('active');
				$('.cactus-thumb-slider-listing .swiper-slide', $this).eq(index).addClass('active');
			};	
			
			addRemoveActive(0);
			
			$cactusSwiperSyncPostStart[index]=0;
			$cactusSwiperSyncListingStart[index]=0;
			
			function playVideoActive(){
				var activeVideo = $('.cactus-thumb-slider-container .swiper-slide.swiper-slide-active', $this).find('video');
				
				if(activeVideo.length > 0) {
					var myVideoPlay = document.getElementById(activeVideo.attr('id'));
					myVideoPlay.play();
				};
			};
			
			$cactusSwiperSyncPost[index].params.onInit = function(){
				playVideoActive();
			};
			
			$cactusSwiperSyncPost[index].params.onSlideChangeStart = function(){
				if($cactusSwiperSyncListingStart[index]==1) {
					$cactusSwiperSyncListingStart[index]=0;
				}else{
					$cactusSwiperSyncPostStart[index]=1;			
					$cactusSwiperSyncListing[index].slideTo($cactusSwiperSyncPost[index].activeIndex);
					addRemoveActive($cactusSwiperSyncPost[index].activeIndex);
				};
				
				$('video', $this).each(function(index, element) {
                    var myVideoPlay = document.getElementById($(this).attr('id'));
					myVideoPlay.pause();
					myVideoPlay.currentTime = 0;
                });
				playVideoActive();
			};
			
			$cactusSwiperSyncListing[index].params.onSlideChangeStart = function(){
				if($cactusSwiperSyncPostStart[index]==1) {
					$cactusSwiperSyncPostStart[index]=0;
				}else{
					$cactusSwiperSyncListingStart[index]=1;				
					$cactusSwiperSyncPost[index].slideTo( $cactusSwiperSyncListing[index].activeIndex, 500, false);
					addRemoveActive($cactusSwiperSyncListing[index].activeIndex);
				};
			};
				
				var intSlidesLength = index;
							
			$this.find('.slider-thumb .cactus-thumb-slider-listing .swiper-slide').each(function(index, element) {

                $(this).find('h3').on('click', function(){
                	console.log("h3");
					$cactusSwiperSyncPost[intSlidesLength].stopAutoplay();
					$cactusSwiperSyncPost[intSlidesLength].slideTo( index, 500, false);
					$cactusSwiperSyncListing[intSlidesLength].slideTo( index, 500, false);
					$this.find('.swiper-slide').removeClass('active');
					$(this).parents('.swiper-slide').addClass('active');
					// console.log(index);						
					// console.log( $cactusSwiperSyncPost[intSlidesLength]);
					// console.log( $cactusSwiperSyncListing[intSlidesLength]);
					// console.log($cactusSwiperSyncListing[intSlidesLength].clickedIndex);
					// if($('.cactus-thumb-slider-listing .swiper-slide', $this).eq($cactusSwiperSyncListing[index].clickedIndex).offset().left <= $this.find('.slider-thumb').offset().left) {
						// console.log('abc');

					// 	[index].slideTo( $cactusSwiperSyncListing[index].clickedIndex-1, 500, false);
					// 	console.log($cactusSwiperSyncListing[index].clickedIndex);	
					// }else{
						// console.log('aabc')
					// 	$cactusSwiperSyncListing[index].slideTo( $cactusSwiperSyncListing[index].clickedIndex, 500, false);	
					// };
					// $cactusSwiperSyncPostStart[index]=0;
					// $cactusSwiperSyncListingStart[index]=0;
					// return false;
				});
            });
            	
			$cactusSwiperSyncListing[index].params.onClick = function(){
				console.log('aaa')
			// 	$cactusSwiperSyncPost[index].stopAutoplay();
			// 	addRemoveActive($cactusSwiperSyncListing[index].clickedSlideIndex);
			// 	$cactusSwiperSyncPost[index].slideTo($cactusSwiperSyncListing[index].clickedSlideIndex);

			// 	if($('.cactus-thumb-slider-listing .swiper-slide', $this).eq($cactusSwiperSyncListing[index].clickedSlideIndex).offset().left <= $this.find('.slider-thumb').offset().left) {
			// 		$cactusSwiperSyncListing[index].slideTo( $cactusSwiperSyncListing[index].clickedSlideIndex-1, 500, false);	
			// 	}else{
			// 		$cactusSwiperSyncListing[index].slideTo( $cactusSwiperSyncListing[index].clickedSlideIndex, 500, false);	
			// 	};
			// 	$cactusSwiperSyncPostStart[index]=0;
			// 	$cactusSwiperSyncListingStart[index]=0;
			};				
		});
		
	});
}(jQuery));
/*end shortcode posts thumb slider*/

/*====================================================================================================================================================================================================*/

/*shortcode posts parallax*/

;(function($){
	function parallaxBanner(){
		(function($){
			$('.cactus-banner-parallax').each(function(index, element) {
				var $this=$(this).find('.cactus-banner-parallax-content');
				var speed = 0.4;
				var scrollPos = $(window).scrollTop()-$this.offset().top;
				if($this.offset().top < window.innerHeight){
					speed = 0.6;
					scrollPos = $(window).scrollTop();
				};					
				if($(window).scrollTop() >= ($this.offset().top-window.innerHeight) && $(window).scrollTop()<($this.offset().top+window.innerHeight+$this.outerHeight())){		
					$this.css({"background-position":"50% "+ -(scrollPos * speed) +"px"});
				};
			});
		}(jQuery));
	};

	$(document).ready(function() {
		parallaxBanner();
		$(window).on("scroll", function() { 
			requestAnimationFrame(parallaxBanner);
		});
		
	});
}(jQuery));


/*end shortcode posts parallax*/

/*====================================================================================================================================================================================================*/

/*shortcode posts grid*/
;(function($){
	$(document).ready(function() {
		
		/*Slider*/	
		function isNumber(n) {return !isNaN(parseFloat(n)) && isFinite(n);};
		var $cactusSwiperPerView = [];
		var iz= [];
		var checkSetSlider = [];
		$('.cactus-slider-wrap.slidesPerView').each(function(index, element) {	
			checkSetSlider[index] = 0;		
			var $this = $(this);
			var intAutoPlay = $this.attr('data-auto-play');
			$cactusSwiperPerView[index] = $('.cactus-swiper-container', $this).swiper({
				slidesPerView: 'auto',
    			loop: false,
				calculateHeight:true,
				loopedSlides:($this.width() > 1140)?5:3,
				speed:500,	
				autoplayDisableOnInteraction:false,		
			});
			$cactusSwiperPerView[index].update();
			$this.find('.cactus-slider-btn-next').on('click', function(){

				if($cactusSwiperPerView[index].activeIndex==($cactusSwiperPerView[index].slides.length-1) || ($this.offset().left+$this.width()+8 >= $this.find('.swiper-slide:last-child').offset().left+$this.find('.swiper-slide:last-child').width())){
					$cactusSwiperPerView[index].slideTo(0);						
				}else{
					$cactusSwiperPerView[index].slideNext();
				};	
			});			
			$this.find('.cactus-slider-btn-prev').on('click', function(){
				if($cactusSwiperPerView[index].activeIndex==0){							
					$cactusSwiperPerView[index].slideTo($cactusSwiperPerView[index].slides.length-1);					
				}else{
					$cactusSwiperPerView[index].slidePrev();
				};	
			});
			
			if(intAutoPlay!='' && intAutoPlay!=null && typeof(intAutoPlay)!='undefined' && isNumber(intAutoPlay)) {
				$cactusSwiperPerView[index].params.autoplay=intAutoPlay;
				$cactusSwiperPerView[index].startAutoplay();
				var checkAutoPlay = 0;
				var funcSetTimeOut = null;
				
				function _x_off(){					
					if(($this.find('.swiper-slide:last-child').offset().left+$this.find('.swiper-slide:last-child').width()-4)<=($this.width()+$this.offset().left)) {
						return true;
					}else{
						return false;
					};					
				};
				
				$this.on({
					mouseenter: function(){
						if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
						checkAutoPlay = 1;
						$cactusSwiperPerView[index].stopAutoplay();
					}, 
					mouseleave: function(){
						checkAutoPlay = 0;
						if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
						if($this.find('.swiper-slide:last-child').hasClass('swiper-slide-visible') && _x_off()){
							$cactusSwiperPerView[index].stopAutoplay();
							funcSetTimeOut = setTimeout(function(){$cactusSwiperPerView[index].slideTo(0, 1000); $cactusSwiperPerView[index].startAutoplay();},5000);
						}else{
							$cactusSwiperPerView[index].startAutoplay();
						};
					}
				});
				
				$cactusSwiperPerView[index].params.onSlideChangeEnd = function(){										
					if(checkAutoPlay == 0){
						if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
						if($this.find('.swiper-slide:last-child').hasClass('swiper-slide-visible') && _x_off()){
							$cactusSwiperPerView[index].stopAutoplay();
							funcSetTimeOut = setTimeout(function(){if(checkAutoPlay==0){$cactusSwiperPerView[index].slideTo(0, 1000); $cactusSwiperPerView[index].startAutoplay();}},5000);							
						};
					};					
					
					
					$this.on({
						mouseenter: function(){
							if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};	
							$cactusSwiperPerView[index].stopAutoplay();
						}, 
						mouseleave: function(){
							if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
							if($this.find('.swiper-slide:last-child').hasClass('swiper-slide-visible') && _x_off()){
								$cactusSwiperPerView[index].stopAutoplay();
								funcSetTimeOut = setTimeout(function(){$cactusSwiperPerView[index].slideTo(0, 1000); $cactusSwiperPerView[index].startAutoplay();},5000);
							}else{
								$cactusSwiperPerView[index].startAutoplay();
							};
						}
					});
				};					
							
			};

			function createMobileSlider(){
				var activeClassCheck = 	$('.swiper-slide:not(.swiper-slide-duplicate)', $this).find('.width-25percent:not(.add-mobile) .slide-post-item:nth-child(2)');
				var intLengthSlideAdd = activeClassCheck.length;
				if(checkSetSlider[index]==0) {
					// for(iz[index]=0; iz[index] < intLengthSlideAdd; iz[index]++){
					// 	var htmlString = activeClassCheck.eq(iz[index]).html();
					// 	if($('.width-25percent.add-mobile.add-mobile-'+iz[index], $this).length==0 && htmlString!='' && htmlString!=null && typeof(htmlString)!='undefined'){
					// 		$cactusSwiperPerView[index].appendSlide('<div class="width-25percent add-mobile add-mobile-'+iz[index]+'"><div class="slide-post-item">'+activeClassCheck.eq(iz[index]).html()+'</div></div>');
					// 		$('.width-25percent.add-mobile.add-mobile-'+iz[index]).css('width', ($this.find('.cactus-swiper-container').width())+'px');														
					// 	};
					// };	
					$cactusSwiperPerView[index].update();
					$cactusSwiperPerView[index].onResize();
					checkSetSlider[index]=1;
				};
			};
			
			function removeResponsiveSlide(){
				var intLengthSlideRemove = $this.find('.swiper-slide:not(.swiper-slide-duplicate) .width-25percent.add-mobile').length;
				for(var k=0; k < intLengthSlideRemove; k++){
					// $cactusSwiperPerView[index].removeLastSlide();									
				};
				$cactusSwiperPerView[index].update();
				$cactusSwiperPerView[index].onResize();
				checkSetSlider[index]=0;
			};
			
			function calWidthResponsive(){
				var dpr = window.devicePixelRatio;
				if(typeof dpr =='undefined') { dpr = 1;};
				dpr = 1;
				var width = (window.innerWidth * dpr);
				if(width < 768){
					$('.width-50percent, .width-25percent', $this).css('width', ($this.find('.cactus-swiper-container').width())+'px');
					$this.find('.cactus-swiper-container').css('max-height', $this.find('.width-50percent').height());						
					$cactusSwiperPerView[index].params.loopedSlides=1;
					createMobileSlider();				
				}else{
					$('.width-50percent, .width-25percent', $this).css('width', '');
					$this.find('.cactus-swiper-container').css('max-height', '');
					($this.width() > 1140)?$cactusSwiperPerView[index].params.loopedSlides=5:$cactusSwiperPerView[index].params.loopedSlides=3;
					removeResponsiveSlide();
				};	
				
				if($this.find('.swiper-slide.swiper-slide-visible').length == $cactusSwiperPerView[index].slides.length && $this.outerWidth()+8 >= $this.find('.swiper-wrapper').outerWidth()) {
					$this.find('.cactus-slider-btn-next').hide();
					$this.find('.cactus-slider-btn-prev').hide();					
				}else{
					$this.find('.cactus-slider-btn-next').show();
					$this.find('.cactus-slider-btn-prev').show();
				};			
			};
			
			function FixResponsiveSlider(){				
				calWidthResponsive();
				$cactusSwiperPerView[index].update();
				$cactusSwiperPerView[index].onResize();
				$cactusSwiperPerView[index].slideTo(0);		
			};	
							
			FixResponsiveSlider();
			var _df_width = $(window).width();
			$(window).on('resize', function(){
				if($(window).width()!=_df_width){
					FixResponsiveSlider();
					_df_width = $(window).width();
				};
			});			
		});
		/*Slider*/
	});
}(jQuery))

/*end shortcode posts grid*/

/*====================================================================================================================================================================================================*/

/*shortcode smart content box*/

;(function($){
	$.fn.cactus_smart_content_box = function(options){
		
		var $this=$(this);	// Wrap
		function isNumber(n) {return !isNaN(parseFloat(n)) && isFinite(n);};
		
		var sliderItemWrap = [];
		$this.each(function(index, element) {
			
			var $this_item = $(this);
			var $this_category=$('.current-category > a.current-data', $this_item);			
			var urlGetData = $this_item.attr('data-ajax-server');
			var jsonGetData = $this_item.attr('data-json-server');
			var defaultFirstCategoryData = $this_category.attr('data-category-id');
			var smc_bg_color = $this_item.attr('data-bg-color');
			var smc_title_color = $this_item.attr('data-title-color');			
			var smc_data_shortcode = $this_item.attr('data-shortcode');
			var smc_data_ids = $this_item.attr('data-ids');
			var smc_info_err = $this_item.attr('data-lang-err');
			
			if(smc_bg_color!='' && smc_bg_color!=null && typeof(smc_bg_color)!='undefined') {
				//$('<style>.cactus-scb[data-bg-color="'+smc_bg_color+'"] .cactus-scb-title,.cactus-scb[data-bg-color="'+smc_bg_color+'"] .cactus-scb-title:before{background-color:'+smc_bg_color+'}</style>').appendTo('head');
			};
			
			if(smc_title_color!='' && smc_title_color!=null && typeof(smc_title_color)!='undefined') {
				//$('<style>.cactus-scb[data-title-color="'+smc_title_color+'"] .cactus-scb-title {color:'+smc_title_color+'}</style>').appendTo('head');
			};
			
			if(smc_data_shortcode=='' || smc_data_shortcode==null || typeof(smc_data_shortcode)=='undefined') {
				smc_data_shortcode='';
			};
			
			if(smc_data_ids=='' || smc_data_ids==null || typeof(smc_data_ids)=='undefined') {
				smc_data_ids='';
			};
			
			var totalRecords, itemInPage, page, oddItem;
			function reCalpage(intTotalRecords, intItemInPage) {
				totalRecords = intTotalRecords;
				if(!isNumber(totalRecords)) {totalRecords=0};
				totalRecords = parseInt(totalRecords);
				
				itemInPage = intItemInPage;
				if(!isNumber(itemInPage)) {itemInPage=0};
				itemInPage = parseInt(itemInPage);
				
				page = 1;
				
				if(totalRecords > itemInPage) {
					oddItem = (totalRecords % itemInPage);		
					if(oddItem!=0){
						page=( (totalRecords-oddItem) / itemInPage ) + 1;
					}else{
						page=(totalRecords / itemInPage );
					};	
				};
			};
			
			reCalpage($this_item.attr('data-total-records'), $this_item.attr('data-item-in-page'));
			
			function setHeightSlider() {
				var intHeight = $('.swiper-slide.swiper-slide-active > .append-slide-auto > .cactus-listing-wrap', $this_item).height();
				$('.cactus-swiper-container, .swiper-wrapper, .swiper-slide, .append-slide-auto', $this_item).height(intHeight);
			};
			
			var loading = 	'<div class="circularG-wrap">'+
								'<div class="circularG_1 circularG"></div>'+
								'<div class="circularG_2 circularG"></div>'+
								'<div class="circularG_3 circularG"></div>'+
								'<div class="circularG_4 circularG"></div>'+
								'<div class="circularG_5 circularG"></div>'+
								'<div class="circularG_6 circularG"></div>'+
								'<div class="circularG_7 circularG"></div>'+
								'<div class="circularG_8 circularG"></div>'+
							'</div>';
										
			var loading_1 =	'<div class="floatingCirclesG">'+
								'<div class="f_circleG frotateG_01"></div>'+
								'<div class="f_circleG frotateG_02"></div>'+
								'<div class="f_circleG frotateG_03"></div>'+
								'<div class="f_circleG frotateG_04"></div>'+
								'<div class="f_circleG frotateG_05"></div>'+
								'<div class="f_circleG frotateG_06"></div>'+
								'<div class="f_circleG frotateG_07"></div>'+
								'<div class="f_circleG frotateG_08"></div>'+
							'</div>';						
			
			function setNewSlide(mySwiper){
				var slideLength = (mySwiper.activeIndex+2);
								
				if( (slideLength) > page) {
					return -1;										
				}else{
					$('.pre-carousel', $this_item).removeClass('cactus-disable');
					if((slideLength) == page) {
						$('.next-carousel', $this_item).addClass('cactus-disable');						
					};					
					if($('[data-page="'+slideLength+'"]', $this_item).length==0){
						
						var height = $('.swiper-slide.swiper-slide-active', $this_item).height();		
						var newSlider = mySwiper.appendSlide('<div class="swiper-slide"><div class="append-slide-auto" data-page="'+slideLength+'" style="height:'+height+'px">'+loading+'</div></div>');
						// newSlider.append();										
						return slideLength;
					}else{						
						return -1;
					};					
				};
			};
			
            sliderItemWrap[index] = $this_item.find('.cactus-swiper-container').height($this_item.find('.swiper-wrapper .append-slide-auto').height()).swiper({ // Kh?i t?o slider
				loop: false,	
				simulateTouch:false,
				swipeToNext:false,
				speed:500,
				onSwiperCreated:function(){
					setHeightSlider();
					setTimeout(setHeightSlider,368);
				},
				onSlideChangeStart:function(){
					setHeightSlider();
					setTimeout(setHeightSlider,368);
					if(sliderItemWrap[index].activeIndex==0){
						$('.pre-carousel', $this_item).addClass('cactus-disable');
					};
				},
				onSlideChangeEnd:function(){
					setHeightSlider();
					setTimeout(setHeightSlider,368);
				},
				onInit:function(){
					setHeightSlider();
					setTimeout(setHeightSlider,368);
				},				
			});
			
			$this_item.find('.hidden-next-carousel').on('click', function(){sliderItemWrap[index].slideNext()});			
			$('.pre-carousel', $this_item).on('click', function(){
				sliderItemWrap[index].slidePrev();
				$('.next-carousel', $this_item).removeClass('cactus-disable');
			});
			
			function loadAjaxPage(checkPageFillData, categoryData){
				if(urlGetData!='' && urlGetData!=null) {
					var dataPostToServer_1 = {'category':categoryData, 'page':checkPageFillData, 'dataShortcode':smc_data_shortcode, 'ids':smc_data_ids, 'action':'cactusSCBdata'};				
					$.ajax({
						url:		urlGetData,						
						type: 		'POST',
						data:		dataPostToServer_1,
						dataType: 	'html',
						success: 	function(data){
							if(data=='0' || data==''){
								sliderItemWrap[index].removeSlide(checkPageFillData-1);
								setTimeout(function(){
									$this_item.attr('data-total-records', $('.cactus-post-item',$this_item).length);
									reCalpage($('.cactus-post-item',$this_item).length, $this_item.attr('data-item-in-page'));
									sliderItemWrap[index].slidePrev();
								},368);
							}else{
								$('[data-page="'+checkPageFillData+'"]', $this_item).html(data+'<div class="effect-ajax"></div>');
								var intHeight = $('[data-page="'+checkPageFillData+'"] .append-slide-auto > .cactus-listing-wrap', $this_item).height();
								$('.cactus-swiper-container, .swiper-wrapper, .swiper-slide, .append-slide-auto', $this_item).height(intHeight);							
								
								var lazyLoadedImages = document.getElementsByClassName("adaptive");
								for (var i = 0; i < lazyLoadedImages.length; i++) {
									loadAdaptiveImage(lazyLoadedImages[i]);
								};
								
								setHeightSlider();
								setTimeout(function(){setHeightSlider;$('[data-page="'+checkPageFillData+'"] .effect-ajax', $this_item).addClass('hidden');},368);							
							};
						},
						error:		function(){
							sliderItemWrap[index].removeSlide(checkPageFillData-1);
							setTimeout(function(){sliderItemWrap[index].slidePrev()},368);
						},
					});
				};
			};
			
			function setDataAjax(){
				var checkPageFillData=setNewSlide(sliderItemWrap[index]);
				$this_item.find('.hidden-next-carousel').trigger('click');

				if(checkPageFillData!= -1) {
					loadAjaxPage(checkPageFillData, $this_category.attr('data-category-id'));
				};
			};
			
			$('.next-carousel', $this_item).on('click', function(){
				setDataAjax();
			});
			
			if(navigator.userAgent.match(/(Android|iPod|iPhone|iPad|IEMobile|Opera Mini)/)) {
				$('.cactus-swiper-container', $this_item).swipe({					
					swipeLeft:function(event, direction, distance, duration, fingerCount, fingerData) {												
						setDataAjax();							
					},
					threshold:50,
					allowPageScroll:'vertical',
					fingers:'all',
					excludedElements: 'label, button, input, select, textarea, .noSwipe',
				});				
			};
			
			$('.current-category > a.current-data', $this_item).on('click', function(){
				var $this_category = $(this);
				if($('.current-category', $this_item).hasClass('active')) {
					$('.current-category', $this_item).removeClass('active');
				}else{
					$('.current-category', $this_item).addClass('active');
				};
			});
			
			$('.current-category > .ajax-submenu > li > a.new-data', $this_item).on('click', function(){
				var defaultMenuText = $this_category.text();
				var defaultDataID = $this_category.attr('data-category-id');
				
				var newMenuText = $(this).text();
				var newDataID = $(this).attr('data-category-id');
				
				$this_category.attr('data-category-id', newDataID);
				$(this).attr('data-category-id', defaultDataID);
				
				$this_category.text(newMenuText);
				$(this).text(defaultMenuText);
				
				$('.current-category', $this_item).removeClass('active');

				sliderItemWrap[index].removeAllSlides();
				
				if($this_item.find('.loading-new-page').length == 0) { $this_item.find('.swiper-wrapper').html('<div class="loading-new-page">'+loading+'</div>'); };
				if($this_item.find('.loading-new-page-1').length == 0) { $this_item.append('<div class="loading-new-page-1">'+loading_1+'</div>'); };
				$('.pre-carousel, .next-carousel', $this_item).removeClass('cactus-disable').hide();
								
				var dataPostToServer_2 = {'category':$this_category.attr('data-category-id'), 'dataShortcode':smc_data_shortcode, 'ids':smc_data_ids, 'action':'cactusSCBjson',};
				$.ajax({
					url:		jsonGetData,
					type: 		'POST',
					data:		dataPostToServer_2,
					dataType: 	'json',
					cache:		false,
					success: 	function(data){
						if(data.totalRecords!='' && data.totalRecords!=null && typeof(data.totalRecords)!='undefined' && data.itemInPage!='' && data.itemInPage!=null && typeof(data.itemInPage)!='undefined') {
							
							$this_item.attr('data-total-records', data.totalRecords);
							$this_item.attr('data-item-in-page', data.itemInPage);														
							
							reCalpage(data.totalRecords, data.itemInPage);
							
							if(parseInt(data.totalRecords)!=0) {							
								var dataPostToServer_3 = {'category':$this_category.attr('data-category-id'), 'page':'1', 'dataShortcode':smc_data_shortcode, 'ids':smc_data_ids, 'action':'cactusSCBdata'};
								$.ajax({
									url:		urlGetData,
									type: 		'POST',
									data:		dataPostToServer_3,
									dataType: 	'html',
									success: 	function(data){
										if(data=='0' || data==''){
										}else{
											setTimeout(function(){
												$this_item.find('.loading-new-page').remove();
												$this_item.find('.loading-new-page-1').remove();										
												$('.pre-carousel, .next-carousel', $this_item).show();
												
												var newSlider = sliderItemWrap[index].createSlide('<div class="append-slide-auto" data-page="1">'+data+'<div class="effect-ajax"></div></div>');
												newSlider.append();
												
												var intHeight = $('.append-slide-auto[data-page="1"] > .cactus-listing-wrap', $this_item).height();
												$('.cactus-swiper-container, .swiper-wrapper, .swiper-slide, .append-slide-auto', $this_item).height(intHeight);
												$('[data-page="1"] .effect-ajax', $this_item).addClass('hidden');
												
												var lazyLoadedImages = document.getElementsByClassName("adaptive");
												for (var i = 0; i < lazyLoadedImages.length; i++) {
													loadAdaptiveImage(lazyLoadedImages[i]);
												};
												
												setHeightSlider();
												setTimeout(setHeightSlider,368);
											},368);																			
										};
									},
									error:		function(){
									},
								});	
								
							}else{								
								$this_item.find('.loading-new-page').remove();
								$this_item.find('.loading-new-page-1').remove();
								$('.cactus-swiper-container, .swiper-wrapper, .swiper-slide, .append-slide-auto', $this_item).height(30);																
							};
							
						}else{
							loadAjaxPage('1', defaultFirstCategoryData);							
						};
					},
					error:		function(){
						loadAjaxPage('1', defaultFirstCategoryData);						
					},
				});
			});
			
			var _df_width = $(window).width();
			$(window).on('resize', function(){
				if($(window).width()!=_df_width){
					sliderItemWrap[index].update();
					setHeightSlider();
					setTimeout(setHeightSlider,368);
					_df_width = $(window).width();
				};
			});
			
        });	
	};
	
	$(document).ready(function() {
		$('.cactus-tab-content>div:first-child').each(function(index, el) {
			$(this).find('.cactus-scb').removeClass('no-tab-ajax-load');
		});
		$('.cactus-scb:not(.no-tab-ajax-load):not(.one-page-no-filter)').cactus_smart_content_box({});
	});
}(jQuery));
/*end shortcode smart content box*/

/*====================================================================================================================================================================================================*/

/*shortcode posts slider*/

;(function($){
	function parallaxBanner(){
		(function($){
			$('.cactus-banner-parallax-slider').each(function(index, element) {
				var $this=$(this).find('.cactus-banner-parallax-content');
				var speed = 0.4;
				var scrollPos = $(window).scrollTop()-$this.offset().top;	
				if($this.offset().top < window.innerHeight){
					speed = 0.6;
					scrollPos = $(window).scrollTop();
				};	
				if($(window).scrollTop() >= ($this.offset().top-window.innerHeight) && $(window).scrollTop()<($this.offset().top+window.innerHeight+$this.outerHeight())){		
					$this.css({"background-position":"50% "+ -(scrollPos * speed) +"px"});
				};
			});
		}(jQuery));
	};
	$(document).ready(function() {
		function isNumber(n) {return !isNaN(parseFloat(n)) && isFinite(n);};
		var cactusFaddingSlider = [];
		$('.cactus-banner-parallax-slider').each(function(index, element) {
			var $this = $(this);
			var intAutoPlay = $this.attr('data-autoplay');
			$this.find('.pagination').attr('data-target', 'cbps-parallax-'+index);
			cactusFaddingSlider[index] = $('.cactus-swiper-container', $this).swiper({
				slidesPerView: 1,
				loop: false,
				calculateHeight:true,
				speed:400,
				simulateTouch:true,
				grabCursor: false,
				roundLengths:true,
				watchSlidesProgress:true,
				effect: 'fade',
				// onProgress: function(swiper){
				// 	for (var i = 0; i < swiper.slides.length; i++){
				// 		var slide = swiper.slides[i];
				// 		var progress = slide.progress;
				// 		var translate = progress*swiper.width;  
				// 		var opacity = 1 - Math.min(Math.abs(progress),1);
				// 		slide.style.opacity = opacity;
				// 		swiper.setTransform(slide,'translate3d('+translate+'px,0,0)');
				// 	};
				// },
				// onTouchStart:function(swiper){				
				// 	for (var i = 0; i < swiper.slides.length; i++){
				// 		swiper.setTransition(swiper.slides[i], 0);
				// 	};
				// },
				// onSetTransition: function(swiper, speed) {					
				// 	for (var i = 0; i < swiper.slides.length; i++){
				// 		swiper.setTransition(swiper.slides[i], speed);						
				// 	};					
				// },
			// 	onProgress: function(swiper, progress){
			//         for (var i = 0; i < swiper.slides.length; i++){
			//             var slide = swiper.slides[i];
			//             var progress = slide.progress;
			//             var translate = progress * swiper.width;
			//             var translate, opacity, bOpacity;
			//             // var opacity =  1 - Math.min(Math.abs(progress),1)
			//             if (progress > 0) {
			//                 translate;
			//                 // bOpacity = 0;
			//                 // opacity = 0;
			//             }
			//             else {
			//                 translate = 0;
			//                 // bOpacity = 1  - Math.min(Math.abs(progress),1);
			//                 // opacity ;
			//             }
			//             $(slide).css({
			//                 // opacity: bOpacity,
			//                 transform: 'translate3d(' + 0 + 'px,0,0)' ,
			//                 // opacity:opacity,
			//                 transition: 'opacity 600ms, translate3d 400ms'
			//             });
			//         }
			//     },
			//     onTouchStart: function(swiper){
			//         for (var i = 0; i < swiper.slides.length; i++){
			//             $(swiper.slides[i]).css({ transition: '' });
			//         }
			//     },
			//     onSetTransition: function(swiper, speed) {
			//         for (var i = 0; i < swiper.slides.length; i++){
			//             $(swiper.slides[i]).css({ transition: 'opacity '+600+'ms'+','+'translate3d ' + speed + 'ms' });
			//         }
			//     },
				paginationClickable: true,
				pagination: '.pagination[data-target="cbps-parallax-'+index+'"]',
				autoplayDisableOnInteraction:false,
			});	
			
			cactusFaddingSlider[index].update();
			if(intAutoPlay!='' && intAutoPlay!=null && typeof(intAutoPlay)!='undefined' && isNumber(intAutoPlay) && intAutoPlay=='1') {
				cactusFaddingSlider[index].params.autoplay=5000;
				cactusFaddingSlider[index].startAutoplay();
				var checkAutoPlay = 0;
				var funcSetTimeOut = null;
				$this.on({
					mouseenter: function(){
						if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
						checkAutoPlay = 1;
						cactusFaddingSlider[index].stopAutoplay();
					}, 
					mouseleave: function(){
						checkAutoPlay = 0;
						if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
						if(cactusFaddingSlider[index].activeIndex == cactusFaddingSlider[index].slides.length-1){
							cactusFaddingSlider[index].stopAutoplay();
							funcSetTimeOut = setTimeout(function(){cactusFaddingSlider[index].slideTo(0, 1000); cactusFaddingSlider[index].startAutoplay();},5000);
						}else{
							cactusFaddingSlider[index].startAutoplay();
						};
					}
				});
				
				cactusFaddingSlider[index].params.onSlideChangeEnd = function(){					
					if(checkAutoPlay == 0){
						if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
						if(cactusFaddingSlider[index].activeIndex == cactusFaddingSlider[index].slides.length-1){
							cactusFaddingSlider[index].stopAutoplay();
							funcSetTimeOut = setTimeout(function(){if(checkAutoPlay==0){cactusFaddingSlider[index].slideTo(0, 1000); cactusFaddingSlider[index].startAutoplay();}},5000);
						};
					};	
					$this.on({
						mouseenter: function(){
							if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};	
							cactusFaddingSlider[index].stopAutoplay();
						}, 
						mouseleave: function(){
							if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
							if(cactusFaddingSlider[index].activeIndex == cactusFaddingSlider[index].slides.length-1){
								cactusFaddingSlider[index].stopAutoplay();
								funcSetTimeOut = setTimeout(function(){cactusFaddingSlider[index].slideTo(0, 1000); cactusFaddingSlider[index].startAutoplay();},5000);
							}else{
								cactusFaddingSlider[index].startAutoplay();
							};
						}
					});
				};					
							
			};
			
			// function fixFadingResize(e){
			// 	$this.find('.swiper-container, .swiper-slide').css({'width':window.innerWidth+'px'});
				
			// 	for(var k=0; k < cactusFaddingSlider[index].slides.length; k++){
			// 		cactusFaddingSlider[index].setTransition(cactusFaddingSlider[index].slides[k], 0);
			// 	};	
			// 	$('.swiper-wrapper', $this).stop(true,true).css('transition-duration','0s');
			// 	cactusFaddingSlider[index].reInit();
			// 	cactusFaddingSlider[index].resizeFix();	
			// 	if(cactusFaddingSlider[index].activeIndex>0) {
			// 		cactusFaddingSlider[index].swipeTo(0);	
			// 	};	
			// };

			var _df_width = $(window).width();
			$(window).on('resize', function() { 
				if($(window).width()!=_df_width){
					// fixFadingResize();
					cactusFaddingSlider[index].onResize()
					// cactusFaddingSlider[index].slideTo(0);
					cactusFaddingSlider[index].update();
					_df_width = $(window).width();
				};
			});
		});
			
	});
}(jQuery));


/*end shortcode posts slider*/

/*====================================================================================================================================================================================================*/

/*shortcode posts carousel*/
;(function($){
	$(document).ready(function() {
		function createCarousel(options) {
			function isNumber(n) {return !isNaN(parseFloat(n)) && isFinite(n);};
			var cactusCarousel = [];
			$('.cactus-carousel').each(function(index, element) {
                var $this = $(this);
				var parentsWidth = $this.parent().width();
				var perview = 3;
				var intAutoPlay = $this.attr('data-autoplay');
				var intVisibleItem = $this.attr('data-visible');
				
				function checkPerviewLoop() {
					if (parentsWidth >= 1890){
						perview=6;
					}else if (parentsWidth >= 1550){
						perview=5;
					}else if (parentsWidth >= 1200){
						perview=4;
					}else if(parentsWidth >= 992){
						if(intVisibleItem!='' && intVisibleItem!=null && typeof(intVisibleItem)!='undefined' && isNumber(intVisibleItem)){
							perview=intVisibleItem;
						}else{
							perview=3;
						};
					}else if(parentsWidth >= 768){
						perview=2;	
					}else if(parentsWidth >= 580){
						perview=2;		
					}else{
						perview=1;
					};
				};
				checkPerviewLoop();
				
				cactusCarousel[index] = $('.cactus-swiper-container', $this).swiper({
					slidesPerView: perview,
					loop: false,
					calculateHeight:true,
					speed:600,
					simulateTouch:true,
					loopedSlides:perview,
					grabCursor: true,
					roundLengths:true,
					autoplayDisableOnInteraction:false,
				});	
				cactusCarousel[index].update(true);
				
				$this.find('.next-carousel').on('click', function(){
					if($this.offset().left+$this.width() >= $this.find('.swiper-slide:last-child').offset().left+$this.find('.swiper-slide:last-child').width()){
						cactusCarousel[index].slideTo(0);						
					}else{
						cactusCarousel[index].slideNext();
					};	
				});			
				$this.find('.pre-carousel').on('click', function(){
					if(cactusCarousel[index].activeIndex==0){							
						cactusCarousel[index].slideTo(cactusCarousel[index].slides.length-1);					
					}else{
						cactusCarousel[index].slidePrev();
					};	
				});
				
				if(intAutoPlay!='' && intAutoPlay!=null && typeof(intAutoPlay)!='undefined' && isNumber(intAutoPlay) && intAutoPlay=='1') {
					cactusCarousel[index].params.autoplay=5000;
					cactusCarousel[index].startAutoplay();
					var checkAutoPlay = 0;
					var funcSetTimeOut = null;
					$this.on({
						mouseenter: function(){
							if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
							checkAutoPlay = 1;
							cactusCarousel[index].stopAutoplay();
						}, 
						mouseleave: function(){
							checkAutoPlay = 0;
							if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
							if($this.find('.swiper-slide:last-child').hasClass('swiper-slide-visible')){
								cactusCarousel[index].stopAutoplay();
								funcSetTimeOut = setTimeout(function(){cactusCarousel[index].slideTo(0, 1000); cactusCarousel[index].startAutoplay();},5000);
							}else{
								cactusCarousel[index].startAutoplay();
							};
						}
					});
					
					cactusCarousel[index].params.onSlideChangeEnd = function(){										
						if(checkAutoPlay == 0){
							if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
							if($this.find('.swiper-slide:last-child').hasClass('swiper-slide-visible')){
								cactusCarousel[index].stopAutoplay();
								funcSetTimeOut = setTimeout(function(){if(checkAutoPlay==0){cactusCarousel[index].slideTo(0, 1000); cactusCarousel[index].startAutoplay();}},5000);
								
							};
						};	
						$this.on({
							mouseenter: function(){
								if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};	
								cactusCarousel[index].stopAutoplay();
							}, 
							mouseleave: function(){
								if(funcSetTimeOut!=null) {clearTimeout(funcSetTimeOut);};
								if($this.find('.swiper-slide:last-child').hasClass('swiper-slide-visible')){
									cactusCarousel[index].stopAutoplay();
									funcSetTimeOut = setTimeout(function(){cactusCarousel[index].slideTo(0, 1000); cactusCarousel[index].startAutoplay();},5000);
								}else{
									cactusCarousel[index].startAutoplay();
								};
							}
						});
					};					
								
				};
				
				function showHideNControl(){
					if($this.find('.swiper-slide.swiper-slide-visible').length == cactusCarousel[index].slides.length) {
						$this.find('.next-carousel').hide();
						$this.find('.pre-carousel').hide();
					}else{
						$this.find('.next-carousel').show();
						$this.find('.pre-carousel').show();
					};
				};
				
				function calWidthResponsive(){
					parentsWidth = $this.parent().width();
					checkPerviewLoop();
					// cactusCarousel[index].appendSlide('<div class="swiper-slide"><div class="carousel-item"></div></div>');					
					cactusCarousel[index].params.slidesPerView=perview;
					cactusCarousel[index].params.loopedSlides=perview;						
					// cactusCarousel[index].removeLastSlide();			
					cactusCarousel[index].update();
					cactusCarousel[index].onResize();	
					cactusCarousel[index].slideTo(0);	
					showHideNControl();			
				};
				
				calWidthResponsive();				
				var _df_width = $(window).width();
				$(window).on('resize', function(){
					if($(window).width()!=_df_width){
						calWidthResponsive();	
						_df_width = $(window).width();
					};
				});

            });
		};
		createCarousel({});
	});
}(jQuery));
/*end shortcode posts carousel*/

/*====================================================================================================================================================================================================*/

/*tab smart*/
;(function($){

	$('.cactus-tab-button > .sub-items:not(.show-on-mobile) > span:not(.not-button)').on('click', function(){
		var $this = $(this);
		var $__group = $this.parents('.cactus-tab-button');
		var $__parents = $this.parents('.cactus-tab');
		var $__content = $('.cactus-tab-content > div', $__parents);
		

		if($this.hasClass('active')) {return false;}
		
		$('.sub-items:not(.show-on-mobile)>span', $__group).removeClass('active');
		$this.addClass('active');
		$('.sub-items.show-on-mobile > .not-button', $__group).html($this.html());
		
		var $__active_id = $this.attr('data-active');
		$__content.removeClass('active');
		$('.cactus-tab-content > div[data-active="'+$__active_id+'"]', $__parents).addClass('active');		

		if(!$('.cactus-tab-content > div[data-active="'+$__active_id+'"].active', $__parents).hasClass('check-smart-init')) {
			$('.cactus-tab-content > div[data-active="'+$__active_id+'"].active:not(.check-smart-init) .cactus-scb.no-tab-ajax-load:not(.one-page-no-filter)', $__parents).cactus_smart_content_box({});
			$('.cactus-tab-content > div[data-active="'+$__active_id+'"].active:not(.check-smart-init)', $__parents).addClass('check-smart-init');
		}

		var intHeight = $('.cactus-tab-content > div[data-active="'+$__active_id+'"].active .cactus-scb:not(.one-page-no-filter) .swiper-slide-visible.swiper-slide-active > .append-slide-auto > .cactus-listing-wrap', $__parents).height();
		
		$('.cactus-tab-content > div[data-active="'+$__active_id+'"].active .cactus-scb:not(.one-page-no-filter) .cactus-swiper-container, .cactus-tab-content > div[data-active="'+$__active_id+'"].active .cactus-scb:not(.one-page-no-filter) .swiper-wrapper, .cactus-tab-content > div[data-active="'+$__active_id+'"].active .cactus-scb:not(.one-page-no-filter) .swiper-slide, .cactus-tab-content > div[data-active="'+$__active_id+'"].active .cactus-scb:not(.one-page-no-filter) .append-slide-auto', $__parents).height(intHeight);

		$('.sub-items:not(.show-on-mobile)', $__group).removeClass('active');
	});
	
	$('.cactus-tab-button > .sub-items.show-on-mobile > span.not-button').on('click', function(){
		var $this = $(this);
		$this.parent('.sub-items').next('.sub-items:not(.show-on-mobile)').toggleClass('active');
	});
}(jQuery));