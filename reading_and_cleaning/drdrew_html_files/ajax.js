( function() {
	// Save current page
	if(typeof cactus.query_vars !== 'undefined'){
		_current_page = cactus.query_vars.paged;
	} else {
		_current_page = -1;
	}
	if(_current_page == 0) _current_page = 1;
	// flag to check if an ajax is executing
	_ajax_loading = false;

	function do_ajax(blog_layout)
	{

		if(jQuery('#navigation-ajax').length > 0){
			jQuery('#navigation-ajax').live('click', function(e){
				  e.preventDefault();
				  if(_current_page > -1 && !_ajax_loading){
						item_template = jQuery(this).attr('data-template');
						icon_loading 			= jQuery('.navigation-ajax i');
						ajax_button 			= jQuery('#navigation-ajax');
						var id_playlist;
						if(jQuery('#single-playlist').length > 0) {
							id_playlist=jQuery('#single-playlist').val();
						}else{
							id_playlist='';
						};
						data = 	{
									action: 'load_more',
									page: _current_page,
									template: item_template,
									vars:cactus.query_vars,
									blog_layout: blog_layout,
									id_playlist: id_playlist,

								};

						content_div = jQuery(this).attr('data-target');

						_ajax_loading = true;
						ajax_button.addClass('hidden1-loading');
						icon_loading.removeClass('hidden-loading');

					    jQuery.ajax({
							  type: 'POST',
							  url: cactus.ajaxurl,
							  cache: false,
							  data: data,
							  success: function(data, textStatus, XMLHttpRequest){
								if(data != ''){

									jQuery(content_div).append(data);

									jQuery('.fa-refresh').removeClass("fa-spin");
									jQuery('.fa-refresh').addClass("hide");
									jQuery('.load-title').removeClass("hidden");
									jQuery('#navigation-ajax').removeClass("disabled");
									
									// increase current page
									_current_page = _current_page + 1;

									if(jQuery('.no-posts').length > 0){
										// no more post
										_current_page = -1;
										jQuery(".navigation-ajax").hide();
									}

									icon_loading.addClass('hidden-loading');
									ajax_button.removeClass('hidden1-loading');

								} else {
									_current_page = -1;
									// do something else when there is no more results
									// alert('No more results. You should do something, like hiding this link button. Edit me in /js/ajax.js');
									 jQuery(".navigation-ajax").hide();
								}

								_ajax_loading = false;
							  },
							  error: function(MLHttpRequest, textStatus, errorThrown){
									alert(errorThrown);
									_ajax_loading = false;
									icon_loading.addClass('hidden-loading');
									ajax_button.removeClass('hidden1-loading');
							  }
						  });
					}

				});
		}
	}

	jQuery(document).ready(function(){
		var blog_layout 			= jQuery('input[name=hidden_blog_layout]').val();

		jQuery('#navigation-ajax').click(function() {
			jQuery('.fa-refresh').addClass("fa-spin");
			jQuery('.fa-refresh').removeClass("hide");
			jQuery('.load-title').addClass("hidden");
			jQuery('#navigation-ajax').addClass("disabled");
			do_ajax(blog_layout);
		});

	});
}) ();