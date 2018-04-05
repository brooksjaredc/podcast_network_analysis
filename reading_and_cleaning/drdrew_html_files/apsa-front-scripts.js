/**
 * Set coockie function
 * 
 * @param str cname
 * @param str cvalue
 * @param int exseconds
 * @returns {undefined}
 */
function apsa_set_cookie(cname, cvalue, exseconds) {
    var d = new Date();
    d.setTime(d.getTime() + (exseconds * 1000));
    var expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + "; " + expires + "; path=/";
}

/**
 * Get coockie function
 * 
 * @param str cname
 * @returns {String}
 */
function apsa_get_cookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ')
            c = c.substring(1);
        if (c.indexOf(name) == 0)
            return c.substring(name.length, c.length);
    }
    return "";
}

/**
 * Detect IE version
 * 
 * @returns {Boolean}
 */
function apsa_ie_version() {
    var ua = window.navigator.userAgent;
    var edge = ua.indexOf('Edge/');
    var msie = ua.indexOf("MSIE ");
    if (msie > 0)  // If Internet Explorer, return version number
    {
        return parseInt(ua.substring(msie + 5, ua.indexOf(".", msie)));
    } else if (!!navigator.userAgent.match(/Trident.*rv\:11\./)) {
        return 11;
    } else if (edge > 0) {
        return (parseInt(ua.substring(edge + 5, ua.indexOf('.', edge)), 10));
    }

    return false;
}


/*
 * Background element scripts 
 */
function apsa_set_bg(option, info, anticache) {
    var apsa_bg_options = option;
    var apsa_bg_info = info;
    if (typeof apsa_bg_options !== "undefined") {
        // hook before element ready
        if (typeof apsa_before_element_show == 'function') {
            var that = jQuery(apsa_bg_options["bg_selector"]);
            apsa_bg_options.camp_type = 'background';
            apsa_bg_options = apsa_before_element_show(that, apsa_bg_options);
        }

        // Update element statistics
        apsa_add_event(apsa_bg_options["bg_element_id"], 'view');
        if (typeof apsa_bg_options["bg_selector"] == "string" && apsa_bg_options["bg_selector"] !== "") {
            jQuery(apsa_bg_options["bg_selector"]).addClass("apsa-bg-" + apsa_bg_options["bg_element_type"]).attr('data-apsa-element-id', apsa_bg_options["bg_element_id"]).attr('data-apsa-campaign-id', apsa_bg_info["campaign_id"]);
            if (anticache) {
                jQuery('body').append('<style id="apsa-bg-element-style" type="text/css">' + apsa_bg_options['bg_element_style'] + '</style>');
            }
        }

        // hook when element ready
        if (typeof apsa_element_show == 'function') {
            var that = jQuery(apsa_bg_options["bg_selector"]);
            apsa_bg_options.camp_type = 'background';
            apsa_element_show(that, apsa_bg_options);
        }

        /** Set campaign info coockie */
        if (typeof apsa_bg_info !== 'undefined' && apsa_bg_info !== "") {
            var apsa_bg_info_str = JSON.stringify(apsa_bg_info);
            apsa_set_cookie("apsa_bg_info", apsa_bg_info_str, 30 * 86400);
        }
        if (apsa_bg_options["bg_change_interval"] != "during") {
            apsa_set_cookie("apsa_bg_change_interval", apsa_bg_options["bg_change_intervall"], parseInt(apsa_bg_options["bg_change_interval"]));
        }

    }
}


/**
 * Popup element scripts
 */
