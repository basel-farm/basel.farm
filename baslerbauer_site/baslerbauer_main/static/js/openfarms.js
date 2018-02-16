
top.openfarms_urls = {farms: 'http://f.datalets.ch/api/v2/farms/', produce: 'http://f.datalets.ch/api/v2/produce/'};
top.openfarms = {
  _farms_got_all: false,
  farms: {},
  _produce_got_all: false,
  produce: {},

  listFarms: function(url, success, fail) {
    if (top.openfarms._farms_got_all) {
      success(top.openfarms.farms);
    } else {
      $.getJSON(top.openfarms_urls.farms, function(data) { 
        top.openfarms.farms = {};
        $.each(data['items'], function(i,farm) {
          top.openfarms.farms[farm['meta']['detail_url']] = farm;
        });
        top.openfarms._farms_got_all = true;
        success(top.openfarms.farms);
      }).fail(fail);
    }
  },


  listProduces: function(url, success, fail) {
    if (top.openfarms._produces_got_all) {
      success(top.openfarms.produces);
    } else {
      $.getJSON(top.openfarms_urls.produces, function(data) { 
        top.openfarms.produces = {};
        $.each(data['items'], function(i,produce) {
          top.openfarms.produces[produce['meta']['detail_url']] = produce;
        });
        top.openfarms._produces_got_all = true;
        success(top.openfarms.produces);
      }).fail(fail);
    }
  },

  getProducer: function(url, success, fail) {
    if (top.openfarms.farms[url] !== null) {
      success(top.openfarms.farms[url]);
    } else {
      $.getJSON(url, function(data) { 
        top.openfarms.farms[url] = data; 
        success(data); 
      }).fail(fail);
    }
  },

  getProduce: function(url, success, fail) {
    if (top.openfarms.produce[url] !== null) {
      success(top.openfarms.produce[url]);
    } else {
      $.getJSON(url, function(data) { top.openfarms.produce[url] = data; success(data); }).fail(fail);
    }
  }
};


