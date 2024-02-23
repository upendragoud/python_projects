<!DOCTYPE html>
<!-- saved from url=(0055)https://github.com/Azure/Hangman/blame/master/README.md -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-a11y-link-underlines="true" class="js-focus-visible" data-js-focus-visible="" data-turbo-loaded=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style>
    
  <link rel="dns-prefetch" href="https://github.githubassets.com/">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com/">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">
  <link rel="preconnect" href="https://github.githubassets.com/" crossorigin="">
  <link rel="preconnect" href="https://avatars.githubusercontent.com/">

  


  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./README_files/light-0eace2597ca3.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./README_files/dark-a167e256da9c.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-d11f2cf8009b.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-ea7373db06c8.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-afa99dcf40f7.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-af6c685139ba.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-578cdbc8a5a9.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-5cb699a7e247.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-9b32204967c6.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./README_files/primer-primitives-2ef2a46b27ee.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./README_files/primer-08e422afeb43.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./README_files/global-05ed4a7e07b5.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./README_files/github-8eaab228448a.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./README_files/repository-6247ca238fd4.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./README_files/code-ac2c2f3d57f1.css">

  


  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["code_vulnerability_scanning","copilot_conversational_ux_history_refs","copilot_modal_reference_viewer","copilot_persistent_chat_panel","copilot_smell_icebreaker_ux","copilot_implicit_context","docset_management_ui","failbot_handle_non_errors","geojson_azure_maps","image_metric_tracking","marketing_forms_api_integration_contact_request","marketing_pages_search_explore_provider","repository_suggester_elastic_search","turbo_experiment_risky","sample_network_conn_type","no_character_key_shortcuts_in_inputs","custom_inp","remove_child_patch"]}</script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/wp-runtime-0abd42484719.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_dompurify_dist_purify_js-6890e890956f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-a4c183-79f9611c275b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_github_hydro-analytics-client_dist_analytics-client_js-node_modules_gith-6a10dd-e66ebda625fb.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/ui_packages_failbot_failbot_ts-afaa9a250f2e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/environment-4ff0d843ea45.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_github_selector-observer_dist_index_esm_js-9f960d9b217c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_behaviors_dist_esm_focus-zone_js-086f7a27bac0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_github_relative-time-element_dist_index_js-c76945c5961a.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_details-dialog-elemen-29dc30-a2a71f11a507.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_github_auto-complete-element_dist_index_js-d6c09d7e4e48.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-b7d8f4-8cd02f324209.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-6ff72b-44df89427254.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/github-elements-91586b615d25.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/element-registry-58eba3853ad3.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-978abc0-add939c751ce.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_lit-html_lit-html_js-5b376145beff.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_alive-client_dist-bf5aa2-1b562c29ab8e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_morphdom_dist_morphdom-esm_js-5bff297a06de.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-c91f4ad18b62.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_color-convert_index_js-72c9fbde5ad4.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_scroll-anchoring_dist_scro-231ccf-aa129238d13b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_behaviors_dist_esm_dimensions_js-node_modules_github_jtml_lib_index_js-95b84ee6bc34.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_github_paste-markdown_dist_index_esm_js-node_modules_github_quote-select-cbac5f-5c15271fc07d.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/app_assets_modules_github_updatable-content_ts-5e0904652c1c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_onfocus_ts-app_ass-421cec-751caa0072bd.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/app_assets_modules_github_sticky-scroll-into-view_ts-cbcee0788fe3.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-467754-b59a2b2827ad.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-b85e9f4f1304.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/app_assets_modules_github_blob-anchor_ts-app_assets_modules_github_filter-sort_ts-app_assets_-c96432-ca86212e46a4.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/behaviors-bde2e016b2b8.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-d0256ebff5cd.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/notifications-global-99d196517b1b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/code-menu-2658b004279a.js.download"></script>
  
  <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/react-lib-1fbfc5be2c18.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_octicons-react_dist_index_esm_js-node_modules_primer_react_lib-es-2e8e7c-b299afe58dd7.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_react_lib-esm_Box_Box_js-ebfceb11fb57.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_react_lib-esm_Button_Button_js-0528cb519251.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_react_lib-esm_ActionList_index_js-e001d0eead25.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_react_lib-esm_Overlay_Overlay_js-node_modules_primer_react_lib-es-fa1130-8d276499c3fb.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_react_lib-esm_Text_Text_js-node_modules_primer_react_lib-esm_Text-85a14b-249efa9c2fae.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_behaviors_dist_esm_scroll-into-view_js-node_modules_primer_react_-39745e-56454ece1686.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_react_lib-esm_FormControl_FormControl_js-e905f63cdd0f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_react_lib-esm_ActionMenu_ActionMenu_js-a3c61ff6363e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_react-router-dom_dist_index_js-3b41341d50fe.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_react_lib-esm_PageLayout_PageLayout_js-a0f5dc4acaba.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_react_lib-esm_ConfirmationDialog_ConfirmationDialog_js-1396cd0754d9.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_react_lib-esm_Dialog_js-node_modules_primer_react_lib-esm_Flash_F-ad64b6-7663299a84eb.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_react_lib-esm_Avatar_Avatar_js-node_modules_primer_react_lib-esm_-abca1b-e1f48b432bcb.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_react_lib-esm_TreeView_TreeView_js-5d623f8c8e93.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_primer_react_lib-esm_Ava-691638-41f6b165755b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/ui_packages_react-core_create-browser-history_ts-ui_packages_react-core_deferred-registry_ts--ebbb92-64923177f972.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/ui_packages_react-core_register-app_ts-f7fc9821bc0f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/ui_packages_paths_index_ts-6ac43f859e31.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/ui_packages_ref-selector_RefSelector_tsx-858bb94813b1.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/ui_packages_commit-attribution_index_ts-ui_packages_commit-checks-status_index_ts-ui_packages-1e98c0-59848352f3aa.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/app_assets_modules_react-code-view_components_directory_DirectoryContent_index_ts-app_assets_-1a05f3-64fd38a62884.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/react-code-view-ca607a3ccbc3.js.download"></script>


  <title>Blaming Hangman/README.md at master · Azure/Hangman</title>



  <meta name="route-pattern" content="/:user_id/:repository/blob/*name(/*path)" data-turbo-transient="">
  <meta name="route-controller" content="blob" data-turbo-transient="">
  <meta name="route-action" content="show" data-turbo-transient="">

    
  <meta name="current-catalog-service-hash" content="82c569b93da5c18ed649ebd4c2c79437db4611a6a1373e805a3cb001c64130b7">


  <meta name="request-id" content="FC29:14CEAB:110E46F:12B6879:65D866F9" data-turbo-transient="true"><meta name="html-safe-nonce" content="a054c3c2fb831ff6795d2ca6eaa90616a6980cd419799e0a96dd46509e955e7c" data-turbo-transient="true"><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVxdWVzdF9pZCI6IkZDMjk6MTRDRUFCOjExMEU0NkY6MTJCNjg3OTo2NUQ4NjZGOSIsInZpc2l0b3JfaWQiOiIzMjgyMTY0MzU5NDc0NzIxMDg0IiwicmVnaW9uX2VkZ2UiOiJjZW50cmFsaW5kaWEiLCJyZWdpb25fcmVuZGVyIjoiaWFkIn0=" data-turbo-transient="true"><meta name="visitor-hmac" content="e33aff8a8cc5b50ac11de2d9afc5e3937eae53d120aedfe4bd65bf276d33e137" data-turbo-transient="true">


    <meta name="hovercard-subject-tag" content="repository:91612665" data-turbo-transient="">


  <meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree,copilot" data-turbo-transient="true">
  

  <meta name="selected-link" value="repo_source" data-turbo-transient="">
  <link rel="assets" href="https://github.githubassets.com/">

    <meta name="google-site-verification" content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY">
  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">
  <meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I">

<meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="octolytics-actor-id" content="86071546"><meta name="octolytics-actor-login" content="upendragoud"><meta name="octolytics-actor-hash" content="fa38ab20470d900142eb0aa897c049990da6a36093c6219d8f89c78bb92ee638">

  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient="true">

  




  

    <meta name="user-login" content="upendragoud">

  <link rel="sudo-modal" href="https://github.com/sessions/sudo_modal">

    <meta name="viewport" content="width=device-width">
    
      <meta name="description" content="A tutorial demonstrating how to train a neural network to play hangman using CNTK - Hangman/README.md at master · Azure/Hangman">
      <link rel="search" type="application/opensearchdescription+xml" href="https://github.com/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <meta property="fb:app_id" content="1401488693436528">
    <meta name="apple-itunes-app" content="app-id=1477376905, app-argument=https://github.com/Azure/Hangman/blob/master/README.md">
      <meta name="twitter:image:src" content="https://opengraph.githubassets.com/833b12954a865cddbe793a3ac706d56f99bcbb9d5ec17239cd9c9696fe7ceccd/Azure/Hangman"><meta name="twitter:site" content="@github"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="Hangman/README.md at master · Azure/Hangman"><meta name="twitter:description" content="A tutorial demonstrating how to train a neural network to play hangman using CNTK - Azure/Hangman">
      <meta property="og:image" content="https://opengraph.githubassets.com/833b12954a865cddbe793a3ac706d56f99bcbb9d5ec17239cd9c9696fe7ceccd/Azure/Hangman"><meta property="og:image:alt" content="A tutorial demonstrating how to train a neural network to play hangman using CNTK - Azure/Hangman"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="600"><meta property="og:site_name" content="GitHub"><meta property="og:type" content="object"><meta property="og:title" content="Hangman/README.md at master · Azure/Hangman"><meta property="og:url" content="https://github.com/Azure/Hangman/blob/master/README.md"><meta property="og:description" content="A tutorial demonstrating how to train a neural network to play hangman using CNTK - Azure/Hangman">
      

      <link rel="shared-web-socket" href="wss://alive.github.com/_sockets/u/86071546/ws?session=eyJ2IjoiVjMiLCJ1Ijo4NjA3MTU0NiwicyI6MTMwNzAwMzkyMywiYyI6OTA1MTIxMjA4LCJ0IjoxNzA4NjgwOTU0fQ==--e3f0ddc99f4fe958c6b958347a8f051906af73af3136866fefb8bcfb5f3a8015" data-refresh-url="/_alive" data-session-id="2c1611f93cfab1653cba301952bd468eaccfe9c0e5c8a9757b5c9ddceeb3710c">
      <link rel="shared-web-socket-src" href="https://github.com/assets-cdn/worker/socket-worker-9cc1149b224c.js">


        <meta name="hostname" content="github.com">


      <meta name="keyboard-shortcuts-preference" content="all">

        <meta name="expected-hostname" content="github.com">


  <meta http-equiv="x-pjax-version" content="7ee350b25cd1cc60fac66f46da032d0c4ce1580169254e800007a3b845df2f2c" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="5dcfbec3488c5fd5a334e287ce6a17058b7d4beb91db2d4d184e4d55bbf1d7d7" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="fb6c7ab00db5de9a93dcfc20e6359c4b2fbd4dc6d29094144ad33e7a8751b95d" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="3e43b1a22e884fe8e6e0e339ee51012b9e8efbcc49ac44538b06d409ccabbd71" data-turbo-track="reload">

  <meta name="turbo-cache-control" content="no-preview" data-turbo-transient="">

      <meta name="turbo-cache-control" content="no-cache" data-turbo-transient="">
    <meta data-hydrostats="publish">

  <meta name="go-import" content="github.com/Azure/Hangman git https://github.com/Azure/Hangman.git">

  <meta name="octolytics-dimension-user_id" content="6844498"><meta name="octolytics-dimension-user_login" content="Azure"><meta name="octolytics-dimension-repository_id" content="91612665"><meta name="octolytics-dimension-repository_nwo" content="Azure/Hangman"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="91612665"><meta name="octolytics-dimension-repository_network_root_nwo" content="Azure/Hangman">



  <meta name="turbo-body-classes" content="logged-in env-production page-responsive">


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon-dark.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon-dark.svg">