function apsa_set_pop(option, info) {
    var overlayTransitionTime = jQuery("#apsa-popup-overlay").css('transition-duration') ? parseFloat(jQuery("#apsa-popup-overlay").css('transition-duration')) * 1000 : 200;
    var apsa_pop_options = option;
    var apsa_popup_info = info;
    if (typeof apsa_pop_options !== "undefined") {
        if (apsa_pop_options["pop_element_type"] == "image") {
            jQuery("body").prepend('<img id="apsa-pop-hidden-img" src="' + apsa_pop_options["pop_element_content"] + '" />');
        }

        /** Set campaign info coockie */
        if (typeof apsa_popup_info !== 'undefined' && apsa_popup_info !== "") {
            var apsa_popup_info_str = JSON.stringify(apsa_popup_info);
            apsa_set_cookie("apsa_popup_info", apsa_popup_info_str, 30 * 86400);
        }

        /** Append overlay popup */
        jQuery("body").append('<div id="apsa-popup-overlay"' + ((apsa_pop_options["pop_overlay_pattern"] != "none") ? ' class="apsa-pop-dark-overlay apsa-suspense-hidden"' : "") + '></div>');
        if (apsa_pop_options["pop_overlay_pattern"] != "none" && apsa_pop_options["pop_overlay_pattern"] != "gray") {
            jQuery('#apsa-popup-overlay').css('background-image', 'url("' + apsa_plugin_dir + 'view/front/images/patterns/' + apsa_pop_options["pop_overlay_pattern"] + '")');
        }

        /** Draw and append popup block if cache enabled */
        if (typeof apsa_extra_options.apsa_cache_enabled != 'undefined' && apsa_extra_options.apsa_cache_enabled == 'true') {
            var popup_class = "apsa-pop-" + apsa_pop_options['pop_popup_direction'];

            jQuery("body").append('<div id="apsa-popup-cont" style="width: ' + apsa_pop_options['pop_width'] + '; height: ' + apsa_pop_options['pop_height'] + '" class="' + ((apsa_pop_options["pop_put_in_frame"] == "on") ? ' apsa-popup-border ' : "") + popup_class + ' apsa-suspense-hidden apsa-reset-start apsa-popup-' + apsa_pop_options['pop_element_type'] + ' ' + apsa_pop_options['pop_popup_direction_in'] + '" data-apsa-in="' + apsa_pop_options['pop_popup_direction_in'] + '" data-apsa-out="' + apsa_pop_options['pop_popup_direction_out'] + '" data-apsa-correction-out="' + apsa_pop_options['pop_popup_correction_out'] + '" data-apsa-element-id="' + apsa_pop_options['pop_element_id'] + '" data-apsa-campaign-id="' + apsa_popup_info['campaign_id'] + '"><div id="apsa-popup-header">\n\
                          <span class="apsa-close-popup apsa-pop-hidden-close" style="color: ' + apsa_pop_options["pop_frame_color"] + '"></span>\n\
                          <div id="apsa-hide-text" class="apsa-hide-text-hidden"><span class="apsa-hide-settlement" style="color: ' + apsa_pop_options["pop_frame_color"] + ';">' + ((apsa_pop_options["pop_hide_element_after"] !== "-1") ? apsa_pop_options["pop_hide_element_after"] : "") + '</span></div>\n\
                          <div id="apsa-close-text"><span class="apsa-close-settlement"' + ' style="color: ' + apsa_pop_options["pop_frame_color"] + ';"' + '>' + ((apsa_pop_options["pop_show_close_after"] !== "0") ? apsa_pop_options["pop_show_close_after"] : "") + '</span></div>\n\
                          </div><div id="apsa-popup-element"' + ((apsa_pop_options["pop_put_in_frame"] == "on") ? ' style="background-color: ' + apsa_pop_options["pop_frame_color"] + '; border-color: ' + apsa_pop_options["pop_frame_color"] + '"' : "") + '></div></div>');

            /** Set content element */
            jQuery("#apsa-popup-element").append(apsa_pop_options["pop_element_html"]);
        }

        function apsa_show_popup() {
            // hook before element ready
            if (typeof apsa_before_element_show == 'function') {
                var that = jQuery('#apsa-popup-cont');
                apsa_pop_options.camp_type = 'popup';
                apsa_pop_options = apsa_before_element_show(that, apsa_pop_options);
            }

            // Add "apsa-reset-style" class to appropriate elements
            apsa_reset_style();

            setTimeout(function () {
                //  when set popup window scroll hidden
                jQuery('html, body').addClass("apsa-hide-scroll");

                /** Determine and set element content position */
                apsa_set_popup_correction(apsa_pop_options, true);

                if (apsa_pop_options["pop_overlay_pattern"] != 'none') {
                    setTimeout(function () {
                        jQuery("#apsa-popup-cont").removeClass("apsa-suspense-hidden");
                    }, overlayTransitionTime);
                    jQuery("#apsa-popup-overlay").removeClass("apsa-suspense-hidden").removeClass('apsa-pop-dark-overlay');
                    jQuery("#apsa-popup-overlay")[0].offsetHeight;
                    jQuery("#apsa-popup-overlay").addClass('apsa-pop-dark-overlay-show');
                } else {
                    jQuery("#apsa-popup-cont").removeClass("apsa-suspense-hidden");
                }
                jQuery("#apsa-popup-cont")[0].offsetHeight;
                jQuery("#apsa-popup-cont").css("opacity", "1");

                var show_close_after = apsa_pop_options['pop_show_close_after'];
                var hide_element_after = apsa_pop_options['pop_hide_element_after'];

                if (show_close_after !== 0) {
                    var close_after = setInterval(function () {
                        if (show_close_after == 1) {
                            clearInterval(close_after);
                            if (hide_element_after !== "-1") {
                                jQuery("#apsa-hide-text").removeClass("apsa-hide-text-hidden");
                            }
                        }

                        show_close_after = show_close_after - 1;
                        jQuery(".apsa-close-settlement").text(show_close_after)
                    }, 1000);
                }

                if (hide_element_after !== "-1") {
                    if (show_close_after == 0) {
                        jQuery("#apsa-hide-text").removeClass("apsa-hide-text-hidden");
                    }
                    var hide_after = setInterval(function () {
                        if (hide_element_after == 0) {
                            clearInterval(hide_after);
                        }

                        hide_element_after = hide_element_after - 1;
                        jQuery(".apsa-hide-settlement").text(hide_element_after)
                    }, 1000);
                }

                // set popup correction
                var apsaId;
                jQuery(window).resize(function () {
                    if (jQuery("#apsa-popup-cont").length > 0) {
                        clearTimeout(apsaId);
                        apsaId = setTimeout(function () {
                            apsa_set_popup_correction(apsa_pop_options);
                        }, 100);
                    }
                });

                // Display close popup button
                setTimeout(function () {
                    jQuery("#apsa-close-text").remove();
                    jQuery(".apsa-close-popup").removeClass("apsa-pop-hidden-close");
                }, apsa_pop_options['pop_show_close_after'] * 1000);

                // Hide element if set appropriate option
                if (apsa_pop_options["pop_hide_element_after"] !== '-1') {
                    setTimeout(apsa_close_popup, apsa_pop_options['pop_hide_element_after'] * 1000);
                }

                // hook when element ready
                if (typeof apsa_element_show == 'function') {
                    var that = jQuery('#apsa-popup-cont');
                    apsa_pop_options.camp_type = 'popup';
                    apsa_element_show(that, apsa_pop_options);
                }

                // Update element statistics
                apsa_add_event(apsa_pop_options["pop_element_id"], 'view');
            }, apsa_pop_options['pop_view_after'] * 1000);
        }

        if (apsa_pop_options["pop_element_type"] == "image") {
            jQuery("#apsa-pop-hidden-img").on('load', function () {
                apsa_show_popup();
            }).error(function (e) {
                jQuery("#apsa-popup-element").empty();
                apsa_show_popup();
            });
        } else {
            apsa_show_popup();
        }

        apsa_set_cookie("apsa_pop_view_interval", apsa_pop_options["pop_view_interval"], parseInt(apsa_pop_options["pop_view_interval"]));

        if (apsa_pop_options["pop_change_interval"] != "during") {
            apsa_set_cookie("apsa_pop_change_interval", apsa_pop_options["pop_change_interval"], parseInt(apsa_pop_options["pop_change_interval"]));
        }
    }
}

