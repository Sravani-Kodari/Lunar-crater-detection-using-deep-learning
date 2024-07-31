var SiteConfig = {"environment":"production","suffix":"","route_url":"http://route.arcgis.com/arcgis/rest/services/World/Route/NAServer/Route_World","portal":"https://www.arcgis.com/sharing/rest","billing":"https://billing.arcgis.com/developers/rest","billingapi":"https://billingapi.arcgis.com/developersubscription","ecas":"https://www.webaccounts.com","ago":"www.arcgis.com","ago_maps":".maps.arcgis.com","destination":"https://developers.arcgis.com","feedback_url":"https://resources.arcgis.com/apps/feedback/dev_feedback.php","diecomm_url":"https://xiecomm.paymetric.com/diecomm/Ajax","marketplace":"http://marketplace.arcgis.com","download_server":"https://downloads.arcgis.com","developers_api":"https://api.developers.arcgis.com","my_esri":"https://my.esri.com","search_api":"https://esearchapi.esri.com","config_script":"https://developers.arcgis.com/assets/js/config.js","api_key":"AAPK9250e700411749c9b0f45c5c54662f24eGi6gpLH6WTEpI4rw0r6VT0MBuAEWhFUpHonLTRzLQfho48WPf4vBRkm0QFyErIP","api_key_dev":"AAPK69c151a127fe4e1bbfbb20961381f7f5SCf-KoVpDDZ8XVidWraG37mL2ROKX9N0q5tN6ehsrPM0jUVyegGu1JW8LnX7Sfbr","api_key_qa":"AAPK8ff40924da464c3b97f6a506820450c1XxY-L33udaca6lwIk7yvpdnVRVopi6DTIoQmTwUrRi05UlzkTL-vSzo1XsrSLv0C","api_key_prod":"AAPK9250e700411749c9b0f45c5c54662f24eGi6gpLH6WTEpI4rw0r6VT0MBuAEWhFUpHonLTRzLQfho48WPf4vBRkm0QFyErIP","api_key_prod_no_referrer":"AAPK54568f8e50f647bcb4818862d9cb9188a95IN1S1HqlagLv8KPAkBN-plJL6VxUmGqKO-mxQ4fHq7PVnAAvbc59Gh7ItL2I-","cesium_access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1MjU0ZDc0Yy01OTVjLTRhZmYtOTBhYy03ZTg0ZDA4NGM3NTciLCJpZCI6MTIyMjk3LCJpYXQiOjE2NzQ2NzYyMTR9.PVXaUe-qwBgqXDm30Z9RUdzKhTBRVRPiOoNRKYd-wuU"};

var dojoConfig = {
  async: true,
  locale: 'en-us',
  useDeferredInstrumentation: true,
  packages: [{
    name: "SessionManager",
    location: "/assets/js/legacy/SessionManager"
  },{
    name: "Notifications",
    location: "/assets/js/legacy/Notifications"
  },{
    name: "Config",
    location: "/assets/js/legacy/Config"
  },{
    name: "calcite-web",
    location: "/assets/js",
    main: "calcite-web"
  }]
};;