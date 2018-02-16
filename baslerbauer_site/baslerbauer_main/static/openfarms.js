
top.openfarms = {
  producers: {},
  produce: {},

  getProducer: function(url, success, fail) {
    if (top.openfarms.producers[url] !== null) {
      success(top.openfarms.producers[url]);
    } else {
      $.getJSON(url, function(data) { top.openfarms.producers[url] = data; success(data); }).fail(fail);
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