//function for close popup
function apsa_close_popup() {
    var overlayTransitionTime = jQuery("#apsa-popup-overlay").css('transition-duration') ? parseFloat(jQuery("#apsa-popup-overlay").css('transition-duration')) * 1000 : 200;
    jQuery('#apsa-popup-cont').removeClass(jQuery('#apsa-popup-cont').data('apsa-in'));
    jQuery('#apsa-popup-cont').addClass(jQuery('#apsa-popup-cont').data('apsa-out'));
    setTimeout(function () {
        jQuery("#apsa-popup-cont").remove();
        jQuery("#apsa-popup-overlay").addClass('apsa-opasity-0');
        jQuery("#apsa-popup-overlay").removeClass('apsa-pop-dark-overlay-show');
        setTimeout(function () {
            jQuery("#apsa-popup-overlay").remove();
        }, overlayTransitionTime);
        //when close popup window scroll is show
        jQuery('html, body').removeClass("apsa-hide-scroll");
        jQuery(window).resize();
    }, (parseFloat(jQuery('#apsa-popup-cont').css('animation-duration')) - jQuery('#apsa-popup-cont').data('apsa-correction-out')) * 1000);
}

/** Determine and set embed campaigns cookie */
function apsa_set_embed_cookie() {
    jQuery(".apsa-embed-info").each(function () {
        var info_array = jQuery(this).serializeArray();
        var campaign_id = info_array[0]["value"];
        var last = info_array[1]["value"];
        var last_id = info_array[2]["value"];
        var change_interval = info_array[3]["value"];

        var apsa_emb_info = {};
        apsa_emb_info["campaign_id"] = campaign_id;
        apsa_emb_info["last"] = last;
        apsa_emb_info["last_id"] = last_id;

        // check if cookcie already set or not
        if (apsa_get_cookie("apsa_embeds_info") == "" || apsa_get_cookie("apsa_embeds_info") == null || apsa_get_cookie("apsa_embeds_info") == "undefined") {
            var apsa_embeds_info = {};
        } else {
            apsa_embeds_info = JSON.parse(apsa_get_cookie("apsa_embeds_info"));
        }

        // Set embed coockie
        apsa_embeds_info[campaign_id] = apsa_emb_info;
        var apsa_embeds_info_str = JSON.stringify(apsa_embeds_info);
        apsa_set_cookie("apsa_embeds_info", apsa_embeds_info_str, 30 * 86400);
        if (change_interval !== "dontset") {
            apsa_set_cookie("apsa_emb_change_interval_" + campaign_id, change_interval, parseInt(change_interval));
        }
    });
}