<meta name="theme-color" content="#1e2327">
<meta name="color-scheme" content="light dark">


  <link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials">

  <style data-styled="active" data-styled-version="5.3.6"></style><style id="ms-consent-banner-main-styles">.w8hcgFksdo30C8w-bygqu{color:#000}.ydkKdaztSS0AeHWIeIHsQ a{color:#0067B8}.erL690_8JwUW-R4bJRcfl{background-color:#EBEBEB;border:none;color:#000}.erL690_8JwUW-R4bJRcfl:enabled:hover{color:#000;background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}.erL690_8JwUW-R4bJRcfl:enabled:focus{background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}.erL690_8JwUW-R4bJRcfl:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2);border:none}._1zNQOqxpBFSokeCLGi_hGr{border:none;background-color:#0067B8;color:#fff}._1zNQOqxpBFSokeCLGi_hGr:enabled:hover{color:#fff;background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}._1zNQOqxpBFSokeCLGi_hGr:enabled:focus{background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}._1zNQOqxpBFSokeCLGi_hGr:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,120,215,0.2);border:none}._23tra1HsiiP6cT-Cka-ycB{position:relative;display:flex;z-index:9999;width:100%;background-color:#F2F2F2;justify-content:space-between;text-align:left}div[dir="rtl"]._23tra1HsiiP6cT-Cka-ycB{text-align:right}._1Upc2NjY8AlDn177YoVj0y{margin:0;padding-left:5%;padding-top:8px;padding-bottom:8px}div[dir="rtl"] ._1Upc2NjY8AlDn177YoVj0y{margin:0;padding:8px 5% 8px 0;float:none}._23tra1HsiiP6cT-Cka-ycB svg{fill:none;max-width:none;max-height:none}._1V_hlU-7jdtPiooHMu89BB{display:table-cell;padding:12px;width:24px;height:24px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:24px;line-height:0}.f6QKJD7fhSbnJLarTL-W-{display:table-cell;vertical-align:middle;padding:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:16px}.f6QKJD7fhSbnJLarTL-W- a{text-decoration:underline}._2j0fmugLb1FgYz6KPuB91w{display:inline-block;margin-left:5%;margin-right:5%;min-width:40%;min-width:calc((150px + 3 * 4px) * 2 + 150px);min-width:-webkit-fit-content;min-width:-moz-fit-content;min-width:fit-content;align-self:center;position:relative}._1XuCi2WhiqeWRUVp3pnFG3{margin:4px;padding:5px;min-width:150px;min-height:36px;vertical-align:top;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._1XuCi2WhiqeWRUVp3pnFG3:focus{box-sizing:border-box}._1XuCi2WhiqeWRUVp3pnFG3:disabled{cursor:not-allowed}._2bvsb3ubApyZ0UGoQA9O9T{display:block;position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.6);overflow:auto;text-align:left}div[dir="rtl"]._2bvsb3ubApyZ0UGoQA9O9T{text-align:right}div[dir="rtl"] ._2bvsb3ubApyZ0UGoQA9O9T{left:auto;right:0}.AFsJE948muYyzCMktdzuk{position:relative;top:8%;margin-bottom:40px;margin-left:auto;margin-right:auto;box-sizing:border-box;width:640px;background-color:#fff;border:1px solid #0067B8}._3kWyBRbW_dgnMiEyx06Fu4{float:right;z-index:1;margin:2px;padding:12px;border:none;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:13px;display:flex;align-items:center;text-align:center;color:#666;background-color:#fff}div[dir="rtl"] ._3kWyBRbW_dgnMiEyx06Fu4{margin:2px;padding:12px;float:left}.uCYvKvHXrhjNgflv1VqdD{position:static;margin-top:36px;margin-left:36px;margin-right:36px}._17pX1m9O_W--iZbDt3Ta5r{margin-top:0;margin-bottom:12px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:24px;text-transform:none}._1kBkHQ1V1wu3kl-YcLgUr6{height:446px;overflow:auto}._20_nXDf6uFs9Q6wxRXG-I-{margin-top:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._20_nXDf6uFs9Q6wxRXG-I- a{text-decoration:underline}dl._2a0NH_GDQEQe5Ynfo7suVH{margin-top:36px;margin-bottom:0;padding:0;list-style:none;text-transform:none}dt._3j_LCPv7fyXv3A8FIXVwZ4{margin-top:20px;float:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;list-style:none}.k-vxTGFbdq1aOZB2HHpjh{margin:0;padding:0;border:none}._2Bucyy75c_ogoU1g-liB5R{margin:0;padding:0;border-bottom:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;text-transform:none}._63gwfzV8dclrsl2cfd90r{display:inline-block;margin-top:0;margin-bottom:13px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._1l8wM_4mRYGz3Iu7l3BZR7{display:block}._2UE03QS02aZGkslegN_F-i{display:inline-block;position:relative;left:5px;margin-bottom:13px;margin-right:34px;padding:3px}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{margin:0 0 13px 34px;padding:3px;float:none}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{left:auto;right:5px}._23tra1HsiiP6cT-Cka-ycB *::before,._2bvsb3ubApyZ0UGoQA9O9T *::before,._23tra1HsiiP6cT-Cka-ycB *::after,._2bvsb3ubApyZ0UGoQA9O9T *::after{box-sizing:inherit}._1HSFn0HzGo6w4ADApV8-c4{outline:2px solid rgba(0,0,0,0.8)}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2{display:inline-block;position:relative;margin-top:0;margin-left:0;margin-right:0;height:0;width:0;border-radius:0;cursor:pointer;outline:none;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{display:block;position:absolute;top:5px;left:3px;height:19px;width:19px;content:"";border-radius:50%;border:1px solid #000;background-color:#fff}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{left:auto;right:3px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:rgba(0,0,0,0.8)}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label{cursor:not-allowed}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label::before{border:1px solid rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2)}._3RJzeL3l9Rl_lAQEm6VwdX{display:block;position:static;float:right;margin-top:0;margin-bottom:0;margin-left:19px;margin-right:0;padding-top:0;padding-bottom:0;padding-left:8px;padding-right:0;width:80%;width:calc(100% - 19px);font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-transform:none;cursor:pointer;box-sizing:border-box}div[dir="rtl"] ._3RJzeL3l9Rl_lAQEm6VwdX{margin:0 19px 0 0;padding:0 8px 0 0;float:left}.nohp3sIG12ZBhzcMnPala{margin-top:20px;margin-bottom:48px}._2uhaEsmeotZ3P-M0AXo2kF{padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._2uhaEsmeotZ3P-M0AXo2kF:focus{box-sizing:border-box}._2uhaEsmeotZ3P-M0AXo2kF:disabled{cursor:not-allowed}._3tOu1FJ59c_xz_PmI1lKV5{float:right;padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._3tOu1FJ59c_xz_PmI1lKV5:focus{box-sizing:border-box}._3tOu1FJ59c_xz_PmI1lKV5:disabled{cursor:not-allowed}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0;padding:0;float:left}@media only screen and (max-width: 768px){._2j0fmugLb1FgYz6KPuB91w,._1Upc2NjY8AlDn177YoVj0y{padding-top:8px;padding-bottom:12px;padding-left:3.75%;padding-right:3.75%;margin:0;width:92.5%}._23tra1HsiiP6cT-Cka-ycB{display:block}._1XuCi2WhiqeWRUVp3pnFG3{margin-bottom:8px;margin-left:0;margin-right:0;width:100%}._2bvsb3ubApyZ0UGoQA9O9T{overflow:hidden}.AFsJE948muYyzCMktdzuk{top:1.8%;width:93.33%;height:96.4%;overflow:hidden}.uCYvKvHXrhjNgflv1VqdD{margin-top:24px;margin-left:24px;margin-right:24px;height:100%}._1kBkHQ1V1wu3kl-YcLgUr6{height:62%;height:calc(100% - 188px);min-height:50%}._2uhaEsmeotZ3P-M0AXo2kF{width:100%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:12px;margin-left:0;width:100%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 12px 0;padding:0;float:none}}@media only screen and (max-width: 768px) and (orientation: landscape), only screen and (max-height: 260px), only screen and (max-width: 340px){.AFsJE948muYyzCMktdzuk{overflow:auto}}@media only screen and (max-height: 260px), only screen and (max-width: 340px){._1XuCi2WhiqeWRUVp3pnFG3{min-width:0}._3kWyBRbW_dgnMiEyx06Fu4{padding:3%}.uCYvKvHXrhjNgflv1VqdD{margin-top:3%;margin-left:3%;margin-right:3%}._17pX1m9O_W--iZbDt3Ta5r{margin-bottom:3%}._1kBkHQ1V1wu3kl-YcLgUr6{height:calc(79% - 64px)}.nohp3sIG12ZBhzcMnPala{margin-top:5%;margin-bottom:10%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:3%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 3% 0;padding:0;float:none}}
</style><style type="text/css" id="ms-consent-banner-theme-styles">._23tra1HsiiP6cT-Cka-ycB {
            background-color: var(--color-scale-gray-9) !important;
        }.w8hcgFksdo30C8w-bygqu {
            color: var(--color-scale-white) !important;
        }.ydkKdaztSS0AeHWIeIHsQ a {
            color: var(--color-scale-purple-2) !important;
        }._2bvsb3ubApyZ0UGoQA9O9T {
            background-color: rgba(23, 23, 23, 0.8) !important;
        }.AFsJE948muYyzCMktdzuk {
            background-color: var(--color-scale-gray-9) !important;
            border: 1px solid var(--color-scale-purple-2) !important;
        }._3kWyBRbW_dgnMiEyx06Fu4 {
            color: var(--color-scale-purple-2) !important;
            background-color: var(--color-scale-gray-9) !important;
        }._1zNQOqxpBFSokeCLGi_hGr {
            border: 1px solid var(--color-scale-white) !important;
            background-color: var(--color-scale-white) !important;
            color: var(--color-scale-black) !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:hover {
            color: var(--color-scale-black) !important;
            background-color: var(--color-scale-purple-2) !important;
            box-shadow: none !important;
            border: 1px solid transparent !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:focus {
            background-color: var(--color-scale-purple-2) !important;
            box-shadow: none !important;
            border: 2px solid var(--color-scale-white) !important;
        }._1zNQOqxpBFSokeCLGi_hGr:disabled {
            opacity: 0.5 !important;
            color: var(--color-scale-black) !important;
            background-color: var(--color-scale-white) !important;
            border: 1px solid transparent !important;
        }.erL690_8JwUW-R4bJRcfl {
            border: 1px solid var(--color-scale-gray-1) !important;
            background-color: var(--color-scale-gray-8) !important;
            color: var(--color-scale-white) !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:hover {
            color: var(--color-scale-white) !important;
            background-color: var(--color-scale-gray-9) !important;
            box-shadow: none !important;
            border: 1px solid var(--color-scale-white) !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:focus {
            background-color: var(--color-scale-gray-9) !important;
            box-shadow: none !important;
            border: 2px solid var(--color-scale-gray-5) !important;
        }.erL690_8JwUW-R4bJRcfl:disabled {
            opacity: 0.5 !important;
            color: var(--color-scale-white) !important;
            background-color: var(--color-scale-gray-7) !important;
            border: 1px solid var(--color-scale-gray-5) !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label::before {
            border: 1px solid var(--color-scale-purple-2) !important;
            background-color: var(--color-scale-gray-9) !important;
        }._1HSFn0HzGo6w4ADApV8-c4 {
            outline: 2px solid var(--color-scale-white) !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked + label::after {
            background-color: var(--color-scale-purple-2) !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::before {
            border: 1px solid var(--color-scale-white) !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::after {
            background-color: var(--color-scale-white) !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::before {
            border: 1px solid var(--color-scale-white) !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::after {
            background-color: var(--color-scale-purple-2) !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled + label::before {
            border: 1px solid rgba(227, 227, 227, 0.2) !important;
            background-color: rgba(227, 227, 227, 0.2) !important;
        }</style></head>

  <body class="logged-in env-production page-responsive intent-mouse" style="overflow-wrap: break-word; --dialog-scrollgutter: 17px;">
    <div data-turbo-body="" class="logged-in env-production page-responsive" style="word-wrap: break-word;">
      


    <div class="position-relative js-header-wrapper ">
      <a href="https://github.com/Azure/Hangman/blame/master/README.md#start-of-content" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>
      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
  




<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_github_hotkey_dist_index_js-node_modules_lodash-es_capitalize_js-b7930811adc2.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_primer_react_lib-esm_Button_IconButton_js-node_modules_primer_react_lib--821147-97ee2d5830e9.js.download"></script>

<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/keyboard-shortcuts-dialog-9b7386ec0bee.js.download"></script>

<react-partial partial-name="keyboard-shortcuts-dialog" data-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA__">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>



      

        <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_allex_crc32_lib_crc32_esm_js-node_modules_github_mini-throttle_dist_deco-b38cad-748e74df23ce.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/vendors-node_modules_github_clipboard-copy-element_dist_index_esm_js-node_modules_delegated-e-b37f7d-2f24d321a3fb.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/app_assets_modules_github_command-palette_items_help-item_ts-app_assets_modules_github_comman-48ad9d-b180134b83d3.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./README_files/command-palette-4a91d9475ff6.js.download"></script>

            <header class="AppHeader">
    

    <div class="AppHeader-globalBar pb-2 js-global-bar">
      <div class="AppHeader-globalBar-start">
          <deferred-side-panel data-url="/_side-panels/global" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
      <button aria-label="Open global navigation menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-97499bcc-65d4-4fbc-b659-0e2e53453572" id="dialog-show-dialog-97499bcc-65d4-4fbc-b659-0e2e53453572" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-bg-transparent p-0 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-three-bars Button-visual">
    <path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path>
</svg>
</button>

<dialog-helper>
  <dialog data-target="deferred-side-panel.panel" id="dialog-97499bcc-65d4-4fbc-b659-0e2e53453572" aria-modal="true" aria-labelledby="dialog-97499bcc-65d4-4fbc-b659-0e2e53453572-title" aria-describedby="dialog-97499bcc-65d4-4fbc-b659-0e2e53453572-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade Overlay--placement-left SidePanel">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-97499bcc-65d4-4fbc-b659-0e2e53453572-title">
        Global navigation
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
</div></div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-97499bcc-65d4-4fbc-b659-0e2e53453572" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <scrollable-region data-labelled-by="dialog-97499bcc-65d4-4fbc-b659-0e2e53453572-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body d-flex flex-column px-2">    <div data-view-component="true" class="d-flex flex-column mb-3">
        <nav aria-label="Site navigation" data-view-component="true" class="ActionList">
  
  <nav-list data-catalyst="">
    <ul data-view-component="true" class="ActionListWrap">
        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g d" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;HOME&quot;,&quot;label&quot;:null}" id="item-2f2a99c3-e18d-4aae-ac45-db2eb0dc5085" href="https://github.com/dashboard" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-home">
    <path d="M6.906.664a1.749 1.749 0 0 1 2.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019A1.75 1.75 0 0 1 13.25 15h-3.5a.75.75 0 0 1-.75-.75V9H7v5.25a.75.75 0 0 1-.75.75h-3.5A1.75 1.75 0 0 1 1 13.25V6.23c0-.531.242-1.034.657-1.366l5.25-4.2Zm1.25 1.171a.25.25 0 0 0-.312 0l-5.25 4.2a.25.25 0 0 0-.094.196v7.019c0 .138.112.25.25.25H5.5V8.25a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 .75.75v5.25h2.75a.25.25 0 0 0 .25-.25V6.23a.25.25 0 0 0-.094-.195Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Home
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES&quot;,&quot;label&quot;:null}" id="item-ffc89913-78a6-4e26-9286-2c3f4c682746" href="https://github.com/issues" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS&quot;,&quot;label&quot;:null}" id="item-6b8b6761-92bd-4777-8a13-983df5927ff6" href="https://github.com/pulls" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PROJECTS&quot;,&quot;label&quot;:null}" id="item-b0d94428-b759-45f4-98da-fb53d37b211d" href="https://github.com/projects" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;DISCUSSIONS&quot;,&quot;label&quot;:null}" id="item-39e8ef06-fccc-4ea6-9b86-489f8384f7a3" href="https://github.com/discussions" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Discussions
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;CODESPACES&quot;,&quot;label&quot;:null}" id="item-3cfbae54-9bf4-4862-8e47-c1b68074ce41" href="https://github.com/codespaces" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Codespaces
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;EXPLORE&quot;,&quot;label&quot;:null}" id="item-80269234-f6d8-4c7c-a863-2c4e85140801" href="https://github.com/explore" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-telescope">
    <path d="M14.184 1.143v-.001l1.422 2.464a1.75 1.75 0 0 1-.757 2.451L3.104 11.713a1.75 1.75 0 0 1-2.275-.702l-.447-.775a1.75 1.75 0 0 1 .53-2.32L11.682.573a1.748 1.748 0 0 1 2.502.57Zm-4.709 9.32h-.001l2.644 3.863a.75.75 0 1 1-1.238.848l-1.881-2.75v2.826a.75.75 0 0 1-1.5 0v-2.826l-1.881 2.75a.75.75 0 1 1-1.238-.848l2.049-2.992a.746.746 0 0 1 .293-.253l1.809-.87a.749.749 0 0 1 .944.252ZM9.436 3.92h-.001l-4.97 3.39.942 1.63 5.42-2.61Zm3.091-2.108h.001l-1.85 1.26 1.505 2.605 2.016-.97a.247.247 0 0 0 .13-.151.247.247 0 0 0-.022-.199l-1.422-2.464a.253.253 0 0 0-.161-.119.254.254 0 0 0-.197.038ZM1.756 9.157a.25.25 0 0 0-.075.33l.447.775a.25.25 0 0 0 .325.1l1.598-.769-.83-1.436-1.465 1Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Explore
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;MARKETPLACE&quot;,&quot;label&quot;:null}" id="item-77e44fa4-83c4-41be-9981-62b7f4a7489e" href="https://github.com/marketplace" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gift">
    <path d="M2 2.75A2.75 2.75 0 0 1 4.75 0c.983 0 1.873.42 2.57 1.232.268.318.497.668.68 1.042.183-.375.411-.725.68-1.044C9.376.42 10.266 0 11.25 0a2.75 2.75 0 0 1 2.45 4h.55c.966 0 1.75.784 1.75 1.75v2c0 .698-.409 1.301-1 1.582v4.918A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V9.332C.409 9.05 0 8.448 0 7.75v-2C0 4.784.784 4 1.75 4h.55c-.192-.375-.3-.8-.3-1.25ZM7.25 9.5H2.5v4.75c0 .138.112.25.25.25h4.5Zm1.5 0v5h4.5a.25.25 0 0 0 .25-.25V9.5Zm0-4V8h5.5a.25.25 0 0 0 .25-.25v-2a.25.25 0 0 0-.25-.25Zm-7 0a.25.25 0 0 0-.25.25v2c0 .138.112.25.25.25h5.5V5.5h-5.5Zm3-4a1.25 1.25 0 0 0 0 2.5h2.309c-.233-.818-.542-1.401-.878-1.793-.43-.502-.915-.707-1.431-.707ZM8.941 4h2.309a1.25 1.25 0 0 0 0-2.5c-.516 0-1 .205-1.43.707-.337.392-.646.975-.879 1.793Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Marketplace
</span></a>
  
  
</li>

</ul>  </nav-list>
</nav>

        <div data-view-component="true" class="my-3 d-flex flex-justify-center height-full">
          <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</div>
</div>
      <div data-view-component="true" class="flex-1"></div>


      <div data-view-component="true" class="px-2">      <p class="color-fg-subtle text-small text-light">© 2024 GitHub, Inc.</p>

      <div data-view-component="true" class="d-flex flex-wrap text-small text-light">
          <a target="_blank" href="https://github.com/about" data-view-component="true" class="Link mr-2">About</a>
          <a target="_blank" href="https://github.blog/" data-view-component="true" class="Link mr-2">Blog</a>
          <a target="_blank" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link mr-2">Terms</a>
          <a target="_blank" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link mr-2">Privacy</a>
          <a target="_blank" href="https://github.com/security" data-view-component="true" class="Link mr-2">Security</a>
          <a target="_blank" href="https://www.githubstatus.com/" data-view-component="true" class="Link mr-3">Status</a>

</div></div>
</div>
      </scrollable-region>
      
</dialog></dialog-helper>

  </include-fragment>
</deferred-side-panel>

        <a class="AppHeader-logo ml-2" href="https://github.com/" data-hotkey="g d" aria-label="Homepage " data-turbo="false" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}">
          <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle color-fg-default">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
        </a>

          <div class="AppHeader-context">
  <div class="AppHeader-context-compact">
      <button aria-expanded="false" aria-haspopup="dialog" aria-label="Page context: Azure / Hangman" id="dialog-show-context-region-dialog" data-show-dialog-id="context-region-dialog" type="button" data-view-component="true" class="AppHeader-context-compact-trigger Truncate Button--secondary Button--medium Button box-shadow-none">  <span class="Button-content">
    <span class="Button-label"><span class="AppHeader-context-compact-lead">
                <span class="AppHeader-context-compact-parentItem">Azure</span>
                <span class="no-wrap">&nbsp;/</span>

            </span>

            <strong class="AppHeader-context-compact-mainItem d-flex flex-items-center Truncate">
  <span class="Truncate-text ">Hangman</span>

</strong></span>
  </span>
</button>

<dialog-helper>
  <dialog id="context-region-dialog" aria-modal="true" aria-labelledby="context-region-dialog-title" aria-describedby="context-region-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="context-region-dialog-title">
        Navigate back to
      </h1>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="context-region-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <scrollable-region data-labelled-by="context-region-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">          <ul role="list" class="list-style-none">
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;Azure&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="https://github.com/Azure" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
            <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-organization mr-1">
    <path d="M1.75 16A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0h8.5C11.216 0 12 .784 12 1.75v12.5c0 .085-.006.168-.018.25h2.268a.25.25 0 0 0 .25-.25V8.285a.25.25 0 0 0-.111-.208l-1.055-.703a.749.749 0 1 1 .832-1.248l1.055.703c.487.325.779.871.779 1.456v5.965A1.75 1.75 0 0 1 14.25 16h-3.5a.766.766 0 0 1-.197-.026c-.099.017-.2.026-.303.026h-3a.75.75 0 0 1-.75-.75V14h-1v1.25a.75.75 0 0 1-.75.75Zm-.25-1.75c0 .138.112.25.25.25H4v-1.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 .75.75v1.25h2.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25ZM3.75 6h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 3.75A.75.75 0 0 1 3.75 3h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 3.75Zm4 3A.75.75 0 0 1 7.75 6h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 7 6.75ZM7.75 3h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 9.75A.75.75 0 0 1 3.75 9h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 9.75ZM7.75 9h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5Z"></path>
</svg>

          Azure
        </span>

</a>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;Hangman&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="https://github.com/Azure/Hangman" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
            <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-repo mr-1">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>

          Hangman
        </span>

</a>
    </li>
</ul>

</div>
      </scrollable-region>
      
</dialog></dialog-helper>
  </div>

  <div class="AppHeader-context-full">
    <nav role="navigation" aria-label="Page context">
      <ul role="list" class="list-style-none">
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;Azure&quot;,&quot;screen_size&quot;:&quot;full&quot;}" data-hovercard-type="organization" data-hovercard-url="/orgs/Azure/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Azure" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

          Azure
        </span>

</a>
        <span class="AppHeader-context-item-separator">/</span>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;Hangman&quot;,&quot;screen_size&quot;:&quot;full&quot;}" href="https://github.com/Azure/Hangman" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

          Hangman
        </span>

</a>
    </li>
</ul>

    </nav>
  </div>
</div>

      </div>
      <div class="AppHeader-globalBar-end">
          <div class="AppHeader-search">
              


<qbsearch-input class="search-input" data-scope="repo:Azure/Hangman" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="gAjUVunCvgWxa_yxZpHi-MPGoBG1Q09zu3UXFpK6sRcCVqwKNwYEe9GedZ4AGbrktvjxz59PZ_MPtzC9kLbrXw" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="Azure/Hangman" data-current-org="Azure" data-current-owner="" data-logged-in="true" data-copilot-chat-enabled="false" data-blackbird-indexed-repo-csrf="&lt;input type=&quot;hidden&quot; value=&quot;DIqNnygN0Chdsxzren32fhfEtnasJ0T_gXuezpUTCG4ZFnLIsUe2rEYZRxZOX3QqgV4SORI42jZqf9n2vvg8AQ&quot; data-csrf=&quot;true&quot; /&gt;" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">
      
            <button type="button" data-action="click:qbsearch-input#handleExpand" class="AppHeader-button AppHeader-search-whenNarrow" aria-label="Search or jump to…" aria-expanded="false" aria-haspopup="dialog">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </button>


<div class="AppHeader-search-whenRegular">
  <div class="AppHeader-search-wrap AppHeader-search-wrap--hasTrailing">
    <div class="AppHeader-search-control">
      <label for="AppHeader-searchInput" aria-label="Search or jump to…" class="AppHeader-search-visual--leading">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
      </label>

                <button type="button" data-target="qbsearch-input.inputButton" data-action="click:qbsearch-input#handleExpand" class="AppHeader-searchButton form-control input-contrast text-left color-fg-subtle no-wrap placeholder" data-hotkey="s,/" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SEARCH&quot;,&quot;label&quot;:null}">
            <div class="overflow-hidden">
              <span id="qb-input-query" data-target="qbsearch-input.inputButtonText">
                  Type <kbd class="AppHeader-search-kbd">/</kbd> to search
              </span>
            </div>
          </button>

    </div>


      <button type="button" id="AppHeader-commandPalette-button" class="AppHeader-search-action--trailing js-activate-command-palette" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;command_palette&quot;,&quot;label&quot;:&quot;open command palette&quot;}" aria-labelledby="tooltip-6de095a6-ed8f-4b26-8b28-d54e48840301">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-command-palette">
    <path d="m6.354 8.04-4.773 4.773a.75.75 0 1 0 1.061 1.06L7.945 8.57a.75.75 0 0 0 0-1.06L2.642 2.206a.75.75 0 0 0-1.06 1.061L6.353 8.04ZM8.75 11.5a.75.75 0 0 0 0 1.5h5.5a.75.75 0 0 0 0-1.5h-5.5Z"></path>
</svg>
      </button>

      <tool-tip id="tooltip-6de095a6-ed8f-4b26-8b28-d54e48840301" for="AppHeader-commandPalette-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Command palette</tool-tip>
  </div>
</div>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/Azure/Hangman/blame/master/README.md" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-37c45f0a-232c-44d8-a2f7-39f9456358a0" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results"></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-37c45f0a-232c-44d8-a2f7-39f9456358a0" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">
              Search syntax tips
</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="-SNmpM9RiZ4OFWfFPJYbJ4mSVK7CwYn9d4fzYCUeRdakDIw1JglyRPeoW6Qi9G7NoYLg1XLJ8xCcnIQqvMpRzw">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="FouX8zOWSFBJZnErkVa5koxOgiuSoaTrXtucuf_8sqcWZoQ4tvEn7dDpjO9ub5PGTYCjEwmCNBpmxBSdGDq0Jw">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="_dNTycmDzexOMU3x-krQDVXWOg9FpIAkA9cXnp-wqtwEWXR-_8RdvCJkdR3h-SwUvCKA9p_S3yHYV815vOsrOQ" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input><input type="hidden" value="QDH3fE0MACDxT3xZ9kv9f2ejp-KLkhs5LtxILheVo0F9eU09eWnBwOl39wnDkoYMDp6xV52t64KffTw4EiVFAw" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf">

          </div>

        <div class="AppHeader-actions position-relative">
          <action-menu data-select-variant="none" data-view-component="true" data-catalyst="">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="global-create-menu-button" popovertarget="global-create-menu-overlay" aria-label="Create something new" aria-controls="global-create-menu-list" aria-haspopup="true" type="button" data-view-component="true" class="AppHeader-button Button--secondary Button--small Button width-auto color-fg-muted" aria-describedby="tooltip-df755d11-ec74-420d-87b0-3ccf72063a0f">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
      </span>
    <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg></span>
  </span>
</button><tool-tip id="tooltip-df755d11-ec74-420d-87b0-3ccf72063a0f" for="global-create-menu-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Create new...</tool-tip>


<anchored-position id="global-create-menu-overlay" anchor="global-create-menu-button" align="end" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 36px auto auto 70.6px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <div data-view-component="true">
  <ul aria-labelledby="global-create-menu-button" id="global-create-menu-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new repository&quot;}" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/new" tabindex="-1" id="item-019f8a8f-1efb-4217-9c4b-6eb244a76c9f" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
              New repository

</span></a>
  
  
</li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;import repository&quot;}" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/new/import" tabindex="-1" id="item-f9fb2dde-7ab9-4ed2-80fe-39438a3b4e5c" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-push">
    <path d="M1 2.5A2.5 2.5 0 0 1 3.5 0h8.75a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0V1.5h-8a1 1 0 0 0-1 1v6.708A2.493 2.493 0 0 1 3.5 9h3.25a.75.75 0 0 1 0 1.5H3.5a1 1 0 0 0 0 2h5.75a.75.75 0 0 1 0 1.5H3.5A2.5 2.5 0 0 1 1 11.5Zm13.23 7.79h-.001l-1.224-1.224v6.184a.75.75 0 0 1-1.5 0V9.066L10.28 10.29a.75.75 0 0 1-1.06-1.061l2.505-2.504a.75.75 0 0 1 1.06 0L15.29 9.23a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                Import repository

</span></a>
  
  
</li>
      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new codespace&quot;}" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/codespaces/new" tabindex="-1" id="item-92baed66-2742-4fa0-a97e-4af9209da5fd" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New codespace

</span></a>
  
  
</li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new gist&quot;}" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://gist.github.com/" tabindex="-1" id="item-2f0ff32d-9254-4d16-aa0b-72ff07285242" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New gist

</span></a>
  
  
</li>
      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
      <li data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/account/organizations/new" tabindex="-1" data-dont-follow-via-test="true" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new organization&quot;}" id="item-b3c46bd3-bc03-4096-b563-911726ddd4ec" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-organization">
    <path d="M1.75 16A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0h8.5C11.216 0 12 .784 12 1.75v12.5c0 .085-.006.168-.018.25h2.268a.25.25 0 0 0 .25-.25V8.285a.25.25 0 0 0-.111-.208l-1.055-.703a.749.749 0 1 1 .832-1.248l1.055.703c.487.325.779.871.779 1.456v5.965A1.75 1.75 0 0 1 14.25 16h-3.5a.766.766 0 0 1-.197-.026c-.099.017-.2.026-.303.026h-3a.75.75 0 0 1-.75-.75V14h-1v1.25a.75.75 0 0 1-.75.75Zm-.25-1.75c0 .138.112.25.25.25H4v-1.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 .75.75v1.25h2.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25ZM3.75 6h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 3.75A.75.75 0 0 1 3.75 3h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 3.75Zm4 3A.75.75 0 0 1 7.75 6h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 7 6.75ZM7.75 3h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 9.75A.75.75 0 0 1 3.75 9h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 9.75ZM7.75 9h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New organization

</span></a>
  
  
</li>
</ul>  
</div>

</div>
      
</div></anchored-position>  </focus-group>
</action-menu>


          <a href="https://github.com/issues" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-c2d993ea-d087-45f6-863f-1e82746b1c18" aria-labelledby="tooltip-bca4c6c3-baf9-47ce-a018-2bf9677224f7" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened Button-visual">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
</a><tool-tip id="tooltip-bca4c6c3-baf9-47ce-a018-2bf9677224f7" for="icon-button-c2d993ea-d087-45f6-863f-1e82746b1c18" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Issues</tool-tip>

          <a href="https://github.com/pulls" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-6ed4103b-d88f-4e33-8a05-1dd630f60de4" aria-labelledby="tooltip-c9864b0c-e1d8-4d15-a4df-1eee35c25fcb" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request Button-visual">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-c9864b0c-e1d8-4d15-a4df-1eee35c25fcb" for="icon-button-6ed4103b-d88f-4e33-8a05-1dd630f60de4" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Pull requests</tool-tip>

        </div>

        
<notification-indicator data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6ODYwNzE1NDYiLCJ0IjoxNzA4NjgwOTU0fQ==--225ba07a600975bf391711b377c27250bec3396b24fe5d1f136b00539c34529a" data-indicator-mode="none" data-tooltip-global="You have unread notifications" data-tooltip-unavailable="Notifications are unavailable at the moment." data-tooltip-none="You have no unread notifications" data-header-redesign-enabled="true" data-fetch-indicator-src="/notifications/indicator" data-fetch-indicator-enabled="true" data-view-component="true" class="js-socket-channel" data-fetch-retry-delay-time="500" data-catalyst="">
    <a id="AppHeader-notifications-button" href="https://github.com/notifications" aria-label="Notifications" data-hotkey="g n" data-target="notification-indicator.link" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;NOTIFICATIONS_HEADER&quot;,&quot;label&quot;:&quot;icon:read&quot;}" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted" aria-describedby="tooltip-137fd06b-d147-44b8-b4d1-91bc09aa7198">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-inbox Button-visual">
    <path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path>
</svg>
</a>

    <tool-tip data-target="notification-indicator.tooltip" id="tooltip-137fd06b-d147-44b8-b4d1-91bc09aa7198" for="AppHeader-notifications-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>You have no unread notifications</tool-tip>
</notification-indicator>

        

        <div class="AppHeader-user">
          <deferred-side-panel data-url="/_side-panels/user?repository_id=91612665" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
      <user-drawer-side-panel data-catalyst="">
    <button aria-label="Open user account menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-e8632bb6-bff2-4c9f-9298-883b243f7dc2" id="dialog-show-dialog-e8632bb6-bff2-4c9f-9298-883b243f7dc2" type="button" data-view-component="true" class="AppHeader-logo Button--invisible Button--medium Button Button--invisible-noVisuals color-bg-transparent p-0">  <span class="Button-content">
    <span class="Button-label"><img src="./README_files/86071546" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle"></span>
  </span>
</button>

<dialog-helper>
  <dialog data-target="deferred-side-panel.panel" id="dialog-e8632bb6-bff2-4c9f-9298-883b243f7dc2" aria-modal="true" aria-labelledby="dialog-e8632bb6-bff2-4c9f-9298-883b243f7dc2-title" aria-describedby="dialog-e8632bb6-bff2-4c9f-9298-883b243f7dc2-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade Overlay--placement-right SidePanel">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-e8632bb6-bff2-4c9f-9298-883b243f7dc2-title">
        Account menu
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <img src="./README_files/86071546" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle">
</div>        <div data-view-component="true" class="overflow-hidden d-flex width-full">        <div data-view-component="true" class="lh-condensed overflow-hidden d-flex flex-column flex-justify-center ml-2 f5 mr-auto width-full">
          <span data-view-component="true" class="Truncate text-bold">
    <span data-view-component="true" class="Truncate-text">
            upendragoud
</span>
</span>          </div>
        <action-menu data-select-variant="none" data-view-component="true" class="d-sm-none d-md-none d-lg-none" data-catalyst="">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="user-create-menu-button" popovertarget="user-create-menu-overlay" aria-label="Create something new" aria-controls="user-create-menu-list" aria-haspopup="true" type="button" data-view-component="true" class="AppHeader-button Button--secondary Button--small Button width-auto color-fg-muted" aria-describedby="tooltip-6793e0e8-23ca-40d0-94de-7824f9027483">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
      </span>
    <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg></span>
  </span>
</button><tool-tip id="tooltip-6793e0e8-23ca-40d0-94de-7824f9027483" for="user-create-menu-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Create new...</tool-tip>


<anchored-position id="user-create-menu-overlay" anchor="user-create-menu-button" align="end" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 4px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <div data-view-component="true">
  <ul aria-labelledby="user-create-menu-button" id="user-create-menu-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new repository&quot;}" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/new" tabindex="-1" id="item-e0b5354f-5299-41db-a1d4-917ed406218a" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
              New repository

</span></a>
  
  
</li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;import repository&quot;}" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/new/import" tabindex="-1" id="item-d2a6f3d2-b69f-4000-8dca-e3e6ed47d5d4" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-push">
    <path d="M1 2.5A2.5 2.5 0 0 1 3.5 0h8.75a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0V1.5h-8a1 1 0 0 0-1 1v6.708A2.493 2.493 0 0 1 3.5 9h3.25a.75.75 0 0 1 0 1.5H3.5a1 1 0 0 0 0 2h5.75a.75.75 0 0 1 0 1.5H3.5A2.5 2.5 0 0 1 1 11.5Zm13.23 7.79h-.001l-1.224-1.224v6.184a.75.75 0 0 1-1.5 0V9.066L10.28 10.29a.75.75 0 0 1-1.06-1.061l2.505-2.504a.75.75 0 0 1 1.06 0L15.29 9.23a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                Import repository

</span></a>
  
  
</li>
      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new codespace&quot;}" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/codespaces/new" tabindex="-1" id="item-3782e691-4aac-4564-837f-a4735da68ac2" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New codespace

</span></a>
  
  
</li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new gist&quot;}" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://gist.github.com/" tabindex="-1" id="item-901c9e8a-6f8e-455e-8acf-6d4bca41351b" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New gist

</span></a>
  
  
</li>
      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
      <li data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://github.com/account/organizations/new" tabindex="-1" data-dont-follow-via-test="true" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new organization&quot;}" id="item-16395a3e-0d23-4df6-a9bb-8bc3f04eccdd" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-organization">
    <path d="M1.75 16A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0h8.5C11.216 0 12 .784 12 1.75v12.5c0 .085-.006.168-.018.25h2.268a.25.25 0 0 0 .25-.25V8.285a.25.25 0 0 0-.111-.208l-1.055-.703a.749.749 0 1 1 .832-1.248l1.055.703c.487.325.779.871.779 1.456v5.965A1.75 1.75 0 0 1 14.25 16h-3.5a.766.766 0 0 1-.197-.026c-.099.017-.2.026-.303.026h-3a.75.75 0 0 1-.75-.75V14h-1v1.25a.75.75 0 0 1-.75.75Zm-.25-1.75c0 .138.112.25.25.25H4v-1.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 .75.75v1.25h2.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25ZM3.75 6h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 3.75A.75.75 0 0 1 3.75 3h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 3.75Zm4 3A.75.75 0 0 1 7.75 6h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 7 6.75ZM7.75 3h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 9.75A.75.75 0 0 1 3.75 9h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 9.75ZM7.75 9h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New organization

</span></a>
  
  
</li>
</ul>  
</div>

</div>
      
</div></anchored-position>  </focus-group>
</action-menu>

