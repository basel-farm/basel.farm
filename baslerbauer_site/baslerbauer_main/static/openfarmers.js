
top.openfarmers = {
  producers: {},
  produce: {},

  getProducer: function(url, success, fail) {
    if (top.openfarmers.producers[url] !== null) {
      success(top.openfarmers.producers[url]);
    } else {
      $.getJSON(url, function(data) { top.openfarmers.producers[url] = data; success(data); }).fail(fail);
    }
  },

  getProduce: function(url, success, fail) {
    if (top.openfarmers.produce[url] !== null) {
      success(top.openfarmers.produce[url]);
    } else {
      $.getJSON(url, function(data) { top.openfarmers.produce[url] = data; success(data); }).fail(fail);
    }
  }
};