/*
 * set popup correction
 */
function apsa_set_popup_correction(apsa_pop_options, onLoad) {
    var windowHeight = jQuery(window).height();
    var windowWidth = jQuery(window).width();
    var popHeight;
    var popWidth;
    var leftBorderSize = parseInt(jQuery('#apsa-popup-element').css('border-left-width'));
    var rightBorderSize = parseInt(jQuery('#apsa-popup-element').css('border-right-width'));
    var topBorderSize = parseInt(jQuery('#apsa-popup-element').css('border-top-width'));
    var bottomBorderSize = parseInt(jQuery('#apsa-popup-element').css('border-bottom-width'));
    var popupHeaderSize = parseInt(jQuery('#apsa-popup-header').css('height'));

    // check popup width % or px
    if (apsa_pop_options['pop_width'].slice(-1) == '%') {
        if (windowWidth < (windowWidth * parseInt(apsa_pop_options['pop_width']) / 100 + leftBorderSize + rightBorderSize)) {
            popWidth = windowWidth - (leftBorderSize + rightBorderSize);
        } else {
            popWidth = windowWidth * parseInt(apsa_pop_options['pop_width']) / 100;
        }
    } else {
        if (windowWidth < (parseInt(apsa_pop_options['pop_width']) + leftBorderSize + rightBorderSize)) {
            popWidth = windowWidth - (leftBorderSize + rightBorderSize);
        } else {
            popWidth = apsa_pop_options['pop_width'];
        }
    }

    // check popup height set % or px
    if (apsa_pop_options['pop_height'].slice(-1) == '%') {
        if ((windowHeight) < (windowHeight * parseInt(apsa_pop_options['pop_height']) / 100 + popupHeaderSize + topBorderSize + bottomBorderSize))
            popHeight = (windowHeight - (popupHeaderSize + topBorderSize + bottomBorderSize));
        else
            popHeight = windowHeight * parseInt(apsa_pop_options['pop_height']) / 100;
    } else {
        if ((windowHeight) < (parseInt(apsa_pop_options['pop_height']) + popupHeaderSize + topBorderSize + bottomBorderSize))
            popHeight = (windowHeight - (popupHeaderSize + topBorderSize + bottomBorderSize));
        else
            popHeight = apsa_pop_options['pop_height'];
    }

    jQuery("#apsa-popup-cont")[0].offsetHeight;
    jQuery("#apsa-popup-cont").css("bottom", 'initial');
    if (windowWidth >= apsa_mobile_size) {
        jQuery('#apsa-popup-cont').css('margin-top', 'auto');
        jQuery('#apsa-popup-cont').removeClass('mobileView');
        var top = Math.max(parseInt((windowHeight - parseInt(popHeight)) / 2), (popupHeaderSize + topBorderSize));
        jQuery('#apsa-popup-cont').css({
            'top': top,
            'height': popHeight,
            'width': popWidth
        });
    } else {
        jQuery('#apsa-popup-cont').css({
            'height': windowHeight,
        });
        jQuery('#apsa-popup-cont').addClass('mobileView');
    }
}