</div>
</div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-e8632bb6-bff2-4c9f-9298-883b243f7dc2" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <scrollable-region data-labelled-by="dialog-e8632bb6-bff2-4c9f-9298-883b243f7dc2-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body d-flex flex-column px-2">    <div data-view-component="true" class="d-flex flex-column mb-3">
        <nav aria-label="User navigation" data-view-component="true" class="ActionList">
  
  <nav-list data-catalyst="">
    <ul data-view-component="true" class="ActionListWrap">
        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <button id="item-34d48a11-c99c-4c52-ae84-12541e943513" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PROFILE&quot;,&quot;label&quot;:null}" id="item-a42c1eb0-a752-4516-8c43-3eb5ae4a4a66" href="https://github.com/upendragoud" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-person">
    <path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your profile
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <button id="item-a16b5e8c-c187-4571-a22a-d38298465a32" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_REPOSITORIES&quot;,&quot;label&quot;:null}" id="item-1bf94e6e-04fb-4eed-98cb-2967d1ce66fb" href="https://github.com/upendragoud?tab=repositories" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your repositories
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_PROJECTS&quot;,&quot;label&quot;:null}" id="item-f39f88eb-3c25-42cc-80fb-c67bb6e25821" href="https://github.com/upendragoud?tab=projects" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project">
    <path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25ZM11.75 3a.75.75 0 0 1 .75.75v7.5a.75.75 0 0 1-1.5 0v-7.5a.75.75 0 0 1 .75-.75Zm-8.25.75a.75.75 0 0 1 1.5 0v5.5a.75.75 0 0 1-1.5 0ZM8 3a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 3Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your projects
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <button id="item-15902fe0-0565-45e9-a722-f594b3abd24e" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <button id="item-c8b89acc-6b5e-417a-8fbb-b4713a3562d2" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_STARS&quot;,&quot;label&quot;:null}" id="item-205630f7-ea69-44f3-b027-b4e7cc34d71d" href="https://github.com/upendragoud?tab=stars" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your stars
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SPONSORS&quot;,&quot;label&quot;:null}" id="item-fd5eca72-2870-4247-91ec-7363b0bcaf35" href="https://github.com/sponsors/accounts" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-heart">
    <path d="m8 14.25.345.666a.75.75 0 0 1-.69 0l-.008-.004-.018-.01a7.152 7.152 0 0 1-.31-.17 22.055 22.055 0 0 1-3.434-2.414C2.045 10.731 0 8.35 0 5.5 0 2.836 2.086 1 4.25 1 5.797 1 7.153 1.802 8 3.02 8.847 1.802 10.203 1 11.75 1 13.914 1 16 2.836 16 5.5c0 2.85-2.045 5.231-3.885 6.818a22.066 22.066 0 0 1-3.744 2.584l-.018.01-.006.003h-.002ZM4.25 2.5c-1.336 0-2.75 1.164-2.75 3 0 2.15 1.58 4.144 3.365 5.682A20.58 20.58 0 0 0 8 13.393a20.58 20.58 0 0 0 3.135-2.211C12.92 9.644 14.5 7.65 14.5 5.5c0-1.836-1.414-3-2.75-3-1.373 0-2.609.986-3.029 2.456a.749.749 0 0 1-1.442 0C6.859 3.486 5.623 2.5 4.25 2.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your sponsors
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_GISTS&quot;,&quot;label&quot;:null}" id="item-44f3971d-68a0-4992-a440-480fd505b377" href="https://gist.github.com/mine" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code-square">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your gists
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <button id="item-8a68bb33-8f04-47a5-ac0b-07bf9a67d311" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <button id="item-e56eac0a-0eb7-4e55-8308-f63cb780b57b" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SETTINGS&quot;,&quot;label&quot;:null}" id="item-e3d7d215-b00b-4655-b639-4790e2c1c176" href="https://github.com/settings/profile" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear">
    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Settings
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;DOCS&quot;,&quot;label&quot;:null}" id="item-75a38ef2-037d-4bd4-93c3-69a12b83fd00" href="https://docs.github.com/" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          GitHub Docs
</span></a>
  
  
</li>

        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SUPPORT&quot;,&quot;label&quot;:null}" id="item-0e78ecb5-a165-474d-9452-950d667dd1d1" href="https://support.github.com/" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-people">
    <path d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          GitHub Support
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-targets="nav-list.items nav-list.items" data-item-id="" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;LOGOUT&quot;,&quot;label&quot;:null}" id="item-a5690dc5-fd49-4b17-8120-0a9a329dba9b" href="https://github.com/logout" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          Sign out
</span></a>
  
  
</li>

</ul>  </nav-list>
</nav>


</div>
</div>
      </scrollable-region>
      
</dialog></dialog-helper>
  </user-drawer-side-panel>

  </include-fragment>
</deferred-side-panel>
          
        </div>

        <div class="position-absolute mt-2">
            
<site-header-logged-in-user-menu data-catalyst="">

</site-header-logged-in-user-menu>

        </div>
      </div>
    </div>


      <div class="AppHeader-localBar">
        <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="https://github.com/Azure/Hangman" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /Azure/Hangman" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected" aria-current="page">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="https://github.com/Azure/Hangman/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /Azure/Hangman/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="https://github.com/Azure/Hangman/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /Azure/Hangman/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="https://github.com/Azure/Hangman/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /Azure/Hangman/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="https://github.com/Azure/Hangman/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /Azure/Hangman/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="https://github.com/Azure/Hangman/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /Azure/Hangman/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="https://github.com/Azure/Hangman/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /Azure/Hangman/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true" data-catalyst="">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-menu-5ebed915-5e0d-44c0-bcf4-aa08f2f1fe96-button" popovertarget="action-menu-5ebed915-5e0d-44c0-bcf4-aa08f2f1fe96-overlay" aria-controls="action-menu-5ebed915-5e0d-44c0-bcf4-aa08f2f1fe96-list" aria-haspopup="true" aria-labelledby="tooltip-7eed53b4-cfea-4b51-a0fc-15e2917e3f33" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-7eed53b4-cfea-4b51-a0fc-15e2917e3f33" for="action-menu-5ebed915-5e0d-44c0-bcf4-aa08f2f1fe96-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Additional navigation options</tool-tip>


<anchored-position id="action-menu-5ebed915-5e0d-44c0-bcf4-aa08f2f1fe96-overlay" anchor="action-menu-5ebed915-5e0d-44c0-bcf4-aa08f2f1fe96-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 36px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <div data-view-component="true">
  <ul aria-labelledby="action-menu-5ebed915-5e0d-44c0-bcf4-aa08f2f1fe96-button" id="action-menu-5ebed915-5e0d-44c0-bcf4-aa08f2f1fe96-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
      <li hidden="" data-menu-item="i0code-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-c643c614-6fc3-422f-976e-d8cf5afabd40" href="https://github.com/Azure/Hangman" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span></a>
  
  
</li>
      <li hidden="" data-menu-item="i1issues-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-e79253da-201f-4bb8-b913-418b1c308d2b" href="https://github.com/Azure/Hangman/issues" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span></a>
  
  
</li>
      <li hidden="" data-menu-item="i2pull-requests-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-f6cfe914-d0d2-4e2a-a811-0962225a49ce" href="https://github.com/Azure/Hangman/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span></a>
  
  
</li>
      <li hidden="" data-menu-item="i3actions-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-0b681e4e-9ba9-4cda-bd19-29ff25580617" href="https://github.com/Azure/Hangman/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Actions
</span></a>
  
  
</li>
      <li hidden="" data-menu-item="i4projects-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-639cdc0a-dc48-45b3-8857-48b48e7750fb" href="https://github.com/Azure/Hangman/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span></a>
  
  
</li>
      <li hidden="" data-menu-item="i5security-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-e436ee9f-9693-4a9d-b81a-512c928762b9" href="https://github.com/Azure/Hangman/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Security
</span></a>
  
  
</li>
      <li hidden="" data-menu-item="i6insights-tab" data-targets="action-list.items action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a tabindex="-1" id="item-3e6ec334-04ab-446d-9ee1-c63ee6cddaaa" href="https://github.com/Azure/Hangman/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Insights
</span></a>
  
  
</li>
</ul>  
</div>

</div>
      
</div></anchored-position>  </focus-group>
</action-menu></div>
</nav>
      </div>
</header>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full mb-3">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a class="Link--inTextBlock" href="https://github.com/Azure/Hangman/blame/master/README.md">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a class="Link--inTextBlock" href="https://github.com/Azure/Hangman/blame/master/README.md">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a class="Link--inTextBlock" href="https://github.com/Azure/Hangman/blame/master/README.md">Reload</a> to refresh your session.</span>

    <button id="icon-button-6a703411-39e8-401f-a8ad-d479e5caea15" aria-labelledby="tooltip-35aa4783-f7bf-4f05-a9e5-048882a8e748" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-35aa4783-f7bf-4f05-a9e5-048882a8e748" for="icon-button-6a703411-39e8-401f-a8ad-d479e5caea15" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Dismiss alert</tool-tip>


  
</div>
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" data-turbo-replace="">





  <template class="js-flash-template"></template>
