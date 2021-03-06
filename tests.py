class testlist:
    Smoketests = []
    #Smoketests.append([module, class, method])
    Smoketests.append({"testcase":{"module":"test_search_advanced_checked",
                                   "class":"AdvancedSearchChecked",
                                   "method":"test_advanced_search_checked"},
                       "tags":["prod"]})

    Smoketests.append({"testcase":{"module":"test_search_on_home_page",
                                   "class":"SearchOnHomePage",
                                   "method":"test_search_on_home_page"},
                       "tags":["prod"]})
    
# 
#    """ commented until post question anonymously is implemented """
##    Smoketests.append({"testcase":{"module":"test_anon_submitting_a_new_question",
##                                   "class":"anon_submitting_a_new_question",
##                                   "method":"test_anon_submitting_a_new_question"},
##                       "tags":[]})
 
    Smoketests.append({"testcase":{"module":"test_cant_find_what_youre_looking_for_test",
                                   "class":"cant_find_what_youre_looking_for_test",
                                   "method":"test_cant_find_what_youre_looking_for_test"},
                       "tags":["prod"]})
    
    """
      commented due to bug 650303
    """
#    Smoketests.append({"testcase":{"module":"test_inproduct",
#                                   "class":"inproduct",
#                                   "method":"test_inproduct"},
#                       "tags":["prod"]})
# 
#    Smoketests.append({"testcase":{"module":"test_kb_static",
#                                   "class":"kb_static",
#                                   "method":"test_kb_static"},
#                       "tags":["prod"]})
##    
    Smoketests.append({"testcase":{"module":"test_loggedin_ask_a_new_question",
                                   "class":"TestAAQ",
                                   "method":"test_that_posting_question_works"},
                       "tags":[]})
# 
#    Smoketests.append({"testcase":{"module":"test_loggedin_search_on_homepage",
#                                   "class":"loggedin_search_on_homepage",
#                                   "method":"test_loggedin_search_on_homepage"},
#                       "tags":["prod"]})
# 
#    Smoketests.append({"testcase":{"module":"test_login",
#                                   "class":"TestLogin",
#                                   "method":"test_login"},
#                       "tags":["easy"]})
# 
    Smoketests.append({"testcase":{"module":"test_other_firefox_support",
                                   "class":"TestOtherSupport",
                                   "method":"test_other_support_page"},
                       "tags":["prod"]})
 
    Smoketests.append({"testcase":{"module":"test_search_decoding",
                                   "class":"SearchDecoding",
                                   "method":"test_search_decoding"},
                       "tags":["prod"]})
 
    Smoketests.append({"testcase":{"module":"test_search_unknownchars",
                                   "class":"search_unknownchars",
                                   "method":"test_search_unknownchars"},
                       "tags":["prod"]})
 
    Smoketests.append({"testcase":{"module":"test_tiki_search_results",
                                   "class":"TikiSearchResult",
                                   "method":"test_tiki_search_result"},
                       "tags":["prod"]})
 
    Smoketests.append({"testcase":{"module":"test_search_num_results",
                                   "class":"SearchNumResults",
                                   "method":"test_search_num_results"},
                       "tags":["prod"]})
 
    Smoketests.append({"testcase":{"module":"test_search_advanced_links",
                                   "class":"AdvancedSearchLinks",
                                   "method":"test_search_advanced_links"},
                       "tags":["prod"]})

    Smoketests.append({"testcase":{"module":"test_search_quotes_pagination",
                                   "class":"SearchPageQuotes",
                                   "method":"test_that_pagination_works_for_search_terms_with_quotes"},
                       "tags":["prod"]})
       
    Smoketests.append({"testcase":{"module":"test_no_query_adv_forum_search",
                                   "class":"no_query_adv_forum_search",
                                   "method":"test_no_query_adv_forum_search"},
                       "tags":["prod"]})
 
    Smoketests.append({"testcase":{"module":"test_search_nonnumeric_pages",
                                   "class":"NonNumericSearchPages",
                                   "method":"test_nonnumeric_search_pages"},
                       "tags":["prod"]})

    Smoketests.append({"testcase":{"module":"test_forum_reply_logged_out",
                                   "class":"ForumReply",
                                   "method":"test_forum_reply_logged_out"},
                       "tags":["prod"]})
                       
    Smoketests.append({"testcase":{"module":"test_search_tags_only",
                                   "class":"SearchTagsOnly",
                                   "method":"test_search_only_tags_dont_return_zero"},
                       "tags":["prod"]})
    

#===============================================================================


    
    BFT = []
    BFT.extend(Smoketests)

    """ commented due to timeout issues"""