/**
 *  function for set embed animation
 */
function apsa_set_embed_animation() {
    jQuery(".apsa-embed-cont").each(function () {
        var embed = jQuery(this);

        // hook before element ready
        if (embed.data("apsa-before-show") !== true) {
            if (typeof apsa_before_element_show == 'function' && !embed.hasClass('apsa-not-loaded')) {
                var options = {
                    camp_type: 'embed'
                }
                apsa_before_element_show(embed, options);
            }            
                        
            // Add "apsa-reset-style" class to appropriate elements
            apsa_reset_style();

            embed.data("apsa-before-show", true);
        }

        if (!embed.hasClass(embed.data('apsa-animation-name')) && !embed.hasClass('apsa-not-loaded') && apsa_is_scrolled_into_view(embed)) {
            // hook when element ready
            if (typeof apsa_element_show == 'function') {
                var options = {
                    camp_type: 'embed'
                }
                apsa_element_show(embed, options);
            }

            embed.addClass('apsa-embed-cont-visible');
            embed.addClass(embed.data('apsa-animation-name'));
        }
    });
}


// detect element on scroll
function apsa_is_scrolled_into_view(elem) {
    var docViewTop = jQuery(window).scrollTop();
    var docViewBottom = docViewTop + jQuery(window).height();

    var elemTop = jQuery(elem).offset().top;
    var elemBottom = elemTop + jQuery(elem).height();

    // Check when element smaller than window then show it when icluded in window else show when visible above part of element
    if (jQuery(elem).height() <= jQuery(window).height()) {
        return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
    } else {
        return ((elemBottom >= docViewTop) && (elemTop <= docViewBottom));
    }
}

/*
 * function for add statistic event
 */
function apsa_add_event(element_id, type) {
    jQuery.ajax({
        type: "POST",
        url: apsa_ajax_url,
        data: {
            action: "apsa_ajax_update_element_statistics",
            element_id: element_id,
            type: type,
        },
        success: function () {
        },
        error: function () {
        }
    });
}

/*
 *  when anti-cache enabled add custom css
 */
function apsa_add_custom_css(customCss) {
    jQuery('body').append('<style id="apsa-element-styles-inline-css" type="text/css">' + customCss + '</style>');
}

/**
 * Add reset styles
 */
function apsa_reset_style() {
    jQuery('.apsa-reset-start').each(function () {
        jQuery(this).find("*").addBack().not(".apsa-reset-stop *").removeClass("apsa-reset-start apsa-reset-stop").addClass("apsa-reset-style");
    })
}