</div>


    
    <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6ODYwNzE1NDYiLCJ0IjoxNzA4NjgwOTU0fQ==--225ba07a600975bf391711b377c27250bec3396b24fe5d1f136b00539c34529a" data-view-component="true" class="js-socket-channel" data-refresh-delay="500" data-catalyst=""></notification-shelf-watcher>
  <div hidden="" data-initial="" data-target="notification-shelf-watcher.placeholder"></div>






      <details class="details-reset details-overlay details-overlay-dark js-command-palette-dialog" id="command-palette-pjax-container" data-turbo-replace="">
  <summary aria-label="Command palette trigger" tabindex="-1" role="button"></summary>
  <details-dialog class="command-palette-details-dialog d-flex flex-column flex-justify-center height-fit" aria-label="Command palette" role="dialog" aria-modal="true">
    <command-palette class="command-palette color-bg-default rounded-3 border color-shadow-small" return-to="/Azure/Hangman/blob/master/README.md" user-id="86071546" activation-hotkey="Mod+k,Mod+Alt+k" command-mode-hotkey="Mod+Shift+K" data-action="
        command-palette-input-ready:command-palette#inputReady
        command-palette-page-stack-updated:command-palette#updateInputScope
        itemsUpdated:command-palette#itemsUpdated
        keydown:command-palette#onKeydown
        loadingStateChanged:command-palette#loadingStateChanged
        selectedItemChanged:command-palette#selectedItemChanged
        pageFetchError:command-palette#pageFetchError
      " data-catalyst="">

        <command-palette-mode data-char="#" data-scope-types="[&quot;&quot;]" data-placeholder="Search issues and pull requests" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="#" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-placeholder="Search issues, pull requests, discussions, and projects" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="!" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-placeholder="Search projects" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="@" data-scope-types="[&quot;&quot;]" data-placeholder="Search or jump to a user, organization, or repository" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="@" data-scope-types="[&quot;owner&quot;]" data-placeholder="Search or jump to a repository" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="/" data-scope-types="[&quot;repository&quot;]" data-placeholder="Search files" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="?" data-placeholder="" data-catalyst="" data-scope-types=""></command-palette-mode>
        <command-palette-mode data-char="&gt;" data-placeholder="Run a command" data-scope-types="" data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="" data-scope-types="[&quot;&quot;]" data-placeholder="Search or jump to..." data-catalyst=""></command-palette-mode>
        <command-palette-mode data-char="" data-scope-types="[&quot;owner&quot;]" data-placeholder="Search or jump to..." data-catalyst=""></command-palette-mode>
      <command-palette-mode class="js-command-palette-default-mode" data-char="" data-placeholder="Search or jump to..." data-scope-types="" data-catalyst=""></command-palette-mode>

      <command-palette-input placeholder="Search or jump to..." data-action="
          command-palette-input:command-palette#onInput
          command-palette-select:command-palette#onSelect
          command-palette-descope:command-palette#onDescope
          command-palette-cleared:command-palette#onInputClear
        " data-catalyst="" class="d-flex flex-items-center flex-nowrap py-1 pl-3 pr-2 border-bottom">
        <div class="js-search-icon d-flex flex-items-center mr-2" style="height: 26px">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search color-fg-muted">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
        </div>
        <div class="js-spinner d-flex flex-items-center mr-2 color-fg-muted" hidden="">
          <svg aria-label="Loading" class="anim-rotate" viewBox="0 0 16 16" fill="none" width="16" height="16">
            <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke"></circle>
            <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
          </svg>
        </div>
        <command-palette-scope data-catalyst="" class="d-inline-flex">
          <div data-target="command-palette-scope.placeholder" hidden="" class="color-fg-subtle">/&nbsp;&nbsp;<span class="text-semibold color-fg-default">...</span>&nbsp;&nbsp;/&nbsp;&nbsp;</div>
              <command-palette-token data-text="Azure" data-id="MDEyOk9yZ2FuaXphdGlvbjY4NDQ0OTg=" data-type="owner" data-value="Azure" data-targets="command-palette-scope.tokens" class="color-fg-default text-semibold" style="white-space:nowrap;line-height:20px;" id="" data-catalyst="">Azure<span class="color-fg-subtle text-normal">&nbsp;&nbsp;/&nbsp;&nbsp;</span></command-palette-token>
              <command-palette-token data-text="Hangman" data-id="MDEwOlJlcG9zaXRvcnk5MTYxMjY2NQ==" data-type="repository" data-value="Hangman" data-targets="command-palette-scope.tokens" class="color-fg-default text-semibold" style="white-space:nowrap;line-height:20px;" id="" data-catalyst="">Hangman<span class="color-fg-subtle text-normal">&nbsp;&nbsp;/&nbsp;&nbsp;</span></command-palette-token>
        </command-palette-scope>
        <div class="command-palette-input-group flex-1 form-control border-0 box-shadow-none" style="z-index: 0">
          <div class="command-palette-typeahead position-absolute d-flex flex-items-center Truncate">
            <span class="typeahead-segment input-mirror" data-target="command-palette-input.mirror"></span>
            <span class="Truncate-text" data-target="command-palette-input.typeaheadText"></span>
            <span class="typeahead-segment" data-target="command-palette-input.typeaheadPlaceholder"></span>
          </div>
          <input class="js-overlay-input typeahead-input d-none" disabled="" tabindex="-1" aria-label="Hidden input for typeahead">
          <input type="text" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" class="js-input typeahead-input form-control border-0 box-shadow-none input-block width-full no-focus-indicator" aria-label="Command palette input" aria-haspopup="listbox" aria-expanded="false" aria-autocomplete="list" aria-controls="command-palette-page-stack" role="combobox" data-action="
              input:command-palette-input#onInput
              keydown:command-palette-input#onKeydown
            " placeholder="Search or jump to...">
        </div>
          <div data-view-component="true" class="position-relative d-inline-block">
    <button aria-keyshortcuts="Control+Backspace" data-action="click:command-palette-input#onClear keypress:command-palette-input#onClear" data-target="command-palette-input.clearButton" id="command-palette-clear-button" hidden="hidden" type="button" data-view-component="true" class="btn-octicon command-palette-input-clear-button" aria-labelledby="tooltip-073bb96f-a0d8-452e-88a2-a9a04ab45587">      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>    <tool-tip id="tooltip-073bb96f-a0d8-452e-88a2-a9a04ab45587" for="command-palette-clear-button" popover="manual" data-direction="w" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tool-tip-position-top, 0) auto auto var(--tool-tip-position-left, 0) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host:before{
        position: absolute;
        z-index: 1000001;
        color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
        content: "";
        border: 6px solid transparent;
        opacity: 0;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: 12px;
        content: "";
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open),
      :host(.\:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
        animation-delay: .4s;
      }

      :host(.tooltip-s):before,
      :host(.tooltip-n):before {
        right: 50%;
        margin-right: -6px;
      }
      :host(.tooltip-s):before,
      :host(.tooltip-se):before,
      :host(.tooltip-sw):before {
        bottom: 100%;
        border-bottom-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }
      :host(.tooltip-n):before,
      :host(.tooltip-ne):before,
      :host(.tooltip-nw):before {
        top: 100%;
        border-top-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }
      :host(.tooltip-se):before,
      :host(.tooltip-ne):before {
        left: 0;
        margin-left: 6px;
      }
      :host(.tooltip-sw):before,
      :host(.tooltip-nw):before {
        right: 0;
        margin-right: 6px;
      }
      :host(.tooltip-w):before {
        top: 50%;
        bottom: 50%;
        left: 100%;
        margin-top: -6px;
        border-left-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }
      :host(.tooltip-e):before {
        top: 50%;
        right: 100%;
        bottom: 50%;
        margin-top: -6px;
        border-right-color: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus));
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Clear Command Palette</tool-tip>
</div>
      </command-palette-input>

      <command-palette-page-stack data-default-scope-id="MDEwOlJlcG9zaXRvcnk5MTYxMjY2NQ==" data-default-scope-type="Repository" data-action="command-palette-page-octicons-cached:command-palette-page-stack#cacheOcticons" data-current-mode="" data-catalyst="" data-target="command-palette.pageStack" data-current-query-text="">
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search pull requests
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search issues
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search discussions
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">!</kbd> to search projects
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;owner&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">@</kbd> to search teams
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">@</kbd> to search people and organizations
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">&gt;</kbd> to activate command mode
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Go to your accessibility settings to change your keyboard shortcuts
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type author:@me to search your content
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:pr to filter to pull requests
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:issue to filter to issues
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:project to filter to projects
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip class="color-fg-muted f6 px-3 py-1 my-2" data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-mode="#" data-value="" data-match-mode="" data-catalyst="" hidden="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:open to filter to open content
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
        <command-palette-tip class="mx-3 my-2 flash flash-error d-flex flex-items-center" data-scope-types="*" data-on-error="" data-mode="*" data-catalyst="" hidden="" data-match-mode="" data-value="*">
          <div>
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
          </div>
          <div class="px-2">
            We’ve encountered an error and some results aren't available at this time. Type a new search or try again later.
          </div>
        </command-palette-tip>
        <command-palette-tip class="h4 color-fg-default pl-3 pb-2 pt-3" data-on-empty="" data-scope-types="*" data-match-mode="[^?]|^$" data-mode="*" data-catalyst="" hidden="" data-value="*">
          No results matched your search
        </command-palette-tip>

        <div hidden="">

            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="arrow-right-color-fg-muted">
              <svg height="16" class="octicon octicon-arrow-right color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8.22 2.97a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l2.97-2.97H3.75a.75.75 0 0 1 0-1.5h7.44L8.22 4.03a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="arrow-right-color-fg-default">
              <svg height="16" class="octicon octicon-arrow-right color-fg-default" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8.22 2.97a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l2.97-2.97H3.75a.75.75 0 0 1 0-1.5h7.44L8.22 4.03a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="codespaces-color-fg-muted">
              <svg height="16" class="octicon octicon-codespaces color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="copy-color-fg-muted">
              <svg height="16" class="octicon octicon-copy color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="dash-color-fg-muted">
              <svg height="16" class="octicon octicon-dash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M2 7.75A.75.75 0 0 1 2.75 7h10a.75.75 0 0 1 0 1.5h-10A.75.75 0 0 1 2 7.75Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="file-color-fg-muted">
              <svg height="16" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="gear-color-fg-muted">
              <svg height="16" class="octicon octicon-gear color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="lock-color-fg-muted">
              <svg height="16" class="octicon octicon-lock color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M4 4a4 4 0 0 1 8 0v2h.25c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 12.25 15h-8.5A1.75 1.75 0 0 1 2 13.25v-5.5C2 6.784 2.784 6 3.75 6H4Zm8.25 3.5h-8.5a.25.25 0 0 0-.25.25v5.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25ZM10.5 6V4a2.5 2.5 0 1 0-5 0v2Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="moon-color-fg-muted">
              <svg height="16" class="octicon octicon-moon color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M9.598 1.591a.749.749 0 0 1 .785-.175 7.001 7.001 0 1 1-8.967 8.967.75.75 0 0 1 .961-.96 5.5 5.5 0 0 0 7.046-7.046.75.75 0 0 1 .175-.786Zm1.616 1.945a7 7 0 0 1-7.678 7.678 5.499 5.499 0 1 0 7.678-7.678Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="person-color-fg-muted">
              <svg height="16" class="octicon octicon-person color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="pencil-color-fg-muted">
              <svg height="16" class="octicon octicon-pencil color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="issue-opened-open">
              <svg height="16" class="octicon octicon-issue-opened open" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="git-pull-request-draft-color-fg-muted">
              <svg height="16" class="octicon octicon-git-pull-request-draft color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M3.25 1A2.25 2.25 0 0 1 4 5.372v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.251 2.251 0 0 1 3.25 1Zm9.5 14a2.25 2.25 0 1 1 0-4.5 2.25 2.25 0 0 1 0 4.5ZM2.5 3.25a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0ZM3.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm9.5 0a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM14 7.5a1.25 1.25 0 1 1-2.5 0 1.25 1.25 0 0 1 2.5 0Zm0-4.25a1.25 1.25 0 1 1-2.5 0 1.25 1.25 0 0 1 2.5 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="search-color-fg-muted">
              <svg height="16" class="octicon octicon-search color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="sun-color-fg-muted">
              <svg height="16" class="octicon octicon-sun color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 12a4 4 0 1 1 0-8 4 4 0 0 1 0 8Zm0-1.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Zm5.657-8.157a.75.75 0 0 1 0 1.061l-1.061 1.06a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l1.06-1.06a.75.75 0 0 1 1.06 0Zm-9.193 9.193a.75.75 0 0 1 0 1.06l-1.06 1.061a.75.75 0 1 1-1.061-1.06l1.06-1.061a.75.75 0 0 1 1.061 0ZM8 0a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0V.75A.75.75 0 0 1 8 0ZM3 8a.75.75 0 0 1-.75.75H.75a.75.75 0 0 1 0-1.5h1.5A.75.75 0 0 1 3 8Zm13 0a.75.75 0 0 1-.75.75h-1.5a.75.75 0 0 1 0-1.5h1.5A.75.75 0 0 1 16 8Zm-8 5a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0v-1.5A.75.75 0 0 1 8 13Zm3.536-1.464a.75.75 0 0 1 1.06 0l1.061 1.06a.75.75 0 0 1-1.06 1.061l-1.061-1.06a.75.75 0 0 1 0-1.061ZM2.343 2.343a.75.75 0 0 1 1.061 0l1.06 1.061a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018l-1.06-1.06a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="sync-color-fg-muted">
              <svg height="16" class="octicon octicon-sync color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M1.705 8.005a.75.75 0 0 1 .834.656 5.5 5.5 0 0 0 9.592 2.97l-1.204-1.204a.25.25 0 0 1 .177-.427h3.646a.25.25 0 0 1 .25.25v3.646a.25.25 0 0 1-.427.177l-1.38-1.38A7.002 7.002 0 0 1 1.05 8.84a.75.75 0 0 1 .656-.834ZM8 2.5a5.487 5.487 0 0 0-4.131 1.869l1.204 1.204A.25.25 0 0 1 4.896 6H1.25A.25.25 0 0 1 1 5.75V2.104a.25.25 0 0 1 .427-.177l1.38 1.38A7.002 7.002 0 0 1 14.95 7.16a.75.75 0 0 1-1.49.178A5.5 5.5 0 0 0 8 2.5Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="trash-color-fg-muted">
              <svg height="16" class="octicon octicon-trash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11 1.75V3h2.25a.75.75 0 0 1 0 1.5H2.75a.75.75 0 0 1 0-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75ZM4.496 6.675l.66 6.6a.25.25 0 0 0 .249.225h5.19a.25.25 0 0 0 .249-.225l.66-6.6a.75.75 0 0 1 1.492.149l-.66 6.6A1.748 1.748 0 0 1 10.595 15h-5.19a1.75 1.75 0 0 1-1.741-1.575l-.66-6.6a.75.75 0 1 1 1.492-.15ZM6.5 1.75V3h3V1.75a.25.25 0 0 0-.25-.25h-2.5a.25.25 0 0 0-.25.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="key-color-fg-muted">
              <svg height="16" class="octicon octicon-key color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.5 0a5.499 5.499 0 1 1-1.288 10.848l-.932.932a.749.749 0 0 1-.53.22H7v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22H5v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22h-2A1.75 1.75 0 0 1 0 14.25v-2c0-.199.079-.389.22-.53l4.932-4.932A5.5 5.5 0 0 1 10.5 0Zm-4 5.5c-.001.431.069.86.205 1.269a.75.75 0 0 1-.181.768L1.5 12.56v1.69c0 .138.112.25.25.25h1.69l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l1.023-1.025a.75.75 0 0 1 .768-.18A4 4 0 1 0 6.5 5.5ZM11 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="comment-discussion-color-fg-muted">
              <svg height="16" class="octicon octicon-comment-discussion color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="bell-color-fg-muted">
              <svg height="16" class="octicon octicon-bell color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="bell-slash-color-fg-muted">
              <svg height="16" class="octicon octicon-bell-slash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="m4.182 4.31.016.011 10.104 7.316.013.01 1.375.996a.75.75 0 1 1-.88 1.214L13.626 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947V5.305L.31 3.357a.75.75 0 1 1 .88-1.214Zm7.373 7.19L4.5 6.391v1.556c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01c0 .005.002.009.005.012l.006.004.007.001ZM8 1.5c-.997 0-1.895.416-2.534 1.086A.75.75 0 1 1 4.38 1.55 5 5 0 0 1 13 5v2.373a.75.75 0 0 1-1.5 0V5A3.5 3.5 0 0 0 8 1.5ZM8 16a2 2 0 0 1-1.985-1.75c-.017-.137.097-.25.235-.25h3.5c.138 0 .252.113.235.25A2 2 0 0 1 8 16Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="paintbrush-color-fg-muted">
              <svg height="16" class="octicon octicon-paintbrush color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11.134 1.535c.7-.509 1.416-.942 2.076-1.155.649-.21 1.463-.267 2.069.34.603.601.568 1.411.368 2.07-.202.668-.624 1.39-1.125 2.096-1.011 1.424-2.496 2.987-3.775 4.249-1.098 1.084-2.132 1.839-3.04 2.3a3.744 3.744 0 0 1-1.055 3.217c-.431.431-1.065.691-1.657.861-.614.177-1.294.287-1.914.357A21.151 21.151 0 0 1 .797 16H.743l.007-.75H.749L.742 16a.75.75 0 0 1-.743-.742l.743-.008-.742.007v-.054a21.25 21.25 0 0 1 .13-2.284c.067-.647.187-1.287.358-1.914.17-.591.43-1.226.86-1.657a3.746 3.746 0 0 1 3.227-1.054c.466-.893 1.225-1.907 2.314-2.982 1.271-1.255 2.833-2.75 4.245-3.777ZM1.62 13.089c-.051.464-.086.929-.104 1.395.466-.018.932-.053 1.396-.104a10.511 10.511 0 0 0 1.668-.309c.526-.151.856-.325 1.011-.48a2.25 2.25 0 1 0-3.182-3.182c-.155.155-.329.485-.48 1.01a10.515 10.515 0 0 0-.309 1.67Zm10.396-10.34c-1.224.89-2.605 2.189-3.822 3.384l1.718 1.718c1.21-1.205 2.51-2.597 3.387-3.833.47-.662.78-1.227.912-1.662.134-.444.032-.551.009-.575h-.001V1.78c-.014-.014-.113-.113-.548.027-.432.14-.995.462-1.655.942Zm-4.832 7.266-.001.001a9.859 9.859 0 0 0 1.63-1.142L7.155 7.216a9.7 9.7 0 0 0-1.161 1.607c.482.302.889.71 1.19 1.192Z"></path></svg>
            </div>

            <command-palette-item-group data-group-id="top" data-group-title="Top result" data-group-hint="" data-group-limits="{}" data-default-priority="0" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Top result
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Top result results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="commands" data-group-title="Commands" data-group-hint="Type &gt; to filter" data-group-limits="{&quot;static_items_page&quot;:50,&quot;issue&quot;:50,&quot;pull_request&quot;:50,&quot;discussion&quot;:50}" data-default-priority="1" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Commands
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              Type &gt; to filter
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Commands results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="global_commands" data-group-title="Global Commands" data-group-hint="Type &gt; to filter" data-group-limits="{&quot;issue&quot;:0,&quot;pull_request&quot;:0,&quot;discussion&quot;:0}" data-default-priority="2" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Global Commands
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              Type &gt; to filter
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Global Commands results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="this_page" data-group-title="This Page" data-group-hint="" data-group-limits="{}" data-default-priority="3" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              This Page
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="This Page results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="files" data-group-title="Files" data-group-hint="" data-group-limits="{}" data-default-priority="4" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Files
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Files results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="default" data-group-title="Default" data-group-hint="" data-group-limits="{&quot;static_items_page&quot;:50}" data-default-priority="5" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Default results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="pages" data-group-title="Pages" data-group-hint="" data-group-limits="{&quot;repository&quot;:10}" data-default-priority="6" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Pages
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Pages results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="access_policies" data-group-title="Access Policies" data-group-hint="" data-group-limits="{}" data-default-priority="7" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Access Policies
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Access Policies results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="organizations" data-group-title="Organizations" data-group-hint="" data-group-limits="{}" data-default-priority="8" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Organizations
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Organizations results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="repositories" data-group-title="Repositories" data-group-hint="" data-group-limits="{}" data-default-priority="9" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Repositories
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Repositories results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="references" data-group-title="Issues, pull requests, and discussions" data-group-hint="Type # to filter" data-group-limits="{}" data-default-priority="10" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Issues, pull requests, and discussions
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              Type # to filter
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Issues, pull requests, and discussions results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="teams" data-group-title="Teams" data-group-hint="" data-group-limits="{}" data-default-priority="11" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Teams
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Teams results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="users" data-group-title="Users" data-group-hint="" data-group-limits="{}" data-default-priority="12" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Users
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Users results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="memex_projects" data-group-title="Projects" data-group-hint="" data-group-limits="{}" data-default-priority="13" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Projects
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Projects results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="projects" data-group-title="Projects (classic)" data-group-hint="" data-group-limits="{}" data-default-priority="14" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Projects (classic)
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Projects (classic) results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="footer" data-group-title="Footer" data-group-hint="" data-group-limits="{}" data-default-priority="15" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Footer results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="modes_help" data-group-title="Modes" data-group-hint="" data-group-limits="{}" data-default-priority="16" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Modes
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Modes results"></div>
        </command-palette-item-group>
            <command-palette-item-group data-group-id="filters_help" data-group-title="Use filters in issues, pull requests, discussions, and projects" data-group-hint="" data-group-limits="{}" data-default-priority="17" data-catalyst="" class="py-2 border-top" hidden="true" data-skip-template="">
            
          <div class="d-flex flex-justify-between my-2 px-3">
            <span data-target="command-palette-item-group.header" class="color-fg-muted text-bold f6 text-normal">
              Use filters in issues, pull requests, discussions, and projects
            </span>
            <span data-target="command-palette-item-group.header" class="color-fg-muted f6 text-normal">
              
            </span>
          </div>
          <div role="listbox" class="list-style-none" data-target="command-palette-item-group.list" aria-label="Use filters in issues, pull requests, discussions, and projects results"></div>
        </command-palette-item-group>

            <command-palette-page data-page-title="Azure" data-scope-id="MDEyOk9yZ2FuaXphdGlvbjY4NDQ0OTg=" data-scope-type="owner" data-targets="command-palette-page-stack.defaultPages" hidden="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" style="max-height:400px;">
            </command-palette-page>
            <command-palette-page data-page-title="Hangman" data-scope-id="MDEwOlJlcG9zaXRvcnk5MTYxMjY2NQ==" data-scope-type="repository" data-targets="command-palette-page-stack.defaultPages" hidden="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" style="max-height:400px;">
            </command-palette-page>
        </div>

        <command-palette-page data-is-root="" hidden="" data-page-title="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" data-targets="command-palette-page-stack.pages" style="max-height:400px;" data-scope-id="" data-scope-type="">
        </command-palette-page>
          <command-palette-page data-page-title="Azure" data-scope-id="MDEyOk9yZ2FuaXphdGlvbjY4NDQ0OTg=" data-scope-type="owner" hidden="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" data-targets="command-palette-page-stack.pages" style="max-height:400px;">
          </command-palette-page>
          <command-palette-page data-page-title="Hangman" data-scope-id="MDEwOlJlcG9zaXRvcnk5MTYxMjY2NQ==" data-scope-type="repository" hidden="" data-catalyst="" class="rounded-bottom-2 page-stack-transition-height" data-targets="command-palette-page-stack.pages" style="max-height:400px;">
          </command-palette-page>
      </command-palette-page-stack>

      <server-defined-provider data-type="search-links" data-targets="command-palette.serverDefinedProviderElements" data-supported-modes="" data-catalyst="" data-fetch-debounce="" data-supported-scope-types="" data-src="" data-supports-commands=""></server-defined-provider>
      <server-defined-provider data-type="help" data-targets="command-palette.serverDefinedProviderElements" data-supported-modes="" data-catalyst="" data-fetch-debounce="" data-supported-scope-types="" data-src="" data-supports-commands="">
          <command-palette-help data-group="modes_help" data-prefix="#" data-scope-types="[&quot;&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>issues</strong> and <strong>pull requests</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">#</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="#" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>issues, pull requests, discussions,</strong> and <strong>projects</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">#</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="@" data-scope-types="[&quot;&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>organizations, repositories,</strong> and <strong>users</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">@</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="!" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>projects</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">!</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="/" data-scope-types="[&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search for <strong>files</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">/</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="modes_help" data-prefix="&gt;" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Activate <strong>command mode</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">&gt;</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# author:@me" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search your issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># author:@me</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# author:@me" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Search your issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># author:@me</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:pr" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to pull requests</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:pr</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:issue" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to issues</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:issue</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:discussion" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:discussion</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:project" data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to projects</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:project</kbd>
              </span>
          </command-palette-help>
          <command-palette-help data-group="filters_help" data-prefix="# is:open" data-scope-types="" data-catalyst="" hidden="">
            <span data-target="command-palette-help.titleElement">Filter to open issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:open</kbd>
              </span>
          </command-palette-help>
      </server-defined-provider>

        <server-defined-provider data-type="commands" data-fetch-debounce="0" data-src="/command_palette/commands" data-supported-modes="[]" data-supports-commands="" data-targets="command-palette.serverDefinedProviderElements" data-supported-scope-types="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="prefetched" data-fetch-debounce="0" data-src="/command_palette/jump_to_page_navigation" data-supported-modes="[&quot;&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/issues" data-supported-modes="[&quot;#&quot;,&quot;#&quot;]" data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;,&quot;&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/jump_to" data-supported-modes="[&quot;@&quot;,&quot;@&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/jump_to_members_only" data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="prefetched" data-fetch-debounce="0" data-src="/command_palette/jump_to_members_only_prefetched" data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="files" data-fetch-debounce="0" data-src="/command_palette/files" data-supported-modes="[&quot;/&quot;]" data-supported-scope-types="[&quot;repository&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/discussions" data-supported-modes="[&quot;#&quot;]" data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/projects" data-supported-modes="[&quot;#&quot;,&quot;!&quot;]" data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="prefetched" data-fetch-debounce="0" data-src="/command_palette/recent_issues" data-supported-modes="[&quot;#&quot;,&quot;#&quot;]" data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;,&quot;&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/teams" data-supported-modes="[&quot;@&quot;,&quot;&quot;]" data-supported-scope-types="[&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
        <server-defined-provider data-type="remote" data-fetch-debounce="200" data-src="/command_palette/name_with_owner_repository" data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]" data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]" data-targets="command-palette.serverDefinedProviderElements" data-supports-commands="" data-catalyst=""></server-defined-provider>
    <client-defined-provider data-catalyst="" data-provider-id="main-window-commands-provider" data-targets="command-palette.clientDefinedProviderElements"></client-defined-provider></command-palette>
  </details-dialog>
</details>

<div class="position-fixed bottom-0 left-0 ml-5 mb-5 js-command-palette-toasts" style="z-index: 1000">
  <div hidden="" class="Toast Toast--loading">
    <span class="Toast-icon">
      <svg class="Toast--spinner" viewBox="0 0 32 32" width="18" height="18" aria-hidden="true">
        <path fill="#959da5" d="M16 0 A16 16 0 0 0 16 32 A16 16 0 0 0 16 0 M16 4 A12 12 0 0 1 16 28 A12 12 0 0 1 16 4"></path>
        <path fill="#ffffff" d="M16 0 A16 16 0 0 1 32 16 L28 16 A12 12 0 0 0 16 4z"></path>
      </svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden="" class="anim-fade-in fast Toast Toast--error">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden="" class="anim-fade-in fast Toast Toast--warning">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>


  <div hidden="" class="anim-fade-in fast Toast Toast--success">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden="" class="anim-fade-in fast Toast">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-info">
    <path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM6.5 7.75A.75.75 0 0 1 7.25 7h1a.75.75 0 0 1 .75.75v2.75h.25a.75.75 0 0 1 0 1.5h-2a.75.75 0 0 1 0-1.5h.25v-2h-.25a.75.75 0 0 1-.75-.75ZM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>
</div>


  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
      
    

    

      <div class="flash flash-warn flash-full border-top-0 text-center text-bold py-2">
    This repository has been archived by the owner on Jul 14, 2023. It is now read-only.
  </div>






    
  <div id="repository-container-header" data-turbo-replace="" hidden=""></div>




<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content ">
      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".,Mod+Alt+.">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+.,Shift+&gt;,&gt;" target="_blank" rel="noopener noreferrer">Open in a new github.dev tab</a>
    <a class="d-none" data-hotkey=",,Mod+Alt+," target="_blank" href="https://github.com/codespaces/new/Azure/Hangman/tree/master?resume=1">Open in codespace</a>



    
      
    





<react-app app-name="react-code-view" initial-path="/Azure/Hangman/blob/master/README.md" style="min-height: calc(100vh - 64px)" data-ssr="true" data-lazy="false" data-alternate="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"allShortcutsEnabled":true,"fileTree":{"":{"items":[{"name":"images","path":"images","contentType":"directory"},{"name":"webapp","path":"webapp","contentType":"directory"},{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":"LICENSE","path":"LICENSE","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"Train a Neural Network to Play Hangman.ipynb","path":"Train a Neural Network to Play Hangman.ipynb","contentType":"file"}],"totalCount":6}},"fileTreeProcessingTime":1.7170969999999999,"foldersToFetch":[],"repo":{"id":91612665,"defaultBranch":"master","name":"Hangman","ownerLogin":"Azure","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2017-05-18T00:56:47.000+05:30","ownerAvatar":"https://avatars.githubusercontent.com/u/6844498?v=4","public":true,"private":false,"isOrgOwned":true},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1495049208.0","canEdit":true,"refType":"branch","currentOid":"5ce0b9674e7fcd13ca938b33daedd40caa02278b"},"path":"README.md","currentUser":{"id":86071546,"login":"upendragoud","userEmail":"upendra8sai7@gmail.com"},"blob":{"rawLines":null,"stylingDirectives":null,"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/Azure/Hangman/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false},"displayName":"README.md","displayUrl":"https://github.com/Azure/Hangman/blob/master/README.md?raw=true","headerInfo":{"blobSize":"9.84 KB","deleteTooltip":"Fork this repository and delete the file","editTooltip":"Fork this repository and edit the file","deleteInfo":{"deleteTooltip":"Fork this repository and delete the file"},"editInfo":{"editTooltip":"Fork this repository and edit the file"},"ghDesktopPath":"https://desktop.github.com","isGitLfs":false,"gitLfsPath":null,"onBranch":true,"shortPath":"7031c98","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FAzure%2FHangman%2Fblob%2Fmaster%2FREADME.md","isCSV":false,"isRichtext":true,"toc":[{"level":1,"text":"Play Hangman with CNTK","anchor":"play-hangman-with-cntk","htmlText":"Play Hangman with CNTK"},{"level":2,"text":"Outline","anchor":"outline","htmlText":"Outline"},{"level":2,"text":"Training","anchor":"training","htmlText":"Training"},{"level":3,"text":"Prerequisites","anchor":"prerequisites","htmlText":"Prerequisites"},{"level":3,"text":"Sample code (contained in Jupyter Notebook)","anchor":"sample-code-contained-in-jupyter-notebook","htmlText":"Sample code (contained in Jupyter Notebook)"},{"level":2,"text":"Operationalization","anchor":"operationalization","htmlText":"Operationalization"},{"level":3,"text":"Prerequisites","anchor":"prerequisites-1","htmlText":"Prerequisites"},{"level":3,"text":"Deploying an Azure Web App","anchor":"deploying-an-azure-web-app","htmlText":"Deploying an Azure Web App"},{"level":3,"text":"Web App Setup","anchor":"web-app-setup","htmlText":"Web App Setup"},{"level":4,"text":"Install the Python 3.5.4 x64 Extension","anchor":"install-the-python-354-x64-extension","htmlText":"Install the Python 3.5.4 x64 Extension"},{"level":4,"text":"Configure Local Git Deployment","anchor":"configure-local-git-deployment","htmlText":"Configure Local Git Deployment"},{"level":3,"text":"Playing Hangman","anchor":"playing-hangman","htmlText":"Playing Hangman"},{"level":2,"text":"Contributing","anchor":"contributing","htmlText":"Contributing"}],"lineInfo":{"truncatedLoc":"132","truncatedSloc":"97"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Markdown","languageID":222,"large":false,"loggedIn":true,"planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/Azure/Hangman/blob/master/README.md","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/Azure/Hangman/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/Azure/Hangman/raw/master/README.md","renderImageOrRaw":false,"richText":"\u003carticle class=\"markdown-body entry-content container-lg\" itemprop=\"text\"\u003e\u003ch1 tabindex=\"-1\" dir=\"auto\"\u003e\u003ca id=\"user-content-play-hangman-with-cntk\" class=\"anchor\" aria-hidden=\"true\" tabindex=\"-1\" href=\"#play-hangman-with-cntk\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003ePlay Hangman with CNTK\u003c/h1\u003e\n\u003cp dir=\"auto\"\u003eby Mary Wahl, Shaheen Gauher, Fidan Boylu Uz, Katherine Zhao\u003c/p\u003e\n\u003cp align=\"center\" dir=\"auto\"\u003e\u003ca target=\"_blank\" rel=\"noopener noreferrer\" href=\"/Azure/Hangman/blob/master/images/screenshot.PNG\"\u003e\u003cimg src=\"/Azure/Hangman/raw/master/images/screenshot.PNG\" width=\"400px\" style=\"max-width: 100%;\"\u003e\u003c/a\u003e\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eIn the classic children's game of Hangman, a player's objective is to identify a hidden word of which only the number of letters is originally revealed. In each round, the player guesses a letter of the alphabet: if it's present in the word, all instances are revealed; otherwise one of the hangman's body parts is drawn in on a gibbet. The game ends in a win if the word is entirely revealed by correct guesses, and ends in loss if the hangman's body is completely revealed instead. To assist the player, a visible record of all guessed letters is typically maintained.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eFor this project, we trained a neural network to play Hangman by appropriately guessing letters in a partially or fully obscured word. The network receives as input a representation of the word (total number of characters, the identity of any revealed letters) as well as a list of which letters have been guessed so far. It returns a guess for the letter that should be picked next. This repo shows our method for training the network with Microsoft's \u003ca href=\"https://github.com/Microsoft/CNTK\"\u003eCognitive Toolkit (CNTK)\u003c/a\u003e and validating its performance on a withheld test set, as well as operationalizing the model for gameplay on an Azure Web App.\u003c/p\u003e\n\u003ch2 tabindex=\"-1\" dir=\"auto\"\u003e\u003ca id=\"user-content-outline\" class=\"anchor\" aria-hidden=\"true\" tabindex=\"-1\" href=\"#outline\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003eOutline\u003c/h2\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ca href=\"#train\"\u003eTraining\u003c/a\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ca href=\"#trainprereq\"\u003ePrerequisites\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#traincode\"\u003eSample code (contained in Jupyter Notebook)\u003c/a\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#op\"\u003eOperationalization\u003c/a\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ca href=\"#opprereq\"\u003ePrerequisites\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#deploy\"\u003eDeploying an Azure Web App\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#setup\"\u003eWeb App Setup\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"#gameplay\"\u003ePlaying Hangman\u003c/a\u003e\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003cp dir=\"auto\"\u003eNote that it is not necessary to complete the \"Training\" section before completing the \"Operationalization\" section, as a sample trained model is provided.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003ca name=\"user-content-train\"\u003e\u003c/a\u003e\u003c/p\u003e\n\u003ch2 tabindex=\"-1\" dir=\"auto\"\u003e\u003ca id=\"user-content-training\" class=\"anchor\" aria-hidden=\"true\" tabindex=\"-1\" href=\"#training\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003eTraining\u003c/h2\u003e\n\u003cp dir=\"auto\"\u003e\u003ca name=\"user-content-trainprereq\"\u003e\u003c/a\u003e\u003c/p\u003e\n\u003ch3 tabindex=\"-1\" dir=\"auto\"\u003e\u003ca id=\"user-content-prerequisites\" class=\"anchor\" aria-hidden=\"true\" tabindex=\"-1\" href=\"#prerequisites\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003ePrerequisites\u003c/h3\u003e\n\u003cp dir=\"auto\"\u003eYou will need:\u003c/p\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eA computer with a GPU (such as an Azure NC6 GPU DSVM)\u003c/li\u003e\n\u003cli\u003e\u003ca href=\"https://github.com/Microsoft/CNTK/releases\"\u003eCNTK 2.0 release candidate 2\u003c/a\u003e (or later) installed in an Anaconda Python 3.5 environment able to run Jupyter Notebooks\u003c/li\u003e\n\u003cli\u003eThe \u003ca href=\"http://wordnetcode.princeton.edu/3.0/WordNet-3.0.tar.gz\" rel=\"nofollow\"\u003etarballed version\u003c/a\u003e of Princeton University's \u003ca href=\"http://wordnet.princeton.edu\" rel=\"nofollow\"\u003eWordNet\u003c/a\u003e database, decompressed e.g. uzing \u003ca href=\"http://www.7-zip.org/download.html\" rel=\"nofollow\"\u003e7zip\u003c/a\u003e\u003c/li\u003e\n\u003cli\u003eThe Jupyter notebook contained in the root directory of this repository\u003c/li\u003e\n\u003c/ul\u003e\n\u003cp dir=\"auto\"\u003eNote that the first two requirements can be satisfied by deploying a \"Deep Learning toolkit for the DSVM\" resource on Azure.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003ca name=\"user-content-traincode\"\u003e\u003c/a\u003e\u003c/p\u003e\n\u003ch3 tabindex=\"-1\" dir=\"auto\"\u003e\u003ca id=\"user-content-sample-code-contained-in-jupyter-notebook\" class=\"anchor\" aria-hidden=\"true\" tabindex=\"-1\" href=\"#sample-code-contained-in-jupyter-notebook\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003eSample code (contained in Jupyter Notebook)\u003c/h3\u003e\n\u003cp dir=\"auto\"\u003eLoad the Jupyter notebook -- \u003ccode\u003eTrain a Neural Network to Play Hangman.ipynb\u003c/code\u003e -- from this repository in your CNTK Python 3.5 environment, and follow the instructions inside to complete the training and validation steps.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003ca name=\"user-content-op\"\u003e\u003c/a\u003e\u003c/p\u003e\n\u003ch2 tabindex=\"-1\" dir=\"auto\"\u003e\u003ca id=\"user-content-operationalization\" class=\"anchor\" aria-hidden=\"true\" tabindex=\"-1\" href=\"#operationalization\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003eOperationalization\u003c/h2\u003e\n\u003cp dir=\"auto\"\u003e\u003ca name=\"user-content-opprereq\"\u003e\u003c/a\u003e\u003c/p\u003e\n\u003ch3 tabindex=\"-1\" dir=\"auto\"\u003e\u003ca id=\"user-content-prerequisites-1\" class=\"anchor\" aria-hidden=\"true\" tabindex=\"-1\" href=\"#prerequisites-1\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003ePrerequisites\u003c/h3\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eAn \u003ca href=\"https://azure.microsoft.com/en-us/free/\" rel=\"nofollow\"\u003eAzure subscription\u003c/a\u003e for deploying an Azure Web App resource\u003c/li\u003e\n\u003cli\u003eA cloned or downloaded local copy of this repository\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eWe will refer to the location of this repository on your local computer as \u003ccode\u003e\u0026lt;repo-filepath\u0026gt;\u003c/code\u003e.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003cli\u003eThe command line version of \u003ca href=\"https://git-scm.com/downloads\" rel=\"nofollow\"\u003eGit\u003c/a\u003e installed locally\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003eGit and shell commands will be written for a Windows operating system. However, you may be able to easily adapt these commands for Mac OS/Linux/UNIX.\u003c/li\u003e\n\u003c/ul\u003e\n\u003c/li\u003e\n\u003c/ul\u003e\n\u003cp dir=\"auto\"\u003e\u003ca name=\"user-content-deploy\"\u003e\u003c/a\u003e\u003c/p\u003e\n\u003ch3 tabindex=\"-1\" dir=\"auto\"\u003e\u003ca id=\"user-content-deploying-an-azure-web-app\" class=\"anchor\" aria-hidden=\"true\" tabindex=\"-1\" href=\"#deploying-an-azure-web-app\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003eDeploying an Azure Web App\u003c/h3\u003e\n\u003cp dir=\"auto\"\u003eWe will create an Azure Web App to serve a website containing our neural network. The Web Apps feature of Microsoft Azure App Service is optimized for hosting websites and web applications. To deploy a web app:\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003eLog into \u003ca href=\"https://portal.azure.com\" rel=\"nofollow\"\u003eAzure Portal\u003c/a\u003e.\u003c/li\u003e\n\u003cli\u003eClick the \"+ New\" button at upper-left.\u003c/li\u003e\n\u003cli\u003eIn the search bar, type in \"Web App\" and press Enter.\u003c/li\u003e\n\u003cli\u003eIn the search results, choose the \"Web App\" option published by Microsoft.\u003c/li\u003e\n\u003cli\u003eAfter reading the description in the pane that appears, scroll down and click the \"Create\" button.\u003c/li\u003e\n\u003cli\u003eIn the \"Web App Create\" pane that appears:\n\u003col dir=\"auto\"\u003e\n\u003cli\u003eChoose a unique name for your web app.\u003c/li\u003e\n\u003cli\u003eSelect the appropriate Azure subscription.\u003c/li\u003e\n\u003cli\u003eChoose a resource group for your web app. (We recommend creating a new resource group, so that you can easily delete it and the associated app service plan at the end of this tutorial.)\u003c/li\u003e\n\u003cli\u003eClick on App Service plan. You may choose an existing plan, but we recommend that you create a new one as follows:\n\u003col dir=\"auto\"\u003e\n\u003cli\u003eClick the \"+ Create New\" button.\u003c/li\u003e\n\u003cli\u003eChoose an appropriate name and location for the service plan, then click OK.\u003c/li\u003e\n\u003c/ol\u003e\n\u003c/li\u003e\n\u003cli\u003eClick \"Create\".\u003c/li\u003e\n\u003c/ol\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cp dir=\"auto\"\u003eDeployment may take a few minutes to complete. To monitor deployment, navigate to your resource group by typing its name in the search bar at the top of the Azure Portal website. Refresh until the \"App Service\" resource (your web app) appears in the resource group contents.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003ca name=\"user-content-setup\"\u003e\u003c/a\u003e\u003c/p\u003e\n\u003ch3 tabindex=\"-1\" dir=\"auto\"\u003e\u003ca id=\"user-content-web-app-setup\" class=\"anchor\" aria-hidden=\"true\" tabindex=\"-1\" href=\"#web-app-setup\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003eWeb App Setup\u003c/h3\u003e\n\u003cp dir=\"auto\"\u003eOnce your web app's deployment is complete, navigate to its overview pane (e.g. by clicking on the \"App Service\" resource in your resource group). The steps below will install necessary Python packages on the web app and upload the model files and website code from your local computer.\u003c/p\u003e\n\u003ch4 tabindex=\"-1\" dir=\"auto\"\u003e\u003ca id=\"user-content-install-the-python-354-x64-extension\" class=\"anchor\" aria-hidden=\"true\" tabindex=\"-1\" href=\"#install-the-python-354-x64-extension\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003eInstall the Python 3.5.4 x64 Extension\u003c/h4\u003e\n\u003cp dir=\"auto\"\u003eThe web app comes with Python 2.7 and 3.4 (x86) available by default. We install Python 3.5 x64 to meet the requirements of CNTK.\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003eIn the search bar at the upper left of your web app's overview pane, type in \"Extensions\" and click on the search result.\u003c/li\u003e\n\u003cli\u003eClick the \"+ Add\" button.\u003c/li\u003e\n\u003cli\u003eScroll through the list of extensions to find and click on \"Python 3.5.4 x64\".\u003c/li\u003e\n\u003cli\u003eReview and accept the legal terms by clicking \"OK\".\u003c/li\u003e\n\u003cli\u003eClick \"OK\" to initiate the installation of the extension.\u003c/li\u003e\n\u003cli\u003eAfter a moment, refresh the page to confirm that the extension has installed successfully. (You may receive an Azure notification that the installation timed out even if the install completes successfully.)\u003c/li\u003e\n\u003c/ol\u003e\n\u003ch4 tabindex=\"-1\" dir=\"auto\"\u003e\u003ca id=\"user-content-configure-local-git-deployment\" class=\"anchor\" aria-hidden=\"true\" tabindex=\"-1\" href=\"#configure-local-git-deployment\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003ca href=\"https://docs.microsoft.com/en-us/azure/app-service-web/app-service-deploy-local-git\" rel=\"nofollow\"\u003eConfigure Local Git Deployment\u003c/a\u003e\u003c/h4\u003e\n\u003cp dir=\"auto\"\u003eYou will deploy your app to Azure App Service from a Git repository on your local computer. App Service supports this approach with the Local Git deployment option in the Azure Portal. The first step in this process is to enable the App service app repository.\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003eIn the search bar at the upper left of your web app's overview pane, type in \"Deployment options\" and click on the search result.\u003c/li\u003e\n\u003cli\u003eClick on \"Choose Source\" and select \"Local Git Repository\".\u003c/li\u003e\n\u003cli\u003eIf you have not set up a repository in Azure before, you will need to create login credentials for it. You will see a section that says \"Setup connection\" where you must choose a username and password. You will use them to log into the Azure repository and push changes from your local Git repository.\n\u003col dir=\"auto\"\u003e\n\u003cli\u003eNote that these login credentials are distinct from your github.com account and are used only for logging into Azure repository. They are also different from your Azure subscription credentials.\u003c/li\u003e\n\u003cli\u003eChoose a username and password you will remember: the same login will be automatically associated with local Git deployments on Azure that you create in the future. (Note that you will have the option to change this login in the future.)\u003c/li\u003e\n\u003c/ol\u003e\n\u003c/li\u003e\n\u003cli\u003eClick \"OK\". (There is no need to configure the Performance Test.)\u003c/li\u003e\n\u003cli\u003eFind the Git URL:\n\u003col dir=\"auto\"\u003e\n\u003cli\u003eIn the search bar at the upper left of your web app's overview pane, type in \"Properties\" and click on the search result.\u003c/li\u003e\n\u003cli\u003eCopy the value in the \"GIT URL\" field on the Properties pane and store it locally; you will use this value shortly.\u003c/li\u003e\n\u003c/ol\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cp dir=\"auto\"\u003eOnce the web app is configured, complete the steps below to configure git locally:\u003c/p\u003e\n\u003col dir=\"auto\"\u003e\n\u003cli\u003e(Optional) If you trained your own NN using the Jupyter notebook in this repo and would like to use it on the website, copy your \u003ccode\u003ehangman_model.dnn\u003c/code\u003e file to the folder \u003ccode\u003e\u0026lt;repo-filepath\u0026gt;\\webapp\\models\u003c/code\u003e to overwrite our example model.\u003c/li\u003e\n\u003cli\u003eOpen a command prompt (e.g. by clicking the Windows icon and typing \"cmd\").\u003c/li\u003e\n\u003cli\u003eNavigate to the \u003ccode\u003ewebapp\u003c/code\u003e folder in your local copy of the git repository:\n\u003ccode\u003ecd \u0026lt;repo-filepath\u0026gt;\\webapp\u003c/code\u003e\u003c/li\u003e\n\u003cli\u003eExecute the commands below to create a local git repo and push a commit.\n\u003cdiv class=\"snippet-clipboard-content notranslate position-relative overflow-auto\" data-snippet-clipboard-copy-content=\"git init\ngit remote add azure \u0026lt;git-url-stored-earlier\u0026gt;\ngit add .\ngit commit -m \u0026quot;Install necessary Python packages\u0026quot;\ngit push azure master\"\u003e\u003cpre class=\"notranslate\"\u003e\u003ccode\u003egit init\ngit remote add azure \u0026lt;git-url-stored-earlier\u0026gt;\ngit add .\ngit commit -m \"Install necessary Python packages\"\ngit push azure master\n\u003c/code\u003e\u003c/pre\u003e\u003c/div\u003e\n\u003c/li\u003e\n\u003c/ol\u003e\n\u003cp dir=\"auto\"\u003eYou will be asked to supply the git credentials you chose earlier. By following the steps above you successfully published your app to App Service using Local Git. The push step will take a few minutes to run. When it completes, you have deployed your project and your website is ready for use!\u003c/p\u003e\n\u003cp dir=\"auto\"\u003e\u003ca name=\"user-content-gameplay\"\u003e\u003c/a\u003e\u003c/p\u003e\n\u003ch3 tabindex=\"-1\" dir=\"auto\"\u003e\u003ca id=\"user-content-playing-hangman\" class=\"anchor\" aria-hidden=\"true\" tabindex=\"-1\" href=\"#playing-hangman\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003ePlaying Hangman\u003c/h3\u003e\n\u003cp dir=\"auto\"\u003eTo use your web app, navigate to \u003ccode\u003ehttp://\u0026lt;your web app's resource name\u0026gt;.azurewebsites.net\u003c/code\u003e. After a few seconds of initial loading, you should see a website asking you to choose a secret word for the neural network to guess. You're responsible for remembering the secret word, but you will need to tell the neural network how long the word is.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eAfter specifying the length and clicking Submit, the neural network's first letter guess will be displayed. It's up to you to tell the neural network whether (and if so, where) the letter appears in the word. After providing this feedback, click Submit to begin the next round.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eAfter each round, the neural network's lives remaining is updated, and the neural network makes another guess. Eventually the neural network either guesses the entire word or runs out of lives.\u003c/p\u003e\n\u003ch2 tabindex=\"-1\" dir=\"auto\"\u003e\u003ca id=\"user-content-contributing\" class=\"anchor\" aria-hidden=\"true\" tabindex=\"-1\" href=\"#contributing\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003eContributing\u003c/h2\u003e\n\u003cp dir=\"auto\"\u003eThis project has adopted the \u003ca href=\"https://opensource.microsoft.com/codeofconduct/\" rel=\"nofollow\"\u003eMicrosoft Open Source Code of Conduct\u003c/a\u003e. For more information see the \u003ca href=\"https://opensource.microsoft.com/codeofconduct/faq/\" rel=\"nofollow\"\u003eCode of Conduct FAQ\u003c/a\u003e or contact \u003ca href=\"mailto:opencode@microsoft.com\"\u003eopencode@microsoft.com\u003c/a\u003e with any additional questions or comments.\u003c/p\u003e\n\u003c/article\u003e","renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"Azure","repoName":"Hangman","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"Play Hangman with CNTK","kind":"section_1","ident_start":2,"ident_end":24,"extent_start":0,"extent_end":10076,"fully_qualified_name":"Play Hangman with CNTK","ident_utf16":{"start":{"line_number":0,"utf16_col":2},"end":{"line_number":0,"utf16_col":24}},"extent_utf16":{"start":{"line_number":0,"utf16_col":0},"end":{"line_number":132,"utf16_col":0}}},{"name":"Outline","kind":"section_2","ident_start":1391,"ident_end":1398,"extent_start":1388,"extent_end":1878,"fully_qualified_name":"Outline","ident_utf16":{"start":{"line_number":10,"utf16_col":3},"end":{"line_number":10,"utf16_col":10}},"extent_utf16":{"start":{"line_number":10,"utf16_col":0},"end":{"line_number":24,"utf16_col":0}}},{"name":"Training","kind":"section_2","ident_start":1881,"ident_end":1889,"extent_start":1878,"extent_end":2932,"fully_qualified_name":"Training","ident_utf16":{"start":{"line_number":24,"utf16_col":3},"end":{"line_number":24,"utf16_col":11}},"extent_utf16":{"start":{"line_number":24,"utf16_col":0},"end":{"line_number":43,"utf16_col":0}}},{"name":"Prerequisites","kind":"section_3","ident_start":1925,"ident_end":1938,"extent_start":1921,"extent_end":2640,"fully_qualified_name":"Prerequisites","ident_utf16":{"start":{"line_number":27,"utf16_col":4},"end":{"line_number":27,"utf16_col":17}},"extent_utf16":{"start":{"line_number":27,"utf16_col":0},"end":{"line_number":38,"utf16_col":0}}},{"name":"Sample code (contained in Jupyter Notebook)","kind":"section_3","ident_start":2644,"ident_end":2687,"extent_start":2640,"extent_end":2932,"fully_qualified_name":"Sample code (contained in Jupyter Notebook)","ident_utf16":{"start":{"line_number":38,"utf16_col":4},"end":{"line_number":38,"utf16_col":47}},"extent_utf16":{"start":{"line_number":38,"utf16_col":0},"end":{"line_number":43,"utf16_col":0}}},{"name":"Operationalization","kind":"section_2","ident_start":2935,"ident_end":2953,"extent_start":2932,"extent_end":9723,"fully_qualified_name":"Operationalization","ident_utf16":{"start":{"line_number":43,"utf16_col":3},"end":{"line_number":43,"utf16_col":21}},"extent_utf16":{"start":{"line_number":43,"utf16_col":0},"end":{"line_number":129,"utf16_col":0}}},{"name":"Prerequisites","kind":"section_3","ident_start":2986,"ident_end":2999,"extent_start":2982,"extent_end":3532,"fully_qualified_name":"Prerequisites","ident_utf16":{"start":{"line_number":46,"utf16_col":4},"end":{"line_number":46,"utf16_col":17}},"extent_utf16":{"start":{"line_number":46,"utf16_col":0},"end":{"line_number":54,"utf16_col":0}}},{"name":"Deploying an Azure Web App","kind":"section_3","ident_start":3536,"ident_end":3562,"extent_start":3532,"extent_end":5032,"fully_qualified_name":"Deploying an Azure Web App","ident_utf16":{"start":{"line_number":54,"utf16_col":4},"end":{"line_number":54,"utf16_col":30}},"extent_utf16":{"start":{"line_number":54,"utf16_col":0},"end":{"line_number":75,"utf16_col":0}}},{"name":"Web App Setup","kind":"section_3","ident_start":5036,"ident_end":5049,"extent_start":5032,"extent_end":8875,"fully_qualified_name":"Web App Setup","ident_utf16":{"start":{"line_number":75,"utf16_col":4},"end":{"line_number":75,"utf16_col":17}},"extent_utf16":{"start":{"line_number":75,"utf16_col":0},"end":{"line_number":121,"utf16_col":0}}},{"name":"Install the Python 3.5.4 x64 Extension","kind":"section_4","ident_start":5348,"ident_end":5386,"extent_start":5343,"extent_end":6093,"fully_qualified_name":"Install the Python 3.5.4 x64 Extension","ident_utf16":{"start":{"line_number":79,"utf16_col":5},"end":{"line_number":79,"utf16_col":43}},"extent_utf16":{"start":{"line_number":79,"utf16_col":0},"end":{"line_number":90,"utf16_col":0}}},{"name":"[Configure Local Git Deployment](https://docs.microsoft.com/en-us/azure/app-service-web/app-service-deploy-local-git)","kind":"section_4","ident_start":6098,"ident_end":6215,"extent_start":6093,"extent_end":8875,"fully_qualified_name":"[Configure Local Git Deployment](https://docs.microsoft.com/en-us/azure/app-service-web/app-service-deploy-local-git)","ident_utf16":{"start":{"line_number":90,"utf16_col":5},"end":{"line_number":90,"utf16_col":122}},"extent_utf16":{"start":{"line_number":90,"utf16_col":0},"end":{"line_number":121,"utf16_col":0}}},{"name":"Playing Hangman","kind":"section_3","ident_start":8879,"ident_end":8894,"extent_start":8875,"extent_end":9723,"fully_qualified_name":"Playing Hangman","ident_utf16":{"start":{"line_number":121,"utf16_col":4},"end":{"line_number":121,"utf16_col":19}},"extent_utf16":{"start":{"line_number":121,"utf16_col":0},"end":{"line_number":129,"utf16_col":0}}},{"name":"Contributing","kind":"section_2","ident_start":9726,"ident_end":9738,"extent_start":9723,"extent_end":10076,"fully_qualified_name":"Contributing","ident_utf16":{"start":{"line_number":129,"utf16_col":3},"end":{"line_number":129,"utf16_col":15}},"extent_utf16":{"start":{"line_number":129,"utf16_col":0},"end":{"line_number":132,"utf16_col":0}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/Azure/Hangman/branches":{"post":"30at2eTkitS6mKR-jp0LZEpXr_XoUbt9x028DyxFTZVMYXLsFLKJ0jq_wCLOlIpw353uOvwTVVdTASnzjmAsyQ"},"/repos/preferences":{"post":"79BbQySM4y7cx8wnP1pa8GrocJiFnsVAomzVBO0-CBUvx235Q8NX1drVt-2rzEtbXu03_MvEELLNgsseDJ7WJg"}}},"title":"Hangman/README.md at master · Azure/Hangman","appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-32bb159cc57c.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-c6704d501c10.js","githubDevUrl":"https://github.dev/","enabled_features":{"code_nav_ui_events":false,"copilot_conversational_ux":false,"copilot_conversational_ux_embedding_update":false,"copilot_popover_file_editor_header":true,"copilot_smell_icebreaker_ux":true,"copilot_workspace":false,"codeview_firefox_inert":true}}}</script>
  <div data-target="react-app.reactRoot"><meta data-hydrostats="publish"> <!-- --> <!-- --> <!-- --> <button hidden="" data-testid="header-permalink-button" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="y,Shift+Y"></button><button hidden="" data-hotkey="y,Shift+Y"></button><div class="Box-sc-g0xbh4-0"><div style="--sticky-pane-height: calc(100vh - (max(0px, 0px)));" class="Box-sc-g0xbh4-0 fSWWem"><div class="Box-sc-g0xbh4-0 kPPmzM"><div class="Box-sc-g0xbh4-0 cIAPDV"><div tabindex="0" class="Box-sc-g0xbh4-0 gvCnwW"><div class="Box-sc-g0xbh4-0 xEgty"><div class="Box-sc-g0xbh4-0 eUyHuk"></div><div style="--pane-width:320px" class="Box-sc-g0xbh4-0 gNdDUH"><div class="Box-sc-g0xbh4-0"><div id="repos-file-tree" class="Box-sc-g0xbh4-0 jyDQiw"><div class="Box-sc-g0xbh4-0 hBSSUC"><div class="Box-sc-g0xbh4-0 iPurHz"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 fNPcqd"><span role="tooltip" aria-label="Collapse file tree" id="expand-button-file-tree-button" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-se"><button data-component="IconButton" type="button" data-testid="collapse-file-tree-button" aria-labelledby="expand-button-file-tree-button" aria-expanded="true" aria-controls="repos-file-tree" class="types__StyledButton-sc-ws60qy-0 khvnOK" data-no-visuals="true" data-hotkey="Control+b"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button></span><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+b"></button></h2><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 imcwCi">Files</h2></div><div class="Box-sc-g0xbh4-0 hVHHYa"><div class="Box-sc-g0xbh4-0 idZfsJ"><button type="button" id="branch-picker-repos-header-ref-selector" aria-haspopup="true" tabindex="0" aria-label="master branch" data-testid="anchor-button" class="types__StyledButton-sc-ws60qy-0 kkhncB react-repos-tree-pane-ref-selector width-full ref-selector-class" data-hotkey="w"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text"><div class="Box-sc-g0xbh4-0 bKgizp"><div class="Box-sc-g0xbh4-0 dIAShY"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="Box-sc-g0xbh4-0 caeYDk ref-selector-button-text-container"><span class="Text-sc-17v1xeu-0 bOMzPg">&nbsp;<!-- -->master</span></div></div></span><span data-component="trailingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="w"></button></div><div class="Box-sc-g0xbh4-0 jahcnb"><span role="tooltip" aria-label="Add file" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-s"><a sx="[object Object]" data-component="IconButton" type="button" aria-label="Add file" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 kQvhRC" href="https://github.com/Azure/Hangman/new/master"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></a></span><button data-component="IconButton" type="button" aria-label="Search this repository" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 bPGRMc" data-hotkey="/"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="/"></button></div></div></div><div class="Box-sc-g0xbh4-0 jRttMj"><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="t,Shift+T"></button><button hidden="" data-hotkey="t,Shift+T"></button><span class="TextInputWrapper__TextInputBaseWrapper-sc-1mqhpbi-0 TextInputWrapper-sc-1mqhpbi-1 bkmibs jxgrJS TextInput-wrapper" aria-busy="false"><span class="TextInput-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autocorrect="off" spellcheck="false" placeholder="Go to file" data-component="input" class="UnstyledTextInput-sc-14ypya-0 cDLBls" value=""><span class="TextInput-icon"><div class="Box-sc-g0xbh4-0 cNvKlH"><kbd>t</kbd></div></span></span></div><div class="Box-sc-g0xbh4-0 bYLCoz"><div><div class="react-tree-show-tree-items"><div data-testid="repos-file-tree-container" class="Box-sc-g0xbh4-0 erWCJP"><nav aria-label="File Tree Navigation"><span role="status" aria-live="polite" aria-atomic="true" class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs"></span><ul role="tree" aria-label="Files" class="TreeView__UlBox-sc-4ex6b6-0 dcpVHE"><li class="PRIVATE_TreeView-item" tabindex="-1" id="images-item" role="treeitem" aria-labelledby=":r0:" aria-describedby=":r1: :r2:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":r0:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":r1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>images</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="webapp-item" role="treeitem" aria-labelledby=":r3:" aria-describedby=":r4: :r5:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":r3:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":r4:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>webapp</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id=".gitignore-item" role="treeitem" aria-labelledby=":r6:" aria-describedby=":r7: :r8:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r6:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":r7:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>.gitignore</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="LICENSE-item" role="treeitem" aria-labelledby=":r9:" aria-describedby=":ra: :rb:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r9:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":ra:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>LICENSE</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="README.md-item" role="treeitem" aria-labelledby=":rc:" aria-describedby=":rd: :re:" aria-level="1" aria-current="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":rc:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":rd:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>README.md</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="Train a Neural Network to Play Hangman.ipynb-item" role="treeitem" aria-labelledby=":rf:" aria-describedby=":rg: :rh:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":rf:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":rg:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>Train a Neural Network to Play Hangman.ipynb</span></span></div></div></li></ul></nav></div></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0 jzJYzB"><div role="slider" aria-label="Draggable pane splitter" aria-valuemin="256" aria-valuemax="577" aria-valuenow="320" aria-valuetext="Pane width 320 pixels" tabindex="0" class="Box-sc-g0xbh4-0 bTSsYt"></div></div></div></div><div class="Box-sc-g0xbh4-0 emFMJu"><div class="Box-sc-g0xbh4-0"></div><div class="Box-sc-g0xbh4-0 hlUAHL"><div data-selector="repos-split-pane-content" tabindex="0" class="Box-sc-g0xbh4-0 iStsmI"><div class="Box-sc-g0xbh4-0 eIgvIk"><div class="Box-sc-g0xbh4-0 eVFfWF container"><div class="Box-sc-g0xbh4-0 kgXdnT react-code-view-header--narrow"><div class="Box-sc-g0xbh4-0 kzTa-dF"><div class="Box-sc-g0xbh4-0 bbXCl"><div class="Box-sc-g0xbh4-0 kIpapQ"><div class="Box-sc-g0xbh4-0 eTvGbF"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb-mobile-heading" id="repos-header-breadcrumb-mobile" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="repos-header-breadcrumb-mobile-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 dpowyu" href="https://github.com/Azure/Hangman/tree/master">Hangman</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 ePvrxx">/</span><h1 tabindex="-1" id="file-name-id-mobile" class="Heading__StyledHeading-sc-1c1dgg0-0 diwsLq">README.md</h1></div><button data-component="IconButton" type="button" aria-label="Copy path" data-testid="breadcrumb-copy-path-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 IIGly"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div><div class="Box-sc-g0xbh4-0 hGGMNu"> <button hidden="" data-testid="" data-hotkey="l,Shift+L" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="l,Shift+L"></button><button hidden="" data-testid="" data-hotkey="Mod+Alt+g" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Mod+Alt+g"></button><button type="button" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 bzquEC" data-hotkey="b,Shift+B,Control+/ Control+b"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="b,Shift+B,Control+/ Control+b"></button><button data-component="IconButton" type="button" aria-label="More file actions" class="types__StyledButton-sc-ws60qy-0 ecnbuT js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button-nav-menu-narrow" id=":R159badaj5:" aria-haspopup="true" tabindex="0" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button> </div></div></div></div><div id="StickyHeader" class="Box-sc-g0xbh4-0 bDwCYs react-code-view-header--wide"><div class="Box-sc-g0xbh4-0 fywjmm"><div class="Box-sc-g0xbh4-0 dyczTK"><div class="Box-sc-g0xbh4-0 kszRgZ"><div class="Box-sc-g0xbh4-0 eTvGbF"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb-wide-heading" id="repos-header-breadcrumb-wide" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="repos-header-breadcrumb-wide-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 dpowyu" href="https://github.com/Azure/Hangman/tree/master">Hangman</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 ePvrxx">/</span><h1 tabindex="-1" id="file-name-id-wide" class="Heading__StyledHeading-sc-1c1dgg0-0 diwsLq">README.md</h1></div><button data-component="IconButton" type="button" aria-label="Copy path" data-testid="breadcrumb-copy-path-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 IIGly"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div><div class="Box-sc-g0xbh4-0 gtBUEp"><div class="d-flex gap-2"> <button hidden="" data-testid="" data-hotkey="l,Shift+L" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="l,Shift+L"></button><button hidden="" data-testid="" data-hotkey="Mod+Alt+g" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Mod+Alt+g"></button><button type="button" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 bzquEC" data-hotkey="b,Shift+B,Control+/ Control+b"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="b,Shift+B,Control+/ Control+b"></button><button data-component="IconButton" type="button" aria-label="More file actions" class="types__StyledButton-sc-ws60qy-0 ecnbuT js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button-nav-menu-wide" id=":R176jadaj5:" aria-haspopup="true" tabindex="0" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button> </div></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0 hVZtwF react-code-view-bottom-padding"> <div class="Box-sc-g0xbh4-0 cMYnca"></div><div class="Box-sc-g0xbh4-0"></div> <!-- --> <!-- --> </div><div class="Box-sc-g0xbh4-0 hVZtwF"> <!-- --> <!-- --> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="r,Shift+R"></button><button hidden="" data-hotkey="r,Shift+R"></button><div class="Box-sc-g0xbh4-0 dPsqPZ"><div class="Box-sc-g0xbh4-0 eYedVD"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">Latest commit</h2><div data-testid="latest-commit" class="Box-sc-g0xbh4-0 drtGBr"><div class="Box-sc-g0xbh4-0 eScEiW"><div data-testid="author-avatar" class="Box-sc-g0xbh4-0 hLLhje"><a href="https://github.com/mawah" data-testid="avatar-icon-link" data-hovercard-url="/users/mawah/hovercard" class="Link__StyledLink-sc-14289xe-0 elltiT"><img alt="mawah" size="20" src="./README_files/17458994" data-testid="github-avatar" aria-label="mawah" height="20" width="20" class="Avatar__StyledAvatar-sc-2lv0r8-0 gMUnCp"></a><span role="tooltip" aria-label="commits by mawah" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-se"><a href="https://github.com/Azure/Hangman/commits?author=mawah" aria-label="commits by mawah" data-hovercard-url="/users/mawah/hovercard" class="Link__StyledLink-sc-14289xe-0 fcwTtW">mawah</a></span></div><span class="Box-sc-g0xbh4-0"></span></div><div class="Box-sc-g0xbh4-0 fqNQBl react-last-commit-message"><div class="Box-sc-g0xbh4-0 jEKUjt Truncate"><span class="Text-sc-17v1xeu-0 gPDEWA Truncate-text" data-testid="latest-commit-html"><a href="https://github.com/Azure/Hangman/commit/19eea44f537d384a429c178c9b52c87fec579215" class="Link--secondary" title="Updated README instructions to Python 3.5.4

There is no longer an option to install the &quot;Python 3.5.3 x64&quot; extension; it has been replaced by a corresponding 3.5.4 option. This is likely to break the install script since the name of the Python folder will doubtlessly be different now (repo updates to follow)." data-pjax="true" data-hovercard-url="/Azure/Hangman/commit/19eea44f537d384a429c178c9b52c87fec579215/hovercard">Updated README instructions to Python 3.5.4</a></span></div><button data-component="IconButton" type="button" aria-label="Open commit details" aria-pressed="false" aria-expanded="false" data-testid="latest-commit-details-toggle" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 jMpcER"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-ellipsis" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M0 5.75C0 4.784.784 4 1.75 4h12.5c.966 0 1.75.784 1.75 1.75v4.5A1.75 1.75 0 0 1 14.25 12H1.75A1.75 1.75 0 0 1 0 10.25ZM12 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2ZM7 8a1 1 0 1 0 2 0 1 1 0 0 0-2 0ZM4 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2Z"></path></svg></button></div><span class="Text-sc-17v1xeu-0 gApqUp react-last-commit-summary-timestamp"><relative-time class="RelativeTime-sc-lqbqy3-0" datetime="2017-11-02T10:53:57.000-07:00" tense="past" title="Nov 2, 2017, 11:23 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></span></div><div class="Box-sc-g0xbh4-0 jGfYmh"><div data-testid="latest-commit-details" class="Box-sc-g0xbh4-0 lhFvfi"><span class="Text-sc-17v1xeu-0 gApqUp react-last-commit-oid-timestamp"><a class="Link__StyledLink-sc-14289xe-0 elltiT Link--secondary" aria-label="Commit 19eea44" href="https://github.com/Azure/Hangman/commit/19eea44f537d384a429c178c9b52c87fec579215">19eea44</a>&nbsp;·&nbsp;<relative-time class="RelativeTime-sc-lqbqy3-0" datetime="2017-11-02T10:53:57.000-07:00" tense="past" title="Nov 2, 2017, 11:23 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></span><span class="Text-sc-17v1xeu-0 gApqUp react-last-commit-timestamp"><relative-time class="RelativeTime-sc-lqbqy3-0" datetime="2017-11-02T10:53:57.000-07:00" tense="past" title="Nov 2, 2017, 11:23 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></span></div><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">History</h2><a class="types__StyledButton-sc-ws60qy-0 saA-Dg react-last-commit-history-group" href="https://github.com/Azure/Hangman/commits/master/README.md" data-size="small"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text"><span class="Text-sc-17v1xeu-0 UrHoN">History</span></span></span></a><div class="Box-sc-g0xbh4-0 bqgLjk"><button data-component="IconButton" type="button" aria-label="Open commit details" aria-pressed="false" aria-expanded="false" data-testid="latest-commit-details-toggle" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 kiFJWH"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-ellipsis" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M0 5.75C0 4.784.784 4 1.75 4h12.5c.966 0 1.75.784 1.75 1.75v4.5A1.75 1.75 0 0 1 14.25 12H1.75A1.75 1.75 0 0 1 0 10.25ZM12 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2ZM7 8a1 1 0 1 0 2 0 1 1 0 0 0-2 0ZM4 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2Z"></path></svg></button></div><span role="tooltip" aria-label="Commit history" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a class="types__StyledButton-sc-ws60qy-0 saA-Dg react-last-commit-history-icon" href="https://github.com/Azure/Hangman/commits/master/README.md"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a></span></div></div></div><div class="Box-sc-g0xbh4-0 iJmJly"><div class="Box-sc-g0xbh4-0 jACbi container"><div class="Box-sc-g0xbh4-0 gIJuDf react-code-size-details-banner"><div class="Box-sc-g0xbh4-0 fleZSW react-code-size-details-banner"><div class="Box-sc-g0xbh4-0 dVVHlo text-mono"><div title="9.84 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 fUpWeN"><span class="Text-sc-17v1xeu-0 gPDEWA">132 lines (97 loc) · 9.84 KB</span></div></div></div></div><div class="Box-sc-g0xbh4-0 VHzRk react-blob-view-header-sticky" id="repos-sticky-header"><div class="Box-sc-g0xbh4-0 ePiodO"><div class="Box-sc-g0xbh4-0 react-blob-sticky-header"><div class="Box-sc-g0xbh4-0 kQJlnf"><div class="Box-sc-g0xbh4-0 gJICKO"><div class="Box-sc-g0xbh4-0 iZJewz"><nav data-testid="breadcrumbs" aria-labelledby="sticky-breadcrumb-heading" id="sticky-breadcrumb" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="sticky-breadcrumb-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 dpowyu" href="https://github.com/Azure/Hangman/tree/master">Hangman</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 fQxKLn">/</span><h1 tabindex="-1" id="sticky-file-name-id" class="Heading__StyledHeading-sc-1c1dgg0-0 jAEDJk">README.md</h1></div></div><button type="button" data-size="small" class="types__StyledButton-sc-ws60qy-0 ecGgfP" style="--button-color: fg.default;"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-arrow-up" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M3.47 7.78a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0l4.25 4.25a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018L9 4.81v7.44a.75.75 0 0 1-1.5 0V4.81L4.53 7.78a.75.75 0 0 1-1.06 0Z"></path></svg></span><span data-component="text">Top</span></span></button></div></div></div><div class="Box-sc-g0xbh4-0 jtQniD"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">File metadata and controls</h2><div class="Box-sc-g0xbh4-0 bfkNRF"><ul aria-label="File view" class="SegmentedControl__SegmentedControlList-sc-1rzig82-0 dlXtLG"><li class="Box-sc-g0xbh4-0 illvPQ"><button aria-current="false" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 hyYJNu" data-hotkey="Control+/ Control+p"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Preview</div></span></button></li><li class="Box-sc-g0xbh4-0 fXBLEV"><button aria-current="false" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 lfqhlR" data-hotkey="Control+/ Control+c"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Code</div></span></button></li><li class="Box-sc-g0xbh4-0 fXBLEV"><button aria-current="true" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 hINtWo" data-hotkey="b,Shift+B,Control+/ Control+b"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Blame</div></span></button></li></ul><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+/ Control+c"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="b,Shift+B,Control+/ Control+b"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+/ Control+p"></button><div class="Box-sc-g0xbh4-0 fleZSW react-code-size-details-in-header"><div class="Box-sc-g0xbh4-0 dVVHlo text-mono"><div title="9.84 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 fUpWeN"><span class="Text-sc-17v1xeu-0 gPDEWA">132 lines (97 loc) · 9.84 KB</span></div></div></div></div><div class="Box-sc-g0xbh4-0 iBylDf"><button hidden="" data-testid="" data-hotkey="Control+Shift+&gt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+Shift+&gt;"></button><button hidden="" data-testid="" data-hotkey="Control+Shift+&lt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+Shift+&lt;"></button><div class="Box-sc-g0xbh4-0 kSGBPx react-blob-header-edit-and-raw-actions"><div class="ButtonGroup-sc-1gxhls1-0 cjbBGq"><a href="https://github.com/Azure/Hangman/raw/master/README.md" data-testid="raw-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 ctvgFa" data-hotkey="Control+/ Control+r"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Raw</span></span></a><button data-component="IconButton" type="button" aria-label="Copy raw content" data-testid="copy-raw-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 iqlNQz" data-hotkey="Control+Shift+C"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span role="tooltip" aria-label="Download raw file" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><button data-component="IconButton" type="button" aria-label="Download raw content" data-testid="download-raw-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 jKmxIb" data-hotkey="Control+Shift+S"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-download" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path></svg></button></span></div><button hidden="" data-testid="raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+/ Control+r"></button><button hidden="" data-testid="copy-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+Shift+C"></button><button hidden="" data-testid="download-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+Shift+S"></button><a class="Link__StyledLink-sc-14289xe-0 elltiT js-github-dev-shortcut d-none" href="https://github.dev/" data-hotkey="., Control+Shift+/"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="., Control+Shift+/"></button><a class="Link__StyledLink-sc-14289xe-0 elltiT js-github-dev-new-tab-shortcut d-none" href="https://github.dev/" target="_blank" data-hotkey="Shift+.,Shift+&gt;,&gt;"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Shift+.,Shift+&gt;,&gt;"></button><div class="ButtonGroup-sc-1gxhls1-0 cjbBGq"><span role="tooltip" aria-label="Fork this repository and edit the file" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-nw"><a sx="[object Object]" data-component="IconButton" type="button" aria-label="Edit file" data-testid="edit-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 iwejsh" href="https://github.com/Azure/Hangman/edit/master/README.md" data-hotkey="e,Shift+E"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-pencil" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg></a></span><button data-component="IconButton" type="button" aria-label="More edit options" data-testid="more-edit-button" id=":R2l76faladaj5:" aria-haspopup="true" tabindex="0" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 iqlNQz"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></button></div><button hidden="" data-testid="" data-hotkey="e,Shift+E" data-hotkey-scope="read-only-cursor-text-area"></button></div><div class="Box-sc-g0xbh4-0 react-blob-header-edit-and-raw-actions-combined"><button data-component="IconButton" type="button" aria-label="Edit and raw actions" class="types__StyledButton-sc-ws60qy-0 htXhGX js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button" id=":R5v6faladaj5:" aria-haspopup="true" tabindex="0" data-size="small" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button></div></div></div><div class="Box-sc-g0xbh4-0 FRLwL"><div aria-hidden="true" class="Box-sc-g0xbh4-0 cUJqaS"><span class="Text-sc-17v1xeu-0 bjnPpC">Older</span><div class="Box-sc-g0xbh4-0 foLYBW"></div><div class="Box-sc-g0xbh4-0 hvzlSB"></div><div class="Box-sc-g0xbh4-0 gIqhRZ"></div><div class="Box-sc-g0xbh4-0 dvApMy"></div><div class="Box-sc-g0xbh4-0 xnNTv"></div><div class="Box-sc-g0xbh4-0 euKlJB"></div><div class="Box-sc-g0xbh4-0 gEFlzv"></div><div class="Box-sc-g0xbh4-0 gEFlzv"></div><div class="Box-sc-g0xbh4-0 jGGDPa"></div><div class="Box-sc-g0xbh4-0 SBuFJ"></div><span class="Text-sc-17v1xeu-0 duiuMl">Newer</span></div><div class="Box-sc-g0xbh4-0 hLLhje"><div class="Box-sc-g0xbh4-0 iJmJly"><span class="AvatarStack__AvatarStackWrapper-sc-4pdg6v-0 fkMmDD pc-AvatarStack--three"><div class="Box-sc-g0xbh4-0 pc-AvatarStackBody"> <img alt="mawah" size="20" src="./README_files/17458994(1)" data-testid="contributor-avatar" class="Avatar__StyledAvatar-sc-2lv0r8-0 bYzzMi AvatarShowMedium pc-AvatarItem" data-hovercard-url="/users/mawah/hovercard" height="20" width="20"><img alt="microsoftopensource" size="20" src="./README_files/22527892" data-testid="contributor-avatar" class="Avatar__StyledAvatar-sc-2lv0r8-0 bYzzMi AvatarShowMedium pc-AvatarItem" data-hovercard-url="/users/microsoftopensource/hovercard" height="20" width="20"><img alt="shaheeng" size="20" src="./README_files/10565021" data-testid="contributor-avatar" class="Avatar__StyledAvatar-sc-2lv0r8-0 bYzzMi AvatarShowMedium pc-AvatarItem" data-hovercard-url="/users/shaheeng/hovercard" height="20" width="20"></div></span></div><button aria-label="Show 3 contributors&quot;" data-testid="contributors-count-button" class="Link__StyledLink-sc-14289xe-0 hhEmJv"><svg aria-hidden="true" focusable="false" role="img" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"></path></svg><span class="Text-sc-17v1xeu-0 fppCuG react-contributors-title">Contributors</span><span aria-hidden="true" class="Box-sc-g0xbh4-0 jhFlKe">3</span><span class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs">&nbsp;(3)</span></button></div></div></div><div class="Box-sc-g0xbh4-0"></div></div><div class="Box-sc-g0xbh4-0 jMJFjm"><section aria-labelledby="file-name-id-wide file-name-id-mobile" class="Box-sc-g0xbh4-0 fGBunA"><div class="Box-sc-g0xbh4-0 axQQh"><div id="highlighted-line-menu-positioner" class="position-relative"><div id="copilot-button-positioner" class="Box-sc-g0xbh4-0 cluMzC"><div class="Box-sc-g0xbh4-0 fLcwut"><div data-hpc="true" class="Box-sc-g0xbh4-0 hhiQMR"><div class="react-blame-segment-wrapper" style="transform: translateY(0px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T14:26:23.000Z" tense="past" title="May 26, 2017, 7:56 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/97be13f9fadc71166d144690d62b9e8102af7e8c/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Begin to add web app and readme

- Added web app files (excluding wheels and CNTK files) to the
repository
- Added setup steps through web app deployment to README
TODO: update deploy.cmd to download wheels and CNTK files from blob
storage." class="color-fg-default" href="https://github.com/Azure/Hangman/commit/97be13f9fadc71166d144690d62b9e8102af7e8c">Begin to add web app and readme</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T14:26:23.000Z" tense="past" title="May 26, 2017, 7:56 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 97be13f, made on 26 May 2017" id="reblame-97be13f" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-97be13f" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/77d21669580b42f2983aba564b1f5c637ab20888/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="1" class="react-line-number react-code-text" style="padding-right: 16px;">1</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC1" class="react-file-line html-div" data-testid="code-cell" data-line-number="1" style="position: relative;"><span class="pl-mh"># <span class="pl-en">Play Hangman with CNTK</span></span></div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(31px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T19:43:31.000Z" tense="past" title="May 18, 2017, 1:13 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/b428ca0ba8ba884f17d4daf395e80112bdf63cf4/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Added info on input data set" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/b428ca0ba8ba884f17d4daf395e80112bdf63cf4">Added info on input data set</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T19:43:31.000Z" tense="past" title="May 18, 2017, 1:13 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change b428ca0, made on 18 May 2017" id="reblame-b428ca0" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-b428ca0" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/54a389cc96e7fe55430913e5752fd6724e8d394b/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="2" class="react-line-number react-code-text" style="padding-right: 16px;">2</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC2" class="react-file-line html-div" data-testid="code-cell" data-line-number="2" style="position: relative;">
</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(62px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-06-02T13:11:37.000Z" tense="past" title="Jun 2, 2017, 6:41 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/56117b94037f636a814ea7e462136e14b242802b/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Update README.md" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/56117b94037f636a814ea7e462136e14b242802b">Update README.md</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-06-02T13:11:37.000Z" tense="past" title="Jun 2, 2017, 6:41 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 56117b9, made on 2 Jun 2017" id="reblame-56117b9" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-56117b9" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/b74c6e511e5de7a30d31a56bfb7dbbdd3548c816/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="3" class="react-line-number react-code-text" style="padding-right: 16px;">3</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC3" class="react-file-line html-div" data-testid="code-cell" data-line-number="3" style="position: relative;">by Mary Wahl, Shaheen Gauher, Fidan Boylu Uz, Katherine Zhao</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(93px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T19:43:31.000Z" tense="past" title="May 18, 2017, 1:13 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/b428ca0ba8ba884f17d4daf395e80112bdf63cf4/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Added info on input data set" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/b428ca0ba8ba884f17d4daf395e80112bdf63cf4">Added info on input data set</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T19:43:31.000Z" tense="past" title="May 18, 2017, 1:13 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change b428ca0, made on 18 May 2017" id="reblame-b428ca0" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-b428ca0" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/54a389cc96e7fe55430913e5752fd6724e8d394b/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="4" class="react-line-number react-code-text" style="padding-right: 16px;">4</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC4" class="react-file-line html-div" data-testid="code-cell" data-line-number="4" style="position: relative;">
</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(124px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-28T15:08:16.000Z" tense="past" title="Jul 28, 2017, 8:38 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/8f67cf42517093054b54eecce025364b255d4443/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Update README.md" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/8f67cf42517093054b54eecce025364b255d4443">Update README.md</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-28T15:08:16.000Z" tense="past" title="Jul 28, 2017, 8:38 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 8f67cf4, made on 28 Jul 2017" id="reblame-8f67cf4" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-8f67cf4" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/42f607dc1d40ab228eb8691fa8846eb8b0270899/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="5" class="react-line-number react-code-text" style="padding-right: 16px;">5</div><div data-line-number="6" class="react-line-number react-code-text" style="padding-right: 16px;">6</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC5" class="react-file-line html-div" data-testid="code-cell" data-line-number="5" style="position: relative;">&lt;<span class="pl-ent">p</span> <span class="pl-e">align</span>=<span class="pl-s">"</span><span class="pl-s">center</span><span class="pl-s">"</span>&gt;&lt;<span class="pl-ent">img</span> <span class="pl-e">src</span>=<span class="pl-s">"</span><span class="pl-s">./images/screenshot.PNG</span><span class="pl-s">"</span> <span class="pl-e">width</span>=<span class="pl-s">"</span><span class="pl-s">400px</span><span class="pl-s">"</span> /&gt;&lt;/<span class="pl-ent">p</span>&gt;</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC6" class="react-file-line html-div" data-testid="code-cell" data-line-number="6" style="position: relative;">
</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(164px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T20:34:00.000Z" tense="past" title="May 18, 2017, 2:04 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/e7aefb91252de649fdfe350b4d8f7d0cc5ded0b9/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Add description and instructions" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/e7aefb91252de649fdfe350b4d8f7d0cc5ded0b9">Add description and instructions</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T20:34:00.000Z" tense="past" title="May 18, 2017, 2:04 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change e7aefb9, made on 18 May 2017" id="reblame-e7aefb9" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-e7aefb9" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/0b9bef44a6c9bc9e8e6c2ce1c9ccea7bac550f64/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="7" class="react-line-number react-code-text" style="padding-right: 16px;">7</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC7" class="react-file-line html-div" data-testid="code-cell" data-line-number="7" style="position: relative;">In the classic children's game of Hangman, a player's objective is to identify a hidden word of which only the number of letters is originally revealed. In each round, the player guesses a letter of the alphabet: if it's present in the word, all instances are revealed; otherwise one of the hangman's body parts is drawn in on a gibbet. The game ends in a win if the word is entirely revealed by correct guesses, and ends in loss if the hangman's body is completely revealed instead. To assist the player, a visible record of all guessed letters is typically maintained.</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(195px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T19:43:31.000Z" tense="past" title="May 18, 2017, 1:13 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/b428ca0ba8ba884f17d4daf395e80112bdf63cf4/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Added info on input data set" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/b428ca0ba8ba884f17d4daf395e80112bdf63cf4">Added info on input data set</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T19:43:31.000Z" tense="past" title="May 18, 2017, 1:13 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change b428ca0, made on 18 May 2017" id="reblame-b428ca0" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-b428ca0" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/54a389cc96e7fe55430913e5752fd6724e8d394b/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="8" class="react-line-number react-code-text" style="padding-right: 16px;">8</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC8" class="react-file-line html-div" data-testid="code-cell" data-line-number="8" style="position: relative;">
</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(226px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T14:26:23.000Z" tense="past" title="May 26, 2017, 7:56 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/97be13f9fadc71166d144690d62b9e8102af7e8c/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Begin to add web app and readme

- Added web app files (excluding wheels and CNTK files) to the
repository
- Added setup steps through web app deployment to README
TODO: update deploy.cmd to download wheels and CNTK files from blob
storage." class="color-fg-default" href="https://github.com/Azure/Hangman/commit/97be13f9fadc71166d144690d62b9e8102af7e8c">Begin to add web app and readme</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T14:26:23.000Z" tense="past" title="May 26, 2017, 7:56 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 97be13f, made on 26 May 2017" id="reblame-97be13f" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-97be13f" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/77d21669580b42f2983aba564b1f5c637ab20888/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="9" class="react-line-number react-code-text" style="padding-right: 16px;">9</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC9" class="react-file-line html-div" data-testid="code-cell" data-line-number="9" style="position: relative;">For this project, we trained a neural network to play Hangman by appropriately guessing letters in a partially or fully obscured word. The network receives as input a representation of the word (total number of characters, the identity of any revealed letters) as well as a list of which letters have been guessed so far. It returns a guess for the letter that should be picked next. This repo shows our method for training the network with Microsoft's <span class="pl-s">[</span>Cognitive Toolkit (CNTK)<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">https://github.com/Microsoft/CNTK</span><span class="pl-s">)</span> and validating its performance on a withheld test set, as well as operationalizing the model for gameplay on an Azure Web App.</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(257px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T20:34:00.000Z" tense="past" title="May 18, 2017, 2:04 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/e7aefb91252de649fdfe350b4d8f7d0cc5ded0b9/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Add description and instructions" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/e7aefb91252de649fdfe350b4d8f7d0cc5ded0b9">Add description and instructions</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T20:34:00.000Z" tense="past" title="May 18, 2017, 2:04 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change e7aefb9, made on 18 May 2017" id="reblame-e7aefb9" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-e7aefb9" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/0b9bef44a6c9bc9e8e6c2ce1c9ccea7bac550f64/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="10" class="react-line-number react-code-text" style="padding-right: 16px;">10</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC10" class="react-file-line html-div" data-testid="code-cell" data-line-number="10" style="position: relative;">
</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(288px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T14:26:23.000Z" tense="past" title="May 26, 2017, 7:56 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/97be13f9fadc71166d144690d62b9e8102af7e8c/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Begin to add web app and readme

- Added web app files (excluding wheels and CNTK files) to the
repository
- Added setup steps through web app deployment to README
TODO: update deploy.cmd to download wheels and CNTK files from blob
storage." class="color-fg-default" href="https://github.com/Azure/Hangman/commit/97be13f9fadc71166d144690d62b9e8102af7e8c">Begin to add web app and readme</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T14:26:23.000Z" tense="past" title="May 26, 2017, 7:56 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 97be13f, made on 26 May 2017" id="reblame-97be13f" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-97be13f" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/77d21669580b42f2983aba564b1f5c637ab20888/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="11" class="react-line-number react-code-text" style="padding-right: 16px;">11</div><div data-line-number="12" class="react-line-number react-code-text" style="padding-right: 16px;">12</div><div data-line-number="13" class="react-line-number react-code-text" style="padding-right: 16px;">13</div><div data-line-number="14" class="react-line-number react-code-text" style="padding-right: 16px;">14</div><div data-line-number="15" class="react-line-number react-code-text" style="padding-right: 16px;">15</div><div data-line-number="16" class="react-line-number react-code-text" style="padding-right: 16px;">16</div><div data-line-number="17" class="react-line-number react-code-text" style="padding-right: 16px;">17</div><div data-line-number="18" class="react-line-number react-code-text" style="padding-right: 16px;">18</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC11" class="react-file-line html-div" data-testid="code-cell" data-line-number="11" style="position: relative;"><span class="pl-mh">## <span class="pl-en">Outline</span></span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC12" class="react-file-line html-div" data-testid="code-cell" data-line-number="12" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC13" class="react-file-line html-div" data-testid="code-cell" data-line-number="13" style="position: relative;"><span class="pl-v">-</span> <span class="pl-s">[</span>Training<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">#train</span><span class="pl-s">)</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC14" class="react-file-line html-div" data-testid="code-cell" data-line-number="14" style="position: relative;">   <span class="pl-v">-</span> <span class="pl-s">[</span>Prerequisites<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">#trainprereq</span><span class="pl-s">)</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC15" class="react-file-line html-div" data-testid="code-cell" data-line-number="15" style="position: relative;">   <span class="pl-v">-</span> <span class="pl-s">[</span>Sample code (contained in Jupyter Notebook)<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">#traincode</span><span class="pl-s">)</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC16" class="react-file-line html-div" data-testid="code-cell" data-line-number="16" style="position: relative;"><span class="pl-v">-</span> <span class="pl-s">[</span>Operationalization<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">#op</span><span class="pl-s">)</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC17" class="react-file-line html-div" data-testid="code-cell" data-line-number="17" style="position: relative;">   <span class="pl-v">-</span> <span class="pl-s">[</span>Prerequisites<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">#opprereq</span><span class="pl-s">)</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC18" class="react-file-line html-div" data-testid="code-cell" data-line-number="18" style="position: relative;">   <span class="pl-v">-</span> <span class="pl-s">[</span>Deploying an Azure Web App<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">#deploy</span><span class="pl-s">)</span></div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(448px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T15:56:21.000Z" tense="past" title="May 26, 2017, 9:26 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/9ec5d68325e743813f333bf9fbb30c378ffb5311/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Adding instructions for local git deployment

- Extended instructions to include git deployment setup.
- Uncommented code for installing needed packages" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/9ec5d68325e743813f333bf9fbb30c378ffb5311">Adding instructions for local git deployment</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T15:56:21.000Z" tense="past" title="May 26, 2017, 9:26 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 9ec5d68, made on 26 May 2017" id="reblame-9ec5d68" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-9ec5d68" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/97be13f9fadc71166d144690d62b9e8102af7e8c/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="19" class="react-line-number react-code-text" style="padding-right: 16px;">19</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC19" class="react-file-line html-div" data-testid="code-cell" data-line-number="19" style="position: relative;">   <span class="pl-v">-</span> <span class="pl-s">[</span>Web App Setup<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">#setup</span><span class="pl-s">)</span></div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(479px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T16:47:08.000Z" tense="past" title="May 26, 2017, 10:17 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/328bbd2e77123be547ab3dbe042356b1f112aa5d/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Add final instructions for git deployment and gameplay" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/328bbd2e77123be547ab3dbe042356b1f112aa5d">Add final instructions for git deployment and gameplay</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T16:47:08.000Z" tense="past" title="May 26, 2017, 10:17 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 328bbd2, made on 26 May 2017" id="reblame-328bbd2" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-328bbd2" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/9ec5d68325e743813f333bf9fbb30c378ffb5311/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="20" class="react-line-number react-code-text" style="padding-right: 16px;">20</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC20" class="react-file-line html-div" data-testid="code-cell" data-line-number="20" style="position: relative;">   <span class="pl-v">-</span> <span class="pl-s">[</span>Playing Hangman<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">#gameplay</span><span class="pl-s">)</span></div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(510px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T14:26:23.000Z" tense="past" title="May 26, 2017, 7:56 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/97be13f9fadc71166d144690d62b9e8102af7e8c/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Begin to add web app and readme

- Added web app files (excluding wheels and CNTK files) to the
repository
- Added setup steps through web app deployment to README
TODO: update deploy.cmd to download wheels and CNTK files from blob
storage." class="color-fg-default" href="https://github.com/Azure/Hangman/commit/97be13f9fadc71166d144690d62b9e8102af7e8c">Begin to add web app and readme</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T14:26:23.000Z" tense="past" title="May 26, 2017, 7:56 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 97be13f, made on 26 May 2017" id="reblame-97be13f" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-97be13f" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/77d21669580b42f2983aba564b1f5c637ab20888/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="21" class="react-line-number react-code-text" style="padding-right: 16px;">21</div><div data-line-number="22" class="react-line-number react-code-text" style="padding-right: 16px;">22</div><div data-line-number="23" class="react-line-number react-code-text" style="padding-right: 16px;">23</div><div data-line-number="24" class="react-line-number react-code-text" style="padding-right: 16px;">24</div><div data-line-number="25" class="react-line-number react-code-text" style="padding-right: 16px;">25</div><div data-line-number="26" class="react-line-number react-code-text" style="padding-right: 16px;">26</div><div data-line-number="27" class="react-line-number react-code-text" style="padding-right: 16px;">27</div><div data-line-number="28" class="react-line-number react-code-text" style="padding-right: 16px;">28</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC21" class="react-file-line html-div" data-testid="code-cell" data-line-number="21" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC22" class="react-file-line html-div" data-testid="code-cell" data-line-number="22" style="position: relative;">Note that it is not necessary to complete the "Training" section before completing the "Operationalization" section, as a sample trained model is provided.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC23" class="react-file-line html-div" data-testid="code-cell" data-line-number="23" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC24" class="react-file-line html-div" data-testid="code-cell" data-line-number="24" style="position: relative;">&lt;<span class="pl-ent">a</span> <span class="pl-e">name</span>=<span class="pl-s">"</span><span class="pl-s">train</span><span class="pl-s">"</span>&gt;&lt;/<span class="pl-ent">a</span>&gt;</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC25" class="react-file-line html-div" data-testid="code-cell" data-line-number="25" style="position: relative;"><span class="pl-mh">## <span class="pl-en">Training</span></span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC26" class="react-file-line html-div" data-testid="code-cell" data-line-number="26" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC27" class="react-file-line html-div" data-testid="code-cell" data-line-number="27" style="position: relative;">&lt;<span class="pl-ent">a</span> <span class="pl-e">name</span>=<span class="pl-s">"</span><span class="pl-s">trainprereq</span><span class="pl-s">"</span>&gt;&lt;/<span class="pl-ent">a</span>&gt;</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC28" class="react-file-line html-div" data-testid="code-cell" data-line-number="28" style="position: relative;"><span class="pl-mh">### <span class="pl-en">Prerequisites</span></span></div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(670px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T20:34:00.000Z" tense="past" title="May 18, 2017, 2:04 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/e7aefb91252de649fdfe350b4d8f7d0cc5ded0b9/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Add description and instructions" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/e7aefb91252de649fdfe350b4d8f7d0cc5ded0b9">Add description and instructions</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T20:34:00.000Z" tense="past" title="May 18, 2017, 2:04 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change e7aefb9, made on 18 May 2017" id="reblame-e7aefb9" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-e7aefb9" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/0b9bef44a6c9bc9e8e6c2ce1c9ccea7bac550f64/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="29" class="react-line-number react-code-text" style="padding-right: 16px;">29</div><div data-line-number="30" class="react-line-number react-code-text" style="padding-right: 16px;">30</div><div data-line-number="31" class="react-line-number react-code-text" style="padding-right: 16px;">31</div><div data-line-number="32" class="react-line-number react-code-text" style="padding-right: 16px;">32</div><div data-line-number="33" class="react-line-number react-code-text" style="padding-right: 16px;">33</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC29" class="react-file-line html-div" data-testid="code-cell" data-line-number="29" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC30" class="react-file-line html-div" data-testid="code-cell" data-line-number="30" style="position: relative;">You will need:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC31" class="react-file-line html-div" data-testid="code-cell" data-line-number="31" style="position: relative;"><span class="pl-v">-</span> A computer with a GPU (such as an Azure NC6 GPU DSVM)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC32" class="react-file-line html-div" data-testid="code-cell" data-line-number="32" style="position: relative;"><span class="pl-v">-</span> <span class="pl-s">[</span>CNTK 2.0 release candidate 2<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">https://github.com/Microsoft/CNTK/releases</span><span class="pl-s">)</span> (or later) installed in an Anaconda Python 3.5 environment able to run Jupyter Notebooks</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC33" class="react-file-line html-div" data-testid="code-cell" data-line-number="33" style="position: relative;"><span class="pl-v">-</span> The <span class="pl-s">[</span>tarballed version<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">http://wordnetcode.princeton.edu/3.0/WordNet-3.0.tar.gz</span><span class="pl-s">)</span> of Princeton University's <span class="pl-s">[</span>WordNet<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">http://wordnet.princeton.edu</span><span class="pl-s">)</span> database, decompressed e.g. uzing <span class="pl-s">[</span>7zip<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">http://www.7-zip.org/download.html</span><span class="pl-s">)</span></div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(770px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T14:26:23.000Z" tense="past" title="May 26, 2017, 7:56 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/97be13f9fadc71166d144690d62b9e8102af7e8c/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Begin to add web app and readme

- Added web app files (excluding wheels and CNTK files) to the
repository
- Added setup steps through web app deployment to README
TODO: update deploy.cmd to download wheels and CNTK files from blob
storage." class="color-fg-default" href="https://github.com/Azure/Hangman/commit/97be13f9fadc71166d144690d62b9e8102af7e8c">Begin to add web app and readme</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T14:26:23.000Z" tense="past" title="May 26, 2017, 7:56 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 97be13f, made on 26 May 2017" id="reblame-97be13f" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-97be13f" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/77d21669580b42f2983aba564b1f5c637ab20888/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="34" class="react-line-number react-code-text" style="padding-right: 16px;">34</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC34" class="react-file-line html-div" data-testid="code-cell" data-line-number="34" style="position: relative;"><span class="pl-v">-</span> The Jupyter notebook contained in the root directory of this repository</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(801px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T20:34:00.000Z" tense="past" title="May 18, 2017, 2:04 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/e7aefb91252de649fdfe350b4d8f7d0cc5ded0b9/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Add description and instructions" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/e7aefb91252de649fdfe350b4d8f7d0cc5ded0b9">Add description and instructions</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T20:34:00.000Z" tense="past" title="May 18, 2017, 2:04 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change e7aefb9, made on 18 May 2017" id="reblame-e7aefb9" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-e7aefb9" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/0b9bef44a6c9bc9e8e6c2ce1c9ccea7bac550f64/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="35" class="react-line-number react-code-text" style="padding-right: 16px;">35</div><div data-line-number="36" class="react-line-number react-code-text" style="padding-right: 16px;">36</div><div data-line-number="37" class="react-line-number react-code-text" style="padding-right: 16px;">37</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC35" class="react-file-line html-div" data-testid="code-cell" data-line-number="35" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC36" class="react-file-line html-div" data-testid="code-cell" data-line-number="36" style="position: relative;">Note that the first two requirements can be satisfied by deploying a "Deep Learning toolkit for the DSVM" resource on Azure.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC37" class="react-file-line html-div" data-testid="code-cell" data-line-number="37" style="position: relative;">
</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(861px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T14:26:23.000Z" tense="past" title="May 26, 2017, 7:56 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/97be13f9fadc71166d144690d62b9e8102af7e8c/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Begin to add web app and readme

- Added web app files (excluding wheels and CNTK files) to the
repository
- Added setup steps through web app deployment to README
TODO: update deploy.cmd to download wheels and CNTK files from blob
storage." class="color-fg-default" href="https://github.com/Azure/Hangman/commit/97be13f9fadc71166d144690d62b9e8102af7e8c">Begin to add web app and readme</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T14:26:23.000Z" tense="past" title="May 26, 2017, 7:56 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 97be13f, made on 26 May 2017" id="reblame-97be13f" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-97be13f" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/77d21669580b42f2983aba564b1f5c637ab20888/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="38" class="react-line-number react-code-text" style="padding-right: 16px;">38</div><div data-line-number="39" class="react-line-number react-code-text" style="padding-right: 16px;">39</div><div data-line-number="40" class="react-line-number react-code-text" style="padding-right: 16px;">40</div><div data-line-number="41" class="react-line-number react-code-text" style="padding-right: 16px;">41</div><div data-line-number="42" class="react-line-number react-code-text" style="padding-right: 16px;">42</div><div data-line-number="43" class="react-line-number react-code-text" style="padding-right: 16px;">43</div><div data-line-number="44" class="react-line-number react-code-text" style="padding-right: 16px;">44</div><div data-line-number="45" class="react-line-number react-code-text" style="padding-right: 16px;">45</div><div data-line-number="46" class="react-line-number react-code-text" style="padding-right: 16px;">46</div><div data-line-number="47" class="react-line-number react-code-text" style="padding-right: 16px;">47</div><div data-line-number="48" class="react-line-number react-code-text" style="padding-right: 16px;">48</div><div data-line-number="49" class="react-line-number react-code-text" style="padding-right: 16px;">49</div><div data-line-number="50" class="react-line-number react-code-text" style="padding-right: 16px;">50</div><div data-line-number="51" class="react-line-number react-code-text" style="padding-right: 16px;">51</div><div data-line-number="52" class="react-line-number react-code-text" style="padding-right: 16px;">52</div><div data-line-number="53" class="react-line-number react-code-text" style="padding-right: 16px;">53</div><div data-line-number="54" class="react-line-number react-code-text" style="padding-right: 16px;">54</div><div data-line-number="55" class="react-line-number react-code-text" style="padding-right: 16px;">55</div><div data-line-number="56" class="react-line-number react-code-text" style="padding-right: 16px;">56</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC38" class="react-file-line html-div" data-testid="code-cell" data-line-number="38" style="position: relative;">&lt;<span class="pl-ent">a</span> <span class="pl-e">name</span>=<span class="pl-s">"</span><span class="pl-s">traincode</span><span class="pl-s">"</span>&gt;&lt;/<span class="pl-ent">a</span>&gt;</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC39" class="react-file-line html-div" data-testid="code-cell" data-line-number="39" style="position: relative;"><span class="pl-mh">### <span class="pl-en">Sample code (contained in Jupyter Notebook)</span></span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC40" class="react-file-line html-div" data-testid="code-cell" data-line-number="40" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC41" class="react-file-line html-div" data-testid="code-cell" data-line-number="41" style="position: relative;">Load the Jupyter notebook -- <span class="pl-s">`</span><span class="pl-c1">Train a Neural Network to Play Hangman.ipynb</span><span class="pl-s">`</span> -- from this repository in your CNTK Python 3.5 environment, and follow the instructions inside to complete the training and validation steps.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC42" class="react-file-line html-div" data-testid="code-cell" data-line-number="42" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC43" class="react-file-line html-div" data-testid="code-cell" data-line-number="43" style="position: relative;">&lt;<span class="pl-ent">a</span> <span class="pl-e">name</span>=<span class="pl-s">"</span><span class="pl-s">op</span><span class="pl-s">"</span>&gt;&lt;/<span class="pl-ent">a</span>&gt;</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC44" class="react-file-line html-div" data-testid="code-cell" data-line-number="44" style="position: relative;"><span class="pl-mh">## <span class="pl-en">Operationalization</span></span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC45" class="react-file-line html-div" data-testid="code-cell" data-line-number="45" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC46" class="react-file-line html-div" data-testid="code-cell" data-line-number="46" style="position: relative;">&lt;<span class="pl-ent">a</span> <span class="pl-e">name</span>=<span class="pl-s">"</span><span class="pl-s">opprereq</span><span class="pl-s">"</span>&gt;&lt;/<span class="pl-ent">a</span>&gt;</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC47" class="react-file-line html-div" data-testid="code-cell" data-line-number="47" style="position: relative;"><span class="pl-mh">### <span class="pl-en">Prerequisites</span></span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC48" class="react-file-line html-div" data-testid="code-cell" data-line-number="48" style="position: relative;"><span class="pl-v">-</span> An <span class="pl-s">[</span>Azure subscription<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">https://azure.microsoft.com/en-us/free/</span><span class="pl-s">)</span> for deploying an Azure Web App resource</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC49" class="react-file-line html-div" data-testid="code-cell" data-line-number="49" style="position: relative;"><span class="pl-v">-</span> A cloned or downloaded local copy of this repository</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC50" class="react-file-line html-div" data-testid="code-cell" data-line-number="50" style="position: relative;">   <span class="pl-v">-</span> We will refer to the location of this repository on your local computer as <span class="pl-s">`</span><span class="pl-c1">&lt;repo-filepath&gt;</span><span class="pl-s">`</span>.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC51" class="react-file-line html-div" data-testid="code-cell" data-line-number="51" style="position: relative;"><span class="pl-v">-</span> The command line version of <span class="pl-s">[</span>Git<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">https://git-scm.com/downloads</span><span class="pl-s">)</span> installed locally</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC52" class="react-file-line html-div" data-testid="code-cell" data-line-number="52" style="position: relative;">   <span class="pl-v">-</span> Git and shell commands will be written for a Windows operating system. However, you may be able to easily adapt these commands for Mac OS/Linux/UNIX.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC53" class="react-file-line html-div" data-testid="code-cell" data-line-number="53" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC54" class="react-file-line html-div" data-testid="code-cell" data-line-number="54" style="position: relative;">&lt;<span class="pl-ent">a</span> <span class="pl-e">name</span>=<span class="pl-s">"</span><span class="pl-s">deploy</span><span class="pl-s">"</span>&gt;&lt;/<span class="pl-ent">a</span>&gt;</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC55" class="react-file-line html-div" data-testid="code-cell" data-line-number="55" style="position: relative;"><span class="pl-mh">### <span class="pl-en">Deploying an Azure Web App</span></span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC56" class="react-file-line html-div" data-testid="code-cell" data-line-number="56" style="position: relative;">
</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(1241px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-25T02:22:55.000Z" tense="past" title="Jul 25, 2017, 7:52 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/10565021" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/7f23a4e021f67cd0930973f65517cbcda67b2f11/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="readme" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/7f23a4e021f67cd0930973f65517cbcda67b2f11">readme</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-25T02:22:55.000Z" tense="past" title="Jul 25, 2017, 7:52 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 7f23a4e, made on 25 Jul 2017" id="reblame-7f23a4e" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-7f23a4e" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/10efd26ec19dcaea8984cc5376a277c1cff09ac8/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="57" class="react-line-number react-code-text" style="padding-right: 16px;">57</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC57" class="react-file-line html-div" data-testid="code-cell" data-line-number="57" style="position: relative;">We will create an Azure Web App to serve a website containing our neural network. The Web Apps feature of Microsoft Azure App Service is optimized for hosting websites and web applications. To deploy a web app:</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(1272px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T14:26:23.000Z" tense="past" title="May 26, 2017, 7:56 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/97be13f9fadc71166d144690d62b9e8102af7e8c/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Begin to add web app and readme

- Added web app files (excluding wheels and CNTK files) to the
repository
- Added setup steps through web app deployment to README
TODO: update deploy.cmd to download wheels and CNTK files from blob
storage." class="color-fg-default" href="https://github.com/Azure/Hangman/commit/97be13f9fadc71166d144690d62b9e8102af7e8c">Begin to add web app and readme</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T14:26:23.000Z" tense="past" title="May 26, 2017, 7:56 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 97be13f, made on 26 May 2017" id="reblame-97be13f" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-97be13f" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/77d21669580b42f2983aba564b1f5c637ab20888/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="58" class="react-line-number react-code-text" style="padding-right: 16px;">58</div><div data-line-number="59" class="react-line-number react-code-text" style="padding-right: 16px;">59</div><div data-line-number="60" class="react-line-number react-code-text" style="padding-right: 16px;">60</div><div data-line-number="61" class="react-line-number react-code-text" style="padding-right: 16px;">61</div><div data-line-number="62" class="react-line-number react-code-text" style="padding-right: 16px;">62</div><div data-line-number="63" class="react-line-number react-code-text" style="padding-right: 16px;">63</div><div data-line-number="64" class="react-line-number react-code-text" style="padding-right: 16px;">64</div><div data-line-number="65" class="react-line-number react-code-text" style="padding-right: 16px;">65</div><div data-line-number="66" class="react-line-number react-code-text" style="padding-right: 16px;">66</div><div data-line-number="67" class="react-line-number react-code-text" style="padding-right: 16px;">67</div><div data-line-number="68" class="react-line-number react-code-text" style="padding-right: 16px;">68</div><div data-line-number="69" class="react-line-number react-code-text" style="padding-right: 16px;">69</div><div data-line-number="70" class="react-line-number react-code-text" style="padding-right: 16px;">70</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC58" class="react-file-line html-div" data-testid="code-cell" data-line-number="58" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> Log into <span class="pl-s">[</span>Azure Portal<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">https://portal.azure.com</span><span class="pl-s">)</span>.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC59" class="react-file-line html-div" data-testid="code-cell" data-line-number="59" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> Click the "+ New" button at upper-left.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC60" class="react-file-line html-div" data-testid="code-cell" data-line-number="60" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> In the search bar, type in "Web App" and press Enter.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC61" class="react-file-line html-div" data-testid="code-cell" data-line-number="61" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> In the search results, choose the "Web App" option published by Microsoft.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC62" class="react-file-line html-div" data-testid="code-cell" data-line-number="62" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> After reading the description in the pane that appears, scroll down and click the "Create" button.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC63" class="react-file-line html-div" data-testid="code-cell" data-line-number="63" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> In the "Web App Create" pane that appears:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC64" class="react-file-line html-div" data-testid="code-cell" data-line-number="64" style="position: relative;">   <span class="pl-s">1</span><span class="pl-v">.</span> Choose a unique name for your web app.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC65" class="react-file-line html-div" data-testid="code-cell" data-line-number="65" style="position: relative;">   <span class="pl-s">1</span><span class="pl-v">.</span> Select the appropriate Azure subscription.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC66" class="react-file-line html-div" data-testid="code-cell" data-line-number="66" style="position: relative;">   <span class="pl-s">1</span><span class="pl-v">.</span> Choose a resource group for your web app. (We recommend creating a new resource group, so that you can easily delete it and the associated app service plan at the end of this tutorial.)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC67" class="react-file-line html-div" data-testid="code-cell" data-line-number="67" style="position: relative;">   <span class="pl-s">1</span><span class="pl-v">.</span> Click on App Service plan. You may choose an existing plan, but we recommend that you create a new one as follows:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC68" class="react-file-line html-div" data-testid="code-cell" data-line-number="68" style="position: relative;">      <span class="pl-s">1</span><span class="pl-v">.</span> Click the "+ Create New" button.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC69" class="react-file-line html-div" data-testid="code-cell" data-line-number="69" style="position: relative;">      <span class="pl-s">1</span><span class="pl-v">.</span> Choose an appropriate name and location for the service plan, then click OK.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC70" class="react-file-line html-div" data-testid="code-cell" data-line-number="70" style="position: relative;">   <span class="pl-s">1</span><span class="pl-v">.</span> Click "Create".</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(1532px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T20:34:00.000Z" tense="past" title="May 18, 2017, 2:04 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/e7aefb91252de649fdfe350b4d8f7d0cc5ded0b9/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Add description and instructions" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/e7aefb91252de649fdfe350b4d8f7d0cc5ded0b9">Add description and instructions</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T20:34:00.000Z" tense="past" title="May 18, 2017, 2:04 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change e7aefb9, made on 18 May 2017" id="reblame-e7aefb9" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-e7aefb9" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/0b9bef44a6c9bc9e8e6c2ce1c9ccea7bac550f64/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="71" class="react-line-number react-code-text" style="padding-right: 16px;">71</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC71" class="react-file-line html-div" data-testid="code-cell" data-line-number="71" style="position: relative;">
</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(1563px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T14:26:23.000Z" tense="past" title="May 26, 2017, 7:56 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/97be13f9fadc71166d144690d62b9e8102af7e8c/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Begin to add web app and readme

- Added web app files (excluding wheels and CNTK files) to the
repository
- Added setup steps through web app deployment to README
TODO: update deploy.cmd to download wheels and CNTK files from blob
storage." class="color-fg-default" href="https://github.com/Azure/Hangman/commit/97be13f9fadc71166d144690d62b9e8102af7e8c">Begin to add web app and readme</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T14:26:23.000Z" tense="past" title="May 26, 2017, 7:56 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 97be13f, made on 26 May 2017" id="reblame-97be13f" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-97be13f" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/77d21669580b42f2983aba564b1f5c637ab20888/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="72" class="react-line-number react-code-text" style="padding-right: 16px;">72</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC72" class="react-file-line html-div" data-testid="code-cell" data-line-number="72" style="position: relative;">Deployment may take a few minutes to complete. To monitor deployment, navigate to your resource group by typing its name in the search bar at the top of the Azure Portal website. Refresh until the "App Service" resource (your web app) appears in the resource group contents.</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(1594px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T19:43:31.000Z" tense="past" title="May 18, 2017, 1:13 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/b428ca0ba8ba884f17d4daf395e80112bdf63cf4/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Added info on input data set" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/b428ca0ba8ba884f17d4daf395e80112bdf63cf4">Added info on input data set</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-17T19:43:31.000Z" tense="past" title="May 18, 2017, 1:13 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change b428ca0, made on 18 May 2017" id="reblame-b428ca0" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-b428ca0" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/54a389cc96e7fe55430913e5752fd6724e8d394b/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="73" class="react-line-number react-code-text" style="padding-right: 16px;">73</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC73" class="react-file-line html-div" data-testid="code-cell" data-line-number="73" style="position: relative;">
</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(1625px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T15:56:21.000Z" tense="past" title="May 26, 2017, 9:26 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/9ec5d68325e743813f333bf9fbb30c378ffb5311/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Adding instructions for local git deployment

- Extended instructions to include git deployment setup.
- Uncommented code for installing needed packages" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/9ec5d68325e743813f333bf9fbb30c378ffb5311">Adding instructions for local git deployment</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T15:56:21.000Z" tense="past" title="May 26, 2017, 9:26 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 9ec5d68, made on 26 May 2017" id="reblame-9ec5d68" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-9ec5d68" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/97be13f9fadc71166d144690d62b9e8102af7e8c/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="74" class="react-line-number react-code-text" style="padding-right: 16px;">74</div><div data-line-number="75" class="react-line-number react-code-text" style="padding-right: 16px;">75</div><div data-line-number="76" class="react-line-number react-code-text" style="padding-right: 16px;">76</div><div data-line-number="77" class="react-line-number react-code-text" style="padding-right: 16px;">77</div><div data-line-number="78" class="react-line-number react-code-text" style="padding-right: 16px;">78</div><div data-line-number="79" class="react-line-number react-code-text" style="padding-right: 16px;">79</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC74" class="react-file-line html-div" data-testid="code-cell" data-line-number="74" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC75" class="react-file-line html-div" data-testid="code-cell" data-line-number="75" style="position: relative;">&lt;<span class="pl-ent">a</span> <span class="pl-e">name</span>=<span class="pl-s">"</span><span class="pl-s">setup</span><span class="pl-s">"</span>&gt;&lt;/<span class="pl-ent">a</span>&gt;</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC76" class="react-file-line html-div" data-testid="code-cell" data-line-number="76" style="position: relative;"><span class="pl-mh">### <span class="pl-en">Web App Setup</span></span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC77" class="react-file-line html-div" data-testid="code-cell" data-line-number="77" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC78" class="react-file-line html-div" data-testid="code-cell" data-line-number="78" style="position: relative;">Once your web app's deployment is complete, navigate to its overview pane (e.g. by clicking on the "App Service" resource in your resource group). The steps below will install necessary Python packages on the web app and upload the model files and website code from your local computer.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC79" class="react-file-line html-div" data-testid="code-cell" data-line-number="79" style="position: relative;">
</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(1745px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-11-02T17:53:57.000Z" tense="past" title="Nov 2, 2017, 11:23 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/19eea44f537d384a429c178c9b52c87fec579215/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Updated README instructions to Python 3.5.4

There is no longer an option to install the &quot;Python 3.5.3 x64&quot; extension; it has been replaced by a corresponding 3.5.4 option. This is likely to break the install script since the name of the Python folder will doubtlessly be different now (repo updates to follow)." class="color-fg-default" href="https://github.com/Azure/Hangman/commit/19eea44f537d384a429c178c9b52c87fec579215">Updated README instructions to Python 3.5.4</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-11-02T17:53:57.000Z" tense="past" title="Nov 2, 2017, 11:23 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 19eea44, made on 2 Nov 2017" id="reblame-19eea44" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-19eea44" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/8f67cf42517093054b54eecce025364b255d4443/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="80" class="react-line-number react-code-text" style="padding-right: 16px;">80</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC80" class="react-file-line html-div" data-testid="code-cell" data-line-number="80" style="position: relative;"><span class="pl-mh">#### <span class="pl-en">Install the Python 3.5.4 x64 Extension</span></span></div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(1776px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T15:56:21.000Z" tense="past" title="May 26, 2017, 9:26 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/9ec5d68325e743813f333bf9fbb30c378ffb5311/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Adding instructions for local git deployment

- Extended instructions to include git deployment setup.
- Uncommented code for installing needed packages" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/9ec5d68325e743813f333bf9fbb30c378ffb5311">Adding instructions for local git deployment</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T15:56:21.000Z" tense="past" title="May 26, 2017, 9:26 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 9ec5d68, made on 26 May 2017" id="reblame-9ec5d68" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-9ec5d68" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/97be13f9fadc71166d144690d62b9e8102af7e8c/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="81" class="react-line-number react-code-text" style="padding-right: 16px;">81</div><div data-line-number="82" class="react-line-number react-code-text" style="padding-right: 16px;">82</div><div data-line-number="83" class="react-line-number react-code-text" style="padding-right: 16px;">83</div><div data-line-number="84" class="react-line-number react-code-text" style="padding-right: 16px;">84</div><div data-line-number="85" class="react-line-number react-code-text" style="padding-right: 16px;">85</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC81" class="react-file-line html-div" data-testid="code-cell" data-line-number="81" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC82" class="react-file-line html-div" data-testid="code-cell" data-line-number="82" style="position: relative;">The web app comes with Python 2.7 and 3.4 (x86) available by default. We install Python 3.5 x64 to meet the requirements of CNTK.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC83" class="react-file-line html-div" data-testid="code-cell" data-line-number="83" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC84" class="react-file-line html-div" data-testid="code-cell" data-line-number="84" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> In the search bar at the upper left of your web app's overview pane, type in "Extensions" and click on the search result.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC85" class="react-file-line html-div" data-testid="code-cell" data-line-number="85" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> Click the "+ Add" button.</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(1876px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-11-02T17:53:57.000Z" tense="past" title="Nov 2, 2017, 11:23 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/19eea44f537d384a429c178c9b52c87fec579215/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Updated README instructions to Python 3.5.4

There is no longer an option to install the &quot;Python 3.5.3 x64&quot; extension; it has been replaced by a corresponding 3.5.4 option. This is likely to break the install script since the name of the Python folder will doubtlessly be different now (repo updates to follow)." class="color-fg-default" href="https://github.com/Azure/Hangman/commit/19eea44f537d384a429c178c9b52c87fec579215">Updated README instructions to Python 3.5.4</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-11-02T17:53:57.000Z" tense="past" title="Nov 2, 2017, 11:23 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 19eea44, made on 2 Nov 2017" id="reblame-19eea44" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-19eea44" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/8f67cf42517093054b54eecce025364b255d4443/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="86" class="react-line-number react-code-text" style="padding-right: 16px;">86</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC86" class="react-file-line html-div" data-testid="code-cell" data-line-number="86" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> Scroll through the list of extensions to find and click on "Python 3.5.4 x64".</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(1907px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T15:56:21.000Z" tense="past" title="May 26, 2017, 9:26 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/9ec5d68325e743813f333bf9fbb30c378ffb5311/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Adding instructions for local git deployment

- Extended instructions to include git deployment setup.
- Uncommented code for installing needed packages" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/9ec5d68325e743813f333bf9fbb30c378ffb5311">Adding instructions for local git deployment</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T15:56:21.000Z" tense="past" title="May 26, 2017, 9:26 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 9ec5d68, made on 26 May 2017" id="reblame-9ec5d68" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-9ec5d68" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/97be13f9fadc71166d144690d62b9e8102af7e8c/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="87" class="react-line-number react-code-text" style="padding-right: 16px;">87</div><div data-line-number="88" class="react-line-number react-code-text" style="padding-right: 16px;">88</div><div data-line-number="89" class="react-line-number react-code-text" style="padding-right: 16px;">89</div><div data-line-number="90" class="react-line-number react-code-text" style="padding-right: 16px;">90</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC87" class="react-file-line html-div" data-testid="code-cell" data-line-number="87" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> Review and accept the legal terms by clicking "OK".</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC88" class="react-file-line html-div" data-testid="code-cell" data-line-number="88" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> Click "OK" to initiate the installation of the extension.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC89" class="react-file-line html-div" data-testid="code-cell" data-line-number="89" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> After a moment, refresh the page to confirm that the extension has installed successfully. (You may receive an Azure notification that the installation timed out even if the install completes successfully.)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC90" class="react-file-line html-div" data-testid="code-cell" data-line-number="90" style="position: relative;">
</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(1987px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-25T02:22:55.000Z" tense="past" title="Jul 25, 2017, 7:52 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/10565021" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/7f23a4e021f67cd0930973f65517cbcda67b2f11/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="readme" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/7f23a4e021f67cd0930973f65517cbcda67b2f11">readme</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-25T02:22:55.000Z" tense="past" title="Jul 25, 2017, 7:52 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 7f23a4e, made on 25 Jul 2017" id="reblame-7f23a4e" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-7f23a4e" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/10efd26ec19dcaea8984cc5376a277c1cff09ac8/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="91" class="react-line-number react-code-text" style="padding-right: 16px;">91</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC91" class="react-file-line html-div" data-testid="code-cell" data-line-number="91" style="position: relative;"><span class="pl-mh">#### <span class="pl-en"><span class="pl-s">[</span>Configure Local Git Deployment<span class="pl-s">]</span><span class="pl-s">(</span><span class="pl-corl">https://docs.microsoft.com/en-us/azure/app-service-web/app-service-deploy-local-git</span><span class="pl-s">)</span></span></span></div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2018px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T15:56:21.000Z" tense="past" title="May 26, 2017, 9:26 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/9ec5d68325e743813f333bf9fbb30c378ffb5311/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Adding instructions for local git deployment

- Extended instructions to include git deployment setup.
- Uncommented code for installing needed packages" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/9ec5d68325e743813f333bf9fbb30c378ffb5311">Adding instructions for local git deployment</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T15:56:21.000Z" tense="past" title="May 26, 2017, 9:26 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 9ec5d68, made on 26 May 2017" id="reblame-9ec5d68" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-9ec5d68" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/97be13f9fadc71166d144690d62b9e8102af7e8c/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="92" class="react-line-number react-code-text" style="padding-right: 16px;">92</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC92" class="react-file-line html-div" data-testid="code-cell" data-line-number="92" style="position: relative;">
</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2049px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-25T02:22:55.000Z" tense="past" title="Jul 25, 2017, 7:52 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/10565021" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/7f23a4e021f67cd0930973f65517cbcda67b2f11/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="readme" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/7f23a4e021f67cd0930973f65517cbcda67b2f11">readme</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-25T02:22:55.000Z" tense="past" title="Jul 25, 2017, 7:52 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 7f23a4e, made on 25 Jul 2017" id="reblame-7f23a4e" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-7f23a4e" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/10efd26ec19dcaea8984cc5376a277c1cff09ac8/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="93" class="react-line-number react-code-text" style="padding-right: 16px;">93</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC93" class="react-file-line html-div" data-testid="code-cell" data-line-number="93" style="position: relative;">You will deploy your app to Azure App Service from a Git repository on your local computer. App Service supports this approach with the Local Git deployment option in the Azure Portal. The first step in this process is to enable the App service app repository.</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2080px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T15:56:21.000Z" tense="past" title="May 26, 2017, 9:26 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/9ec5d68325e743813f333bf9fbb30c378ffb5311/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Adding instructions for local git deployment

- Extended instructions to include git deployment setup.
- Uncommented code for installing needed packages" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/9ec5d68325e743813f333bf9fbb30c378ffb5311">Adding instructions for local git deployment</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T15:56:21.000Z" tense="past" title="May 26, 2017, 9:26 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 9ec5d68, made on 26 May 2017" id="reblame-9ec5d68" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-9ec5d68" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/97be13f9fadc71166d144690d62b9e8102af7e8c/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="94" class="react-line-number react-code-text" style="padding-right: 16px;">94</div><div data-line-number="95" class="react-line-number react-code-text" style="padding-right: 16px;">95</div><div data-line-number="96" class="react-line-number react-code-text" style="padding-right: 16px;">96</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC94" class="react-file-line html-div" data-testid="code-cell" data-line-number="94" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC95" class="react-file-line html-div" data-testid="code-cell" data-line-number="95" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> In the search bar at the upper left of your web app's overview pane, type in "Deployment options" and click on the search result.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC96" class="react-file-line html-div" data-testid="code-cell" data-line-number="96" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> Click on "Choose Source" and select "Local Git Repository".</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2140px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-25T02:22:55.000Z" tense="past" title="Jul 25, 2017, 7:52 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/10565021" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/7f23a4e021f67cd0930973f65517cbcda67b2f11/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="readme" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/7f23a4e021f67cd0930973f65517cbcda67b2f11">readme</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-25T02:22:55.000Z" tense="past" title="Jul 25, 2017, 7:52 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 7f23a4e, made on 25 Jul 2017" id="reblame-7f23a4e" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-7f23a4e" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/10efd26ec19dcaea8984cc5376a277c1cff09ac8/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="97" class="react-line-number react-code-text" style="padding-right: 16px;">97</div><div data-line-number="98" class="react-line-number react-code-text" style="padding-right: 16px;">98</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC97" class="react-file-line html-div" data-testid="code-cell" data-line-number="97" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> If you have not set up a repository in Azure before, you will need to create login credentials for it. You will see a section that says "Setup connection" where you must choose a username and password. You will use them to log into the Azure repository and push changes from your local Git repository. </div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC98" class="react-file-line html-div" data-testid="code-cell" data-line-number="98" style="position: relative;">    <span class="pl-s">1</span><span class="pl-v">.</span> Note that these login credentials are distinct from your github.com account and are used only for logging into Azure repository. They are also different from your Azure subscription credentials.</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2180px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-12T14:38:23.000Z" tense="past" title="Jul 12, 2017, 8:08 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/c25cc32bfdd746d2454d2854837c8637abe83498/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Update README.md" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/c25cc32bfdd746d2454d2854837c8637abe83498">Update README.md</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-12T14:38:23.000Z" tense="past" title="Jul 12, 2017, 8:08 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change c25cc32, made on 12 Jul 2017" id="reblame-c25cc32" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-c25cc32" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/ab2e906e0a7791dfaafd7af14cae5d1084a81802/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="99" class="react-line-number react-code-text" style="padding-right: 16px;">99</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC99" class="react-file-line html-div" data-testid="code-cell" data-line-number="99" style="position: relative;">    <span class="pl-s">1</span><span class="pl-v">.</span> Choose a username and password you will remember: the same login will be automatically associated with local Git deployments on Azure that you create in the future. (Note that you will have the option to change this login in the future.)</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2211px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-11T21:02:45.000Z" tense="past" title="Jul 12, 2017, 2:32 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/dc62dbfcff3c637197535baa8c29146a3a30e4ef/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Update README.md" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/dc62dbfcff3c637197535baa8c29146a3a30e4ef">Update README.md</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-11T21:02:45.000Z" tense="past" title="Jul 12, 2017, 2:32 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change dc62dbf, made on 12 Jul 2017" id="reblame-dc62dbf" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-dc62dbf" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/b33a228eddb3d35dac850cf81a58f9222f9a7b44/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="100" class="react-line-number react-code-text" style="padding-right: 16px;">100</div><div data-line-number="101" class="react-line-number react-code-text" style="padding-right: 16px;">101</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC100" class="react-file-line html-div" data-testid="code-cell" data-line-number="100" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> Click "OK". (There is no need to configure the Performance Test.)</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC101" class="react-file-line html-div" data-testid="code-cell" data-line-number="101" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> Find the Git URL:</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2251px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T15:56:21.000Z" tense="past" title="May 26, 2017, 9:26 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/9ec5d68325e743813f333bf9fbb30c378ffb5311/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Adding instructions for local git deployment

- Extended instructions to include git deployment setup.
- Uncommented code for installing needed packages" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/9ec5d68325e743813f333bf9fbb30c378ffb5311">Adding instructions for local git deployment</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T15:56:21.000Z" tense="past" title="May 26, 2017, 9:26 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 9ec5d68, made on 26 May 2017" id="reblame-9ec5d68" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-9ec5d68" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/97be13f9fadc71166d144690d62b9e8102af7e8c/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="102" class="react-line-number react-code-text" style="padding-right: 16px;">102</div><div data-line-number="103" class="react-line-number react-code-text" style="padding-right: 16px;">103</div><div data-line-number="104" class="react-line-number react-code-text" style="padding-right: 16px;">104</div><div data-line-number="105" class="react-line-number react-code-text" style="padding-right: 16px;">105</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC102" class="react-file-line html-div" data-testid="code-cell" data-line-number="102" style="position: relative;">   <span class="pl-s">1</span><span class="pl-v">.</span> In the search bar at the upper left of your web app's overview pane, type in "Properties" and click on the search result.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC103" class="react-file-line html-div" data-testid="code-cell" data-line-number="103" style="position: relative;">   <span class="pl-s">1</span><span class="pl-v">.</span> Copy the value in the "GIT URL" field on the Properties pane and store it locally; you will use this value shortly.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC104" class="react-file-line html-div" data-testid="code-cell" data-line-number="104" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC105" class="react-file-line html-div" data-testid="code-cell" data-line-number="105" style="position: relative;">Once the web app is configured, complete the steps below to configure git locally:</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2331px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T16:47:08.000Z" tense="past" title="May 26, 2017, 10:17 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/328bbd2e77123be547ab3dbe042356b1f112aa5d/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Add final instructions for git deployment and gameplay" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/328bbd2e77123be547ab3dbe042356b1f112aa5d">Add final instructions for git deployment and gameplay</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T16:47:08.000Z" tense="past" title="May 26, 2017, 10:17 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 328bbd2, made on 26 May 2017" id="reblame-328bbd2" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-328bbd2" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/9ec5d68325e743813f333bf9fbb30c378ffb5311/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="106" class="react-line-number react-code-text" style="padding-right: 16px;">106</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC106" class="react-file-line html-div" data-testid="code-cell" data-line-number="106" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> (Optional) If you trained your own NN using the Jupyter notebook in this repo and would like to use it on the website, copy your <span class="pl-s">`</span><span class="pl-c1">hangman_model.dnn</span><span class="pl-s">`</span> file to the folder <span class="pl-s">`</span><span class="pl-c1">&lt;repo-filepath&gt;\webapp\models</span><span class="pl-s">`</span> to overwrite our example model.</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2362px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T15:56:21.000Z" tense="past" title="May 26, 2017, 9:26 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/9ec5d68325e743813f333bf9fbb30c378ffb5311/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Adding instructions for local git deployment

- Extended instructions to include git deployment setup.
- Uncommented code for installing needed packages" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/9ec5d68325e743813f333bf9fbb30c378ffb5311">Adding instructions for local git deployment</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T15:56:21.000Z" tense="past" title="May 26, 2017, 9:26 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 9ec5d68, made on 26 May 2017" id="reblame-9ec5d68" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-9ec5d68" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/97be13f9fadc71166d144690d62b9e8102af7e8c/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="107" class="react-line-number react-code-text" style="padding-right: 16px;">107</div><div data-line-number="108" class="react-line-number react-code-text" style="padding-right: 16px;">108</div><div data-line-number="109" class="react-line-number react-code-text" style="padding-right: 16px;">109</div><div data-line-number="110" class="react-line-number react-code-text" style="padding-right: 16px;">110</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC107" class="react-file-line html-div" data-testid="code-cell" data-line-number="107" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> Open a command prompt (e.g. by clicking the Windows icon and typing "cmd").</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC108" class="react-file-line html-div" data-testid="code-cell" data-line-number="108" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> Navigate to the <span class="pl-s">`</span><span class="pl-c1">webapp</span><span class="pl-s">`</span> folder in your local copy of the git repository:</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC109" class="react-file-line html-div" data-testid="code-cell" data-line-number="109" style="position: relative;">   <span class="pl-s">```</span><span class="pl-c1">cd &lt;repo-filepath&gt;\webapp</span><span class="pl-s">```</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC110" class="react-file-line html-div" data-testid="code-cell" data-line-number="110" style="position: relative;"><span class="pl-s">1</span><span class="pl-v">.</span> Execute the commands below to create a local git repo and push a commit.</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2442px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-11T21:23:58.000Z" tense="past" title="Jul 12, 2017, 2:53 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/7390f1d29f3a668b40992637a31d562645cae0a9/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Update README.md" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/7390f1d29f3a668b40992637a31d562645cae0a9">Update README.md</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-11T21:23:58.000Z" tense="past" title="Jul 12, 2017, 2:53 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 7390f1d, made on 12 Jul 2017" id="reblame-7390f1d" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-7390f1d" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/1e570fd53c9826200a392efbcd2223910e83be0b/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="111" class="react-line-number react-code-text" style="padding-right: 16px;">111</div><div data-line-number="112" class="react-line-number react-code-text" style="padding-right: 16px;">112</div><div data-line-number="113" class="react-line-number react-code-text" style="padding-right: 16px;">113</div><div data-line-number="114" class="react-line-number react-code-text" style="padding-right: 16px;">114</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC111" class="react-file-line html-div" data-testid="code-cell" data-line-number="111" style="position: relative;">   <span class="pl-s">```</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC112" class="react-file-line html-div" data-testid="code-cell" data-line-number="112" style="position: relative;"><span class="pl-c1">   git init</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC113" class="react-file-line html-div" data-testid="code-cell" data-line-number="113" style="position: relative;"><span class="pl-c1">   git remote add azure &lt;git-url-stored-earlier&gt;</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC114" class="react-file-line html-div" data-testid="code-cell" data-line-number="114" style="position: relative;"><span class="pl-c1">   git add .</span></div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2522px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-25T02:22:55.000Z" tense="past" title="Jul 25, 2017, 7:52 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/10565021" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/7f23a4e021f67cd0930973f65517cbcda67b2f11/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="readme" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/7f23a4e021f67cd0930973f65517cbcda67b2f11">readme</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-25T02:22:55.000Z" tense="past" title="Jul 25, 2017, 7:52 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 7f23a4e, made on 25 Jul 2017" id="reblame-7f23a4e" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-7f23a4e" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/10efd26ec19dcaea8984cc5376a277c1cff09ac8/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="115" class="react-line-number react-code-text" style="padding-right: 16px;">115</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC115" class="react-file-line html-div" data-testid="code-cell" data-line-number="115" style="position: relative;"><span class="pl-c1">   git commit -m "Install necessary Python packages"</span></div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2553px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-11T21:23:58.000Z" tense="past" title="Jul 12, 2017, 2:53 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/7390f1d29f3a668b40992637a31d562645cae0a9/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Update README.md" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/7390f1d29f3a668b40992637a31d562645cae0a9">Update README.md</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-11T21:23:58.000Z" tense="past" title="Jul 12, 2017, 2:53 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 7390f1d, made on 12 Jul 2017" id="reblame-7390f1d" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-7390f1d" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/1e570fd53c9826200a392efbcd2223910e83be0b/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="116" class="react-line-number react-code-text" style="padding-right: 16px;">116</div><div data-line-number="117" class="react-line-number react-code-text" style="padding-right: 16px;">117</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC116" class="react-file-line html-div" data-testid="code-cell" data-line-number="116" style="position: relative;"><span class="pl-c1">   git push azure master</span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC117" class="react-file-line html-div" data-testid="code-cell" data-line-number="117" style="position: relative;"><span class="pl-c1">   </span><span class="pl-s">```</span></div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2593px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-11T21:06:08.000Z" tense="past" title="Jul 12, 2017, 2:36 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/1e570fd53c9826200a392efbcd2223910e83be0b/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Update README.md" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/1e570fd53c9826200a392efbcd2223910e83be0b">Update README.md</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-11T21:06:08.000Z" tense="past" title="Jul 12, 2017, 2:36 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 1e570fd, made on 12 Jul 2017" id="reblame-1e570fd" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-1e570fd" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/dc62dbfcff3c637197535baa8c29146a3a30e4ef/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="118" class="react-line-number react-code-text" style="padding-right: 16px;">118</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC118" class="react-file-line html-div" data-testid="code-cell" data-line-number="118" style="position: relative;">   </div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2624px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-25T02:22:55.000Z" tense="past" title="Jul 25, 2017, 7:52 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/10565021" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/7f23a4e021f67cd0930973f65517cbcda67b2f11/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="readme" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/7f23a4e021f67cd0930973f65517cbcda67b2f11">readme</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-25T02:22:55.000Z" tense="past" title="Jul 25, 2017, 7:52 AM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 7f23a4e, made on 25 Jul 2017" id="reblame-7f23a4e" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-7f23a4e" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/10efd26ec19dcaea8984cc5376a277c1cff09ac8/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="119" class="react-line-number react-code-text" style="padding-right: 16px;">119</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC119" class="react-file-line html-div" data-testid="code-cell" data-line-number="119" style="position: relative;">You will be asked to supply the git credentials you chose earlier. By following the steps above you successfully published your app to App Service using Local Git. The push step will take a few minutes to run. When it completes, you have deployed your project and your website is ready for use!</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2655px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T16:47:08.000Z" tense="past" title="May 26, 2017, 10:17 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/328bbd2e77123be547ab3dbe042356b1f112aa5d/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Add final instructions for git deployment and gameplay" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/328bbd2e77123be547ab3dbe042356b1f112aa5d">Add final instructions for git deployment and gameplay</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T16:47:08.000Z" tense="past" title="May 26, 2017, 10:17 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 328bbd2, made on 26 May 2017" id="reblame-328bbd2" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-328bbd2" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/9ec5d68325e743813f333bf9fbb30c378ffb5311/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="120" class="react-line-number react-code-text" style="padding-right: 16px;">120</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC120" class="react-file-line html-div" data-testid="code-cell" data-line-number="120" style="position: relative;">
</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2686px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-05T17:29:01.000Z" tense="past" title="Jul 5, 2017, 10:59 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/fbf1750c5681329bb2b99d4999590cdc645e8ff7/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Update README.md" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/fbf1750c5681329bb2b99d4999590cdc645e8ff7">Update README.md</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-07-05T17:29:01.000Z" tense="past" title="Jul 5, 2017, 10:59 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change fbf1750, made on 5 Jul 2017" id="reblame-fbf1750" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-fbf1750" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/a5a2aa2a1e5cb1d67b1e86459968c645e8a0da6c/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers react-blame-no-line-data"><div data-line-number="121" class="react-line-number react-code-text" style="padding-right: 16px;">121</div></div><div class="react-code-lines react-blame-no-line-data"><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC121" class="react-file-line html-div" data-testid="code-cell" data-line-number="121" style="position: relative;">&lt;<span class="pl-ent">a</span> <span class="pl-e">name</span>=<span class="pl-s">"</span><span class="pl-s">gameplay</span><span class="pl-s">"</span>&gt;&lt;/<span class="pl-ent">a</span>&gt;</div></div></div></div></div></div><div class="react-blame-segment-wrapper" style="transform: translateY(2717px); position: absolute; top: 0px;"><div class="react-blame-for-range d-flex"><div aria-hidden="true" class="age-indicator"><div class="blame-age-indicator" style="background-color: rgb(61, 19, 0);"></div></div><div class="pt-1 timestamp-wrapper-desktop"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T16:47:08.000Z" tense="past" title="May 26, 2017, 10:17 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><div class="author-avatar-wrapper"><img alt="" size="18" src="./README_files/17458994(1)" data-testid="github-avatar" height="18" width="18" class="Avatar__StyledAvatar-sc-2lv0r8-0 feXjpF"></div><div class="Box-sc-g0xbh4-0 iCvHTN"><div class="d-flex"><span data-hovercard-url="/Azure/Hangman/commit/328bbd2e77123be547ab3dbe042356b1f112aa5d/hovercard" class="Text-sc-17v1xeu-0 cDDOjG"><a data-pjax="true" title="Add final instructions for git deployment and gameplay" class="color-fg-default" href="https://github.com/Azure/Hangman/commit/328bbd2e77123be547ab3dbe042356b1f112aa5d">Add final instructions for git deployment and gameplay</a></span></div></div><div class="Box-sc-g0xbh4-0 gXrtud"><div class="pt-1 pr-3 timestamp-wrapper-mobile"><div class="timestamp-ago"><relative-time sx="[object Object]" class="RelativeTime-sc-lqbqy3-0 jHzrDv" datetime="2017-05-26T16:47:08.000Z" tense="past" title="May 26, 2017, 10:17 PM GMT+5:30"><template shadowrootmode="open">7 years ago</template></relative-time></div></div><span role="tooltip" aria-label="Blame prior to change 328bbd2, made on 26 May 2017" id="reblame-328bbd2" class="Tooltip__TooltipBase-sc-17tf59c-0 dkafbw tooltipped-n"><a aria-labelledby="reblame-328bbd2" class="Button Button--iconOnly Button--invisible Button--small" href="https://github.com/Azure/Hangman/blame/9ec5d68325e743813f333bf9fbb30c378ffb5311/README.md"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-versions" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M7.75 14A1.75 1.75 0 0 1 6 12.25v-8.5C6 2.784 6.784 2 7.75 2h6.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14Zm-.25-1.75c0 .138.112.25.25.25h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25h-6.5a.25.25 0 0 0-.25.25ZM4.9 3.508a.75.75 0 0 1-.274 1.025.249.249 0 0 0-.126.217v6.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.75 1.75 0 0 1 3 11.25v-6.5c0-.649.353-1.214.874-1.516a.75.75 0 0 1 1.025.274ZM1.625 5.533h.001a.249.249 0 0 0-.126.217v4.5c0 .09.048.173.126.217a.75.75 0 0 1-.752 1.298A1.748 1.748 0 0 1 0 10.25v-4.5a1.748 1.748 0 0 1 .873-1.516.75.75 0 1 1 .752 1.299Z"></path></svg></a></span></div></div><div class="d-flex flex-row"><div class="react-line-numbers "><div data-line-number="122" class="react-line-number react-code-text" style="padding-right: 16px;">122</div><div data-line-number="123" class="react-line-number react-code-text" style="padding-right: 16px;">123</div><div data-line-number="124" class="react-line-number react-code-text" style="padding-right: 16px;">124</div><div data-line-number="125" class="react-line-number react-code-text" style="padding-right: 16px;">125</div><div data-line-number="126" class="react-line-number react-code-text" style="padding-right: 16px;">126</div></div><div class="react-code-lines "><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC122" class="react-file-line html-div" data-testid="code-cell" data-line-number="122" style="position: relative;"><span class="pl-mh">### <span class="pl-en">Playing Hangman</span></span></div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC123" class="react-file-line html-div" data-testid="code-cell" data-line-number="123" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC124" class="react-file-line html-div" data-testid="code-cell" data-line-number="124" style="position: relative;">To use your web app, navigate to <span class="pl-s">`</span><span class="pl-c1">http://&lt;your web app's resource name&gt;.azurewebsites.net</span><span class="pl-s">`</span>. After a few seconds of initial loading, you should see a website asking you to choose a secret word for the neural network to guess. You're responsible for remembering the secret word, but you will need to tell the neural network how long the word is.</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC125" class="react-file-line html-div" data-testid="code-cell" data-line-number="125" style="position: relative;">
</div></div></div><div class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC126" class="react-file-line html-div" data-testid="code-cell" data-line-number="126" style="position: relative;">After specifying the length and clicking Submit, the neural network's first letter guess will be displayed. It's up to you to tell the neural network whether (and if so, where) the letter appears in the word. After providing this feedback, click Submit to begin the next round.</div></div></div></div></div></div></div></div><div id="copilot-button-container"></div></div><div id="highlighted-line-menu-container"></div></div></div><button hidden="" data-testid="hotkey-button" data-hotkey="Control+f, F3" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+f, F3"></button></section></div></div></div> <!-- --> <!-- --> </div></div></div><div class="Box-sc-g0xbh4-0"></div></div></div></div></div><div id="find-result-marks-container" class="Box-sc-g0xbh4-0 aZrVR"></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+F6,Control+Shift+F6"></button><button hidden="" data-hotkey="Control+F6,Control+Shift+F6"></button></div> <!-- --> <!-- --> <!-- --> <script type="application/json" id="__PRIMER_DATA__">{"resolvedServerColorMode":"night"}</script></div>
</react-app>




  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer pt-8 pb-6 f6 color-fg-muted p-responsive" role="contentinfo" hidden="">
  <h2 class="sr-only">Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com/">
        <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
</a>
      <span>
        © 2024 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com/?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement">
      Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>




    <cookie-consent id="cookie-consent-banner" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-initial-cookie-consent-allowed="" data-cookie-consent-required="false" data-catalyst=""></cookie-consent>


  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>


    <style>
      .user-mention[href$="/upendragoud"] {
        color: var(--color-user-mention-fg);
        background-color: var(--color-user-mention-bg);
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
        padding: 0 2px;
      }
    </style>


    </div>

    <div id="js-global-screen-reader-notice" class="sr-only" aria-live="polite" aria-atomic="true">Blaming Hangman/README.md at master · Azure/Hangman</div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only" aria-live="assertive" aria-atomic="true"></div>
  


<div class="sr-only" id="screenReaderAnnouncementDiv" role="alert" aria-live="assertive"></div><gdiv class="ginger-extension-writer" style="display: none;"><gdiv class="ginger-extension-writer-frame"><iframe src="./README_files/index.html"></iframe></gdiv></gdiv><gdiv id="ginger-floatingG-container" style="position: absolute; top: 0px; left: 0px;"><gdiv class="ginger-floatingG ginger-floatingG-closed" style="display: block;"><gdiv class="ginger-floatingG-disabled-main"><gdiv class="ginger-floatingG-bar-tool-tooltip">Enable Ginger</gdiv></gdiv><gdiv class="ginger-floatingG-offline-main"><gdiv class="ginger-floatingG-bar-tool-tooltip"><em>Cannot connect to Ginger</em> Check your internet connection<br> or reload the browser</gdiv></gdiv><gdiv class="ginger-floatingG-enabled-main"><gdiv class="ginger-floatingG-bar"><gdiv class="ginger-floatingG-bar-tool ginger-floatingG-bar-tool-disable"><ga></ga><gdiv class="ginger-floatingG-bar-tool-tooltip">Disable in this text field</gdiv></gdiv><gdiv class="ginger-floatingG-bar-tool ginger-floatingG-bar-tool-rephrase ginger-floatingG-bar-tool-rephrase_big-circle"><ga class="ginger-floatingG-bar-tool-rephrase__btn" id="ginger__floatingG-bar-tool-rephrase__btn">Rephrase</ga><gdiv class="ginger-floatingG-bar-tool-tooltip ginger-floatingG-bar-tool-tooltip_rephrase">Rephrase current sentence</gdiv></gdiv><gdiv class="ginger-floatingG-bar-tool ginger-floatingG-bar-tool-mistakes"><ga><span class="ginger-floatingG-bar-tool-mistakes-count"></span></ga><gdiv class="ginger-floatingG-bar-tool-tooltip">Edit in Ginger</gdiv></gdiv></gdiv></gdiv><gdiv class="ginger-floatingG-contentPopup"><gdiv class="ginger-floatingG-contentPopup-wrap"><ga class="ginger-floatingG-contentPopup-close">×</ga><gdiv class="ginger-floatingG-contentPopup-frame"><iframe scrolling="no" src="./README_files/saved_resource.html"></iframe></gdiv></gdiv></gdiv></gdiv></gdiv><div id="__primerPortalRoot__" style="position: absolute; top: 0px; left: 0px;"></div></body></html>