#    BFT.append({"testcase":{"module":"test_article_rename_cancel",
#                                   "class":"article_rename_cancel",
#                                   "method":"test_article_rename_cancel"},
#                       "tags":[]})



    BFT.append({"testcase":{"module":"test_forum_new_post",
                                   "class":"ForumPagination",
                                   "method":"test_forum_new_post"},
                       "tags":[]})

    """ commented due to timeout issues"""
    #BFT.append({"testcase":{"module":"test_kb_htc_check_images",
    #                               "class":"kb_htc_check_images",
    #                               "method":"test_kb_htc_check_images"},
    #                   "tags":[]})


    BFT.append({"testcase":{"module":"test_search_quotes",
                                   "class":"SearchQuotes",
                                   "method":"test_search_quotes"},
                       "tags":["prod"]})

    BFT.append({"testcase":{"module":"test_forum_deletion",
                                   "class":"ForumDeletion",
                                   "method":"test_forum_deletion"},
                       "tags":[]})
    
    BFT.append({"testcase":{"module":"test_search_advanced_tags",
                                   "class":"SearchAdvancedTags",
                                   "method":"test_search_advanced_tags"},
                        "tags":["prod"]})
    
    BFT.append({"testcase":{"module":"test_questions_problem_count",
                                   "class":"QuestionProbCount",
                                   "method":"test_questions_problem_count"},
                        "tags":[]})
    
    BFT.append({"testcase":{"module":"test_forum_post_on_prod",
                                   "class":"ForumPostProd",
                                   "method":"test_forum_pagination_on_prod"},
                        "tags":["prod"]})
    
    BFT.append({"testcase":{"module":"test_search_unicode_chars",
                                   "class":"SearchUnicodeChars",
                                   "method":"test_search_unicode_chars"},
                        "tags":["prod"]})
    
    FFT = []
    FFT.extend(BFT)

    FFT.append({"testcase":{"module":"test_article_create_edit_delete",
                                   "class":"TestArticleCreateEditDelete",
                                   "method":"test_that_article_can_be_previewed_before_submitting"},
                       "tags":["prod"]})

    FFT.append({"testcase":{"module":"test_article_create_edit_delete",
                                   "class":"TestArticleCreateEditDelete",
                                   "method":"test_that_article_can_be_created"},
                       "tags":[]})
    
    FFT.append({"testcase":{"module":"test_article_create_edit_delete",
                                   "class":"TestArticleCreateEditDelete",
                                   "method":"test_that_article_can_be_edited"},
                       "tags":[]})

    FFT.append({"testcase":{"module":"test_article_create_edit_delete",
                                   "class":"TestArticleCreateEditDelete",
                                   "method":"test_that_article_can_be_deleted"},
                       "tags":[]})

    FFT.append({"testcase":{"module":"test_new_user_registration",
                                   "class":"TestNewUserRegistration",
                                   "method":"test_that_thank_you_page_is_displayed_after_successful_registration"},
                       "tags":[]})

#    FFT.append({"testcase":{"module":"test_anon_csat_NTF_no",
#                                   "class":"anon_csat_NTF_no",
#                                   "method":"test_anon_csat_ntf_no"},
#                       "tags":[]})
#
#    FFT.append({"testcase":{"module":"test_anon_csat_NTF_yes_new",
#                                   "class":"anon_csat_NTF_yes_new",
#                                   "method":"test_anon_csat_ntf_yes_new"},
#                       "tags":[]})
#
#    FFT.append({"testcase":{"module":"test_anon_csat_popular_article_no",
#                                   "class":"anon_csat_popular_article_no",
#                                   "method":"test_anon_csat_popular_article_no"},
#                       "tags":[]})
#
#    FFT.append({"testcase":{"module":"test_anon_csat_popular_article_yes",
#                                   "class":"anon_csat_popular_article_yes",
#                                   "method":"test_anon_csat_popular_article_yes"},
#                       "tags":[]})
#
#    FFT.append({"testcase":{"module":"test_anon_csat_popular_article_yes_new",
#                                   "class":"anon_csat_popular_article_yes_new",
#                                   "method":"test_anon_csat_popular_article_yes_new"},
#                       "tags":[]})
#
#    FFT.append({"testcase":{"module":"test_article_history",
#                                   "class":"article_history",
#                                   "method":"test_article_history"},
#                       "tags":[]})
#
#    FFT.append({"testcase":{"module":"test_correct_search_whitespace_encoding_test",
#                                   "class":"correct_search_whitespace_encoding_test",
#                                   "method":"test_correct_search_whitespace_encoding_test"},
#                       "tags":[]})
#
#    FFT.append({"testcase":{"module":"test_loggedin_translate_existing_article",
#                                   "class":"loggedin_translate_existing_article",
#                                   "method":"test_loggedin_translate_existing_article"},
#                       "tags":[]})
#
#    #FFT.append({"testcase":{"module":"test_breadcrumbs_forum",
#    #                               "class":"breadcrumbs_forum",
#    #                               "method":"test_breadcrumbs_forum"},
#    #                   "tags":[]})
#    #staging forum isn't always filled
#    
#    FFT.append({"testcase":{"module":"test_breadcrumbs_htc",
#                                   "class":"breadcrumbs_htc",
#                                   "method":"test_breadcrumbs_htc"},
#                       "tags":[]})
#
#    #FFT.append({"testcase":{"module":"test_breadcrumbs_kb",
#    #                               "class":"breadcrumbs_KB",
#    #                               "method":"test_breadcrumbs_kb"},
#    #                   "tags":[]})
#
#    FFT.append({"testcase":{"module":"test_breadcrumbs_misc",
#                                   "class":"breadcrumbs_misc",
#                                   "method":"test_breadcrumbs_misc"},
#                       "tags":[]})
#    
#    FFT.append({"testcase":{"module":"test_locale_redirect",
#                                   "class":"locale_redirect",
#                                   "method":"test_locale_redirect"},
#                       "tags":["prod"]})