var apsa_mobile_size = 782;
/** Document ready actions */
jQuery(document).ready(function ($) {

    var ie_version = apsa_ie_version();

    /**
     * when anti-cache enabled send ajax request for get background and popup options
     */
    if (typeof apsa_extra_options.apsa_cache_enabled != 'undefined' && apsa_extra_options.apsa_cache_enabled == 'true') {
        if (apsa_plugin_data.campaign_types.background == 'true') {

            /**
             * ajax for get background options
             */
            $.ajax({
                type: "POST",
                url: apsa_ajax_url,
                dataType: "json",
                data: {
                    action: "apsa_call_bg_before_page_template_load",
                    type: "view",
                    apsa_page_info: apsa_page_info
                },
                success: function (res) {
                    if (res) {
                        var apsa_bg_options = res.apsa_bg_options;
                        var apsa_bg_info = res.apsa_bg_info;
                        apsa_set_bg(apsa_bg_options, apsa_bg_info, true);
                    }
                },
            });
        }
        if (apsa_plugin_data.campaign_types.popup == 'true') {

            /**
             * ajax for get popup options 
             */
            $.ajax({
                type: "POST",
                url: apsa_ajax_url,
                dataType: "json",
                data: {
                    action: "apsa_call_pop_before_page_template_load",
                    type: "view",
                    apsa_page_info: apsa_page_info
                },
                success: function (res) {
                    if (res) {
                        apsa_set_pop(res.apsa_pop_options, res.apsa_popup_info);
                    }
                },
            });
        }

        if (apsa_plugin_data.campaign_types.embed == 'true') {

            /**
             * Check if auto placements exists and get with ajax
             */
            if ($('.apsa-placement-holder').length !== 0) {
                $.ajax({
                    type: "POST",
                    url: apsa_ajax_url,
                    dataType: "json",
                    data: {
                        action: "apsa_ajax_get_auto_placements",
                        apsa_page_info: apsa_page_info
                    },
                    success: function (res) {
                        if (res['success'] != 1 || res['exists'] != 1) {
                            return false;
                        }

                        $(".apsa-placement-holder").each(function () {
                            if ($(this).hasClass('apsa-before-holder')) {
                                $(this).replaceWith(res['before']);
                            } else if ($(this).hasClass('apsa-after-holder')) {
                                $(this).replaceWith(res['after']);
                            }

                            apsa_set_embed_animation();
                            apsa_set_embed_cookie();
                        });
                    },
                });
            }

            /**
             * ajax for get embed campain content
             */
            $(".apsa-embed-cont").each(function () {
                var apsaEmbedCont = $(this);
                var parentSection = apsaEmbedCont.closest('.widget_apsa_campaign');
                var apsaWidgetId = 0;
                if (parentSection.length) {
                    apsaWidgetId = parentSection.attr('id').replace(/\D/g, '');
                }
                var info_array = apsaEmbedCont.find('.apsa-embed-info').serializeArray();
                if (info_array.length)
                    var campaign_id = info_array[0]["value"];
                else
                    var campaign_id = apsaEmbedCont.attr('data-apsa-campaign-id');
                var embed_alignment = apsaEmbedCont.data('apsa-alignment');
                var vc_class = apsaEmbedCont.data('apsa-vc-class');
                var apsa_content = apsaEmbedCont.find('.apsa-content-holder').html();

                var embed_data = {
                    action: "apsa_call_embed_campaign_func",
                    type: "view",
                    apsa_page_info: apsa_page_info,
                    shortcode_id: campaign_id,
                    apsa_widget_id: apsaWidgetId,
                    apsa_alignment: embed_alignment,
                    apsa_vc_class: vc_class
                };

                if (typeof apsa_content != "undefined") {
                    embed_data.apsa_content = apsa_content;
                }

                $.ajax({
                    type: "POST",
                    url: apsa_ajax_url,
                    dataType: "json",
                    data: embed_data,
                    success: function (res) {
                        if (res) {
                            apsaEmbedCont.replaceWith(res[campaign_id]);
                            apsa_set_embed_animation();
                            apsa_set_embed_cookie();
                        }
                    },
                });
            });
        }

        /**
         * ajax for get extra options
         */
        $.ajax({
            type: "POST",
            url: apsa_ajax_url,
            dataType: "json",
            data: {
                action: "apsa_get_extra_options",
                type: "view",
            },
            success: function (res) {
                if (res) {
                    // add custom css
                    var custom_css = res.apsa_custom_css;
                    apsa_add_custom_css(custom_css);
                }
            },
        });



    } else {
        if (typeof apsa_bg_options !== "undefined" && typeof apsa_bg_info !== 'undefined' && apsa_bg_info !== "")
            apsa_set_bg(apsa_bg_options, apsa_bg_info);
        if (typeof apsa_pop_options !== "undefined" && typeof apsa_popup_info !== 'undefined' && apsa_popup_info !== "")
            apsa_set_pop(apsa_pop_options, apsa_popup_info);
        if (apsa_plugin_data.campaign_types.embed == 'true') {
            // set embed animation on page load
            apsa_set_embed_animation();
            apsa_set_embed_cookie();
        }
    }

    /** Closes popup element */
    $(document).on("click", ".apsa-close-popup, #apsa-popup-overlay", function (e) {

        if (!$(".apsa-close-popup").hasClass("apsa-pop-hidden-close")) {
            apsa_close_popup();
        }
    });

    /** Close popup with escape key press */
    $(document).on('keyup', function (e) {

        if (!$(".apsa-close-popup").hasClass("apsa-pop-hidden-close") && e.which === 27) {
            apsa_close_popup();
        }
    });


    /**
     * Make cursor pointer for element links
     */
    $(document).on("mousemove", ".apsa-bg-image", (function (e) {
        if ($(e.target).hasClass("apsa-element-link")) {
            $(e.target).addClass("apsa-cursor-pointer");

        } else {
            $(".apsa-element-link").removeClass("apsa-cursor-pointer");
        }
    }));

    if (apsa_plugin_data.campaign_types.embed == 'true') {
        // set embed animation on scroll
        $(window).scroll(function () {
            apsa_set_embed_animation();
        });
    }

});